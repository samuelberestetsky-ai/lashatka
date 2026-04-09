b = 1234
d = 0
while b > 0:
    d *= 10
    d += b % 10
    b //= 10
print(d)