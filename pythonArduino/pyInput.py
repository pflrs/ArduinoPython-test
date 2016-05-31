import sys
import serial
import time
import serial.tools.list_ports

print 'Welcome to the program'

print 'This is catch and repeat'
print 'Press \'q\' to exit'

ports = list(serial.tools.list_ports.comports())
for p in ports:
	print p
	if "USB UART" in p[1]:
		print "USB UART detected"

delaytime = 1
#ser = serial.Serial('/dev/cu.usbserial-DC008I9I', 9600)
ser = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(2) # delay for 2 seconds

x = False

while True:
	character = raw_input("Type a character:")
	if character is 'r':
		print "Red"
		ser.write('r')
	elif character is 'g':
		print "Green"
		ser.write('g')
	elif character is 'b':
		print "Blue"
		ser.write('b')
	elif character is '1':
		print "White"
		ser.write('1')
	elif character is '0':
		print "Off"
		ser.write('0')
	elif character is 'q':
		print "Fizz"
		break
	else:
		print "Enter Valid character (r, g, b, 1, 0), q to exit"
print 'Exiting Program'
