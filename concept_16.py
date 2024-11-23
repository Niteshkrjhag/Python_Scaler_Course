#explicit type conversion 
'''
Type conversion is a process by which you can convert one data type into another.
The conversion of one data type into another, done via user intervention or manually as per the requirement, 
is known as explicit type conversion.
It can be achieved with the help of Python’s built-in type conversion functions such
as : 

int()
float()
ord()
float()
hex()
oct()
tuple()
set()
list()
dict()
str()

Explicit type conversion is also known as Type Casting in Python.


'''

#int(x,base) : This function can convert a floating-point number or string into an integer data type.

# a = "1111"
# b = int(a,2)
# c = int(a,10)
# d = int(a,16)
# e = int (a,8)
# print(f"""
#       a = {a},
#       b = {b},
#       c = {c},
#       d = {d},
#       e = {e}
#       """)

#float(x) :  you can convert an integer or string into a floating-point number. 

str = "223.087"
a = float(str)
print(f"a : {a}")

#ord(x) : This ord() function converts characters into their integer ASCII value.
           #ASCII is an integer value that is assigned to each character and symbol.
           
b = ord('x')
print(b)

#hex(x) : Using the hex() function, the user can convert an integer into a hexadecimal string.
#oct(x) : Just like the hex function, this function only converts an integer into an octal string.
#tuple(x) : This function is used to convert any iterable into a tuple.

c = tuple("AEIOU")
print(c)

#set(x) : The set() function is used to convert any iterable into sets.
d = set("AEIOU")
print(d) #imp

#list() : We use the list() function to convert an iterable into a list.
e  = list("AEIOU")
print(e)

#dict(x) : Using this function, the user can convert data type into a dictionary but 
#          the data type should be in the sequence of (key,value) tuples. 
#          examples of key-value pairs are- ((‘1’, Rahul), (‘a’, ‘Alphabet’)).

x = (('a',3),('f',4),('t',9))
print(dict(x))

#str(x) : The str() function is used to convert any data type into the string data type.

