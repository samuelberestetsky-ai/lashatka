import random
aaa = ("")
balance = 130
casePrice = 130
weapon_case = ["🟦MP7| skull","🟦SG 553 | Ultraviolet","🟦AUG | Wings","🟪USP-S | Dark Water","🟪Glock-18 | Dragon Tattoo","🟪M4A1-S | Dark Water","🩷AK-47 | Case Hardened","🩷Desert Eagle | Hypnotic","🟥AWP | Lightning Strike"]
Chance = [30,30,30,5,5,5,3,3,0.5]
prices = [[35,37],[33,174],[33,34],[104,120],[442,568],[167,194],[500,1230],[172,194],[875,1531]]
while aaa != "no" and balance >= casePrice:
    balance -= casePrice
    weapon = random.choices(weapon_case, weights=Chance, k=1)[0]
    index = (weapon_case.index(weapon))
    print(f"name weapon case {casePrice}")
    weaponprice = random.randint(prices[index][0],prices[index][1])
    print(f"name {weapon} and price is {weaponprice} and price of you balance is {weaponprice + balance}")
    balance += weaponprice
    if balance >= casePrice:
        aaa = input("press enter to continiue or say no to stop\n")
    
    else:
        rrr = input("you out of money if you want to make some then say yes and if no then say no\n")
        if rrr == "no":
            print("thats ok good luck Br Br Br Br")
        if rrr != "no":
            kdkd = int(input("please fill your amount of money\n"))
            balance += kdkd