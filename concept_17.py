#Boolean Operators

'''
 Instructions that combine operators and values 
 to perform mathematical or logical computations are called expressions.
 
 or,and are binary operator as they requrie two operand 
 where as not is unary operator as it require one operand
 
'''

#Chaining Comparison Operators
print(1<2<3)
print(1<2 and 2<3)

print(1 == 1.0 > 0.75)
print(2 == 2.0 < 1.5)
print(3 < 2 < "2")

grade = 95
print(100 >= grade >= 80)

#Short-Circuit Chaining
'''
Short-circuiting occurs when the execution of a boolean chain 
stops when the truth value of an expression has been determined.
'''
print("...")
print(3<2<"3")      #no error but print(2<3<"4") error
print(3<2<(1/0))    #no error but print(2<3<(1/0)) error
print("...")

#None as a Boolean Value  -->  None is considered as a Boolean False.
print(bool(None))

#Numbers as a Boolean Value
'''
In Python, 0 is considered to be False. Every other number, 
whether positive or negative, is True. Even Inf and Nan are considered to be True.
'''

#Sequences as a Boolean Value
'''
In Python, the len() value (Length) of objects is considered while evaluating their 
truthiness (whether True or False). 
'''
print(bool(''))    #it will first calculate len of the parameter inside bool fun and then evaluate it.
print(bool([]))

#application of boolean is that (and,not) narrows the search whereas or broaden the search