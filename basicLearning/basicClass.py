#! /usr/bin/env python
#this code is a demo of oop of python

class Filter:
	def init(self):
		self.blocked=[]
	def filter(self,sequence):
		return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
	num=0
	def init(self):
		SPAMFilter.num+=1
		print SPAMFilter.num
		self.blocked=['SPAM']


class Calcu:
	def calculate(self,expression):
		self.value=eval(expression)

class Talker:
	def talk(self):
		print 'Hi, my value is ',self.value

class TalkingCalcu(Calcu,Talker):
	pass

def basicClass():
	f=Filter()
	f.init()
	f.filter([1,2,3])

	s=SPAMFilter()
	s.init()
	s.filter(['SPAM','SPAM','eggs','bacon','SPAM'])

	print issubclass(SPAMFilter,Filter)
	print isinstance(s,SPAMFilter)

def multiSuper():
	tc=TalkingCalcu()
	tc.calculate('1+2*3')
	tc.talk()

	#interface
	print hasattr(tc,'talk')
	print hasattr(tc,'fonrd')
	#callable is not used in python 3.0
	print callable(getattr(tc,'talk',None))
	print callable(getattr(tc,'fonrd',None))

	setattr(tc,'name','Mr.Gumby')
	print tc.name

def main():
	basicClass()
	multiSuper()

if __name__ == '__main__':
	main()
