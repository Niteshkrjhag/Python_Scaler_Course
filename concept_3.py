#Global and Local Python Variables

'''In Python, variables' scope—where they can be accessed—is determined by where they are defined. 
# The two main types of variable scope are global and local.'''

#Global Variables

'''Global variables are declared outside of functions or in the global scope,
meaning they can be accessed throughout your code, including inside functions.'''

# x = 3
# def fun():
#     print("X inside the function value is : {}".format(x))
    
# print(f"X outside: {x}")
# fun()

#Local Variables

'''Local variables are declared inside a function and can only be used within that function's scope of variables in python.
They are created when the function starts and destroyed when the function ends.'''

def fun(x=0):
    x+=x
    print(f"X is inside the function : {x}")

x = 10
print(x)
fun(x)
print(x)

