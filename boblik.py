import random
aaa = ("")
balance = 0
balancecomp = 0
while aaa != "no":
    asdfs = random.randint(1,6)
    kfk= input("press enter to throw the cube")
    print(asdfs)
    asdf = random.randint(1,6)
    print(f"computer turn    {asdf}")
    if asdfs > asdf:
        print("computer win")
        balancecomp += 5
    elif asdf > asdfs:
        balance += 5
        print("you win")
    else:
        print("your score is same")
    print("your score:",balance)
    print("compscore",balancecomp)
    aaa = input("do you want to play more if yes click please on enter and if no the say no")