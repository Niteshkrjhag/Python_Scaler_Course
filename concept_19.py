#For Loop Syntax :
'''
for val in sequence:
    loop body
    
'''
# Python program to iterate over a string using a for loop.
string_var = 'Interviewbit'
# Method 1: Iterating over a string
for character in string_var:
    print(character, end=' ') 
print('\n')
# Method 2: Iterating using indexing
for i in range(len(string_var)):            #by default i will start from 0 and goes till less than value inside range(value)                                         #
    print(string_var[i], end=' ') 
print('\n')
# Method 3: Iterating using enumerate()
for k, v in enumerate(string_var):
    print(v, end=' ')

#The Range function :
'''
This function returns a sequence of numbers that, by default, starts with zero,
increments by 1, and ends at a specified number passed as an argument

range(stop): starts from zero till stop-1 incrementing by 1;

range(start, stop): starts form start till stop-1 incrementing by 1;

range(start, stop, step/Increment): : starts form start till stop-1 incrementing by step;
'''

#Else in Python For Loop

# for i in range(10):
#     print("hello")
# else:
#     print("10times")
    
# Python program having an empty loop

#VVI concept 
name = 'Interviewbit'
for alphabet in name:
    pass
print(f'The last letter in the name is {alphabet}')


'''
	•	The reason alphabet is still accessible is due to Python’s scoping rules: the loop does not 
 introduce a new local scope, so the variable remains defined after the loop ends.
 
 if you want to end the alphabet then you need to use del(alphabet);
'''
