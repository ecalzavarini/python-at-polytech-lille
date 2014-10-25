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


plt.plot(u,T)
plt.show()


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


def S(u,Q,Tdata) :
  a = (transfer(u,Q)  - Tdata )**2.
  s = 0
  for i in range(L):
    s = s+a[i]
  return s

#print(S(u,Q,T))


smin = 1000.
s=10000.

Q=0.1
for i in range(20):
  s=S(u,Q,T)
#  print(s)
  if s<smin : 
    smin=s
    Qbest=Q
  Q += 0.1
  
print("Qbest %f \n" % Qbest )


plt.plot(u,T)
plt.plot(u,transfer(u,Qbest))
plt.show()


