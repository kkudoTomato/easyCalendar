from icalendar import Calendar, Event, Alarm
from datetime import timedelta

"""
tasks_list: list of csv events
ntask: number of tasks that we have to create 
"""
def csv2ics(tasks_list, ntask):
    # put the header in 
    cal_list = list()
    for i in range(4):
        cal_list.append(Calendar())
        cal_list[i].add('VERSION','2.0')
        cal_list[i].add('X-WR-TIMEZONE','Asia/Shanghai')

    cal_list[0].add('X-WR-CALNAME','Work Plan')
    cal_list[1].add('X-WR-CALNAME','Gym Plan')
    cal_list[2].add('X-WR-CALNAME','Chores Plan')
    cal_list[3].add('X-WR-CALNAME','Break Plan')

    cal_list[0].add('X-APPLE-CALENDAR-COLOR','#ff8000')
    cal_list[1].add('X-APPLE-CALENDAR-COLOR','#b3903f')
    cal_list[2].add('X-APPLE-CALENDAR-COLOR','#33aaee')
    cal_list[3].add('X-APPLE-CALENDAR-COLOR','#98cf8b')
    # note cal_list[0] is for work, 1 is for gym, 2 is for chores, 3 is for break
    #cal = Calendar()

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
        if tasks_list[k][4] == 'work':
            cal_list[0].add_component(event_list[k])

        if tasks_list[k][4] == 'gym':
            cal_list[1].add_component(event_list[k])

        if tasks_list[k][4] == 'chores':
            cal_list[2].add_component(event_list[k])

        if tasks_list[k][4] == 'break':
            cal_list[3].add_component(event_list[k])

    #f = open('workPlan.ics', 'wb')
    #for i in range(len(cal_list)):
    #    f.write(cal_list[i].to_ical())
    #f.close()


    f = open('workPlan.ics', 'wb')
    f.write(cal_list[0].to_ical())
    f.close()

    f = open('gymPlan.ics', 'wb')
    f.write(cal_list[1].to_ical())
    f.close()

    f = open('ChoresPlan.ics', 'wb')
    f.write(cal_list[2].to_ical())
    f.close()

    f = open('breakPlan.ics', 'wb')
    f.write(cal_list[3].to_ical())
    f.close()

    #print(cal.to_ical().decode('utf-8')) 






    pass