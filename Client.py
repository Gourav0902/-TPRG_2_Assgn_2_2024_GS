'''Gouravjeet Singh (Fall 2024)
# Student id- 100920691

This program is strictly my own work. Any material
beyond course learning materials that is taken from
the Web or other sources is properly cited, giving.
credit to the original author(s)'''

import socket
import json
s = socket.socket()# Create a socket object
host = '10.102.13.192'
port = 5000

try:
    s.connect((host, port)) 
    jsonRecieved = (s.recv(1024).decode())# Receive data from the server (up to 1024 bytes) and decode it to a string

    data = json.loads(jsonRecieved)# Parse the JSON string into a Python dictionary

    # Extract specific data fields from the parsed JSON
    ret1 = data["Temperature"] # Temperature value
    ret2 = data["Voltage"] # Voltage value
    ret3 = data["Arm_Memory"]# ARM memory usage
    ret4 = data["Arm_Clock"]# ARM clock speed
    ret5 = data["GPU_Memory"]# GPU memory usage



    print ("Temp =",ret1,"\u2103\n")# Print temperature
    print ("Volt =",ret2,"V\n")# Print voltage
    print("Arm_Memory=",ret3,"M\n")# Print ARM memory usage
    print("Frequency=",ret4,"\u3392\n") # Print ARM clock speed
    print("GPU_Memory=", ret5,"M\n")# Print GPU memory usage
    # Close the socket connection
except (socket.error, json.JSONDecodeError):# Handle exceptions that may occur during connection or JSON parsing
    print("check server connection")# Print an error message if a connection or JSON error occurs
    s.close()
