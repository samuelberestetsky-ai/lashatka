import time ,os
hour = 23
minute = 59
second = 40
day = 0
while True:
    os.system("cls || clear")
    print(f"{day}:{hour}:{minute}:{second}")
    second += 1 
    time.sleep(1)
    if second == 60:
        minute += 1
        second = 0
    if minute == 60:
        hour += 1
        minute = 0
    if hour == 24:
        day += 1
        hour = 0
        minute = 0
        second = 0