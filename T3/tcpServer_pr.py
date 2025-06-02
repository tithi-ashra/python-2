import socket
host = socket.gethostname()
port = 5000
server = socket.socket()
server.bind((host,port))
server.listen()
conn,addr = server.accept()
print("connection from : ",str(addr))
while True:
    data = server.recv(1024).decode()
    if not data:
        break
    l = data.split()
    l = list(map(lambda x : int(x),l))
    l = list(map(lambda i : x%2!=0,l))
    l = list(map(lambda i : x**3,l))
    s=""
    for i in l:
        s += str(i)+" "
    data = s
    print("connected user : ",str(data))
    data = input('->')
    conn.send(data.encode())
conn.close()
