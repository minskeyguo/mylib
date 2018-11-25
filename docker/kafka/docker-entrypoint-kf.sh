#!/bin/bash

#
# borrow from zookeeper docker image 
#
set -e

# Generate the config only if it doesn't exist
if [[ ! -f "$KF_CONF_FILE" ]]; then
    CONFIG="$KF_CONF_FILE"

    echo "broker.id=$KF_BROKER_ID" >> "$CONFIG"
    echo "port=$KF_SERVER_PORT" >> "$CONFIG"
    echo "log.dirs=$KF_LOG_DIRS" >> "$CONFIG"
    echo "num.partitions=$KF_NUM_PARTITION" >> "$CONFIG"
    echo "listeners=PLAINTEXT://:$KF_LISTENERS_PORT" >> "$CONFIG"


    echo "num.network.threads=$KF_NUM_NETWORK_THREDS" >> "$CONFIG"
    echo "num.io.threads=$KF_NUM_IO_THREADS" >> "$CONFIG"
    echo "socket.send.buffer.bytes=$KF_SOCKET_SEND_BUFFER_BYTES" >> "$CONFIG"
    echo "socket.receive.buffer.bytes=$KF_SOCKET_RECEIVE_BUFFER_BYTES" >> "$CONFIG"
    echo "socket.request.max.bytes=$KF_SOCKET_REQUEST_MAX_BYTES" >> "$CONFIG"

    echo "log.retention.hours=$KF_LOG_RETENTION_HOURS" >> "$CONFIG"
    echo "zookeeper.connect=$KF_ZOOKEEPER_CONNECT" >> "$CONFIG"
    echo "zookeeper.connection.timeout.ms=$KF_ZK_CONN_TIMEOUT" >> "$CONFIG"

fi

exec "$@"
