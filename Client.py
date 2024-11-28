import socket
import json
s = socket.socket()
host = '10.102.13.215'
port = 5000
s.connect((host, port)) 
jsonRecieved = (s.recv(1024).decode())

data = json.loads(jsonRecieved)
ret1 = data["Temperature"]
ret2 = data["Voltage"]

print(ret1)
print (ret2)
s.close()
