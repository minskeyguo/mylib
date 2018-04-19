#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import git
import subprocess
import shutil



if (os.path.exists("acrnpatches")):
    shutil.rmtree("acrnpatches")

# save commits into the file
os.mkdir("acrnpatches");
acrn_file = os.getcwd() + "/acrnpatches/commits.txt"
out_dir = os.getcwd() + "/acrnpatches/"

# kerne source code
dir_kernel = "/work/acrn-cwp/acrn-new/sos/kernel"

# the dirs or files which ACRN touch
# acrn_dirs = [ "Documentation/ABI/testing/sysfs-class-rpmb", ]
acrn_dirs = ["arch/x86/acrn", 
             "drivers/acrn",
             "drivers/char/vhm",
             "drivers/char/rpmb/",
             "drivers/dma-buf/hyper_dmabuf",
             "drivers/trusty",
             "drivers/vbs",
             "drivers/vhm", 
             "drivers/virtio", 
             "include/linux/rpmb.h",
             "include/linux/trusty/",
             "include/linux/vhm/",
             "include/uapi/linux/rpmb.h",
             "include/uapi/linux/virtio_ids.h",
             "tools/rpmb",
             "Documentation/ABI/testing/sysfs-class-rpmb",
             "Documentation/devicetree/bindings/trusty/",
             "Documentation/virtual/acrn",
             ]


if not (os.path.isdir(dir_kernel)):
    print "The directory of pkt kernel tree doesn't exist: ", dir_kernel;


# all commits in kernel source tree since the time
GIT_LOG_ALL = 'git log --pretty=format:%h --cherry-pick --since=2016-01-01 --no-merges -- '

# use GIT_LOG_ALL to find all commits. return the commit list 
def get_log_kernel(logcmd):
    os.chdir(dir_kernel)
    git_klog = logcmd;
    proc = subprocess.Popen(git_klog.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    logk = stdout.split('\n');
    return logk;



# use GIT_LOG_ACRN + acrn_file_name to find all commits related to ACRN
def get_acrn_commits(dirs_for_search):
    commits = set()
    afiles = set()

    # use this "git log" to to all files in acrn_dirs to get commits;
    GIT_LOG_ACRN = 'git log --follow --pretty=format:%h --cherry-pick ' \
                    '--since=2016-01-01 --no-merges -- '

    os.chdir(dir_kernel)
    for dentry in dirs_for_search:


        if not (os.path.exists(dentry)):
            print "The directory \"",dentry,"\" doesn't exist"
            sys.exit()

        if (os.path.isfile(dentry)):
            fname = dentry;
            afiles.add(fname);
            git_log = GIT_LOG_ACRN + fname 
            proc = subprocess.Popen(git_log.split(),
                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = proc.communicate()
            lines = stdout.split('\n');
            for line in lines:
                commits.add(line)

        for root, dirs, files in os.walk(dentry, topdown=False):
            for name in files:
                fname = os.path.join(root, name);
                afiles.add(fname);

                git_log = GIT_LOG_ACRN + fname
                proc = subprocess.Popen(git_log.split(),
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = proc.communicate()
                lines = stdout.split('\n');
                for line in lines:
                    commits.add(line)

    return commits, afiles


def format_patch(kernel_dir, commits, out_dir):
    GIT_FORMAT_PATCH = 'git format-patch -o ' + out_dir
    os.chdir(dir_kernel)
    for i in range(len(commits)):
        (commit, index) = sort_list[i];
        i = i + 1
        s = GIT_FORMAT_PATCH + '--start-number '+ str(i)  + " -1 " + commit;
        os.system(GIT_FORMAT_PATCH + ' --start-number '+ str(i)  + " -1 " + commit);


if __name__ == "__main__":
    dict_commits = {}

    klogs = get_log_kernel(GIT_LOG_ALL)
    aCommits, aFiles = get_acrn_commits(acrn_dirs)

    sorted_files = [aFiles];

    for commit in aCommits:
        index = klogs.index(commit)
        dict_commits[commit] = index

    sort_list = sorted(dict_commits.items(), key=lambda item:item[1], reverse=True)

    print "Write commits into the file: ", acrn_file
    fobj = open(acrn_file, "w")
    for i in range(len(sort_list)): 
        (commit, index) = sort_list[i];
        fobj.write(str(i) + "\t" + str(index) +"\t" + commit + "\n");
    fobj.close()

    format_patch(dir_kernel, sort_list, out_dir)

