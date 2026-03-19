#программа
#  должна
#  на
#  данный момент хранить
#  информацию о пользователях и также нужно написать
#  функцию входа в аккаунт по логину
#  и паролю
#  и функцию
#  регистрации
#  логина
#  и пароля логин
#  должен быть
#  уникальн
sdfsd = [
    {
        "username": "natawa",
        "password": "15701223",
        "balance": 25000
    },    
    {
        "username": "bobrino",
        "password": "19435667",
        "balance": 343233
    }
    ]
while True:
    print("--Menu--:)")
    print("1 -- Register!")
    print("2 -- Log in!")
    asd = input("Make a choice (1 / 2 / nothing) ==>  ")
    if asd == "1":
        cd = input("enter your username ---->  ")
        fb = input("enter password ---->  ")
        fb = fb.replace(" ", "")
        if len(fb) < 6:
            print("password must be more than 6 characters")
            continue
        print("check on you")
        result =  ""
        for user in sdfsd:
            if cd == user["username"]:
                result = "this usernameis already exist"
                
        print(result)
        if result == "":
            print("you are registered")
            sdfsd.append({"username":cd,
                "password":fb,
                "balance":0})
    elif asd == "2":
        vb = input("enter your username ---->  ")
        bf = input("enter password ---->  ")
        result = ""
        for user in sdfsd:
            if vb == user["username"]:
                if bf == user["password"]:
                    result = "you are log in"
                    while True:
                        print("-- Menu -- ")
                        print("1 -- check balance")
                        print("2 -- add money")
                        print("3 -- take money")
                        print("4 -- exit")
                        choice = input("Make a choice (1 / 2 / 3 / 4) ==>  ")
                        if choice == "1":
                            

                            print(user["balance"])


                        elif choice == "2":
                            sv = int(input("please add your balance in full numbers -- "))
                            user["balance"] += sv
                            print(user["balance"])
                        elif choice == "3":
                            fg = int(input("how much money do you want to take from your account?"))
                            if user["balance"] < fg:
                                print("Error")
                            else:
                                user["balance"] -= fg
                                print(user["balance"])
                        elif choice == "4":
                            break
                    break
                else:
                    result = "your password is in correct please try agian"
                    break
            else:
                result = "this username is not found"
        print(result)
        