'''
try:
    n=int(input("Enter number:"))
    assert n%2==0
except:
    print("Not in even number")
else:
    a=1/n
    print(a)
'''

#x=2
#print(x)
'''
x="t"
y=2
z=x+y
print(z)
'''

'''
mySet = [1, 2, 3]
myList = [4, 5, 6]
result=mySet+myList
print(result)
'''

'''
myset={'t','a','m','i','l'}
print(myset)
'''

'''
geek = "GeeksforGeeks"
print(geek())
'''

'''
geeky_list = ["geek", "GeeksforGeeks", "geeky", "geekgod"]
index = "1"
print(geeky_list[index])
'''

try:
    x=int(input("Enter a number:"))
    y=10%x
    print("the result is:",y)
except ValueError:
    print("you must enter a valid intrger.")
except ZeroDivisionError:
    print("you cannot divide by zero.")
