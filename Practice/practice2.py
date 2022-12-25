import time

timeLine = time.strftime('%H:%M:%S')
hour = int(input("Enter Hour : "))
# print(timeLine)

timestamp = time.strftime('%H')
if hour > 25:
    print("Invalid hour ")
elif hour < 4:
    print("Mid Night")
elif hour >= 4 and hour < 12:
    print("Good morning")

elif hour > 12 and hour < 15:
    print("Lunch Time")
elif hour > 15 and hour <= 20:
    print("Good Afternoon")
elif hour > 20:
    print("Good night")
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
