#Strings

'''
The strings cannot be partially replaced, so it is always replaced completely with a new string.
'''

s= "Scaler Topics"
print(s[7:])

#slice()
'''
slice has two overload methods, each taking two different sets of parameters:

slice(stop) // takes start as 0 & step as 1

slice (start, stop, step)
'''

s = "Welcome to scaler docs"
s1 = slice(6) # takes start as 0 automatically
print("s1-obj:", s1)
print("s1-res:", s[s1])
s2 = slice(2,8) # using slice(start, end, step) without step
print("s2-obj:", s2)
print("s2-res:", s[s2])
s3 = slice(1, 20, 2) # using slice(start, end, step) with step
print("s3-obj:", s3)
print("s3-res:", s[s3])

'''
‘Step’ can never be zero.

String[ : : ] => start = 0, stop = length of string, step = 1.
String[2 : : ] => start = 2, stop = length of string, step = 1
String[ :2: ] => start = 0, stop = 2, step = 1
String[:6] OR String[1:6] => are valid syntaxes as ‘step’ is an optional parameter for this operation.

‘Start’ and ‘stop’ indices and the step can have a negative value, respectively. 
'''

#Reversing a substring using a negative ‘step’ in a slice
'''
 When reversing: ‘step’ < 0, ‘start’ > ‘stop’ in slice(start, stop, step). Whereas when not reversing: 
 when ‘step’ > 0, startIndex < stopIndex in slice(start, stop, step)
'''

s = "welcome to scaler"
# reversing complete string
s1 = s[::-1]
print("s1:", s1)
# reversing complete string by stepping to every 2nd element
s2 = s[::-2]
print("s2:", s2)
# reversing from 10th index until start, 'stop' index here automatically will be till starting of the string
s3 = s[10::-1]
print("s3:", s3)
# reversing from end until 10th index, 'start' index will automatically be the first element
s4 = s[:10:-1]
print("s4:", s4)
# reversing from 16th index till 10th index
s5 = s[16:10:-1]
print("s5:", s5)
# this will return empty, as we're not reversing here. But NOTE that this 'start' cannot be greater than ‘stop’ until & unless we're reversing
s6 = s[11:2]
print("s6:", s6)
# reversing from 14th index from the end until 4th index from the end.
s7 = s[-4:-14:-1]
print("s7:", s7)


#Performing slice operations on a List to fetch sub-lists


tempList =  ["Welcome", "to", "scaler", "docs.", "Have", "a", "great", "day"]
# fetching complete list
list1 = tempList[::]
print("list1:", list1)
# fetching list from 0th index to 6th index
list2 = tempList[0 : 6]
print("list2:", list2)
# jumping every third element from start to end
list3 = tempList[:: 3]
print("list3:", list3)
# jumping to every 2nd element starting from 1st index until 5th index
list4 = tempList[1:5:2]
print("list4:", list4)
# 8th index from end to 5th index from end
list5 = tempList[-8:-5]
print("list5:", list5)
# jumping every 3rd element in reverse
list6 = tempList[::-3]
print("list6:", list6)
# alternate implementation of list4
list7 = tempList[-7:-3:2]
print("list7:", list7)




#Performing slice operations on a Tuple to fetch sub-tuples

temptuple =  ("Welcome", "to", "scaler", "docs.", "Have", "a", "great", "day")
tuple1 = temptuple[::] # fetching complete tuple
print("tuple1:", tuple1)
tuple2 = temptuple[0 : 6] # fetching tuple from 0th index to 6th index
print("tuple2:", tuple2)
tuple3 = temptuple[:: 3] # jumping every third element from start to end
print("tuple3:", tuple3)
tuple4 = temptuple[1:5:2] # jumping to every 2nd element starting from 1st index until 5th index
print("tuple4:", tuple4)
tuple5 = temptuple[-8:-5] # 8th index from end to 5th index from end
print("tuple5:", tuple5)
tuple6 = temptuple[::-3] # jumping every 3rd element in reverse
print("tuple6:", tuple6)
tuple7 = temptuple[-7:-3:2] # alternate implementation of tuple4
print("tuple7:", tuple7)
