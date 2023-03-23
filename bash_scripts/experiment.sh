#!/bin/bash
nohup ./stress.sh >> ../results/experiment.log & pid1=$!
nohup ./monitor.sh >> ../results/experiment.log & pid2=$!
wait $pid1
kill $pid2