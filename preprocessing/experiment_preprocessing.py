import pandas as pd
import glob

filename = glob.glob('energy_*.csv')[0]
timestamp = filename.split('_')[1].split('.')[0]
# read the .csv energy file
df_ene = pd.read_csv(filename)

# convert the 'Date' column into a date format
df_ene['Date'] = pd.to_datetime(df_ene['Date'], format='%Y-%m-%d')
df_ene['Timestamp'] = df_ene['Date'].dt.strftime('%Y%m%d') + '-' + df_ene['Time']

# drop the original 'Date' and 'Time' columns
df_ene = df_ene.drop(['Date', 'Time'], axis=1)

filename = glob.glob('cpu_*.csv')[0]
# Clean the degrees column to make it only numeric
df_cpu = pd.read_csv(filename)


# extract the temperature columns as a series
temp_columns = ['temp_cpu0', 'temp_cpu1', 'temp_cpu2', 'temp_cpu3', 'temp_cpu4', 'temp_cpu5', 'temp_cpu6', 'temp_cpu7']
temp_series_list = [df_cpu[col].str.extract(r'(\d+\.\d+)')[0].astype(float) for col in temp_columns]

# calculate the average temperature value and add it as a new column to the DataFrame
df_cpu['avg_cpu_temp'] = sum(temp_series_list) / len(temp_series_list)

# # extract the temperature column as a series
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

filename = glob.glob('mem_*.csv')[0]
df_mem = pd.read_csv(filename)

# convert timestamp columns to datetime format
df_ene['Timestamp'] = pd.to_datetime(df_ene['Timestamp'])
df_cpu['Timestamp'] = pd.to_datetime(df_cpu['Timestamp'])
df_mem['Timestamp'] = pd.to_datetime(df_mem['Timestamp'])

# merge the two datasets on the 'Timestamp' column
df4 = pd.merge(df_ene, df_cpu, on='Timestamp', how='outer')
df_final = pd.merge(df_mem, df4, on='Timestamp', how='outer')

# rename the columns to 'Timestamp', 'Value1', 'Value2', and 'Value3'
df_final.rename(columns={'Value_x': 'Value1', 'Value_y': 'Value2', 'Value': 'Value3'}, inplace=True)

# sort the dataset by the 'Timestamp' column
df_final = df_final.sort_values(by='Timestamp')

# # make the 'Timestamp' column the first column
# cols = df_final.columns.tolist()
# cols = cols[:1] + cols[-3:] + cols[1:-3]
# df_final = df_final[cols]

# write the combined dataset to a new .csv file
df_final.to_csv("experiment_" + timestamp + ".csv", index=False)

