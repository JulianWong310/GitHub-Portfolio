"""
2025-12-31
summary
1️⃣ increasing growing (add) VS constant growing
Common forms
add = add + 1      growing increase
add = add + v      growing increase with variable

x = x + add        growing increase final value x
S = S + add        growing increase sum
add = add + 1      growing increase
add = add + v      growing increase with variable 

x = x + add        growing increase final value x
S = S + x          growing sum

x= x + 1           constant increasing final value x
S = S + x          constant increasing sum

2️⃣ sum for the special numbers
All numbers from a to b
S  = 0
for i in range (a,b+1)
   if condition：
      S = S + i   

3️⃣ count : How many times ( repeating times)
count = 0
while condition:
    ...
    count += 1
"""

"""
Problem 1 — add, x
Description
A number starts at x = 10.
The machine runs 4 times.
At the start, add = 2
Each time:
Add add to x
Increase add by 3
Print the final value of x.
"""
x=10
add=2
for i in range(4):
    x=x+add # 12, 17, 25, 36
    add=add+3 # 5, 8, 11, 14
print(x)

"""
Problem 2 — add, x
Description
A child saves money for n weeks.
In week 1, the child saves a dollars
Each week, the saved amount increases by b dollars
Print the total money saved after n weeks.
Input
a
b
n
"""
a=int(input()) # 2
b=int(input()) # 3
n=int(input()) # 5
add=a
x=0
for i in range(n):
    x=x+add # 2, 7, 15, 26, 40
    add=add+b # 5, 8, 11, 14, 17
print(x)

"""
Problem 3 — S, count, add
Description
Numbers start from 1 and increase by 1 each time.
Add numbers one by one: 1, 2, 3, ...
Stop when the total sum becomes greater than or equal to T
Print how many numbers were added.
Input
T
"""
T=int(input()) #10
x=0
add=1
count=0
while x<T:
    x=x+add # 1,3,6,11
    add=add+1 # 2,3,4,5
    count=count+1 #1,2,3,4
print(count)

"""
Problem 4 — S + i 
Description
Given two integers a and b (a ≤ b):
From a to b, add all numbers that are:
divisible by 4 or
divisible by 7
Print the final sum.
"""
a=int(input()) # 5
b=int(input()) # 20
S=0
for i in range(a,b+1):
    if i % 4==0 or i % 7==0: # 7,8,12,14,16,20
        S=S+i # 7,15,27,41,57,77
print(S)

"""
Problem 5 — add, count, x
Description
A walker starts at position 0.
On step 1, the walker moves a units
Each step after that, the movement increases by b units
Stop when the position becomes greater than n.
Print how many steps were taken.
Input
a
b
n
"""
a=int(input()) 
b=int(input())
n=int(input())
add=a
count=0
x= 0
while x<=n:
    x=x+add
    add=add+b
    count=count+1
print(count)

"""
Problem 6 — count, add, x
Description
A child saves money every week.
In week 1, saves a dollars
Each week, the saved amount increases by b dollars
Every 5th week, the child gets an extra bonus of c dollars
Stop when total savings reach at least T.
Print how many weeks are needed.
Input
a
b
c
T
"""
a= int(input())
b= int(input())
c= int(input())
T= int(input())
count=0
add=a
x=0
while  x < T:
    x = x + add
    add= add+ b
    count=count+1
    if count % 5==0:
        x=x+c
print(count)

"""
Problem 7 — S
A number sequence starts at 3.
Each time, the number increases by a constant amount of 3.
The sequence continues until the value reaches 12.
📌 Task
Add all the numbers in the sequence.
📋 Example Sequence
3, 6, 9, 12
❓ Question
What is the total sum of all the numbers in this sequence?
"""
S=0
x=3
for i in range(4):
    S=S+x
    x=x+3
print(S)

"""
Problem 8 — add, S
A number sequence starts at 3.
Each time, the number increases by 1 more than the previous increase.
First increase: +3
Second increase: +4
Third increase: +5
The sequence has 4 numbers in total.
📌 Task
Add all the numbers in the sequence.
📋 Example Sequence
3, 6, 10, 15
❓ Question
What is the total sum of all the numbers in this sequence?
"""
S=0
add=3
x=3
for i in range(4):
    S=S+x
    x=x+add
    add=add+1
print(S)