import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect("abc.gmail.com", 80)
cmd = 'GET http://data.abc.org/home.txt Http/1.0\n\n'.encode()
mySocket.send(cmd)

while(True):
    data = mySocket.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())
mySocket.close()