import pandas as pd
import numpy as np
from datetime import datetime as dt

pd.set_option('display.max_columns', None)
text_file = '''C:/Users/Davinder/PycharmProjects/adventofcode2018/day4input.txt'''

with open(text_file, 'r') as f:
    data = [str(line.strip()) for line in f]

formatted_data = []

for i in data:
    temp_list = []
    timestamp, description = i[1:17], i[19:]
    temp_list.extend([timestamp, description])
    formatted_data.append(temp_list)

df = pd.DataFrame(formatted_data, columns=['timestamp', 'description'])

df['timestamp'] = df['timestamp'].apply(lambda x: x.replace('1518', '2018'))
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.sort_values(by='timestamp', ascending=True, inplace=True)
df.reset_index(drop=True, inplace=True)

df['guard_no'] = df['description'].apply(lambda x: int(x.replace('Guard #', '').replace(' begins shift', '')) if '#' in x else None)
df['guard_no'].ffill(inplace=True)
df['start'] = df['timestamp'].shift(periods=1)
df['diff'] = (df['timestamp'] - df['start']).astype('timedelta64[m]')
# df['diff2'] = df['timestamp'].dt.minute - df['lag1'].dt.minute #need dt for vector operation not for element
# df['diff3'] = (df['timestamp'] - df['lag1']).dt.seconds/60 #this is preferred since it gives a timedelta and no astype required


sleep_rank = df[df['description'] == 'wakes up'].groupby('guard_no').sum().sort_values(by='diff', ascending=False)
most_sleepy = sleep_rank.index[0]

df_filtered = df[(df['guard_no'] == most_sleepy) & (df['description'] == 'wakes up')]

minutes_count = []
for i in range(len(df_filtered)):
    for minute in range(60):
        if minute >= df_filtered.iloc[i]['start'].minute and minute < df_filtered.iloc[i]['timestamp'].minute:
            minutes_count.append(minute)

minutes_series = pd.Series(minutes_count).value_counts().sort_values(ascending=False)

# print 'Part1', most_sleepy * minutes_series.index[0]

#part 2

df_clean = df[df['description'] == 'wakes up']

most_minute = pd.Series()

for i in range(len(df_clean)):
    for minute in range(60):
        if minute >= df_clean.iloc[i]['start'].minute and minute < df_clean.iloc[i]['timestamp'].minute:
            most_minute = most_minute.append(pd.Series([minute], index=[df_clean.iloc[i]['guard_no']]))


top_most_minute = most_minute.groupby(most_minute.index).value_counts().sort_values(ascending=False)

print top_most_minute.index[0][0] * top_most_minute.index[0][1]
