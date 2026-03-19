side = [2,12,13]
o = 0
for i in side:
    o += 1
if o == 3 and side[0] + side[2] > side[1] and side[1] + side[0] > side[2] and side[2] + side[1] > side[0]:
    print("This is a tringle")
    if side[0] != side[1] != side[2]:
        print("This is scalene")
    elif side[0] == side[1] == side[2]:
        print("This is equilateral tringle")
    else:
        print("This is isosceles tringle")
        
else:
    print("This isnt a tringle")