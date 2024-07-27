'''
def my_function(fname):
    print(fname + "welcome")
my_function("hai")
my_function("hello")
'''

'''
def function(fname,lname):
    print(fname +" "+ lname)
a=input("enter a:")
b=input("enter b:")
function(a,b)
'''
'''
def my_function(child2,child1):
    print("the youngest child is"+child2)
my_function(child2="hai",child1="hello")
my_function("java","python")
'''
'''
def my_function(**kid):
    print("his last name is",kid["fname"],kid["lname"])
my_function(fname="raja",lname="ram")
'''
'''
def my_function(*kids):
    print("the youngest child is"+kids[1])
my_function("hai","hello")
'''

'''
def my_function(country="norway"):
    print("i am from" + country)
my_function("india")
my_function()
my_function("brazil")
'''
'''
def my_function(food):
    for x in food:
        print(x)
fruit=["apple","orange"]
hat=["a","b","c"]
my_function(fruit)
my_function(hat)
my_function("javapython")
'''

'''
#lambda function,.-

def my(a):
    return a*20
print(my(2))

x= lambda a:a-10
print(x(4))

x= lambda a,b,c:a+b+c+10
print(x(2,2,2))

def myfunc(n):
    return lambda a:a*n
x= myfunc(2)
print(x(2))
print(x(4))
'''

