#!/bin/bash
echo "Logging the measurements..."
interval=9
timestamp_file=$(date +"%Y%m%d-%H%M%S")

#Headers for csv
echo "Timestamp,temp_cpu0,temp_cpu1,temp_cpu2,temp_cpu3,temp_cpu4,temp_cpu5,temp_cpu6,temp_cpu7,%usr,%sys,%IOwait,%Idle" >> ../tests/cpu_$timestamp_file.csv
echo "Timestamp,Used,Available" >> ../tests/mem_$timestamp_file.csv


while true; do
    timestamp=$(date +"%Y%m%d-%T")
   
    cpu_data=$(mpstat 1 1| awk 'FNR == 4 {print $3 "," $5 "," $6 "," $12}')
    mem_data=$(free -m | awk 'FNR == 2 {print $3 "," $7}')
    temp_data=$(sensors | awk 'BEGIN{RS="\n"; line=""} /^Core [0-9]:/ {line = line $3 ","} END{print line}')
    
    echo "$timestamp,$temp_data$cpu_data" >> ../tests/cpu_$timestamp_file.csv
    echo "$timestamp,$mem_data" >> ../tests/mem_$timestamp_file.csv
    #echo "$timestamp,$io_data" >> ../tests/io_$timestamp_file.csv

    sleep $interval
done
