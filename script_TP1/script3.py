from math import *

# Open a file
f = open("pressure.txt", "r")
# define an empty list
data=[]
# read full file and split into its parts 
data=f.read().split()
# Close opend file
f.close()


ps = 24000. 
rho = 0.91875

sum=0.0;

for i in range(0,len(data)) :

    data[i] = sqrt( (float(data[i]) - ps)/rho )

    data[i] *= 3600./1000.

    print(data[i]) 

    sum += data[i]

print("The average velocity is %f" % (sum/len(data))+" Km/h")    
