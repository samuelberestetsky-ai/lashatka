hours = int(input("please put hours"))
minutes = int(input("please enther minutes"))
secounds = int(input("please enter secounds"))
day = 0
while secounds >= 60:
    secounds -= 60
    minutes += 1
while minutes >= 60:
    minutes -= 60
    hours += 1
while hours >= 24:
    hours -= 24
    day += 1
print(day,hours,minutes,secounds)