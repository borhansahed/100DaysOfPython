import time

timestamp = int(time.strftime('%H'))
print(timestamp)

if(timestamp > 12):
    timestamp = timestamp - 12
    print(timestamp)
print(timestamp)