import numpy as np 

a1 = np.array([[-2,4],[2,5]])

print (np.power(a1,3))
print (np.square(a1))
print (np.sin(a1))

print (np.amin(a1)) #amax
print (np.amin(a1,1)) 
print (np.amin(a1,0)) 
print (np.ptp(a1))
print (np.percentile(a1,40,1))
print (np.isfinite(a1))
print (np.isinf(a1))

a2 = np.array([44,20,np.nan, 89,np.nan,39+6j,499,5.8+7j])
print (a2)
print (a2[~np.isnan(a2)])
print (a2[a2>20])
print (a2[np.iscomplex(a2)])

print (np.real(a2))
print (np.imag(a2))
print (np.conj(a2))
print (np.angle(a2))
print (np.angle(a2, deg=True))


a3 = np.array([0,30,45,60,90])
s = np.sin(a3*np.pi/180) # likewise cos, tan
print (s)
print (np.around(s))
print (np.around(s,decimals = 1))
print (np.floor(s))
print (np.ceil(s))

arc = np.arcsin(s)
print (arc)
print (np.degrees(arc))
