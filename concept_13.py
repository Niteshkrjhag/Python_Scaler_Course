#Displaying Output in Python
'''
print(object(s), sep=' ', end='\n', file=file, flush=False)


1)object(s)         are the values to be printed on the screen. 
                    They are converted to strings before getting printed.

2)sep keyword       is used to specify how to separate the objects inside the same print statement. 
                    By default, we have it as sep=' ', a space between two objects.
                    
3)end               is used to print a particular thing after all the values are printed. By default,
                    we have end as \n, which provides a new line after each print() statement.

4)file              is used to specify where to display the output. By default, it is sys.stdout 
                    (which is the screen).

5)flush             specifies the boolean expression if the output is False or True. 
                    By default, it is False. In Python, the output from the print() goes into a buffer. 
                    Using the flush= True parameter helps in flushing the buffer as soon as we use the 
                    print() statement.
'''

print("apple","banana","cat",sep=', ')
print("Hello",end=' ')
print("world")

#. Using formatted string literals
name = "Nitesh"
print(f"my name is {name}")
print("my name is {}".format(name))

num = 10
print("The number is %d" % num)  #%d only works for real number only

#Manual String Formatting  =>Manual string formatting involves using string operations like concatenation 
#                           and methods like str.ljust(), str.rjust(), and str.center() to format strings.
print(name.ljust(10,'-'))
print(name.rjust(10,'-'))
print(name.center(10,'-'))
