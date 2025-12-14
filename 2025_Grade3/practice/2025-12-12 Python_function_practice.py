"""
2025/12/12
Summary
🧑‍🏫Standard Template
def f(...):
    # do math / logic
    return result
print(f(...))

❌ print + print = unnecessary
✅ return + print = standard
⚠️ print + call = allowed but not recommended

1) If a function has no return, it returns None.
2) return ends the function immediately.
3) parameters are variables that receive values from function calls.
"""

"""
📌 Important
You should still write a function to solve each problem
Then call the function using input
Print the required output
"""
"""
⭐ Problem 1 — Greeting
Description
Write a program that prints a greeting message.
Input
No input.
Output
Print:
Hello Mario!
"""
def qwerty():
    print("Hello Mario!")

qwerty()

"""
⭐ Problem 2 — Greet by Name
Description
Write a program that greets a person using their name.
Input
One line containing a name.
Output
Print:
Hello, <name>!
"""
def greeting (name):
    print(f"Hello,{name} ")

name=input()
greeting(name)

""""
⭐⭐ Problem 3 — Add Two Numbers
Description
Write a program that adds two numbers.
Input
Two integers a and b, each on a separate line.
Output
Print the sum of the two numbers.
"""
def Julian(a,b):
    return a+b

a = int(input())
b = int(input())
print(Julian(a,b))

"""
⭐⭐ Problem 4 — Double the Number
Description
Write a program that doubles a number.
Input
One integer n.
Output
Print the value of n × 2.
"""
def gg(n):
    return n*2

n=int(input())
B=gg (n)
print(B)

"""
⭐⭐⭐ Problem 5 — Bigger Number
Description
Write a program that compares two numbers and prints the bigger one.
Input
Two integers a and b.
Output
Print the larger number.
If they are equal, print either one.
"""
def pp(a,b):
    if a>b:
        return a
    else:
        return b

a=int(input())
b=int(input())
j=pp(a,b)
print(j)

"""
⭐⭐⭐ Problem 6 — Count Up
Description
Write a program that prints all numbers from 1 to n.
Input
One integer n.
Output
Print numbers from 1 to n, one number per line.
"""
def pj(n):
    for i in range(1,n+1):
        print(i)
n=int(input())
pj(n)