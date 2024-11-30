'''Gouravjeet Singh (Fall 2024)
# Student id- 100920691

This program is strictly my own work. Any material
beyond course learning materials that is taken from
the Web or other sources is properly cited, giving.
credit to the original author(s)

'''
# This server runs on Pi, sends Pi's your 4 arguments from the vcgencmds, sent as Json object.

# details of the Pi's vcgencmds - https://www.tomshardware.com/how-to/raspberry-pi-benchmark-vcgencmd
# more vcgens on Pi 4, https://forums.raspberrypi.com/viewtopic.php?t=245733
# more of these at https://www.nicm.dev/vcgencmd/

import socket
import os, time
import json

s = socket.socket()
host = '' # Localhost
port = 5000
s.bind((host, port))
s.listen(5)


#gets the Core Temperature from Pi, ref https://github.com/nicmcd/vcgencmd/blob/master/README.mdimport socket
import os, time
import json

s = socket.socket()
host = '' # Localhost
port = 5000
s.bind((host, port))
s.listen(5)

#gets the Core Temperature from Pi, ref https://github.com/nicmcd/vcgencmd/blob/master/README.md
def get_temp():
    t = os.popen('vcgencmd measure_temp').readline() # Run the vcgencmd command to get the core temperature
    return round(float(t.replace("temp=", "").replace("'C", "")), 1) # Extract and return temperature as a float rounded to 1 decimal place
# Function to get the core voltage of the Pi
def get_volt():
    v = os.popen('vcgencmd measure_volts core').readline()# Run the vcgencmd command to get the voltage
    return round(float(v.replace("volt=", "").replace("V", "")), 1) # Extract and return voltage as a float rounded to 1 decimal place
def get_Arm_memory():# Function to get the ARM memory usage of the Pi
    m = os.popen('vcgencmd get_mem arm').readline() # Run the vcgencmd command to get ARM memory usage
    return round(float(m.replace("arm=", "").replace("M", "")), 1)# Extract and return memory in megabytes, rounded to 1 decimal place
def get_Clock_frequency():# Function to get the ARM clock frequency of the Pi
    c = os.popen('vcgencmd measure_clock arm').readline()# Run the vcgencmd command to get ARM clock frequency
    return round(int(c.split('=')[1]) / 1_000_000, 1)# Extract and return frequency in MHz, rounded to 1 decimal place
def get_gpu_memory():# Function to get the GPU memory usage of the Pi
    Gm = os.popen('vcgencmd get_mem gpu').readline()# Run the vcgencmd command to get GPU memory usage
    return round(float(Gm.replace("gpu=", "").replace("M", "")), 1)# Extract and return memory in megabytes, rounded to 1 decimal place
# initialising json object string

ini_string = {"Temperature":get_temp(),
              "Voltage": get_volt(),
              "Arm_Memory":get_Arm_memory(),
              "Arm_Clock":get_Clock_frequency() ,
              "GPU_Memory": get_gpu_memory()
              }
# converting string to json
f_dict = json.dumps(ini_string) # The eval() function evaluates JavaScript code represented as a string and returns its completion value.


try:
    while True:
      c, addr = s.accept() # Accept a client connection
      print ('Got connection from',addr)
      res = bytes(str(f_dict), 'utf-8') # needs to be a byte
      c.send(res) # sends data as a byte type
except KeyboardInterrupt:
    print ("****Good Bye**** ")# Handle graceful shutdown on Ctrl+C
    exit()