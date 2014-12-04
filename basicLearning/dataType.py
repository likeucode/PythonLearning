#! /usr/bin/env python
#this code is a demo of basic datatype of python

#sequence
greeting='hello'
print('***********sequence**********')
print 'Index'
print('greeting[0]:'+greeting[0])
print('greeting[-1]:'+greeting[-1])

print 'slicing'
tag = '<a href="http://www.python.org">Python web site</a>'
print 'tag[9:30]:'+tag[9:30]
numbers=[1,2,3,4,5,6,7,8,9,10]
print 'numbers[-3:-1]:'+str(numbers[-3:-1])
print 'numbers[0:10:2]'+str(numbers[0:10:2])

print "Adding"
addseq=[1,2,3]+[4,5,6]
print '[1,2,3]+[4,5,6]='+str(addseq)

print "Multiplying"
print '[42]*10='+str([42]*10)

print "Methods"
print 'len(numbers)='+str(len(numbers))
print 'max(numbers)='+str(max(numbers))
print 'min(numbers)='+str(min(numbers))
#list
print '*************List*************'
names=['Alice','TOm','John','Hack']
print 'del names[2]'
print 'names[2]=list(a list)'
print 'methods:append,count,extend,index,insert,pop,remove,reverse,sort,'
#tuple
print '*************tuple*************'
x=1,2,3
y=tuple([1,2,3])
print 'x[1]'

#dictionary
print '***********dictionary/mapping*********'
phonebook={'Alice':'123','Tom':'234','John':'111'}
items=[('name','Tesla'),('age',42)]
d=dict(items)
print 'len(dic),dic(key)=value,del dic[key],key in dic'
print 'Methods:dic.clear(), y=x.copy(), dict.fromkeys([k1,k2])'
print 'Methods:dic.get(key),dic.haskey(key),items,keys,popitem,setdefault,update,values'