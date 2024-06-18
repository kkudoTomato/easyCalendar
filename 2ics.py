from icalendar import Calendar, Event, Alarm
from datetime import timedelta
import csv 

def createCalendar():
    cal = Calendar()
    cal.add('VERSION','2.0')
    cal.add('X-WR-CALNAME','生成ics文件测试')
    cal.add('X-APPLE-CALENDAR-COLOR','#540EB9')
    cal.add('X-WR-TIMEZONE','Asia/Shanghai')

    event = Event()
    event.add('UID','2000')
    event.add('DTSTART;VALUE=DATE','20240618T180500')
    #event.add('DURATION','PT1H15M0S')
    event.add('DURATION;VALUE=TIME','PT0H15M0S')
    event.add('SUMMARY','测试事件键')
    event.add('SEQUENCE','0')
    event.add('DESCRIPTION','这是描述')
    event.add('LOCATION','这是地点')
    alarm=Alarm()
    alarm.add('ACTION','NONE')
    alarm.add('TRIGGER;VALUE=DATE-TIME','20240618T180500')
    event.add_component(alarm)

    eventt=Event()
    eventt.add('UID','2001')
    eventt.add('DTSTART;VALUE=DATE','20240618T180500')
    eventt.add('DTEND;VALUE=DATE','20240619T182000')
    eventt.add('SUMMARY','测试事件2')
    eventt.add('SEQUENCE','0')
    eventt.add('DESCRIPTION','这是描述2')
    eventt.add('LOCATION','这是地点2')
    alarmm=Alarm()
    alarmm.add('ACTION','NONE')
    alarmm.add('trigger', timedelta(hours=-1))
    alarmm.add('description', 'Reminder: Event in 1 hour')
    eventt.add_component(alarmm)

    cal.add_component(event)
    cal.add_component(eventt)
    f = open('example.ics', 'wb')
    f.write(cal.to_ical())
    f.close()
    print(cal.to_ical().decode('utf-8')) 


createCalendar()