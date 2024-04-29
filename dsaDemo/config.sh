#!/bin/bash

set -v

accel-config config-device dsa4
[ $? -eq 0 ] || exit;
accel-config config-engine dsa4/engine4.2 --group-id=2
[ $? -eq 0 ] || exit;
accel-config config-wq dsa4/wq4.0 --group-id=2 --wq-size=32 --priority=1 --block-on-fault=0 --threshold=4 --type=kernel --driver-name=dmaengine  --name=dsa_kernel_queue --mode=shared --max-batch-size=32 --max-transfer-size=2097152
[ $? -eq 0 ] || exit;
accel-config enable-device dsa4
[ $? -eq 0 ] || exit;
accel-config enable-wq dsa4/wq4.0
[ $? -eq 0 ] || exit;

