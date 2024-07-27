'''
#arithmetic operator
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)
'''
'''
#logical
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print(a<b and a>b)
print(a>b or a<b)
print(not(a<b and a>b))
'''
'''
a=11
if(a>5):
    if(a<10):
        print("yeah")
    else:
        print("oopsss")
elif(a>10):
    print("greater than 10")
else:
    print("no")
'''
'''
a=input("Enter your Name:")
b=int(input("Enter your Age:"))
c=input("Enter your place:")
if(b>18 and c=="mayiladuthurai"):
    print(a,"your eligible for voting")
else:
    print("your not eligible for voting")
'''
'''
a=int(input("enter a number:"))
if(a==18):
    print("excellent")
elif(a>=18):
    print("good")
else:
    print("bad")
 '''
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
if(a>b and b<a):
    print("a is a largest number")
elif(b>c):
    print("b is a largest number")
else:
    print("c is a largest number")



