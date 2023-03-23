#!/bin/bash
echo "Experiment running..."
declare -i CONT=1
echo "CPU Load: 100 %"
for i in {0..10..1}
do
  printf "State before run #%d:" $CONT
  uptime
  stress-ng -c 0 -l 25 -t 5m
  printf "State after run #%d:" $CONT
  uptime
  let CONT++
  echo "Cooling time of 8m"
  sleep 8m
done