word = "I like somethig somethinz supercool" + " "
count = 0
book = ""
maximumword = {}
maxiumimcount = 0
for i in word:
    if i != " ":
        count += 1
        book += i


    else:
        if count > maxiumimcount:
            maxiumimcount = count
        maximumword[book] = count
        count = 0
        book = ""
for i in maximumword:
    if maximumword[i] == maxiumimcount:
        print(i)