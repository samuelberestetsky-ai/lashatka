import random
def check (card):
    if "2" in card:
        return 2
    elif "3" in card:
        return 3
    elif "4" in card:
        return 4
    elif "5" in card:
        return 5
    elif "6" in card:
        return 6
    elif "7" in card:
        return 7
    elif "8" in card:
        return 8
    elif "9" in card:
        return 9
    elif "10" in card:
        return 10
    elif "J" in card:
        return 10
    elif "Q" in card:
        return 10
    elif "K" in card:
        return 10
    elif "A" in card:
        return 11









cards = ["2♠️","2♣️","2♥️","2♦️",
        "3♠️","3♣️","3♥️","3♦️", 
        "4♠️","4♣️","4♥️","4♦️",
        "5♠️","5♣️","5♥️","5♦️",
        "6♠️","6♣️","6♥️","6♦️",
        "7♠️","7♣️","7♥️","7♦️",
        "8♠️","8♣️","8♥️","8♦️",
        "9♠️","9♣️","9♥️","9♦️",
        "10♠️","10♣️","10♥️","10♦️",
        "J♠️","J♣️","J♥️","J♦️",
        "Q♠️","Q♣️","Q♥️","Q♦️",
        "K♠️","K♣️","K♥️","K♦️",
        "A♠️","A♣️","A♥️","A♦️",] 
retue = []
for i in range(3): 
    score = 0 
    print(f"====GAME FOR PLAYER {i + 1}===")  
    for i in range(2):
        randomcard = random.choice(cards)  
        cards.remove(randomcard)  
        print(randomcard) 
        score += check(randomcard) 
    print("you score is",score) 
    while True:  
        vitaminC = input("do you want to take more \n")  
        if vitaminC == "yes":  
            randomcard = random.choice(cards)  
            cards.remove(randomcard) 
            score += check(randomcard)
            print(randomcard)  
        elif vitaminC == "no":
            print("you score is",score)  
            retue.append(score)  
            break 
        else: 
            print("say just yes or no") 
        print("you score is",score) 
        if score > 21: 
            print("you lost") 
            retue.append(score)
            break
print(f"\n Games over this is the score: {retue}")
winner = 0
for i in retue :
    if i <= 21:
        if i > winner:
            winner = i
for i in retue :
    if i == winner:
        print(f"the winner is player {retue.index(i) + 1}")