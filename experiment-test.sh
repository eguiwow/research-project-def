#!/bin/bash
nohup ./stress-test.sh >> ../tests/experiment.log & pid1=$!
nohup ./monitor-test.sh >> ../tests/experiment.log & pid2=$!
wait $pid1
kill $pid2