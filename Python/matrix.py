a=[]
b=[]
c=[]

temp=[]
x=int(input("enter the row of first matrix:"))
y=int(input("enter the column of first matrix:"))
m=int(input("enter the row of second matrix:"))
n=int(input("enter the column of second matrix:"))
if(y==m):
     print("Enter the A value : ")
     for i in range(x):
            for j in range(y):
                str1="Enter the value of [{}] [{}] : ".format(i,j)
                temp.append(int(input(str1)))
            a.append(temp)
            temp=[];
     print(a)
     print("Enter the B value : ")
     for i in range(m):
                      for j in range(n):
                          temp.append(int(input()))
                      b.append(temp)
                      temp=[];
     print(b)
     for i in range(m):
                      for j in range(n):
                          temp.append(0)
                      c.append(temp)
                      temp=[];
    
     for i in range(x):
                              for j in range(y):
                                  c[i][j]=0
                                  for k in range(m):
                                      c[i][j]=c[i][j]+a[i][k]*b[k][j]
     print("Answer is : ")
     for i in range(x):
                                          print(c[i])
else:
    print("multiplication is possible:")
                

        
