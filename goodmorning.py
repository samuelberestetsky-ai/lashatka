masiv = [-2,3,-6,4,-5,-3,-3,-3,-3,-3,-3,-3,-3] 
count = 0

while len(masiv)!= count:
    if masiv[count] < 0:
        z = masiv[count] * masiv[count]
        masiv.insert(count+1, z)
    count+=1
print(masiv)
    