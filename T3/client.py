from socket import *
client = socket()
client.connect(('localhost',9000))
request = "GET/HTTP/1.1\r\n\host:localhost\r\n\r\n"
client.send(request.encode())
response = client.recv(1024).decode()
print(response)
client.close()
