import turtle as t 
from def1 import xy 
 
print("where do you want to put first point")  
x1 = int(input(""))  
x2= int(input(""))   
x1*= 30   
x2*= 30     
t.speed(5)   
t.hideturtle()   
xy ()  
t.up()  
t.goto(x1,x2)  
t.down()  
t.dot(10)  
for i in range(6):  
    print("write anther point")  
    y1= int(input(""))  
    y2= int(input(""))   
    y1 *= 30  
    y2 *= 30  
    t.goto(y1,y2)  
    t.dot(10)  
t.done()  