import numpy as np 

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(24).reshape(4,3,2)

print (a1)
print (a1[1])
print (a1[1:])
print (a1[0:2])
print (a1[0:3:2])
print (a1[slice(0,2)])
print (a1[slice(0,3,2)])
print (a1[-3])
print (a1[:,1])
print (a1[[0, 2, 2,1,0,2], [0, 3, 1,3,2,1]])

print (a2)
print (a2[-1])
print (a2[-1,0:2])
print (a2[-1,0:2][-2])
print (a2[-1,0:2,-2])
print (a2[:,:,0])
print (a2[:,1,:])
print (a2[1,:,1]) # index 1 element in row of index 1
print (a2[1:,1,:]) # From all outer rows except the first, select 1st index element (which itself is an array) completely.
print (a2[:,:1,1])
print (a2[:2,:,1])
print (a2[:2,:1,1])
print (a2[:,1])
print (a2[2,...])
print (a2[2:,...])
print (a2[...,1])
print (a2[...,1:])
print (a2[np.array([[0,2],[1,0]]) , np.array([[0,1],[1,0]])])
