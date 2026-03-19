def check ():
        baba = input("enter your user name\n")
        while len(baba) > 10:
                baba = input("the user name  need to be 10 letters max")
        return (baba)
def sing_up (Lowka): 
        user = check ()
        pas = input("Please write your passwword Here   \n")
        Lowka[0].append(user)
        Lowka[1].append(pas)
        Lowka[2].append(0)
        return (Lowka)
def entera (masive):
        usern = input("enter you user\n")
        passn = input("enter password\n")
        if usern in masive[0]:
                userindex = masive[0].index(usern)
                if masive[1][userindex] == passn:
                        print("you have enter account")
                        return True,userindex
                else:
                        print("invaild password or user")
                        return False , None
        else:
                print("invaild password or user")
                return False , None

def main ():
        html = [["Zaika13","Babior1","Umnik15","Hlopchik17"],
        ["password1","password2","password3","password4"],
        [98736,1234333,9999989,999999981]
        ]
        while True:
                print("1 enter account","\n2 registar","\n3 quit")
                steps = input()  
                if steps == "2":
                        html = sing_up(html)
                elif steps == "3":
                        break
                elif steps == "1" :
                        enter,index = entera(html)
                if enter:
                        while True:
                                print("1 change user\n2 top up your Balnce\n3 quit")
                                step1 = input("")
                                if step1 == "1":
                                        Mc = check()
                                        if Mc not in html[0]:
                                                html[0][index] = Mc
                                        else:
                                                print("this user name allready exist") 
                                        print(html)


                                elif step1 == "2":
                                        abc = int(input("how much do you want to top up your balance\n"))
                                        html[2][index] += abc
                                        print(html[2][index])
                                elif step1 == "3":
                                        break



if __name__ == "__main__": main()