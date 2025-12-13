"""
2025/12/13
🔑 The Most Important return Facts
1) return ends the function immediately.
2) print() shows output, it does not return a value.
3) print() always returns None.
4) Never use return print().
5) A function with no return returns None.
6) Python only shows a return value if you print it.
7) return inside a loop only when stopping early is the goal.
✔ Situations
You are searching for something
You only need the first match
The answer is decided before the loop finishes
The problem says “stop when…”
8) Do not use return in a loop if the loop must finish.
"""

"""
⭐ Problem 1 — Say Hi
Write a function say_hi(name).
The function returns the string:
"Hi <name>"
"""
def say_hi(name):
    return f"Hi {name}"

name = input()
print(say_hi(name))

"""
⭐ Problem 2 — Greet by Name and Gender (Correct f-string Use)
Description
Write a program that greets a person using their name and gender.
If the gender is "M", return "Hello Mr. <name>, welcome!"
If the gender is "F", return "Hello Mrs. <name>, welcome!"
Otherwise, return "Invalid input"
Input
First line: a name
Second line: a gender ("M" or "F")
Output
Examples:
Hello Mr.Wong, welcome!
Hello Mrs. Cang, welcome!
Invalid input
"""
def J(n,g):
    if g=="M":
        return f"Hello Mr.{n},welcome!"
    elif g=="F":
         return f"Hello Mrs.{n},welcome!"
    else:
          return f"Invalid input"

name=input()
gender=input()
print(J(name,gender))

"""
⭐ Problem 3 — Square a Number (Easy)
Write a function square(n).
The function returns n × n.
"""
def square(n):
    return n * n

n = int(input())
print(square(n))

"""
⭐ Problem 4 — Add Three Numbers
Description
Write a program that adds three numbers.
Input
Three integers a , b and c, each on a separate line.
Output
Print the sum of the three numbers.
"""
def py(a,b,c):
    return a+b+c

a=int(input())
b=int(input())
c=int(input())
print(py(a,b,c))

"""
⭐ Problem 5 — Sum from 1 to n
Write a function sum_to_n(n).
The function returns the sum:
1 + 2 + 3 + ... + n
"""
def sum_to_n(n):
    num=0
    for i in range (1,n+1):
        num=num+i
    return num

n=int(input())
print(sum_to_n(n))

