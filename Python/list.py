'''
Name=[]
Age=[]
Course=[]
Place=[]
n=int(input("Number of student:"))
while n>0:
    a=input("Enter your name:")
    Name.append(a)
    b=int(input("Enter your age:"))
    Age.append(b)
    c=input("Enter your course:")
    Course.append(c)
    p=input("Enter your place:")
    Place.append(p)
    n-=1
print(Name)
print(Age)
print(Course)
print(Place)

c=0
while c==0:
    b=0
    n=input("Enter the name want to you want to search : ")
    for x in Name:
        if n==x:
            print(Name[b])
            print(Age[b])
            print(Course[b])
            break
        else:
            b+=1
    else:
        print("no data found !!!")
    c=int(input("do you want continue enter 0"))

'''
'''
a=['name:tamil,age:20,course:bsc']
b=['name:rabin,age:20,course:bsc']
list=['a','b']
if(a,b in list):
    print("tamil is present",a)
else:
    print("tamil is not present",a)
    
if(a,b not in list):
    print("surya is not present")
else:
    print("surya is present")
    
'''


""" n=5
for i in range(n):
    for j in range(i,n):
        print('',end='')
    for j in range(i+1):
        print('*',end='')
    print()  """


""" n=5
for i in range(n):
    for j in range(i,n):
        print('',end='')
    for j in range(i-1):
        print('*',end='')
    for k in range(i,n-1):
        print('',end='')
    print()
 """

""" n=5
for i in range(n):
    for j in range(i,n):
        print('*',end='')
    for j in range(i+1):
        print('',end='')
    print() """

'''
n=5
for i in range(n):
    for j in range(n):
        print('*',end='')
    print()    
'''
'''
n=5
for i in range(n):
    for j in range(i,n):
        print('',end='')
        
    for j in range(i):
        print('*',end='')
        
    for j in range(i+1):
        print('*',end='')
        
    print()
'''
'''
n=5
for i in range(n):
    for j in range(i+1):
        print('',end='')
        
    for j in range(i,n-1):
        print('*',end='')
        
    for j in range(i,n):
        print('*',end='')
        
    print()
'''


""" n=10
i=0
j=1
while(n>0):
    print(" "*n+"*"*i+"*"*j+"*"*i+" "*n)
    i+=1
    n-=1 """
    
