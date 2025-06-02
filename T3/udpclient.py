import socket
host = socket.gethostname()  #or you can write the ip address of other pc
port = 5000
client_socket = socket.socket(type=socket.SOCK_DGRAM)
addr = (host,port)
while True:
    data = input('->')
    if not data:
        break
    client_socket.sendto(data.encode(),addr)
    print('Ready to received message')
    data,addr = client_socket.recvfrom(1024)
    if not data:
        break
    print('Received ',data.decode())
client_socket.close()
