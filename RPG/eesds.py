a = int(input(""))
b = int(input(""))
c = int(input(""))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("это равносторонний !!!!!!!!!!!!!!")
    elif a == b or a == c or b == c:
        print("равнобедренный")
    elif a != b != c:
        print("разносторонний")
else:
    print("не треугольник")