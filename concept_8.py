#Use of async and await Keyword

'''
import asyncio

async def name():
    print("Hello !")
    await asyncio.sleep(3)
    print("Nitesh")

asyncio.run(name())
'''

# Use of from Keyword

'''
from math import pi

print(pi)
'''

#Use of is keyword

'''
x = [1,2,3]
y = [4,5]            # What will be the output?
z = x                 # what will be the output?
print(x is y)
print(z is x)
'''

#Use of import Keyword

'''
import math
print(math.sqrt(16))
'''

 #Use of finally Keyword

'''
try:
    print(1/0)
except ZeroDivisionError:
    print("Division by zero not allowed ")
finally:
    print("Executing at last")
'''

# Use of pass Keyword : `pass` does nothing

'''
for x in [1,2,3]:
    pass
'''

# Use of assert Keyword : (No output, assertion is true)

''' assert 2+2 == 4 '''

#Use of Yield keyword

'''
def generator():
    yield "hello"
    yield "Nitesh"
    
gen = generator()  // similar concept like readLine in aspect of File
print(next(gen))
print(next(gen))
'''

#Use of Global keyword

'''
x = 20
def change():
    global x
    x = 40
change()
print("x: {}".format(x))
'''

# lambda Keyword

'''
add = lambda x,y:x+y
print(add(1,3))
'''

# try, except, raise


'''
try:
    raise ValueError("Error Occured")
except ValueError as e:
    print(e)
'''

    


