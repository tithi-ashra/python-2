from socket import *
server = socket()
server.bind(('localhost',9000))
server.listen()
while(1):
    client,addr = server.accept()
    rd = client.recv(1028).decode()
    print(rd)
    data = "HTTP/1.1 200 OK\r\n"
    data += "conten-type:text/html ; charset=utf-8\r\n"
    data += "\r\n"
    data += "<html><body>hello world</body></html>\r\n\r\n"
    client.send(data.encode())
server.close()
print("http://localhost:9000")
