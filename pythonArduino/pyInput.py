print 'Welcome to the program'

print 'This is catch and repeat'
print 'Press \'q\' to exit'

x = False

while True:
	character = raw_input("Type a character:")
	if character is 'r':
		print "Red"
	elif character is 'g':
		print "Green"
	elif character is 'b':
		print "Blue"
	elif character is '1':
		print "White"
	elif character is '0':
		print "Off"
	elif character is 'q':
		print "Fizz"
		break
	else:
		print "Enter Valid character (r, g, b, 1, 0), q to exit"
print 'Exiting Program'
