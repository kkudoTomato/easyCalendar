from data_process import clean_csv
from convert2ics import csv2ics
import os

print('The file must be in the download folder, and enter the date in format month(0)_date(0)')
fileName = input().strip()
pathName = '/Users/door3/Downloads/daily_plan - '
fullPath = f'{pathName}{fileName}.csv'

tasks = clean_csv(fullPath)

csv2ics(tasks,len(tasks),fileName)

if os.path.exists(fullPath):
  os.remove(fullPath)
else:
  print("The file does not exist")

#print(len(tasks))
#for i in tasks:
    #print(i)