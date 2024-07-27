'''
x=1
y=2
z=5
while(z>0):
    a=x+y
    x=y
    y=a
    print(a)
    z-=1
'''
'''
def factorial(n):
    num=1
    while num>=1:
        num=num*n
        n=n-1
    return num
f=factorial(5)
print(f)
'''
'''
num=1
z=5
n=5
while(num>=1):
    num=num*n
    n=n-1
    print(num)
    z=-1
 '''
'''
num=1
factorial=5
while(num>1):
    factorial=factorial*num
    num=num-1
    print(factorial)
 '''
'''
num = 1
n=5
fact=num
while n >= 1:
    num *= n
    n -= 1
    result=fact(5)
    print("Factorial of 5:", result)

print("Enter the Number: ")
num = int(input())
'''
'''
num=int(input('Enter a number:'))
fact = 1
i = 1
while i<=num:
    fact = fact*i
    i = i+1

print("\nFactorial =", fact)
'''

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1)) #5*4*3*2*1

num = 5
print("The factorial of", num, "is", factorial(num))
    
       
        
    
