#! /usr/bin/env python
#this code shows basic demo of numpy, scipy and matplotlib

import numpy as np 
import scipy as sp
import matplotlib.pyplot as plt

def npshow():
	a=np.array([0,1,2,3,4,5])
	print 'a.ndim=%d'%a.ndim
	print  'a.shape='+str(a.shape)
	b=a.reshape((3,2))
	c=a.reshape((3,2)).copy()

	print 'index'
	print a[np.array([2,3,4])]
	print a[a>4]
	print a.clip(0,4)
	print a.dtype

def sp_plt_show():
	data=sp.genfromtxt("/home/liuke/dataset/MLinPython/web_traffic.tsv",delimiter='\t')
	print(data.shape)
	x=data[:,0]
	y=data[:,1]

	x=x[~sp.isnan(y)]
	y=y[~sp.isnan(y)]

	plt.scatter(x,y)
	plt.title("web traffic over the last month")
	plt.xlabel("Time")
	plt.ylabel("Hits/hour")
	plt.xticks([w*7*24 for w in range(10)],
		['week %i'%w for w in range(10)])
	plt.autoscale(tight=True)
	plt.grid()
	plt.show()

def main():
	npshow()
	sp_plt_show()

if __name__ == '__main__':
	main()
