d1 = int(input("please wirte here a day --\n"))
m1 = int(input("please write right here month --\n"))
y1 = int(input("please write here a year --\n"))
d2 = int(input("please write the second date (day) --\n"))
m2 = int(input("please write the second date (month) --\n"))
y2 = int(input("please write the second date (year) --\n"))

if y1 < y2:
    print("the first date is more earlyer then the second one")
elif y2 < y1:
    print("the second date is earlyer then the first one")
elif y2 == y1:
    if m1 < m2:
        print("the first date is more earlyer then the second one")
    elif m2 < m1:
        print("the second date is more earlyer then the first one")
    elif m2 == m1:
        if d1 < d2:
            print("the first date is more ealyer then the second one")
        elif d1 == d2:
            print("they are the same dates :)")