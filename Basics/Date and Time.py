from datetime import datetime

dt1 = datetime(2020, 7, 20, 11, 30, 0)
dt2 = datetime(2021, 2, 20, 10, 25, 0)

print(dt1)
print(dt2)
print("The difference is", dt2 - dt1) #Output is 'The difference is 214 days, 22:55:00'
print(dt1.strftime('%A %B %d %Y %H:%M:%S')) #Output is 'Tuesday April 20 2021 11:30:00'
