# Python Input and Output

'''

In Python, program output is displayed using the print() function,
while user input is obtained with the input() function.
Python treats all input as strings by default, requiring 
explicit conversion for other data types.

1) input('prompt ')

'''
#Taking single input from the user

a = input('Enter your name ')
b = int(input('Enter your age '))   #type conversion
print(f"Your name is {a} and age is {b}")

#Taking multiple input from the user

'''

Taking multiple inputs from a user in a single line in 
Python can be efficiently handled using the input() function combined with string methods 
like split().

Taking inputs for the Sequence Data Types like List, Set, Tuple
'''
#Taking input for a list of integers
list1 = input('Enter number separated by space : ').split()
print(list1)

# Taking input for a set of integers
integer_set = set(input("Enter numbers separated by space: ").split()) #set doesnot store input as in provided
                                                                    #ordered as they are unordered data type.
print("Set of integers:", integer_set)

#Taking input for a tuple
tuple1 = tuple(input('Enter number separated by space : ').split())
print(tuple1)


