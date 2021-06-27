import numpy as np 

a1 = np.array([[-2,4],[2,5]])
a2 = np.array([[1,2],[3,4]])
print (a1)

for i  in a1:
    print(i)
    
for i  in np.nditer(a1):
    print(i)

for i  in np.nditer(a1,order='F'):
    print(i)
    
for i  in np.nditer(a1,flags = ['external_loop']):
    print(i)
    
for i in np.nditer(a1, op_flags = ['readwrite']):
   i[...] = 5+i
print (a1)

for i,j  in np.nditer([a1,a2]):
    print ("%d,%d" % (i,j))
