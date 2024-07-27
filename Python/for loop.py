'''
#simple for
for x in range(30):
    print("we're on time",x)

'''
'''
#for and break
for x in range(30):
    if x==2:
        break
    print(x)
'''
'''
#for else
for x in range(3):
    print(x)
    if(x==5):
        break
    else:
        print('loop ended')
'''
'''
#for using string
string="hello world"
for x in string:
    print(x)
'''
'''
#collection in for loop
collection=['hi',5,'d']
for x in collection:
    print(x)
'''
'''
#nested loop
adj=["red","blue"]
fruits=["apple","orange"]
for x in adj:
    for y in fruits:
        print(x,y)
'''
'''
#list in forloop
list=[[1,2,3],[4,5,6],[7,8,9]]
for l in list:
    print(1)
    for x in l:
        print(x)
'''
'''
#continue statement
fruits=["apple","banana","cherry"]
for x in fruits:
    if x=="banana":
        continue
    print(x)
'''
'''
#increase value 3
for x in range(2,60,50):
    print(x)
'''
'''
#pass statement
for x in range(7):
    pass
'''
'''
a=0
b=1
fibonacci=8

print(a, b)
for i in range(fibonacci):
    c = a + b
    print(c)
    a = b
    b = c 
'''
'''
i=1
num=5
fact=1
for i in range(1,num+1):
    fact=fact*i
    print("factorial:",fact)
'''
