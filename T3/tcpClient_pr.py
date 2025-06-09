import socket
host=socket.gethostname()
port=5000
client_socket=socket.socket()
client_socket.connect((host,port))
message=input('->')
l=message.split()
n=[]
for i in l:
    n.append(int(i))
odd=list(filter(lambda x:x%2!=0,n))
cube=list(map(lambda x:x**3,odd))
ans=''
for i in cube:
    ans=ans+str(i)+" "
client_socket.send(ans.encode())
client_socket.close()
