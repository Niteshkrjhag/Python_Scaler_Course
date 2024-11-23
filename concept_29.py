# Recursion is a computational problem-solving technique where the solution is dependent on solutions to smaller instances of the same problem. It uses functions that call themselves from within its code to solve such recursive problems.

# recursion is a process in which a function calls itself. Such functions are called recursive functions.

#Python interpreter limits the number of recursive calls for a function to 1000 by giving a recursion error.

# def rec(n = 0):
#     if n==0:
#         print("Hello")
#         return
#     rec(n-1)

# rec(999)

#Syntax 

# def rec_func_name():
#    if(condition)                       # base case
#        simple statement without recursion
#    else                                # general case
#        statement calling rec_func_name()

#A recursive function makes use of a call stack.

# def AddN(n = 0):
#     if n==1:
#         return 1
#     return n+AddN(n-1)

# print(AddN(5))

#All recursive functions have two distinct phases of working - the winding and unwinding phases. The winding phase embarks with the recursive function being called the first time and moves ahead until the last recursive call. In this phase, no return statements are executed. The winding phase terminates when the base case's condition becomes true in a call.

#That's when the unwinding phase begins. In this phase, all recursive functions return in the reverse order till the first instance of the function returns.

'''
Types of Recursion in Python

There are mainly 2 types of recursive functions:

Direct Recursion
Indirect Recursion

1) Direct Recursion

In this type of recursion, the function calls itself.

a) Tail Recursion - A recursive call is said to be tail-recursive if it is the last statement to be executed inside the function.

Example of a Tail Recursive Call

def dispn(n):
    if n == 0:
        return  # Base case
    print(n)
    dispn(n - 1)  # Tail Recursive Call


dispn(5)

Example of a Call That is Not Tail-Recursive

def dispn(n):
    if n == 0:
        return  # Base case
    dispn(n - 1)  # Not a Tail Recursive Call
    print(n)


dispn(5)

Example of a Tail-Recursive Call

def GCD(a, b):
    if b == 0:
        return a  # Base case
    return GCD(b, a % b)  # Tail Recursive Call


print(GCD(49, 35))

Example of a Call that is Not Tail-Recursive

def fact(n):
    if n == 0:
        return 1  # Base case
    return (n * fact(n - 1))  # Not a tail-recursive call


print(fact(5))

The following function is used to calculate the factorial of a given number. Although the call seems to be tail-recursive due to the presence of the function name in the return statement, it is not because the call is a part of an expression in this case.

The general formula for factorial is-

n! = n * n-1 * n-2 ∗….. * 1

Thus at each recursive call, the current n would be multiplied by the factorial of the previous number.

If, in a recursive function, all the calls in it are tail-recursive, then it is called tail recursion. In tail-recursive functions, the last task done by the function is a recursive call, so there is no operation pending after the recursive call occurs.

def tailr(n):
    if n > 0:
        print(n, end=" ")
        tailr(n - 1)


p = 5
tailr(p)

b) Head Recursion

If in a recursive function, the last statement is not a recursive call, i.e., during the unwinding phase, there are still some steps to occur, then it is called head recursion.

'''

'''
2. Indirect Recursion

In this type of recursion, the function calls another function which calls the original function.

def A(n):
    if n > 0:
        print("", n, end='')
        B(n + 1)

def B(n):
    if n > 1:
        print("", n, end='')
        A(n - 5)

A(20)

'''

# def isDivisibleBy7(num):
#     if num < 0:
#         print(-num)
#         return isDivisibleBy7(-num)
#     if num == 0 or num == 7:
#         return True
#     if num < 10:
#         return False
#     return isDivisibleBy7(num // 10 - 2 * (num - num // 10 * 10))

# print(isDivisibleBy7(63))
# print(isDivisibleBy7(70))

# def fibo(n=0):
#     if(n==0):
#         return 0
#     if(n==2 or n==1):
#         return 1
#     return (fibo(n-1) + fibo(n-2))

# print(fibo(6))

#Integer Reversal

res = 0
start = 1


def reverseDigits(num):
    global res
    global start
    if num > 0:
        reverseDigits(int(num / 10))
        res += (num % 10) * start
        start *= 10
    return res


print(reverseDigits(524))

'''
#Checking ascending and descending in python

def isAscending(arr):
   n = len(arr)
   if n == 1 or n == 0:
       return True
   return arr[0] <= arr[1] and isAscending(arr[1:])
 
arr=[1,4,2,3,5]
print(isAscending(arr))
 
arr=[1,2,3,4,5]
print(isAscending(arr))

'''




    
    




