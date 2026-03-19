import time , os
seconds = 0
minutes = 20
while True:
    print(f"{minutes}:{seconds}")
    if seconds == 0 and minutes == 0:
        print("your time is out")
        break
    if seconds == 0:
        minutes -= 1
        seconds = 60
    seconds -= 1
    time.sleep(1)
    os.system("cls || clear")