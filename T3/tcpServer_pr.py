import socket
host=socket.gethostname()
port=5000
server_socket=socket.socket()
server_socket.bind((host,port))
server_socket.listen()
conn,address=server_socket.accept()
data=conn.recv(1024).decode()
print('from connected user:',data)
conn.close()
