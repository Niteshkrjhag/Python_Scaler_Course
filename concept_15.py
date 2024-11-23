#implicit data type conversion

'''
Explicit data type conversion is where you force a Python compiler to convert a data type into another.
When python itself does data type conversion, it's called Implicit Data Type Conversion.
'''

#eg. of implicit datatype conv.
num1  = 2
num2 = 3.2
num3 = num2 + num1
print(f"num1 datatype is {type(num1)} and num2 is {type(num2)}")
print(f"resultant is ",num3,f" datatype is {type(num3)}")

#This implict conversion is done to higher level to avoid data loss.