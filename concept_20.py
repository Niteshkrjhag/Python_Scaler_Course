#what will be the output?

my_list = [1, 2, 3, 4, 5]
i = 0
for i in my_list:
    if i == 3:
        print("found")
        break
    i += 1
else:
    print("not found")
    
'''

	1.	i = 0:
	•	Before the for loop starts, you assign the value 0 to the variable i.
	2.	for i in my_list::
	•	In the for loop, the variable i is re-assigned to each element of the list my_list 
        as the loop iterates. The value you assigned to i before the loop (i.e., i = 0) is overwritten by the 
         first element of the list (1 in this case).
	3   So, i = 0 at the beginning has no effect once the for loop starts, since i is immediately
        updated to 1, the first element of my_list.
    also i in for loop indicates index not the element.
    
    Break, Pass, and Continue statements are loop controls used in python.
    
The pass statement is used to do nothing.

Two of its uses are :
Exception Catching
If elif chains

'''


  
