###############################################
# @author Cloyd Van S. Secuya 
# Date: Febuary 26, 2022
##############################################

# Logical operators are used for combining conditions. These are typically used when we are trying to meet 
# certain multiple conditions that we want to all be met by the program. 


# Grades and score evaluation 
grades = [] 
grades = list(map(int, input('Enter grades: ').split(" ")))
print(grades)
# NOTE: We can enter multiple inputs by using a list then we can separate the values using an empty space through split()
#       Then, using map() we can pass it as input and as float type

# Loop through the list to get the average result from the grades number
sum = 0 
ave = 0 
for num in grades: 
    sum += num
    ave = sum/len(grades)
print(ave) 