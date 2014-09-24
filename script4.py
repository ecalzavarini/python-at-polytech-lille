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


mean = np.mean(y)
std = np.std(y)

ymean = np.ones(n)*mean
yp = np.ones(n)*(mean+std)
ym = np.ones(n)*(mean-std)

plt.plot(x,y)
plt.plot(x,ymean)
plt.plot(x,yp)
plt.plot(x,ym)



plt.ylabel('pression [kPa]')
plt.xlabel('temps [heures]')

plt.show()



plt.hist(y, 50, normed=1, facecolor='r')
plt.xlabel('velocity')
plt.ylabel('Probabilite')
plt.title('Histogramme')
#plt.axis([40, 160, 0, 0.03])

plt.show()
