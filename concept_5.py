#Types of Variable in Python

#1) Integers
a=2
print(f"a : {a}")

#2) float
b = 2.3
print(f"b : {b}")

#3) string
c = "Nitesh"
print(f"c : {c}")

#4) boolean
d = True
print(f"d : {d}")

#5) list : are sequences of elements that maintain an order and can contain items of various types.
e = ['nitesh',1,2.3,True]
print(f"e : {e}")

#6) Tuple : resemble lists in many aspects, yet they are immutable, signifying that once created, they cannot be altered.
f = ('nitesh',1,2.5,False)
print(f"f : {f}")

#7) dictionaries : hold key-value pairs. Keys must be unique and immutable.
g = {"nitesh":2,"sumit":3,4:"nitesh"}
print(f"g : {g}")

#8) Sets : Sets are unordered collections of unique elements.
h = {'nitesh',1,2.5,False}
print(f"h : {h}")

#Delete a variable
'''You can delete a variable or function using the del command in Python.'''
x = 2
print(f"x : {x}")
del x
try:
    print(x)
except :
    print(f"x deleted")