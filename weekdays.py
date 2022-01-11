'''
Are there differences in activity patterns between weekdays and weekends?
1.	Create a new factor variable in the dataset with two levels - "weekday" and "weekend" indicating whether a given date is a weekday or weekend day.
2.	Make a plot containing a time series plot of the 5-minute interval (x-axis) and the average number of steps taken, averaged across all weekdays or weekend days (y-axis).
 

'''
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

filename = 'newActivity.csv'

df = pd.read_csv(filename)

#adding new factor variables in the dataset, weekday and weekend
df['date'] = pd.to_datetime(df['date']) #converting the date column in the csv file to date time
df['dayOfweek'] = df['date'].dt.dayofweek #determining which day of the week it is
df['isWeekday'] = df['date'].dt.dayofweek < 5 #column for weekdays
df['isWeekend'] = df['date'].dt.dayofweek > 5 #column for weekends

#finding the average steps for the weekday
#separating it into a different dataframe
avgWkdy= pd.DataFrame(df['isWeekday'])
avgWkdy['interval'] = df['interval']
avgWkdy['steps'] = df['steps']

#finding the average steps for the weekend
#separating it into a different dataframe
avgWked = pd.DataFrame(df['isWeekend'])
avgWked['interval'] = df['interval']
avgWked['steps'] = df['steps']


#using the aggregate function to sort the average from each interval to either a weekday or a weekend
#weekday average
avgWkdy = avgWkdy.groupby(['interval', 'isWeekday']).agg({'steps':'mean'})

#weekend average
avgWked = avgWked.groupby(['interval', 'isWeekend']).agg({'steps':'mean'})

#resetting the indexes
avgWkdy = avgWkdy.reset_index()
avgWked = avgWked.reset_index()

#plotting the two graphs
#graph 1 (weekdays)
avgWkdy.plot('interval', 'steps', xlabel='Time Interval', ylabel='Average Number of Steps Taken', title='Weekdays', figsize=(20,6))
avgWked.plot('interval', 'steps',xlabel='Time Interval', ylabel='Average Number of Steps Taken', title='Weekends', color='purple', figsize=(20,6))
plt.show()








