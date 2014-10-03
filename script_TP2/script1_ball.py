from math import *

###################################################
# some physical parameters
g=9.81     # acceleration of gravity (ms^{-2})
rho=1.2    # density of air (kg m^{-3})
Cd=0.2     # drag coefficient
# units of velocity
units=["km/h", "m/s"]
###################################################

###################################################
# definition of functions
# conversion of units (km/h ---> m/s)
def unit_conv(a):
  return a*1./3.6

# function: surface
def aire(a):
  return pi*a**2

# function: weight
def weight(a):
  return a*g

# function: drag
def drag(s,u):
  d=0.5*Cd*rho*s*u**2
  return d
###################################################

# input physical variables 
print("")
print("Enter physical parameters of the ball")
R=input("Radius of the ball (in meters): R =  ",)
m=input("Mass of the ball: m (in kilograms) =  ")
v=input("Speed of the ball: v =  ")
un=input("Specify units of velocity: km/h or m/s  ")

# check units of velocity
if un == "km/h":
#  print("v in km/h = %f" %v)
  v=unit_conv(v)
#  print("v in m/s = %f" %v)

# compute cross-section
A=aire(R)
#print("A = %f" %A)

# compute weight
Fg=weight(m)
print("")
print("Forces on the ball:")
print("Fg = %f" %Fg)

# compute drag
Fd=drag(A,v)
print("Fd = %f" %Fd)

# compute ratio Fd/Fg
print("Fd/Fg = %f" %(Fd/Fg))
print("")
