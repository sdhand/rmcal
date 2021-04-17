#!/usr/bin/env python3

import datetime, calendar
from icalevents.icalevents import events
import sys
from string import Template

def datesuffix(d):
     return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

caltemplatef = open('rmcal.tex', mode='r')
caltemplate = caltemplatef.read()
caltemplatef.close()

current_year = datetime.datetime.now().year

icales = events(url=sys.argv[1], start=datetime.date(current_year, 1, 1), end=datetime.date(current_year+1, 1, 1))
es = {}

for e in icales:
    es.setdefault(e.start.date(),[]).append(e)

cal = calendar.Calendar()
days = zip(calendar.month_name[1:], cal.yeardatescalendar(current_year, width=1))

def get_events(day):
    day_events = ""
    if day in es:
        for e in es[day]:
            day_events+="\\truncate{\\textwidth}{\\scriptsize{"+e.start.strftime("%H:%M ")+"\\verb^"+e.summary+"^}}\\\\ "
    return day_events

caltex = ""
notetex = ""
month_counter = 1
for month in days:
    caltex += "\Month{"+month[0]+"}{"+str(current_year)+"}{"
    for week in month[1][0]:
        caltex += "\Week"
        monday = True
        for day in week:
            caltex += "{"
            if day.month == month_counter:
                if monday:
                    notetex += "\Weektodo{week"+day.strftime("%-W")+"}{Week "+day.strftime("%-W")+" "+str(current_year)+" - Beginning "+str(day.day)+"\\textsuperscript{"+datesuffix(day.day)+"} "+month[0]+"}{"+month[0]+"}"
                caltex += "\Day{"+str(day.day)+"}{"+get_events(day)+"}{"+str(day)+"}{"+("\hyperlink{week"+day.strftime("%-W")+"}{\checkmark }}" if monday else "}")
                notetex += "\Daynotes{"+str(day)+"}{"+day.strftime("%A ")+str(day.day)+"\\textsuperscript{"+datesuffix(day.day)+"} "+month[0]+" "+str(current_year)+"}{"+month[0]+"}"
            caltex += "}"
            monday = False
    month_counter += 1
    caltex += "}"

s = Template(caltemplate)
print(s.substitute(calendar=caltex, notepages=notetex))
