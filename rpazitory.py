a = [2132,2,2,2,2,2,2,2,2,132213,2133,3123,213,213]
ns = []
vd = []

for i in a:
    if i % 2 == 0:
        ns.append(i)
    else:
        vd.append(i)
print(ns,vd)