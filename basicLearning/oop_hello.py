#!/usr/bin/env python
#oop for hello

class GreetUser(object):
	"""docstring for GreetUser"""
	def __init__(self):
		print('Create object...')

	def getName(self):
		user=raw_input('Type your name: ')
		return user

	def greet(self,name):
		print('Hello '+name)	

if __name__ == '__main__':
	user=GreetUser()
	name=user.getName()
	user.greet(name)	
