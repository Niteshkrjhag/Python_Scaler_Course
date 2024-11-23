# Global keyword in Python
'''
It's used to declare that a variable inside a function is global, not local,
allowing you to update the global variable's value from within the function.

Without the global keyword, any variable assigned a value within a function
is assumed to be local unless explicitly declared as global.
'''

x = 10
def change_x():
    global x
    x=20

print(f"Before x : {x}");change_x();print(f"After x: {x}")