from data_process import clean_csv
from convert2ics import csv2ics

tasks = clean_csv()
csv2ics(tasks,len(tasks))

#print(len(tasks))
#for i in tasks:
    #print(i)