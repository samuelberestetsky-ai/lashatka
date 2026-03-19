customer= {"pasha":[100,200,500,400],
         "masha":[130,40,52],
         "sasha":[200,25,25],
         "dasha":[75,85,100],
         "dimon":[36,24,28,15,17]}
maxiumum = 0
for i in customer:
    values = 0
    for d in customer[i]:
        values += d
        customer[i] = values
    if values > maxiumum:
        maxiumum = values
for i in customer:
    if customer[i] == maxiumum:
        print(i)
print(maxiumum)