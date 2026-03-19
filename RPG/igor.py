import time

time1 = int(input("Please enter a number in sec"))
while time1 != 0:
    time.sleep(1)
    time1 -= 1
    print(time1 + 1)
if time1 == 0:
    print("timer ended, you can exit your")