# script for conversion

print("Conversion of pressure measurements")

unit_in = input("Please insert pressure units, choosing among [ pa, bar , atm , psi , torr ] ")
print("chosen unit is %s" % unit_in )

val_in = input("Please insert pressure value =  ")
val_in = float(val_in)
print("given value is " + str(val_in) + " " + str(unit_in) )


unit_out = input("Please insert pressure output units, choosing among [ pa , bar , atm , psi , torr ] ")
print("chosen output unit is %s" % unit_out )


# first we convert the in value to Pascal
if unit_in == 'psi' :
    val_pa  = val_in * 6.8948e+3  
elif unit_in == 'atm' : 
    val_pa  = val_in * 1.01325e+5  
elif unit_in == 'bar' :
    val_pa  = val_in * 1.e+5    
elif unit_in == 'torr' :
    val_pa  = val_in * 133.3224  
elif unit_in == 'pa' :
    val_pa  = val_in 
else :
    print("unknown given unit")

# then we convert the Pascal to the desired value
if unit_out == 'psi' :
    print("converted to psi")
    val_out  = val_pa * 1.450377e-4
elif unit_out == 'atm' :
    val_out  = val_pa * 9.8692e-6
    print("converted to atm")
elif unit_out == 'bar' :
    val_out  = val_pa * 1.e-5
    print("converted to bar")
elif unit_out == 'pa' :
    val_out  = val_pa 
    print("converted to pa")
elif unit_out == 'torr' :
    val_out  = val_pa * 7.5006e-3
    print("converted to torr")

print(val_out)
