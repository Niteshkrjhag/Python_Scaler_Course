
# *args and **kwargs 

'''
Python has *args, which allows us to pass a variable number of non-keyword arguments to a function. Non-keyword here means that the arguments should not be a dictionary (key-value pair), and they can be numbers or strings.

def multiply(*args):
    ans = 1
    for i in args:
        ans*=i
    return ans


a = multiply(2,3,4,5)
print(a)

When an asterisk(*) is passed before the variable name in a Python function, then it understands that here the number of arguments is not fixed. Python makes a tuple of these arguments with the name we use after the asterisk(*) and makes this variable available to us inside the function. This asterisk(*) is called an “unpacking operator”.

Keyword arguments mean that they contain a key-value pair, like a Python dictionary.
In Python, these keyword arguments are passed to the program as a Python dictionary.

def makeSentence(**words):
    sentence=''
    for word in words.values():
        sentence+=word
    return sentence
 
print('Sentence:', makeSentence(a='Kwargs ',b='are ', c='awesome!'))

In the makeSentence function, we are iterating over a dictionary, so we have to use values() to use the values. Otherwise, it will only return the keys and not the values.

def whatTechTheyUse(**kwargs):
    result = []
    for key, value in kwargs.items():
        result.append("{} uses {}".format(key, value))
    return result
 
print(whatTechTheyUse(Google='Angular', Facebook='react', Microsoft='.NET'))

Using Both *args and **kwargs in Python to Call a Function

the order of the arguments matters; *args have to come before *kwargs.

So, if you are using standard arguments along with *args and **kwargs, then you have to follow this order-

Standard Arguments
*args
**kwargs

def printingData(codeName, *args, **kwargs):
    print("I am ", codeName)
    for arg in args:
        print("I am arg: ", arg)
    for keyWord in kwargs.items():
        print("I am kwarg: ", keyWord)
 
printingData('007', 'agent', firstName='James', lastName='Bond') 

==> Output: 

  I am 007 
  I am arg: agent 
  I am kwarg: (‘firstName’, ‘James’) 
  I am kwarg: (‘lastname’ , ‘Bond’)

	*args: Allows you to pass a variable number of positional arguments to the function. In this case, it’s used to capture the rectangle’s length and width.
 
	•	**kwargs: Allows you to pass a variable number of keyword arguments to the function, used here to capture optional attributes like color and label.
 

'''

 class EnhancedRectangle:
    def __init__(self, *args, **kwargs):    #The class EnhancedRectangle has an __init__ method, which is a special method called the constructor. It initializes the attributes of an object when the object is created.
        self.length, self.width = args  #	•	This line unpacks the args into two values, length and width. So, args must contain two values (as passed when creating the rectangle object).

        self.color = kwargs.get('color', 'white') #	•	kwargs.get('color', 'white'): This tries to retrieve the value for the key color from kwargs. If no color is passed, it defaults to 'white'.
        self.label = kwargs.get('label', None)  #kwargs.get('label', None): Similarly, this retrieves the value for the key label. If no label is passed, it defaults to None.

rect1 = EnhancedRectangle(4, 6, color='blue', label='Rectangle A')
rect2 = EnhancedRectangle(5, 8, color='red')

print(rect1.color)
print(rect2.label)


#Unpacking operators are used to unpack the variables from iterable data types like lists, tuples, and dictionaries.

'''
carCompany = ['Audi','BMW','Lamborghini']
print(*carCompany)

Output => Audi BMW Lamborghini

Here, the asterisk(*) passed before carCompany unpacked all the values. In other words, the values are printed as separate strings rather than a list.

techStackOne = {"React": "Facebook", "Angular" : "Google", "dotNET" : "Microsoft"}
techStackTwo = {"dotNET" : "Microsoft"}
mergedStack = {**techStackOne, **techStackTwo}
print(mergedStack)

Output:
{'React': 'Facebook', 'Angular': 'Google', 'dotNET': 'Microsoft'}

Summary

=>*args and **kwargs are special Python keywords that are used to pass the variable length of arguments to a function

=>When using them together, *args should come before **kwargs









'''