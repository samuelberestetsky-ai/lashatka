number = int(input("Enter a number (0 to stop): "))
values = 0
while number != 0:
    print(f"you enter {number}")
    if number%2 == 0:
        values += number
    number = int(input("please enter baby to stop the program and to know wich number you get from the calcultion"))
print(f"the number is {values}")