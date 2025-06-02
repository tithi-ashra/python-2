import socket
host = socket.gethostname()
port = 5000
client = socket.socket()
client.connect((host,port))
msg = input('->')
while msg.lower().strip()!='bye':
    client.send(msg.encode())
    data = client.recv(1024).decode()
    print("data recived from server : ",data)
    msg = input('->')
client.close()
