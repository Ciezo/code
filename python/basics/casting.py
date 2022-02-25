###############################################
# @author Cloyd Van S. Secuya 
# Date: Febuary 26, 2022
##############################################

# Casting variable is just like wrapping variables under a certain data type wherein we try to 
# explicitly declare a variable by wrapping a data type around it.

# From w3schools: 
#   If you want to specify the data type of a variable, this can be done with casting.

# Lastly, with casting it can be helpful in many ways especially when we are trying to explicitly announce the
# data type of variable we want to assign 


# Casting of int type
var_int = int(31) 
print(var_int)
print(type(var_int))

# Casting float value 
var_fl = float(27.5)
print(var_fl)
print(type(var_fl))

# Casting of string value 
var_str = str("Hello, world!")
print(var_str)
print(type(var_str))

# Casting of boolean type 
isTrue = None
var_bool = bool(isTrue)

if (var_bool == False):
    var_bool = True

print(var_bool)
print(type(var_bool))