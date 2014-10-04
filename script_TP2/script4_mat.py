import numpy as np
from math import *
import matplotlib.pyplot as plt

sx = 1000
sy = 1000
my_mat = np.zeros((sx,sy))


def ring(mat,sizex,sizey,xc,yc,r_in,r_out) :
    for i in range(sizex) :
        for j in range(sizey) :
            r = sqrt(  (i-xc)**2. + (j-yc)**2. )
            if r <= r_out  and  r > r_in :
              mat[i][j] = 1.0


def bar(mat,sizex,sizey,xc,yc,lx,ly) :
    for i in range(sizex) :
        for j in range(sizey) :

            dx = abs(i-xc)
            dy = abs(j-yc)

            if dx < lx/2.0  and  dy < ly/2.0 :
              mat[i][j] = 1.0

xc1 = 500.
yc1 = 200.
r_in1 = 100.
r_out1 = 160.
ring(my_mat,sx,sy,xc1,yc1,r_in1,r_out1)

xc1 = 500.
yc1 = 750.
r_in1 = 30.
r_out1 = 112.
ring(my_mat,sx,sy,xc1,yc1,r_in1,r_out1)


xc3 = 500.
yc3 = 500.
lx = 100.
ly = 300.
bar(my_mat,sx,sy,xc3,yc3,lx,ly)



plt.matshow(my_mat, cmap='Greys')

plt.colorbar()

plt.xticks(range(0,1001,200)) 
plt.yticks(range(0,1001,200))

plt.show()      



plt.plot(my_mat[:][500] , linewidth=4.0)
plt.axis([0.0,1000.0,0.0,1.05])
plt.show()




