# script for conversion

print("Conversion of pressure measurements")

unit_in = input("Please insert pressure units, choosing among ['pa','bar','atm','psi'] ")
print("chosen unit is %s" % unit_in )

val_in = input("Please insert pressure value =  ")
print("given value is " + str(val_in) + " " + str(unit_in) )


unit_out = input("Please insert pressure output units, choosing among ['pa','bar','atm','psi'] ")
print("chosen output unit is %s" % unit_out )


# first we convert the in value to Pascal
if unit_in == 'psi' :
    val_pa  = val_in * 6.8948e+3  #convert to pa   
elif unit_in == 'atm' : 
    val_pa  = val_in * 6.8948e+3  #convert to pa 
elif unit_in == 'bar' :
    val_pa  = val_in * 6.8948e+3  #convert to pa 
elif unit_in == 'pa' :
    val_pa  = val_in * 6.8948e+3  #convert to pa 
else :
    print("unknown given unit")

# then we conver the Pascal to the desired value
if unit_out == 'psi' :
    print("converted to psi")
    val_pa  = val_in * 6.8948e+3  #convert to pa                                    
elif unit_out == 'atm' :
    print("converted to atm")
elif unit_out == 'bar' :
    print("converted to bar")
elif unit_out == 'pa' :
    print("converted to pa")

