#String formatting is also known as String interpolation
'''
It is the process of inserting a custom string or variable in predefined text.
String formating in string can be done using below technique --

1)String Formatting in Python Using Format Specifiers

       %d for int
       %s for string
       %f for floating - point decimal
       %e for floating - point exponential
       %c for single charcter

a = 1
b = 2 
c = 3
print("%d is greater than %d but smaller than %d" % (b,a,c))

2)String Formatting in Python Using f-strings

name = "nitesh"
age = 22
collage = "nit"
print(f"my name is {name} age is {age} and collage is {collage}")

3)String Formatting in Python Using the format() Method

name = "nitesh"
age = 22
collage = "nit"
print("my name is {2} age is {0} and collage is {1}".format(age,collage,name))
'''

'''
What is a significant advantage of using f-strings over the traditional % operator for string formatting?
=>f-strings automatically handle data types and order of variables

Numbers can also be left, right, or center aligned using Python format() method.


 n is the total length of the required output string.
For displaying a number with left alignment, we use the “:<n” symbol inside the placeholder in the format() method. 

#Truncating Strings Using the format() Method in Python
To truncate a string to a specific length, we use the symbol “:.n” 
inside the placeholder of the empty string at which the format() method is invoked. 

#Padding Strings Using the format() Method in Python
We use the same syntax we used for alignment operation to perform padding on the strings. 

#Dynamic Formatting Using the format() Method in Python
 To dynamically set the size of the output string, we can pass the size as input to the format() method. 

'''

a = -1234
print("my output string i want is 10 so {:<10}. ".format(a))
print("my output string i want is 10 so {:>10}. ".format(a))  #right alignment
print("my output string i want is 10 so {:^10}. ".format(a))  #center Alignment

b = "Nitesh"
print("Trauncating string {:.3}.".format(b))

print("Padding left {:*<10}.".format(b))

print('>>>>')
c = 'NItesh'
print("dynamic formatting of c {:>{}}.".format(c,3))
