import pandas as pd
import datetime

day_header = 'Day'
event_header = 'Event'
email_header = 'Email'
start_header = 'Start'
stop_header = 'Stop'
readable_start_header = 'Readable Start'
readable_stop_header = 'Readable Stop'

submissions = pd.read_csv('submissions.csv')
schedule = pd.read_csv('schedule.csv')


days_to_string = {1:'thursday', 2:'friday'}
day_starts = {'thursday':datetime.datetime(2018,6,26,8,45), 'friday':datetime.datetime(2018,6,27,8,30)}
remarks_time = datetime.timedelta(minutes=5)
coffee_times = {'thursday':datetime.timedelta(minutes=25), 'friday':datetime.timedelta(minutes=25)}
talk_time = datetime.timedelta(minutes=20)
lunch_times = {'thursday':datetime.timedelta(minutes=75), 'friday':datetime.timedelta(minutes=75)}
transition_time = datetime.timedelta(minutes=5)

# First pass, just compute the start times of everything

days = list(schedule[day_header])
events = list(schedule[event_header])
start_times = list(schedule[start_header])
stop_times = list(schedule[stop_header])

start_times[0] = day_starts['thursday']

def time_to_add(prev_event, cur_event, day):
    if prev_event == 'talk' and cur_event == 'talk':
        return talk_time + transition_time
    if prev_event == 'talk' and (cur_event == 'lunch' or cur_event == 'coffee'):
        return talk_time
    if prev_event == 'remarks' and cur_event == 'talk':
        return remarks_time
    if prev_event == 'lunch':
        return lunch_times[day]
    if prev_event == 'coffee':
        return coffee_times[day]

i = 1

while int(days[i]) == 1:
    start_times[i] = start_times[i-1] + time_to_add(events[i-1],events[i], 'thursday')
    i += 1

start_times[i] = day_starts['friday']
i += 1

while i < len(days):
    start_times[i] = start_times[i-1] + time_to_add(events[i-1],events[i], 'friday')
    i += 1

# Second pass, I'll add the correct amount of time for each event

# times = {'remarks':remarks_time, 'coffee':coffee_times, 'talk':talk_time, 'lunch':lunch_time}    

def the_times(event, day):
    if event == 'talk':
        return talk_time
    if event == 'remarks':
        return remarks_time
    if event == 'coffee':
        return coffee_times[day]
    if event == 'lunch':
        return lunch_times[day]

for i in range(len(start_times)):
    stop_times[i] = start_times[i] + the_times(events[i], days_to_string[days[i]])

# Update and save

schedule[start_header] = start_times
schedule[stop_header] = stop_times

# Update with printable times

def time_string(time):
    suf = "am"
    if time.hour >= 12: suf = 'pm'
    hour = time.hour % 12
    if hour == 0: hour = 12
    minute = "%02d" % time.minute
    return str(hour) + ":" + minute + suf

schedule[readable_start_header] = [time_string(time) for time in start_times]
schedule[readable_stop_header] = [time_string(time) for time in stop_times]

schedule.to_csv('schedule.csv')









