#Control Flow Statements in Python

'''
Python has three types of control structures:

Sequential
Selection
Repetition
'''

#Short Hand if-else statement in Python (ternary operator)
''' statement_when_True if expression else statement_when_False '''   

# age = 29
# result = "Adult" if age>29 else "Minor"
# print(result)

#While Loop with else
'''
the else statement will be executed once the execution of the while is completed normally but if breaks 
in middle then else will not be executed.
'''

# a = 10
# while(a>0):
#     print(f"a is : {a}")
#     if(a==5):
#         print("stopped")
#         break
#     a-=1
# else:
#     print("while completed without interrupt")

'''The prefix 0O or 0o indicates that the number is written in octal.'''
#VVI question what will be its soution can you find it
i = 5
while True:
 if i%0o11 == 0:
  break
 print(i)
 i += 1
 