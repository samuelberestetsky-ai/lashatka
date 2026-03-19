aa = "     Hlelo  there   I                        am                really good      "
aa += " "
value = 0
for i in range (0,len(aa)):
    if aa[i] == " " and aa[i-1] != " ":
        value += 1
print(value)