import numpy as np 
print '*******numpy array***********'
randArray = np.random.rand(4,4)
randMat   = np.mat(randArray)
irandMat  = randMat.I

a1=np.array(range(10,30,5))
a11=a1.reshape((2,2))
a111 = np.arange(12).reshape(3,4)

a2=np.linspace(0,2,10)
b=np.zeros((3,4))
c=np.ones((2,3,4),dtype='int16')
d=np.empty((2,3))
print a1,a11,a2,b,c,d

A1=np.arange(12)
print A1
A1.shape=(3,4) #A.reshape(3,4)
M=np.mat(A1.copy())

#Vector Stacking
x = np.arange(0,10,2)                     # x=([0,2,4,6,8])
y = np.arange(5)                          # y=([0,1,2,3,4])
m = np.vstack([x,y])                      # m=([[0,2,4,6,8],
                                       #     [0,1,2,3,4]])
xy = np.hstack([x,y])                     # xy =([0,2,4,6,8,0,1,2,3,4])

A=np.array([[1,1],[0,1]])
B=np.array([[2,0],[3,4]])
C=A*B            # elementwise product
D=np.dot(A,B)       # matrix product

a = np.random.random((2,3))
asum=a.sum()
amin=a.min()
amax=a.max()
print a,asum,amin,amax

print '*******numpy matrix***********'
A=np.matrix('1.0,2.0;3.0,4.0')
AT=A.T
B=A*AT
print A,AT,B