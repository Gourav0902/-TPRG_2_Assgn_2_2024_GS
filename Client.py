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
ret3 = data["Arm_Memory"]
ret4 = data["Arm_Clock"]
ret5 = data["GPU_Memory"]

print(ret1)
print (ret2)
print(ret3)
print(ret4)
print(ret5)
s.close()
