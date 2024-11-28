'''Gouravjeet Singh (Fall 2024)
# Student id- 100920691

This program is strictly my own work. Any material
beyond course learning materials that is taken from
the Web or other sources is properly cited, giving.
credit to the original author(s)'''

import socket
import json
s = socket.socket()# Create a socket object
host = '10.102.13.215'
port = 5000
s.connect((host, port)) 
jsonRecieved = (s.recv(1024).decode())# Receive data from the server (up to 1024 bytes) and decode it to a string

data = json.loads(jsonRecieved)# Parse the JSON string into a Python dictionary

# Extract specific data fields from the parsed JSON
ret1 = data["Temperature"] # Temperature value
ret2 = data["Voltage"] # Voltage value
ret3 = data["Arm_Memory"]# ARM memory usage
ret4 = data["Arm_Clock"]# ARM clock speed
ret5 = data["GPU_Memory"]# GPU memory usage

print(ret1)# Print temperature
print (ret2)# Print voltage
print(ret3)# Print ARM memory usage
print(ret4) # Print ARM clock speed
print(ret5)# Print GPU memory usage
# Close the socket connection
s.close()
