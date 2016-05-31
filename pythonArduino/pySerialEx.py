import sys
import serial
import time
import serial.tools.list_ports

print "Hello World"
ports = list(serial.tools.list_ports.comports())
for p in ports:
	print p
	if "USB UART" in p[1]:
		print "USB UART detected"

delaytime = 1
ser = serial.Serial('/dev/cu.usbserial-DC008I9I', 9600)
time.sleep(2) # delay for 2 seconds

ser.write('r')
print "red"
time.sleep(delaytime)

ser.write('g')
print "green"
time.sleep(delaytime)

ser.write('b')
print "blue"
time.sleep(delaytime) # delay for 2 seconds

ser.write('r')
print "red"
time.sleep(delaytime)

ser.write('g')
print "green"
time.sleep(delaytime)

ser.write('b')
print "blue"
time.sleep(delaytime)

ser.write('1')
print "white"
time.sleep(delaytime)

ser.write('0')
print "off"


print "Application Stops"