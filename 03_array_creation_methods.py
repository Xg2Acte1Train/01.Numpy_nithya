import numpy as np 

print (np.linspace(1, 10, 5)) # 5 is size 

print (np.linspace(1,10,5,endpoint=False))

print (np.linspace(1,10,5,endpoint=False,retstep=True))

print (np.linspace(0,1,24).reshape(3,4,2)) 

print (np.logspace(1,2,num = 10))

print (np.logspace(1,2,num = 10, base = 2))

print ((range(12)))
print (iter(range(12)))
print (np.fromiter(iter(range(12)), dtype = float))

# np.random.seed(100) need meaning of this
print (np.random.rand(3,2))

print (np.random.randn(3,2))

print (10 + 2*np.random.randn(3,2)) # normal distribution with mean 10 and sd 2

print (np.random.randint(1,20,7)) # low=-30, high=30, size=(5,6)

print (np.random.normal(loc=5, scale=2.5, size=20)) # normal distribution of 20 elements with mean 5 and sd 2.5 

#Which of the following numpy method is used to simulate a binomial distribution? np. random. binomial(n, p, size) 
l1 = [1,2,3,4]
print (np.array(l1, dtype = np.dtype([('id', 'i1'), ('name', 'S20')])))

from io import StringIO
x = StringIO('''88.25 93.45 72.60 90.90
72.3 78.85 92.15 65.75
90.5 92.45 89.25 94.50''')

print (np.loadtxt(x,delimiter=' '))
