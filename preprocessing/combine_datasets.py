import pandas as pd

# read both .csv files into memory
df1 = pd.read_csv("combined_timestamp.csv")
df2 = pd.read_csv("cpu_20230129-231401.csv")
df3 = pd.read_csv("mem_20230129-231401.csv")

# convert timestamp columns to datetime format
df1['Timestamp'] = pd.to_datetime(df1['Timestamp'])
df2['Timestamp'] = pd.to_datetime(df2['Timestamp'])
df3['Timestamp'] = pd.to_datetime(df3['Timestamp'])

# merge the two datasets on the 'Timestamp' column
df4 = pd.merge(df1, df2, on='Timestamp', how='outer')
df = pd.merge(df3, df4, on='Timestamp', how='outer')

# rename the columns to 'Timestamp', 'Value1', 'Value2', and 'Value3'
df.rename(columns={'Value_x': 'Value1', 'Value_y': 'Value2', 'Value': 'Value3'}, inplace=True)

# sort the dataset by the 'Timestamp' column
df = df.sort_values(by='Timestamp')

# make the 'Timestamp' column the first column
cols = df.columns.tolist()
cols = cols[:1] + cols[-3:] + cols[1:-3]
df = df[cols]

# write the combined dataset to a new .csv file
df.to_csv("combined_datasets2.csv", index=False)

