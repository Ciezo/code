###############################################
# @author Cloyd Van S. Secuya 
# Date: Febuary 26, 2022
##############################################

# Statements allow us to execute lines of codes in Python and other programming languages. 
# We have been executing statements all this time such as the print() and type() as well as assigning values to variables
# Executing statements come by line per line when the interpreter goes to read and execute your Python file. 
# Moreover, a bunch of statements can create a huge block of code or sometimes a script to complete a task. 


##############################################
# From the book: 
#   A statement is a unit of code that the Python interpreter can execute. We have
#   seen two kinds of statements: print being an expression statement and assignment.
#     
#   When a line of code has an expected output or result to be displayed. The interpreter executes it 
#   and displays the output if there is one.
# 
##############################################

# A statement where we assign a variable 
x, y, name = 1, 2, "Cloyd"
# NOTE: This is called assigning and declaring multiple variables into one line or a single statement 
#       where each value will go into each variable respectively 

# Before function call:
print("Before function call: ")
print(x)
print(y)
print(name) 

def get_user_input(x, y, name): 
    x_new, y_new, name_new = x, y, name
    return x_new, y_new, name_new

x = int(input("Enter an Integer number: "))
y = float(input("Enter a Float number: ")) 
name = str(input("Enter your name: "))

# Call the function and assign the returning values into a new variable
get_x, get_y, get_name = get_user_input(x, y, name)

# Print the result after the function call
print(get_x)
print(get_y)
print(get_name)

##############################################
# Conclusion and wrap up
# From book: 
#   A script usually contains a sequence of statements. If there is more than one
#   statement, the results appear one at a time as the statements execute.

#   What we did so far is we simply tried to showcase different ways statements can be seen and used in Python. 
#   Remember that statement is a unit of code where we can execute what that line of code does. And if there is an output
#   It will be displayed accordingly and rightfully by the interpreter. 
# 
#   Actually, what you are always writing in code is a bunch of statements, expressions, and code blocks where we try and solve
#   the task in an objective and procedural way. So always remember that you are always creating statements whenever you code! 
##############################################


#################################
# NEXT: Operators and Operands