def  check(a):  

 if(a%2==0):
    return 1#even
 else:
    return 0#odd


a=int(input("Enter no:"))
b=int(input("Enter no:"))
c=int(input("Enter no:"))

i=check(a)+check(b)+check(c)

print(i)

if(i==0):
    print(a+b+c)
elif(i==1):
    print(a-b-c)
elif(i==2):
    print(a*b*c)
elif(i==3):`
    print(a/b/c)
    
