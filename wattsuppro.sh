#!/bin/bash
timestamp_file=$(date +"%Y%m%d-%H%M%S")
# INPUT <TIMEOUT>
/usr/bin/python3 /home/ander/wattsuppro_logger/WattsupPro.py -l -p /dev/ttyUSB1 -t $1 -o /home/ander/results/energy.log
/usr/bin/python3 /home/ander/scripts/output_2_csv.py
mv /home/ander/results/energy.log /home/ander/results/energy_$timestamp_file.log
# TODO scp connection and file sending
# scp ander@145.108.225.16:~/results/$new_fileName /home/ander/thesis/results/$new_fileName