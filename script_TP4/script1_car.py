from math import *

###################################################
# some physical parameters
g = 9.81     # acceleration of gravity (ms^{-2})
mus = 0.8    # coefficient of static friction
# units of velocity
units = ["km/h", "m/s"]
###################################################

###################################################
# definition of functions
# conversion of units of velocity (km/h ---> m/s)
def unit_conv1(a):
  return a*1./3.6

# conversion of units of velocity (m/s ---> km/h)
def unit_conv2(b):
  return b*3.6

# function: centripetal acceleration
def accel(r):
  return v**2/r

# function: maximum allowed velocity
def velmax(r):
  return sqrt(mus*r*g)

# function: length to stop (v=0)
def stoplength(vv):
  return vv**2/(2*mus*g)
###################################################

# input physical variables 
print("")
print("Turn of a car")
print("Enter physical parameters")
R = input("Radius of curvature (in meters): R =  ",)
v = input("Car speed: v =  ")
un = input("Specify units of velocity: km/h or m/s  ")

# check units of velocity
if un == "km/h":
#  print("v in km/h = %f" %v)
  v = unit_conv1(v)
#  print("v in m/s = %f" %v)

# compute centripetal acceleration
acc = accel(R)

# friction force per unit mass 
Ft = mus*g
# max possible velocity in the turn
vM = velmax(R)
# min length to stop (v=0) 
lm = stoplength(v) 

# conversion of units (for printing information)
v = unit_conv2(v)
vM = unit_conv2(vM)

###################################################
# print warning messages for the driver:

# (0) Current situation of the car 
# before starting to turn
print("")
print("Turn radius = %f m" %R)
print("Your velocity is v = %f km/h" %v)

# (1) check if velocity is appropriate for the turn
if v > vM: 
  print("Slow down!")
  print("Max allowed velocity is vM = %f km/h" %vM)

# (2) inform the driver about minimum length to stop the car
# on straight road (e.g., after coming out of the turn)
print("")
print("Rectilinear road")
print("Length to stop is lm %f m" %lm)
###################################################

