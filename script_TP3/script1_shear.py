import matplotlib.pylab as plt
import numpy as np
from math import *


# parameter for the domain size and the shear rate
s=0.12
h=20


# plot the shear field
X,Y = np.meshgrid( np.arange(-h,h,1), np.arange(-h,h,1) )
U = s*Y
V = 0
C =  ( U**2. + V**2. )**.5

Q = plt.quiver( X, Y, U, V , C, scale = 10.)
plt.title("linear shear field")
plt.show()

#build gradient matrix

grad_u = np.zeros((2,2))
grad_u[0,1]= s
print("grad_u ")
print(str(grad_u))

#extract sym and asym

sym = np.zeros((2,2))
asy = np.zeros((2,2))

sym = 0.5*(grad_u + np.transpose(grad_u))
asy = 0.5*(grad_u - np.transpose(grad_u))

# velocity fields
UA = asy[0,1]*Y 
VA = asy[1,0]*X
C =  ( UA**2. + VA**2. )**.5

plt.title("pure rotation field")
Q = plt.quiver( X, Y, UA, VA , C, scale = 10.)
plt.show()


US = sym[0,1]*Y
VS = sym[1,0]*X
C =  ( US**2. + VS**2. )**.5

plt.title("pure strain field")
Q = plt.quiver( X, Y, US, VS , C, scale = 10.)
plt.show()

# sum
plt.title("sum ")
C =  ( (US+UA)**2. + (VS+VA)**2. )**.5
Q = plt.quiver( X, Y, US+UA, VS+VA , C, scale = 10.)
plt.show()



