greats ={"sasha":5,
         "dasha":2,
         "anton":5} 
greats["sasha"] = 3
greats["oleg"] = 1
del greats["anton"]
greats["sonya"] = 4
#print (greats.keys())
#print (greats.values())

for i in greats:
    if greats[i]>2:
        print(i)