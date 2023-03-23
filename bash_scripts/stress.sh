#!/bin/bash
# 5m of stress; 1m of sleep
echo "Experiment running..."
declare -i CONT=1
for i in {0..100..10}
do
  echo "CPU Load: $i %"
  printf "State before run #%d:" $CONT
  uptime
  stress-ng -c 0 -l $i -t 5m
  printf "State after run #%d:" $CONT
  uptime
  let CONT++
  echo "Cooling time of 60s"
  sleep 60s
done