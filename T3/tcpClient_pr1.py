import socket
host = 'localhost'
port = 5000
buffer_size = 1024
with socket.socket() as s:
    s.connect((host,port))
    with open('ch-8.ipynb','rb') as f:
        while True:
            data = f.read(buffer_size)
            if not data:
                break
            s.sendAll(data)
        print('file sent')
