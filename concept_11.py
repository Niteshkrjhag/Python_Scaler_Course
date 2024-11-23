#Operators in Python

'''
Operators in Python are special symbols that carry arithmetic or logical operations.
The value that the operator operates on is called the operand.
In Python, there are seven different types of operators: arithmetic operators,
assignment operators, comparison operators, logical operators, identity operators, 
membership operators, and boolean operators.


'''

a = 5//2   #Floor Division : ignores the decimal value if present
b = 5/2
c= 5**2    #Gives the result of 5 to the power 2
print(f"a: {a}, b: {b}, c: {c}")

#Identity Operators 

'''
These operators compare the left and right operands and check if they are equal,
the same object, and have the same memory location.

is      ->  Return true if both variables are the same object
is not  ->  Return true if both variables are not the same object

'''


list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)  # True, because both lists have the same values
print(list1 is list2)  # False, because they are different objects in memory

a = 10**8
b = 10**8
c = a       # This assign same memory to the object as here for c and a
print(a == b)   # True, because the values of a and b are both 5
print(a is b)   # True, because small integers like 5 are cached by Python, so a and b reference the same object in memory
print(c is b)   # True, because c is assigned the value of a, which is the same object as b
print(c is a)   # True, because c is assigned to a, so they point to the same object
print(a is c)   # True, the same reason as above


#MEMBERSHIP OPERATORs in Python

'''
These operators search for the value in a specified sequence and return True or False accordingly

in -> 
not in ->
'''

print(5 in list1)
print(3 in list1)


x,y,z=7,5,4
print((x^y&z))   #what will be the answer?


#look for precedence table



