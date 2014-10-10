# moments of inertia of aluminium plate
# rho(Al) = 2.7 g/cm^3 
# surface = 2 m x 10 m 
# height = 1 cm (negligible) 
# rho --> rho*h = 27 kg/m^3
import numpy as np
from math import *

##########################################
# input precision
print("")
delta=input("precision: delta = ")

# geometrical parameters (lengths in meters)
a = 2.
b = 5.
# h small ===> c = 0 (along z)
c = 0.
nx = int(a/delta)+1
ny = int(b/delta)+1
nz = int(c/delta)+1
print("nx = %d" % nx)
print("ny = %d" % ny)
print("nz = %d" % nz)

# mass (in kg) and surface density
m=270.
rho=m/(a*b)

# function: compute 2d integral 
# used for moments of inertia
def mominert(x1):
   integral = 0.
   integral = sum(sum(x1))
   integral *= delta**2 
   return rho*integral

# function: compute 2d integral 
# used for products of inertia
def prodinert(x1,x2):
   intx1 = 0.
   intx2 = 0.
   intx1 = sum(x1)
   intx1 *= delta
   intx2 *= x2
   intx2 = sum(x2)
   intx2 *= delta
   intx2 *= intx1 
#   print("integral = %f" % inty)
   return rho*intx2 
##########################################

x = np.linspace(0,b,nx)
y = np.linspace(0,a,ny)
z = np.linspace(0,c,nz)

np.set_printoptions(precision=4)
#print("x = ") 
#print(x)
#print("y = ") 
#print(y)
#print("z = ") 
#print(z)

# moments of inertia 
# (diagonal terms of inertia operator)
# results in kg*m^2
print("")
print("moments of inertia:")
intgnd=np.zeros((nx,ny))
for i in range(0,nx):
   intgnd[i,:] = np.multiply(y,y)[:] + np.multiply(z,z)[:]
#print("intgnd = ")
#print(intgnd)
Iox = mominert(intgnd)
print("Iox = %f " % Iox) 

intgnd=np.zeros((nx,ny))
for j in range(0,ny):
   intgnd[:,j] = np.multiply(x,x)[:] + np.multiply(z,z)[:]
#print("intgnd = ")
#print(intgnd)
Ioy = mominert(intgnd)
print("Ioy = %f " % Ioy) 

intgnd=np.zeros((nx,ny))
for i in range(0,nx):
   for j in range(0,ny):
      intgnd[i,j] = np.multiply(x,x)[i] + np.multiply(y,y)[j]
#print("intgnd = ")
#print(intgnd)
Ioz = mominert(intgnd)
print("Ioz = %f " % Ioz) 
# check of results: Ioz = Iox + Ioy
print("check: Iox + Ioy = %f" %(Iox + Ioy))


# products of inertia
# (off-diagonal terms of inertia operator)
# results in kg*m^2
print("")
print("products of inertia:")
Ioxy = prodinert(x,y)
print("Ioxy = %f " % Ioxy) 

Ioyz = prodinert(y,z)
print("Ioyz = %f " % Ioyz) 

Iozx = prodinert(z,x)
print("Iozx = %f " % Iozx) 

# operator of inertia
# 3x3 matrix constructed with precious integrals
print("")
print("operator of inertia:")
IoS=np.zeros((3,3))
IoS = np.array([[Iox, -Ioxy, -Iozx], [-Ioxy, Ioy, -Ioyz], [-Iozx, -Ioyz, Ioz]])
print("[Io(S)] = ")
print(IoS)
print("")

