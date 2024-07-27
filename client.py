import socket              

s = socket.socket()         
host = socket.gethostname() 
port =9876              

s.connect((host, port))
a=s.recv(1024)
print(a.decode()+" I am fine","i am client")
s.close()