import numpy as np                 #here we load numpy, calling it 'np' from now on
import matplotlib.pyplot as plt    #here we load matplotlib, calling it 'plt'
from math import *

nx = 81  #  be careful 80 or 79 will not produce the same result. Why?
dx = 2./(nx-1)
nt = 25    #nt is the number of timesteps we want to calculate
dt = .025  #dt is the amount of time each timestep covers (delta t)
c = 1.      #assume wavespeed of c = 1


u = np.ones(nx)      #numpy function ones()
u[.5/dx : 1/dx+1]=2  #setting u = 2 between 0.5 and 1 as per our I.C.s
print u

plt.plot(np.linspace(0,2,nx), u)
plt.show()

u0 = u.copy() # make a copy of the initial value 
un = np.ones(nx) # initialize a temporary array

def advection(u,c,dt,dx,nx):
    un = u.copy()    # copy the existing values of u into un    
    for i in range(1,nx):  #loop on all the indexes of u exept the first 
        u[i] = un[i]-c*dt/dx*(un[i]-un[i-1])
    return u    

for n in range(nt):  # loop for values of n from 0 to nt, so it will run nt times
    u = advection(u,c,dt,dx,nx)


plt.plot(np.linspace(0,2,nx), u0 , label="t=0")
plt.plot(np.linspace(0,2,nx),u, label="t=6.25")
plt.legend()
plt.show()

