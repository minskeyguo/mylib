#!/bin/bash


# 1. download kafka from: http://mirrors.tuna.tsinghua.edu.cn/apache/kafka/2.1.0/kafka_2.12-2.1.0.tgz
# 2. tar -xf kafka_2.12-2.1.0.tgz
# 3. mv kafka_2.12-2.1.0.tgz kafka
# 4. run this script

KAFKA_TOP=kafka

TMP_OUT=./tmp

function create_zk_dockerfile() {
cat <<EOF> $TMP_OUT/Dockerfile_zk
FROM ubuntu:latest
MAINTAINER minskey.guo@outlook.com
LABEL verion="1.0"
LABEL description="create a kafka cluster for test"

RUN sed -i 's/https:\/\/archive/https:\/\/cn.archive/g' /etc/apt/sources.list
RUN sed -i 's/http:\/\/archive/http:\/\/cn.archive/g' /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y openjdk-8-jdk

RUN mkdir -p /usr/local/$KAFKA_TOP

RUN mkdir -p /var/zookeeper/logs
RUN mkdir -p /var/zookeeper/data
RUN mkdir -p /var/zookeeper/datalog

COPY $KAFKA_TOP /usr/local/$KAFKA_TOP
ENV PATH \$PATH:/usr/local/$KAFKA_TOP/bin

ENV ZOOKEEPER_HOME /usr/local/$KAFKA_TOP
ENV ZOO_CONF_FILE /usr/local/$KAFKA_TOP/config/zookeeper.properties
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

COPY docker-entrypoint-zk.sh /docker-entrypoint.sh

WORKDIR /usr/local/$KAFKA_TOP
CMD ["zookeeper-server-start.sh", "/usr/local/$KAFKA_TOP/config/zookeeper.properties"]
ENTRYPOINT [ "/docker-entrypoint.sh"]
EOF
}

function create_kf_dockerfile() {
cat <<EOF> $TMP_OUT/Dockerfile_kf
FROM ubuntu:latest
MAINTAINER minskey.guo@outlook.com
LABEL verion="1.0"
LABEL description="create a kafka cluster for test"

RUN sed -i 's/https:\/\/archive/https:\/\/cn.archive/g' /etc/apt/sources.list
RUN sed -i 's/http:\/\/archive/http:\/\/cn.archive/g' /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y openjdk-8-jdk

RUN mkdir -p /usr/local/$KAFKA_TOP
RUN mkdir -p /var/kafka/logs

COPY $KAFKA_TOP /usr/local/$KAFKA_TOP
ENV PATH \$PATH:/usr/local/$KAFKA_TOP/bin

ENV KF_CONF_FILE /usr/local/$KAFKA_TOP/config/server.properties
ENV KF_NUM_PARTITION 1
ENV KF_NUM_NETWORK_THREDS 3
ENV KF_NUM_IO_THREADS 8
ENV KF_SOCKET_SEND_BUFFER_BYTES 102400
ENV KF_SOCKET_RECEIVE_BUFFER_BYTES 102400
ENV KF_SOCKET_REQUEST_MAX_BYTES 102400
ENV KF_ZK_CONN_TIMEOUT 6000
ENV KF_LOG_RETENTION_HOURS 168
ENV KF_LOG_DIRS /var/kafka/logs
ENV KF_LISTENERS_PORT 9093

COPY docker-entrypoint-kf.sh /docker-entrypoint.sh

WORKDIR /usr/local/$KAFKA_TOP
CMD ["/usr/local/$KAFKA_TOP/bin/kafka-server-start.sh", "/usr/local/$KAFKA_TOP/config/server.properties"]
ENTRYPOINT [ "/docker-entrypoint.sh"]
EOF
}

mkdir -p $TMP_OUT
cp docker-entrypoint-*.sh $TMP_OUT/

create_zk_dockerfile
create_kf_dockerfile
docker build  -t minskey/kafka-zk -f $TMP_OUT/Dockerfile_zk .
docker build  -t minskey/kafka-kf -f $TMP_OUT/Dockerfile_kf .
