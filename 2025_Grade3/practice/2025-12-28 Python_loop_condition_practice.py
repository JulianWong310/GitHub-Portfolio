"""
2025/12-28
✅ Problem 1 — Double & Stop
A machine starts with:
x = 1
It keeps doing this rule again and again:
	•	If x is less than 50, multiply it by 2
	•	If x is 50 or more, stop the machine
👉 Question:
How many times does the machine run before it stops?
What is the final value of x?
"""
x=1
y=0
while x<50:
    x=x*2
    y=y+1
print(y) # y=6
print(x) # x=2,4,8,16,32,64

"""
✅ Problem 2 — Secret Number Lock 
A secret lock starts with:
number = 3
Every time you press the button:
	•	If the number is even, divide it by 2
	•	If the number is odd, add 5
The lock stops when the number becomes 1.
"""
n=3
while n>1:
    if n%2==0:
        n=n//2
    else:
        n=n+5
print(n)
# n=8,4,2,1

"""
Problem 3 — Count Changes
You are given an integer N.
Starting from x = 1, repeat the following N times:
If x is even → x = x / 2
If x is odd → x = x * 3 + 1
After finishing N loops, print the value of x.
Input Example:
7
Output Example:
10
"""
N= int(input())
x=1
for i in range(N):
    if x%2==0:
        x=x//2
    else:
        x=x*3+1
print(x)

"""
✅ Problem 4 — Count the Steps
Write a program that reads N, and then prints how many numbers from 1 to N are:
divisible by 3,
but not divisible by 2.
Input Example:
20
Output Example:
3
(But for different N, output will be different.)
"""
N=int(input())
count=0
for i in range(1,N+1):
    if i%3==0 and i%2!=0:
        count=count+1
print(count)

"""
✅ Problem 5 — Robot Position Tracker
You will be given a number N, followed by N lines of robot moves:
UP
DOWN
LEFT
RIGHT
The robot starts at position (0, 0).
After all commands, output the final x y.
Input Example:
5
UP
UP
LEFT
RIGHT
DOWN
Output Example:
0 1
"""
N=int(input())
x=0
y=0
for i in range(N):
    C=input()
    if C=="UP":
        y=y+1
    elif C=="DOWN":
        y=y-1
    elif C=="LEFT":
        x=x-1
    elif C=="RIGHT":
        x=x+1
print(x,y)
