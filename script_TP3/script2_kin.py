# kinematics: transport of velocity formula

import numpy as np
from math import *

# dimensions
d=3

# function: input of vector components
def readvec(vec,vecname):
   for i in range(0,d):
      vec[i] = input("%s[%d] = " %(vecname,i+1))
   return vec

# function: vector product
def vectprod(x,y):
   mat=np.zeros((d,d))
   z=np.zeros(d)
   for j in range(0,d):
      mat[0,j]=j
   for j in range(0,d):
      mat[1,j]=x[j]
      mat[2,j]=y[j]
   z[0]=(-1)**mat[0,0]*(mat[1,1]*mat[2,2]-mat[1,2]*mat[2,1])
   z[1]=(-1)**mat[0,1]*(mat[1,0]*mat[2,2]-mat[1,2]*mat[2,0])
   z[2]=(-1)**mat[0,2]*(mat[1,0]*mat[2,1]-mat[1,1]*mat[2,0])
   return z

# fucntion: modulus of vector
def vecmod(x):
   m=0.
   for i in range(0,d):
      m += x[i]**2
   m=sqrt(m)
   return m

# initialization:
# point A,B coordinates
# velocity at vA,vB components
# angular velocity omega
A=np.zeros(d)
B=np.zeros(d)
vA=np.zeros(d)
vB=np.zeros(d)
omega=np.zeros(d)

# input vector components
print("")
print("enter coordinates of first point:")
readvec(A,"A")
#print(A)

print("enter velocity components at first point:")
readvec(vA,"vA")
#print(vA)

print("enter angular velocity components:")
readvec(omega,"omega")
#print(omega)

print("enter coordinates of scond point:")
readvec(B,"B")
#print(B)

# construct vector AB
AB=B-A
# compute omega vectprod AB
omAB=vectprod(omega,AB)
# transport of velocity formula
vB=vA+omAB

print("")
# print velocity at point B
for i in range(0,d): 
    print("vB[%i] = %f" %(i+1,vB[i]))

#compute and modulus of velocity in B
mvB=vecmod(vB)
print("|vB| = %f" %mvB)

print("")
