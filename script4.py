from math import *
import numpy as np 
import matplotlib.pyplot as plt

# Open a file
f = open("pressure.txt", "r")
# define an empty list
data=[]
# read full file and split into its parts 
data=f.read().split()
# Close opend file
f.close()

n = len(data)
#print(n)

x=np.linspace(0,n,n)
x /= 3600. # conversion en heures
#print(len(x))


y=np.asarray(data, dtype=float)   # convert a list into np array  see http://docs.scipy.org/doc/numpy/reference/generated/numpy.asarray.html
y /= 1000.  # conversion en kPa
#print(len(y))


plt.plot(x,y)

plt.ylabel('pression [kPa]')
plt.xlabel('temps [heures]')

plt.show()
