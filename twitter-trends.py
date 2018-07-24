#generating Twitter World Trends for
from twitter import *
import csv
from pandas import DataFrame as df
import numpy as np
from datetime import date, datetime

access_key = '415534051-J3LdrCL77ckIlUSrwo4a1erZoiCIq362YMhsdqX9'
access_secret = 'LzWNo62DbPnT6hgakEQOrs6dSK28RZsX1PnwVOcHoHqsR'
consumer_key = 'Rks5Yq74klwrNwtdPCJt9Ubs4'
consumer_secret = 'KGUDLbRKONZO53jtUzzmGRoHcgZJc69jspMyEJJAvh55xycOXA'

twitter = Twitter(auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))
#results = twitter.trends.place(_id = 23424977)

today = date.today()
time_now = datetime.now()
time_now = str(time_now.hour).zfill(2) + str(time_now.minute).zfill(2) + str(time_now.second).zfill(2)
today_str = str(today.year) + str(today.month).zfill(2) + str(today.day).zfill(2) + str(time_now)
print ('Started generating Twitter World Trends for ' + today_str)

filename = 'twitter_trends_' + today_str + '.csv'
with open(filename,'w') as output:
   fieldnames = ['place', 'name','url', 'promoted_content', 'query', 'tweet_volume']
   trendswriter = csv.DictWriter(output, fieldnames=fieldnames,delimiter=',', lineterminator='\n')
   trendswriter.writeheader()
   places = {'UK':23424975, 'USA':23424977, 'Germany':23424829, 'Nigeria':23424908, 'Kenya':23424863, 'Nigeria':23424908, 'India':23424848}
   for key,val in places.items():
      results = twitter.trends.place(_id = val)
      for location in results:
         for trend in location['trends']:
            trend['place'] = key
            trendswriter.writerow(trend)

print ('Done.....filename = ' + filename)                        























