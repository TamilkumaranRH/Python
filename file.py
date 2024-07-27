#open("new1.txt","x")

""" f=open("new1.txt","w")
f.write("something231") """

""" f=open("new1.txt","a")
f.write("\tsomething231") """

""" f=open("new1.txt","r")
a=f.read()

print(a.split("\n")) """

"""import os
os.remove("new1.txt") 
os.rmdir("sdflkj")"""

""" name=input("Enter your name:")
age=int(input("Enter your age:"))
place=input("Enter your place:")

f=open("new1.txt","a")
f.write("\n"+name+"\t"+str(age)+"\t"+place) """

""" user="tamil"
password="nvurh"
age="20"
f=open("new1.txt","r")
data=f.read().split("\n")
print(data)
for d in data:
    info=d.split("\t")
    if(info[0]==user and info[1]==age and info[2]==password):
        print("user success")
        break
else:
        print("not") """