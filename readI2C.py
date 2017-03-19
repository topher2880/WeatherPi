# reads from WXLink RX
#
import smbus
import time
import sys
import subprocess

bus = smbus.SMBus(1)

address = 0x08
twoblockMessages = 0
oneblockMessages =0
errorMessages = 0

#sudo modprobe - r i2c_bcm2708
#sudo modprobe i2c_bcm2708 baudrate=32000

while True:
 flag = 0
 data = ""
 print "-----------"
 try:
  print "block 1"
 data = bus.read_i2c_block_data(address, 0);
 print ' '.join(hex(x) for x in data)
except IOError:
 #subprocess.call(['i2cdetect', '-y', '1'])
 flag = 1 #optional flag to signal your code to resend or something
#time.sleep(3)
 try
 print "block 2"
 data = bus.read_i2c_block_data(address, 1);
 print ' '.join(hex(x) for x in data)
 print "-----------"
except IOError:
 #subprocess.call(['i2cdetect', '-y', '1'])
 flag = 1 #optional flag to signal your code to resend or something
 
print "flag=", flag
 if (flag == 0):
  twoblockMessages = twoblockMessages + 1
 else:
  errorMessages = errorMessages + 1
 
 print "twoblock = %i error = %i percent error=%6.2f%%" % (twoblockMessages, errorMessages, 100*(float(errorMessages)/float(errorMessages+twoblockMessages)))
 time.sleep(2);
 
  
