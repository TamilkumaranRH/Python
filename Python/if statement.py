
num=int(input("Enter any number between 1to7:"))
try:
    if(num==1):
        print("sunday")
    elif(num==2):
        print("monday")
    elif(num==3):
        print("tuesday")
    elif(num==4):
        print("wednesday")
    elif(num==5):
        print("thursday")
    elif(num==6):
        print("friday")
    elif(num==7):
        print("saturday")
else:
    print("Nothing went wrong")
'''
def a():
    a=[1,2,3,4,5,6]
    if a%2==0:
        even=[]
        a.append(even)
        print(a,"is even number:")
    else:
        odd=[]
        odd.append(a)
        print(a,"is odd number:")
    
'''

a1=[1,2,3,4,5,6]
for a in a1:
    if a%2==0:
        print(a,"is even number")
    else:
        print(a,"is odd number:")

'''
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
def a1():
    if(a+b):
        print("Add:",a1)
    elif(a-b):
        print("Sub:",a1)
    elif(a*b):
        print("Multiple:",a1)
    elif(a/b):
        print("divide:",a1)
'''
'''
def addition(n1,n2):
    return n1+n2
def subtraction(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2
print("select number is")
print("1.Addition \n"
      "2.Subtraction \n"
      "3.Multiply \n"
      "4.division \n")
select=int(input("enter a number 1/2/3/4:"))
n1=int(input("enter a number:"))
n2=int(input("enter a number:"))        
if select == 1:
    print(n1, "+", n2, "=",add(n1, n2))
 
elif select == 2:
    print(n1, "-", n2, "=",subtract(n1, n2))
 
elif select == 3:
    print(n1, "*", n2, "=",multiply(n1, n2))
 
elif select == 4:
    print(n1, "/", n2, "=", divide(n1, n2))
else:
    print("Invalid input")

'''
'''
print("select number is")
print("1.adm no\n"
      "2.armstrong \n"
      "3.palindrome\n"
      "4.fibonnaci \n"
      "5.factorial \n")
select=int(input("choice the number:1/2/3/4/5:"))
if select==1:
    def adamno():
         a=144
         b=0
         while(a>0):
             r=a%10
             b=(b*10)+r
             a=a//10
         print(b)
    
elif select == 2:
    def armstrong():
        strong=153
        a=strong
        b=0
        while(a>0):
            r=a%10
            b=b+r**3
            a=a//10
        print(b)
         
elif select == 3:
    def palindrome():
        a=input('enter a name:')
        txt=a[::-1]
        print(a)
        print(txt)

elif select == 4:
    def fibonnaci():
        a,b=0,1
        fib=8
        print(a,b,end='')
        for i in range(fib):
            c=a+b
            print(c,end='')
            a=b
            b=c

elif select==5:
    def factorial():
        i=1
        num=5
        fact=1
        for i in range(i,num+1):
            fact=fact*i
            print("factorial:",fact)
else:
    print("Invalid input")
 '''     

   
   

     


