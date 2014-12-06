#! /usr/bin/env python
#this program is coded for express of python

num=input('Enter a number: ')
if num>0:
	print 'positive'
elif num<0:
	print 'negative'
else:
	print 'zero'

while num<=100:
	print num
	num +=1
sum_number=0
for number in range(1,101):
	sum_number += number
	print sum_number

y=[x*x for x in range(10) if x%3==0]
print y

if len(y)>10:
	del y
else:
	pass

exec "print 'exec function'"
scope={}
scope['x']=2
scope['y']=3
eval('x*y',scope)