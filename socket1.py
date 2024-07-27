import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=9876
s.bind((host,port))
s.listen(5)
while True:
    c, addr=s.accept()
    print("Got connection for",addr)
    s2="thankyou for connecting"
    c.send(s2.encode())
    print("HI.. how are you")
    c.close()
