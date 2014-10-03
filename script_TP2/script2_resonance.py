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
Qmax=10.
deltaQ=2.
Q=0.05
u=np.linspace(0,2,100)

# compute transfer function
# for various values of Q
while Q<Qmax:
   T=transfer(u,Q)

   plt.plot(u,T,label="Q = %1.2f" % Q)
   Q *= deltaQ

###################################################
# plot curves of T(u) for several values of Q
plt.xlabel("u")
plt.ylabel("T(u)")
plt.legend(loc='upper right')
plt.show()

