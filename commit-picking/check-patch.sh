#!/bin/bash


DIR_PATCH=./acrnpatches/


cd $DIR_PATCH;

mkdir gerrit-patch
mkdir git-am-ok
mkdir git-am-fail

for i in `grep "Change-Id" *.patch | awk -F: '{print $1}'`;
do
	mv $i gerrit-patch/
done;

cd ..

GDIR=${DIR_PATCH}/gerrit-patch/
OK_DIR=${DIR_PATCH}/git-am-ok/
FAIL_DIR=${DIR_PATCH}/git-am-fail/

echo "Apply patch in the directory: "${GDIR}

for patch in `ls ${GDIR}/`;
do
	echo "check: "$patch;
	git am ${GDIR}/$patch
	if [ $? != 0 ];
	then 
		echo "Failed to apply the patch:"${GDIR}/$patch; 
		echo "Try to merge it manully";
		mv ${GDIR}/$patch $FAIL_DIR
		exit;
	else
		mv ${GDIR}/$patch $OK_DIR
	fi;
		
done;
