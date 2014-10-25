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
###################################################

# First I generate the data for the students just addign noise to the theroretical data
# some parameters
Nmax=1.e6
n=1
L=150
deltaQ=0.000001
Q=0.9
u=np.linspace(0,3,L)
T=transfer(u,Q)
noise= 0.1*( 2.*np.random.rand(L) - 1.0)
T = T+noise


#plt.plot(u,T)
#plt.show()

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


################ From here we start the script.
#open file and read the data
#Ouverture d'un nouveau fichier                                                                             

# Ouverture premier fichier
f = open("transfert.txt", "r")
Tdata=[]
Tdata=f.read().split()
f.close()

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


# function to compute tha parameter S
def S(xdata,Q,ydata) :
  a = (transfer(xdata,Q)  - ydata )**2.
  s = 0
  for i in range(len(ydata)):
    s = s+a[i]
  return s


smin = 1000.
s=10000.

Q=0.1
dQ=0.1
NQ=int(2.0/dQ)-1
for i in range(NQ):
  s=S(Udata,Q,Tdata)
#  print(s)
  if s<smin : 
    smin=s
    Qbest=Q
  Q += dQ
  
print("Qbest %f \n" % Qbest )


plt.plot(Udata,Tdata)
plt.plot(Udata,transfer(Udata,Qbest))
plt.show()


