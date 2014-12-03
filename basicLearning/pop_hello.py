#!/usr/bin/env python
#procedure oriented program for hello world

def getuser():
	user=raw_input("Type your name here: ") #you should keep informed input & raw_input
	print('Hello,'+ user + '!')

if __name__ == '__main__':
	getuser()