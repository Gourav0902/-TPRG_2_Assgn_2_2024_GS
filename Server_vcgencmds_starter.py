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


#gets the Core Temperature from Pi, ref https://github.com/nicmcd/vcgencmd/blob/master/README.md
t = os.popen('vcgencmd measure_temp').readline() #gets from the os, using vcgencmd - the core-temperature
v = os.popen('vcgencmd measure_volts core').readline()#gets from the os, using vcgencmd - the core-volt
# initialising json object string
temp = str(float(t.replace("temp=","").replace("'C\n",""))) 
volt = str(float(v.replace("volt=","").replace("V\n","")))
 # The eval() function evaluates JavaScript code represented as a string and returns its completion value.
f_dict = {"Temperature":temp,
          "Voltage":volt
          }


while True:
  c, addr = s.accept()
  print ('Got connection from',addr)
  res = bytes(str(f_dict), 'utf-8') # needs to be a byte
  c.send(res) # sends data as a byte type
  c.close()