#!/bin/bash
# 2s of stress; 1s of sleep
declare -i CONT=1
echo "Experiment test..."
for i in {0..100..10}
do
  echo "CPU Load: $i %"
  printf "State before run #%d:" $CONT
  stress-ng -c 5 -l $i -t 2s
  printf "State after run #%d:" $CONT
  uptime
  let CONT++
  echo "Cooling time of 5s"
  sleep 1s
done