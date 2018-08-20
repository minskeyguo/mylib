#!/bin/bash

set -x

function launch_android()
{
if [ ! -f "/data/$5/$5.img" ]; then
  echo "no /data/$5/$5.img, exit"
  exit
fi

#vm-name used to generate uos-mac address
mac=$(cat /sys/class/net/en*/address)
vm_name=vm$1
vm_name=${vm_name}-${mac:9:8}

# create a unique tap device for each VM
tap=tap_AaaG
tap_exist=$(ip a | grep acrn_"$tap" | awk '{print $1}')
if [ "$tap_exist"x != "x" ]; then
  echo "tap device existed, reuse acrn_$tap"
else
  ip tuntap add dev acrn_$tap mode tap
fi

# if acrn-br0 exists, add VM's unique tap device under it
br_exist=$(ip a | grep acrn-br0 | awk '{print $1}')
if [ "$br_exist"x != "x" -a "$tap_exist"x = "x" ]; then
  echo "acrn-br0 bridge aleady exists, adding new tap device to it..."
  ip link set acrn_"$tap" master acrn-br0
  ip link set dev acrn_"$tap" down
  ip link set dev acrn_"$tap" up
fi

#Use MMC name + serial for ADB serial no., same as native android
# mmc_name=`cat /sys/block/mmcblk1/device/name`
# mmc_serial=`cat /sys/block/mmcblk1/device/serial | sed -n 's/^..//p'`
# ser=$mmc_name$mmc_serial
ser=vm-123

#check if the vm is running or not
vm_ps=$(pgrep -a -f acrn-dm)
result=$(echo $vm_ps | grep "${vm_name}")
if [[ "$result" != "" ]]; then
  echo "$vm_name is running, can't create twice!"
  exit
fi


#for VT-d device setting
modprobe pci_stub
echo "8086 9d2f" > /sys/bus/pci/drivers/pci-stub/new_id
echo "0000:00:14.0" > /sys/bus/pci/devices/0000:00:14.0/driver/unbind
echo "0000:00:14.0" > /sys/bus/pci/drivers/pci-stub/bind


echo "8086 9d30" > /sys/bus/pci/drivers/pci-stub/new_id
echo "0000:00:14.1" > /sys/bus/pci/devices/0000:00:14.1/driver/unbind
echo "0000:00:14.1" > /sys/bus/pci/drivers/pci-stub/bind

#for memsize setting
memsize=`cat /proc/meminfo|head -n 1|awk '{print $2}'`
if [ $memsize -gt 4000000 ];then
    mem_size=2048M
else
    mem_size=1750M
fi

if [ "$setup_mem" != "" ];then
    mem_size=$setup_mem
fi

kernel_cmdline_generic="maxcpus=$2 nohpet tsc=reliable intel_iommu=off \
   androidboot.serialno=$ser \
   i915.enable_rc6=1 i915.enable_fbc=1 i915.enable_guc_loading=0 i915.avail_planes_per_pipe=$4 \
   i915.enable_hangcheck=0 use_nuclear_flip=1 i915.enable_guc_submission=0"

boot_dev_flag=",b"
boot_image_option="--vsbl /root/VSBL.bin"
kernel_cmdline="$kernel_cmdline_generic"

: '
select right virtual slots for acrn_dm:
1. some passthru device need virtual slot same as physical, like audio 0:e.0 at
virtual #14 slot, so "-s 14,passthru,0/e/0"
2. acrn_dm share vioapic irq between some virtual slots: like 6&14, 7&15. Need
guarantee no virt irq sharing for each passthru device.
FIXME: picking a virtual slot (#24 now) which is level-triggered to make sure
audio codec passthrough working
3. the bootable device slot is configured in compile stating in Android Guest
image, it should be kept using 3 as fixed value for Android Guest on Gordon_peak
ACRN project
'

acrn-dm --help 2>&1 | grep 'GVT args'
if [ $? == 0 ];then
  GVT_args=$3
  boot_GVT_option=" -s 2,pci-gvt -G "
else
  boot_GVT_option=''
  GVT_args=''
fi


 acrn-dm -A -m $mem_size -c $2 $boot_GVT_option"$GVT_args" -s 0:0,hostbridge -s 1:0,lpc -l com1,stdio \
   -l com1,stdio \
   -s 9,virtio-net,$tap \
   -s 3,virtio-blk$boot_dev_flag,/data/$5/$5.img \
   -s 13,virtio-rpmb \
   -s 7,passthru,0/14/0 \
   -s 8,passthru,0/14/1 \
   -s 10,virtio-hyper_dmabuf \
   -s 11,wdt-i6300esb \
   $boot_image_option \
   -B "$kernel_cmdline" $vm_name
}

function help()
{
echo "Use luanch_uos.sh like that ./launch_uos.sh -V <#>"
echo "The option -V means the UOSs group to be launched by vsbl as below"
echo "-V 1 means just launching 1 clearlinux UOS"
echo "-V 2 means just launching 1 android UOS"
echo "-V 3 means launching 1 clearlinux UOS + 1 android UOS"
echo "-V 4 means launching 2 clearlinux UOSs"
echo "-V 5 means auto check android/linux UOS; if exist, launch it"
}

launch_type=1
debug=0

while getopts "V:M:hd" opt
do
	case $opt in
		V) launch_type=$[$OPTARG]
			;;
		M) setup_mem=$OPTARG
			;;
		d) debug=1
			;;
		h) help
			exit 1
			;;
		?) help
			exit 1
			;;
	esac
done

mkdir -p /data/
mount /dev/sda4  /data


if [ $launch_type == 5 ]; then
	if [ -f "/data/android/android.img" ]; then
	  launch_type=2;
	else
	  launch_type=1;  
	fi
fi

# make sure there is enough 2M hugepages in the pool
echo 1024 > /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages

# offline SOS CPUs except BSP before launch UOS
for i in `ls -d /sys/devices/system/cpu/cpu[1-99]`; do
        online=`cat $i/online`
        idx=`echo $i | tr -cd "[1-99]"`
        echo cpu$idx online=$online
        if [ "$online" = "1" ]; then
                echo 0 > $i/online
                echo $idx > /sys/class/vhm/acrn_vhm/offline_cpu
        fi
done

case $launch_type in
	1) echo "Launch clearlinux UOS"
		launch_clearlinux 1 3 "64 448 8" 0x070F00 clearlinux $debug
		;;
	2) echo "Launch android UOS"
		launch_android 1 3 "64 448 8" 0x070F00 android $debug
		;;
	3) echo "Launch clearlinux UOS + android UOS"
		launch_android 1 2 "64 448 4" 0x00000C android $debug &
		sleep 5
		launch_clearlinux 2 1 "64 448 4" 0x070F00 clearlinux $debug
		;;
	4) echo "Launch two clearlinux UOSs"
		launch_clearlinux 1 1 "64 448 4" 0x00000C clearlinux $debug &
		sleep 5
		launch_clearlinux 2 1 "64 448 4" 0x070F00 clearlinux_dup $debug
		;;
esac

# umount /data


# launch_uos.sh -V 2
