from icalendar import Calendar, Event, Alarm
from datetime import timedelta

"""
tasks_list: list of csv events
ntask: number of tasks that we have to create 
"""
def csv2ics(tasks_list, ntask):
    # put the header in 
    cal = Calendar()
    cal.add('VERSION','2.0')
    cal.add('X-WR-CALNAME','日程安排')
    cal.add('X-APPLE-CALENDAR-COLOR','#540EB9')
    cal.add('X-WR-TIMEZONE','Asia/Shanghai')

    event_list = list()
    for i in range(ntask):
        event_list.append(Event())
        event_list[i].add('UID',f'{2000+i}')
        event_list[i].add('dtstart',tasks_list[i][0])






    pass