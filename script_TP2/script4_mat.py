import numpy as np
from math import *
import matplotlib.pyplot as plt

#size of the matrix
sx = 1000  
sy = 1000

#matrix definition
my_mat = np.zeros((sx,sy))


#function to draw a ring
def ring(mat,sizex,sizey,xc,yc,r_in,r_out) :
    for i in range(sizex) :
        for j in range(sizey) :
            r = sqrt(  (i-xc)**2. + (j-yc)**2. )
            if r <= r_out  and  r > r_in :
#              mat[i][j] = 1.0   # equivalent to instruction below
              mat[i,j] = 1.0   

#function to draw a rectangular shape 
def bar(mat,sizex,sizey,xc,yc,lx,ly) :
    for i in range(sizex) :
        for j in range(sizey) :

            dx = abs(i-xc)
            dy = abs(j-yc)

            if dx < lx/2.0  and  dy < ly/2.0 :
#              mat[i][j] = 1.0   # equivalent to instruction below
              mat[i,j] = 1.0

# coordinates:
# deltax=0.1; everything in units of deltax
# x=(i+1)*deltax; y=(j+1)*deltax
# i=x/deltax-1; j=y/deltax-1

#larger ring
xc1 = 500.-1 
yc1 = 200.-1
r_in1 = 100.
r_out1 = 160.
ring(my_mat,sx,sy,xc1,yc1,r_in1,r_out1)

#smaller ring
xc1 = 500.-1
yc1 = 750.-1
r_in1 = 30.
r_out1 = 112.
ring(my_mat,sx,sy,xc1,yc1,r_in1,r_out1)

# rod linking the rings
xc3 = 500.-1
yc3 = 500.-1
lx = 100.
ly = 300.
bar(my_mat,sx,sy,xc3,yc3,lx,ly)


# plot the matrix
plt.matshow(my_mat, cmap='Greys')
# plot options
plt.colorbar()                   # colorbar
plt.xticks(range(0,1001,200))    # ticks on x-axis
plt.yticks(range(0,1001,200))    # ticks on y-axis
plt.show()      

#plot the centerline section
#plt.plot(my_mat[:][500] , linewidth=4.0)   # this instruction is not equivalent to the one below
# select matrix row containing centers
plt.plot(my_mat[xc1,:] , linewidth=4.0)
plt.axis([0.0,1000.0,0.0,1.05])
plt.show()




