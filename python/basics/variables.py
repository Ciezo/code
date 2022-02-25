###############################################
# @author Cloyd Van S. Secuya 
# Date: Febuary 22, 2022
##############################################

# Declaring a variable in Python is very easy, we do not really need to declare its data type before naming it
# Unlike in othe programming languages like C, C++, and Java, where we declare a data type for each variable. 
# In Python, we simply assign a value into a variable, and the interpreter knows what type it is.  

# Common Data Types 
# Integer, Long, Float, Double, Boolean, String, Character

# Declaring a variable of numeric types 
num_int = 1 
print(num_int)

num_float = 1.50 
print(num_float)

# Declaring a variable of String 
message = "Hello, World!"
print(message)

# Declaring a variable of character 
# NOTE: Characters contain only one literal character value
character = 'E'
print(character)

# NOTE: In Python, whenever we declare a string type or a character. Python considers the character to be of String type. 
#       Any value masked with either single or double quotation marks are of always string value 
print("This variable is a type of", type(character))

##############################################
# From the book: 
#   Not surprisingly, strings belong to the type str and integers belong to the type
#   int. Less obviously, numbers with a decimal point belong to a type called float,
#   because these numbers are represented in a format called floating point.
##############################################


# Declaring a boolean variable with boolean value
isProgramming = True        # This is of type boolean with a True value assigned to it 
isFlying = False            # False value assigned to it 
# NOTE: Just like in any programming languages, the True and False are reserved keywords

##############################################
# Conclusion and wrap up
# From w3schools: 
#   Python has no command for declaring a variable.
#   A variable is created the moment you first assign a value to it.

#   Variables do not need to be declared with any particular type, and can even change type after they have been set.
##############################################

# Moreover, variables can be of any type as long as their is a proper value assigned to it. Variables can have multiple 
# ways of being assigned a value into it. And the last or most recent assignment will be the value contained into that variable
var1 = 1            # This is the first assignment
var1 = 1.5          # This is the second assignment which will overwrite the previous one
var1 = "Cheese"     # This will overwrite the previous one too 
var1 = True         # Now, var1 will be boolean variable in its last recent assignment and assigned value

print("Most recent assignment and value: ", var1)
print("Data and value type of var1: ", type(var1))

#################################
# NEXT: Casting