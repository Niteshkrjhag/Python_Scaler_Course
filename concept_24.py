#Function 

'''
def function_name (parameters):
    """docstring """
   statement1
   statement 2
   …
   …
   return [expr]
   
   #Types of Python Function Arguments
   
   Positional Arguments:            These are the most common arguments, where the argument's
                                    value is based on its position. For example, in func(a, b), a and b are positional 
                                    arguments.
                         
   Keyword Arguments:               The parameter name identifies these and can be supplied in any order, 
                                    making your code more readable. For instance, func(a=1, b=2) explicitly states 
                                    which parameter each argument corresponds to.
                         
   Default Arguments:               A parameter with a default value can be omitted in the function call. 
                                    The function will then use the default value.
                                    
   Variable-length Arguments:       You may need to determine the number of arguments supplied to your function.
                                    Python allows you to handle this with variable-length arguments, defined with 
                                    an asterisk *args and **kwargs.

#Documentation strings, or docstrings, are literal strings used to document a 
Python module, function, class, or method. 

#Python Function within Functions

def outer_function(text):
    def inner_function():
        return text.upper()
    return inner_function()

result = outer_function("hello")
print(result)

#Anonymous Functions in Python

An anonymous in Python is a function that is defined without a name. 
lambda arguments: expression


#Return Statement in Python

The return statement exits a function and returns to where it was called. This statement can 
optionally return a value from the function to the caller. If no expression is specified, 
None is returned.


#Pass by Reference and Pass by Value

Pass by Reference

Concept:            a reference (or pointer) to the actual data is passed in pass-by-reference.
                    Modifications to the parameter within the function affect the passed argument.
                    
Python's Approach:  Python doesn’t strictly follow this but behaves similarly with mutable objects. 
                    When a mutable object is passed, changes to it inside the function are reflected 
                    outside the function.
Pass by Value

Concept:            Pass by value means the actual value is passed. The function works on a copy, 
                    and changes within the function do not affect the original data.
                    
Python's Approach:  With immutable objects (like integers and strings), Python's behaviour is akin 
                    to pass-by-value. Changes made to an immutable object in a function do not reflect in 
                    the original object.

Benefits of Python Functions

Helps in increasing code modularity – Python functions help divide the code into smaller problems and solve 
                                      them individually, thus making it easier to code.

Minimizes Redundancy –                Python functions help you save the effort of rewriting the whole code. 
                                      All you have to do is call the Function once it is defined.

Maximus Code Reusability –            Once defined, the Python Function can be called as many times as 
                                      needed, thus enhancing code reusability.

Improves Clarity of Code –            As the extensive program is divided into sections with the help of 
                                      functions, it helps increase the readability of code while ensuring 
                                      easy debugging.



Python neither uses a pass-by-value nor a pass-by-reference mechanism, 
but it uses pass-by-object reference.

We can pass up to 255 parameters in a function in Python.


'''

square = lambda x: x*x
print(square(2))

def modify_elements(collection):
    if isinstance(collection, list):
        collection.append(100)  # This will affect the passed list
    else:
        collection += 10  # This won't affect the passed integer
        print(collection)
        

# Mutable example
my_list = [1, 2, 3]
modify_elements(my_list)
print(my_list) 

# Immutable example
my_num = 7
modify_elements(my_num)
print(my_num)


'''
Q)Which of the following is true for functions in Python?

1)A Python function can return only a single value
2)A function can take an unlimited number of arguments.
3)A Python function can return multiple values
4)Python function doesn’t return anything unless and until you add a return statement

ans is 2 and 3

1.	A Python function can return only a single value:
False. In Python, a function can return multiple values. These values can be returned as tuples, 
lists, or other collection types.

	2.	A function can take an unlimited number of arguments:
True. In Python, a function can accept an arbitrary number of arguments using *args 
(for positional arguments) or **kwargs (for keyword arguments).
	3.	A Python function can return multiple values:
 
True. A Python function can return multiple values. Technically, the function returns a tuple, 
but it can be unpacked into multiple variables.

	4.	Python function doesn’t return anything unless and until you add a return statement:
False. If a function doesn’t have a return statement, it implicitly returns None by default.

'''