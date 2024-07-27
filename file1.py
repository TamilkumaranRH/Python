select1=int(input("Enter a number 1/2/3:"))
def login():
     if select1==1:
          Name=input("Enter your name:")
          Course=input("Enter your course:")
          Salary=int(input("Enter your salary:"))
          f=open("employee.txt","a")
          f.write("\n"+Name+"\t"+Course+"\t"+str(Salary))
def register():
     if select1==2:
          select=input("choose employee:")
          f=open("employee.txt","r")
          data=f.read().split("\n")
          print(data)
          for d in data:
             info=d.split("\t")
             if(info[0]==select):
                  print(info)
                  print("user success")
                  break
          else:
           print("not")