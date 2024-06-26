#!/bin/bash
#
# This script is expected to run in ClearLinux host or docker developement
# environment. Make sure system has the following commands before executing
#      git
#
URL_ACRN=https://github.com/projectacrn/


# This is the volume on host system, and will be mounted as volume into
# docker -v ${HOST_DIR_VOL}:${ACRN_MNT_VOL}. We "git clone" all ACRN repos,
# and then build disk image there in docker. Make sure that it has 30GB
# space since we create disk image there.
[ -z ${ACRN_MNT_VOL} ] && ACRN_MNT_VOL=/acrn-vol
cd ${ACRN_MNT_VOL} || { echo "Failed to cd "${ACRN_MNT_VOL}; exit -1; }

[ -z ${ACRN_ENV_VARS} ] && ACRN_ENV_VARS=acrn-env.txt
[ -f ${ACRN_ENV_VARS} ] && \
     { for line in `cat ${ACRN_ENV_VARS}`; do export $line; done; }

[ -z ${ACRN_HV_DIR} ] && ACRN_HV_DIR=acrn-hypervisor

[ -z ${ACRN_TRACE_SHELL_ENABLE} ] || set -x

if [ ! -d ${ACRN_HV_DIR} ]; then
	git clone ${URL_ACRN}/${ACRN_HV_DIR} || 
		{ echo "Failed to git-clone ${URL_ACRN}${ACRN_HV_DIR}"; exit 1; }

        echo "Completed git-clone ACRN hypervisor and device model"
fi;

cd ${ACRN_HV_DIR};

# create a test branch
if [ -z "${ACRN_HV_COMMIT}" ] || [ "${ACRN_HV_COMMIT}X" == "X" ]; then
	ACRN_HV_COMMIT=`git rev-parse HEAD`
fi;

BRANCH="commit_${ACRN_HV_COMMIT}"
ret=`git branch | grep "${BRANCH}"`

if [ ! "${ret}" == "${BRANCH}" ]; then

	# In case we run the script few times, the branch might be create last time
        git branch | grep ${BRANCH}
        if [ $? -ne 0 ]; then
	       git branch ${BRANCH} ${ACRN_HV_COMMIT} || \
	    { echo "Failed to create branch: ${BRANCH}"; exit 1; }
	fi;

	git checkout ${BRANCH} || \
		{ echo "Failed to git checkout branch: ${BRANCH}"; exit 1; }

	for i in `ls ../hv*.patch`; do
		commit_id=`head -1 $i | awk '{print $2}'`
		git log -1 ${commit_id} >> /dev/null

		# this patch has been merged already, don't apply it again;
		[ $? -eq 0 ] && continue;

		# the patch is not merged yet, apply it
		echo "Patch ${i} to acrn-hypervisor";
		git am  $i || { echo "Failed to apply $i to hypervisor";
		    echo "Please check if the patch has been merged already. If merged,";
		    echo "delete it from ${ACRN_HV_DIR} and re-run script-00 from ${ACRN_HV_DIR} "; exit 1; }
	done;

fi;


git checkout ${BRANCH} || \
	{ echo "Failed to git checkout branch: ${BRANCH}"; exit 1; }

export ACRN_HV_DIR=${ACRN_HV_DIR}


env | grep ACRN > ${ACRN_MNT_VOL}/${ACRN_ENV_VARS}

exit 0;
