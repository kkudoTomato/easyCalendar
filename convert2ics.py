from icalendar import Calendar, Event, Alarm
from datetime import timedelta

"""
tasks_list: list of csv events
ntask: number of tasks that we have to create 
"""
def csv2ics(tasks_list, ntask,fileName):
    # put the header in 
    cal = Calendar()
    cal.add('VERSION','2.0')
    cal.add('X-WR-CALNAME','日程安排')
    cal.add('X-APPLE-CALENDAR-COLOR','#540EB9')
    cal.add('X-WR-TIMEZONE','Asia/Shanghai')

    event_list = list()
    alarm_list = list()
    for j in range(ntask):
        alarm_list.append(Alarm())

    for i in range(ntask):
        event_list.append(Event())
        event_list[i].add('UID',f'{2000+i}')
        event_list[i].add('dtstart',tasks_list[i][0])
        event_list[i].add('DURATION;VALUE=TIME',tasks_list[i][1])


        event_list[i].add('SUMMARY',tasks_list[i][2])
        event_list[i].add('SEQUENCE','0')

        event_list[i].add('DESCRIPTION',tasks_list[i][3])

        #event_list[i].add('LOCATION','这是地点')

        #alarm_list[i].add('ACTION','NONE')
        #alarm_list[i].add('TRIGGER;VALUE=DATE-TIME','20240618T180500')
        #event.add_component(alarm)


    for k in range(ntask):
        cal.add_component(event_list[k])




    target_name = f'{fileName}_Plan.ics'

    f = open(target_name, 'wb')
    f.write(cal.to_ical())
    f.close()
    print(cal.to_ical().decode('utf-8')) 






    pass