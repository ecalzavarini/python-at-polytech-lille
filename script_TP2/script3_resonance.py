from math import *
import numpy as np

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
deltaQ=0.000001
Q=0.5
u=np.linspace(0,2,100)

# compute transfer function
# and check maximum
while n<Nmax:
   T=transfer(u,Q)

   Q += deltaQ
   n += 1
#   print("n = %d" % n)
   if np.amax(T) > A: 
      break

###################################################
# print results
print("")
print("computation of the critical value between overadamped and resonating oscillations")
# number of iterations for determination of Qstar with resolution deltaQ
print("number of iterations = %d" % n)
# computed critical value
print("Qstar = %1.6f" % Q)
# theoretical critical value: Qstar_T=1./sqrt(2.)
print("Qstar - Qstar_T = %1.6f" % (Q - 1./sqrt(2.)))
print("")
