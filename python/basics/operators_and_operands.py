###############################################
# @author Cloyd Van S. Secuya 
# Date: Febuary 26, 2022
##############################################

# Operators are symbols responsible for computing operations and tasks like addition, multiplication, subraction, division, 
# and exponentiations. Moreover, there are in-built functions that can perform rigourous and long computations with the help of 
# imported libraries. 
# 
# In Python just like other programming languages we have +, -, *, /, and **. All of which are responsble for 
# addition, subtraction, multiplication,division, and exponentiation respectively.
# Lastly, these said operators are for arithmetic operations that can produce a numerical result. 


# On the other hand, we also have comparison operators which are used for comparing values and expressions. 
# These operators include <, >, <=, >=, ==, !=. 
# All of  which corresponds to less than to, greater than to, less than or equal to, greater than or equal to, 
# is equal to, and not equal to respectively. 
# These operators may result to boolean outputs, as such these are used for conditional values when we try to compare
# expressions, values, and statements. 

##############################################
# From the book: 
#   Operators are special symbols that represent computations like addition and multiplication. 
#   The values the operator is applied to are called operands
##############################################

# ARITHMETIC OPERATORS
# ____________________________
# Using the addition operator, + 
a = 10 
b = 11 
c = a + b          # the variables a and b here are called operands with the addition operation 
print(c)

# Using the subtraction operator, - 
d = b - c
print(d)

# Using the multiplication operator, * 
e = a * b  
print(e) 

# Using the division operator, / 
num1 = 64 
num2 = 2
num_result = num1 / num2
print(num_result)

# Using the exponentiation operator, ** 
# NOTE: a ** b, where a is the base and b is the power 
#       so, a to the power of b 
exp_n = 2 ** 3 
print(exp_n) 

exp_n = exp_n * (c + d + e + num_result)
print(exp_n)




# COMPARISON OPERATORS 
# ____________________________
# For this exercise and practice, we will try to define a function which evaluates two numbers whether they 
# are larger, smaller, or equal to each other. 
def eval_output(comp_val1, comp_val2):
    if (comp_val1 == comp_val2):
        print("Both numbers are equal")
    
    elif (comp_val1 >= comp_val2): 
        print("Value 1 is HIGHER")
        result_eval = comp_val1
        return result_eval

    elif (comp_val1 <= comp_val2):
        print("Value 2 is HIGHER")
        result_eval = comp_val2
        return result_eval



# Call the function
# Here, num1 is bigger
eval_op = eval_output(num1, num2)
print("The larger number is: ", eval_op)

# Here, the second parameter is larger
result_op = eval_output(20, 100)
print(result_op)

# For this call, we have both numbers
eval_output(10, 10)