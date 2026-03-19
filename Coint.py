import random 
fj = "" 
score = 0
scoreComp = 0
while not(score == 3 or  scoreComp == 3):
    BRBR = ["🦅","🪙"] 
    randomcoin = random.choice(BRBR) 
    guess = input(f"guess what will be 🪙 🦅\n") 
    if guess == randomcoin: 
        print("GOOD JOBE Nice Very Very Cheap One Pound Fish") 
        score += 1
    elif guess == "🪙" or guess == "🦅":
        print("eeeee")
        scoreComp += 1
    else: 
        print("Error")
    print(f"user :{score} computer :{scoreComp}")

         
 
#🪙  
#🪙 