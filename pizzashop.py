pizza = int(input('how many slices do you want\n'))
choice = ""
if pizza >= 8 and pizza <= 120:
    while choice != True and choice != False:
        choice = (input( "may be you want whole pizza\n"))
        if choice == "no":
            choice = False
        elif choice == "yes":
            choice = True
        else:
            print("write  yes or no")
    if choice == True:
        if pizza %8 == 0:
            print(f"{pizza // 8} pizza")
        else:
            print(f"sorry we can do {pizza // 8} whole pizza and {pizza % 8} slices")
elif pizza > 0 and pizza <8:
    print(f"here {pizza} slices for you, we can't give you a whole pizza becouse the minimum it's 8 slices for whole pizza")
elif pizza > 120:
    print("we cannot do tha many slises")
else:
    print("good joke")