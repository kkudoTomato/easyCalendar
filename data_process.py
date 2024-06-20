import csv
from datetime import timedelta, datetime

def clean_csv(fullPath):
    tasks = list()


    with open(fullPath) as input:
        csv_reader = csv.reader(input, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Header row - {", ".join(row)}')
                line_count += 1
            else:
                row[0] = datetime.fromisoformat(row[0])
                dur_time_list = row[1].split(':')
                if len(dur_time_list) > 1:
                    dur_time_str = f'PT{dur_time_list[0]}H{dur_time_list[1]}M0S'
                row[1] = dur_time_str

                tasks.append(row)

                #print(f'{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}')
                line_count += 1
            

        #print(f'Total: {line_count} lines')
        #for i in tasks:
        #    print(i)
        return tasks

