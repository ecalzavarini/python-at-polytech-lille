from math import *
import numpy as np
import matplotlib.pyplot as plt

###################################################
# A= F/(m*omega**2) amplitude
A=2.
###################################################

###################################################
# definition of transfer function
def transfer(x,gain):
  return A*1./(((1.-x**2)**2+(x/gain)**2)**0.5)    # attention: here sqrt in the denominator wouldn't work

# definition of function to compute the parameter S
def S(xdata,Q,ydata) :
  a = (transfer(xdata,Q)  - ydata )**2.
  xs = 0
  for i in range(len(ydata)):
    xs = xs+a[i]
  return xs

###################################################

# First I generate the data for the students just adding noise to the theroretical data
# Choose value of Q
Q = input("Q = ")
L=150
u=np.linspace(0,3,L)
T=transfer(u,Q)
namp=0.1
noise= namp*( 2.*np.random.rand(L) - 1.0)
T = T+noise

# Ouverture d'un nouveau fichier
f = open("transfert.txt", "w")
for i in range(L):
  f.write('%f\n'%(T[i])) 
# fermeture du fichier 
f.close()

# Ouverture d'un nouveau fichier                                                                                            
f = open("pulsation_adim.txt", "w")
for i in range(L):
  f.write('%f\n'%(u[i]))
# fermeture du fichier
f.close()


###################################################
# From here we start the script.
# open file and read the data

# transfer
f = open("transfert.txt", "r")
Tdata=[]
Tdata=f.read().split()
f.close()

# pulsation
f = open("pulsation_adim.txt", "r")
Udata=[]
Udata=f.read().split()
f.close()

#conversion au type numpy float     
Tdata = np.asarray(Tdata, dtype=float)
Udata = np.asarray(Udata, dtype=float)

#first plot
plt.plot(Udata,Tdata)
plt.show()

# Least squares method
# Minimization of S
smin = 1000.

Q=0.1
dQ=0.1
Qmax=3.0
NQ=int(Qmax/dQ)+1
for i in range(NQ):
  s=S(Udata,Q,Tdata)
#  print("i = %d, Q = %f" %(i,i*dQ))
  if s<smin : 
    smin=s
    Qbest=Q
  Q += dQ
  
print("Qbest %f \n" % Qbest )

plt.plot(Udata,Tdata)
plt.plot(Udata,transfer(Udata,Qbest),'r')
plt.show()


