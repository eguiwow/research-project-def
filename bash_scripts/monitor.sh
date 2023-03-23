#!/bin/bash
echo "Logging the measurements..."
interval=9
timestamp_file=$(date +"%Y%m%d-%H%M%S")

#Headers for csv
echo "Timestamp,temp_cpu0,temp_cpu1,temp_cpu2,temp_cpu3,temp_cpu4,temp_cpu5,temp_cpu6,temp_cpu7,%usr,%sys,%IOwait,%Idle" >> ../results/cpu_$timestamp_file.csv
echo "Timestamp,Used,Available" >> ../results/mem_$timestamp_file.csv

while true; do
    timestamp=$(date +"%Y%m%d-%T")
   
    cpu_data=$(mpstat 1 1| awk 'FNR == 4 {print $3 "," $5 "," $6 "," $12}')
    mem_data=$(free -m | awk 'FNR == 2 {print $3 "," $7}')
    temp_data=$(sensors | awk 'BEGIN{RS="\n"; line=""} /^Core [0-9]:/ {line = line $3 ","} END{print line}')

    echo "$timestamp,$temp_data$cpu_data" >> ../results/cpu_$timestamp_file.csv
    echo "$timestamp,$mem_data" >> ../results/mem_$timestamp_file.csv

    sleep $interval #every 9s +1s of the mpstat instruction = 10s
done
