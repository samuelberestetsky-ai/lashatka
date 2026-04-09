import time
masiv = [1,2,3,4,5,6,7]*1000000
visam = []
start = time.time()
z = len(masiv) // 2
for i in range(len(masiv)):
    if i > z:
        visam.append(masiv[i])
for i in range(len(masiv)):
    if i <= z:
        visam.append(masiv[i])
end = time.time()
print(end - start)

masiv = [1,2,3,4,5,6,7]*100000000
visam = []
start = time.time()
z = len(masiv) // 2
visam = masiv[z:]+masiv[:z]

end = time.time()

print(end - start)