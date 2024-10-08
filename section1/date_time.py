import datetime

date=datetime.date(2025,1,2)

# to get current date
today=datetime.date.today()
print(today)
print(date)

time=datetime.time(12,30,0)
# to get the current time
now=datetime.datetime.now()

#u can format the output
now1=now.strftime("%H %M %S %m %d %Y")
print(now1)
print(time)

print(now)

target_datetime=datetime.datetime(2030,1,2,12,30,1)
print(target_datetime)
current_datetime=datetime.datetime.now()
print(current_datetime)
if current_datetime<target_datetime:
    print("not there yet")
else:
    print("yay u there")