import numpy as np 

a1 = np.array([[-2,4],[2,5]])
a2 = np.array([[1,2],[3,4]])

print (a1 + 10)
print (a1+a2)
print (np.add(a1,a2)) 

print (a1 * 3)
print (a1*a2)
print (np.multiply(a1,a2)) # likewise subtract, divide, mod / remainder
print (a1.dot(a2))

print (a1 % 2)

print (a1.T)
print (np.reciprocal(a1))

print (a1.sum(0)) 
print (a1.sum(axis=1))
print (a1.mean(1))
print (np.mean(a1)) # median,average,var,std
print (a1.argmax(1)) # doubt

i = a1.sum(1)
print (i < 4)
print(a1[i < 4])

