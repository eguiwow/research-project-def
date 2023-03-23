import pandas as pd
import re

# read the .csv file into a DataFrame
df_cpu = pd.read_csv('cpu_20230131-145127.csv')

# extract the temperature column as a series
for i in range(0,8):

    temp_column = df_cpu['temp_cpu'+str(i)]

    # extract the numerical value using a regular expression
    temp_values = temp_column.str.extract(r'(\d+\.\d+)')

    # convert the extracted values to float
    temp_values = temp_values[0].astype(float)

    # add the extracted temperature values as a new column to the DataFrame
    df_cpu['cpu'+str(i)+'_temp'] = temp_values
    # drop the original 'Date' and 'Time' columns
    df_cpu = df_cpu.drop('temp_cpu'+str(i), axis=1)

# write the updated DataFrame to a new .csv file
df_cpu.to_csv('cpu_experiment.csv', index=False)
