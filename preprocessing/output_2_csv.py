import os
import csv
import subprocess
import datetime
import pytz

def txt_2_table(file_in):
    data = []
    with open(file_in, 'r') as f_in:
        for line in f_in:
            fields = line.split()
            data.append(fields)
    return data

def table_2_csv(table, filename):

    # #Initialize the directory name
    # dirname = "results"
    # #Check the directory name exist or not
    # if os.path.isdir(dirname) == False:
    #     #Create the directory
    #     os.mkdir(dirname)
    #     #Print success message
    #     print("The directory is created.")
    # else:
    #     #Print the message if the directory exists
    #     print("The directory already exists.")

    os.chdir('/home/ander/results')
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Time", "Index", "Watts", "Volts", "Amps"])
        writer.writerows(table)

timestr = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
new_filename = 'energy_' + timestr + '.csv'
os.chdir('/home/ander/results')
table = txt_2_table('energy.log')
table_2_csv(table, new_filename)

#cmd = 'scp ander@145.108.225.16:~/results/' +new_filename+ '/home/ander/thesis/results/'+new_filename
#retcode = subprocess.call(cmd,shell=True)