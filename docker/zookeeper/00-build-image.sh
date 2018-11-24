#!/bin/bash

URL_ZK="https://mirrors.tuna.tsinghua.edu.cn/apache/zookeeper/current/"

TMP_OUT=./tmp
PWD=`pwd`

# Download the latest zookeeper tarball release from URL_ZK #
function download_zookeeper() {
	local zk

	cd $TMP_OUT
	curl -sSL $URL_ZK -o zk_thu.html || { echo "Failed to get $URL_ZK"; exit 1; }
	zk=`grep -Pioe "<a +href *=.*zookeeper.*\.tar\.gz.*>zookeeper-.*\.tar\.gz</a>" zk_thu.html | grep -Pioe "\"zookeeper-.*\.tar.gz\"" `
	zk=${zk//\"/}
	wget -c $URL_ZK/$zk || { echo "Failed to download $URL_ZK/$zk"; exit -1; }
	tar -xf $zk || { echo "Failed to uncompress $zk"; exit -1; }
	mv ${zk%%.tar.gz*} zookeeper
	cd $PWD
}

function create_dockerfile() {
cat <<EOF> $TMP_OUT/Dockerfile
FROM ubuntu:latest
MAINTAINER minskey.guo@outlook.com
LABEL verion="1.0"
LABEL description="create a zookeeper cluster for test"

RUN sed -i 's/https:\/\/archive/https:\/\/cn.archive/g' /etc/apt/sources.list
RUN sed -i 's/http:\/\/archive/http:\/\/cn.archive/g' /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y openjdk-8-jdk

RUN mkdir -p /usr/local/zookeeper
RUN mkdir -p /var/zookeeper/logs
RUN mkdir -p /var/zookeeper/data
RUN mkdir -p /var/zookeeper/datalog

COPY $TMP_OUT/zookeeper /usr/local/zookeeper
ENV PATH \$PATH:/usr/local/zookeeper/bin

ENV ZOOKEEPER_HOME /usr/local/zookeeper
ENV ZOO_CONF_DIR /usr/local/zookeeper/conf
ENV ZOO_LOG_DIR /var/zookeeper/logs
ENV ZOO_DATA_DIR /var/zookeeper/data
ENV ZOO_DATA_LOG_DIR=/var/zookeeper/datalog
ENV ZOO_PORT=2181
ENV ZOO_TICK_TIME 2000
ENV ZOO_INIT_LIMIT 5
ENV ZOO_SYNC_LIMIT 2
ENV ZOO_MAX_CLIENT_CNXNS 100
ENV ZOO_AUTOPURGE_PURGEINTERVAL 0
ENV ZOO_AUTOPURGE_SNAPRETAINCOUNT 3

COPY docker-entrypoint.sh /docker-entrypoint.sh

CMD ["zkServer.sh", "start-foreground"]
ENTRYPOINT [ "/docker-entrypoint.sh"]

EOF


}


mkdir -p $TMP_OUT

# download_zookeeper

create_dockerfile
cp docker-entrypoint.sh $TMP_OUT/

docker build  -t minskey/zookeeper -f $TMP_OUT/Dockerfile .
