import random
massive = []
value = 0
for i in range(200):
    sd = random.randint(-100,100)
    massive.append(sd)
"""for b in  massive:
    if b < 0:
        value += 1"""

onion = -99
for d in massive:
    if d > onion:
        onion = d
print(massive)
print(onion)

for i in range(len(massive)):
    onion -= 1
    if onion in massive:
        print(onion)
        break