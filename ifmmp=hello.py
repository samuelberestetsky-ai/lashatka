a = "zoo"
v = "abcdefghijklmnopqrstuvwxyz"
c = ""
h = ""
for i in a:
    if i == " ":
        c += " "
    if i == "z":
        c += "a"
    for x in range(len(v)-1):
        if v[x] == i:
            c += v[x + 1]
for n in c:
    if n == " ":
        h += " "
    for b in range(len(v)):
        if v[b] == n:
            h += v[b-1]
print(h)
