import numpy as np 

l1 = [1,2,3,4]
a1 = np.array(l1) # np.asarray(l1)

print (l1)

print (a1) 

print (np.array([[-2,4],[2,5]]))

print (np.zeros_like(a1))

print (np.eye(3))

print (np.ones((3,2,2))) # shape=(3,2,2)

print (np.ones((3,2,2),dtype=bool))

print (np.repeat((2,3), 7))

print (np.full((2,3), 7)) # fill_value=7

print (np.empty([3,2]))

print (np.arange(24))

print (np.arange(1, 10, 5)) # 5 is a step value
