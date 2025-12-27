"""
Problem 1 — Conditional Growth
A machine starts with:
x = 1
The machine runs 7 times.
Each time:
If x is even, add 4
If x is odd, add 3
Question:
What is the final value of x?
"""
x=1
for i in range(7):
    if x%2==0:
        x=x+4
    else:
        x=x+3
print(x)
# check：4,9,12,17,20,24,28

"""
Problem 2 — Repeated Division
A number starts at:
y = 96
The machine runs 4 times.
Each time:
Divide the number by 2
Question:
What is the value of y after 4 steps?
"""
y=96
for i in range(4):
    y=y/2
print (y)
# check：48,24,12,6

"""
Problem 3 — Increasing Subtraction
A number starts at:
n = 30
The machine runs 6 times.
Each time:
Subtract 2 more than last time
The subtraction starts at 2
So the subtraction sequence is:
−2, −4, −6, −8, −10, −12
Question:
What is the final value of n?
"""
n=30
i=2
for j in range(6):
    n=n-i
    i=i+2
print(n)
# check: 28,24,18,10,0,-12

"""
problem 4: Lucky Number 6 🎰
Problem Description
Julian believes that the number 6 is a lucky number.
Given two integers a and b (with a ≤ b), Julian wants to:
print all numbers between a and b (inclusive) that are divisible by 6
then print the sum of all these numbers

Input
The first line contains an integer a
The second line contains an integer b

Output
Output each number between a and b that is divisible by 6, one per line
On the last line, output the sum of all numbers divisible by 6

Sample Input
1
20

Sample Output
6
12
18
36
"""
a=int(input())
b=int(input())
s=0
for i in range(a,b+1):
    if i%6==0:
        print(i)
        s=s+i
print(s)
# check: 6,18,36

"""
Problem 5: Snail Speed 🐌
Problem Description
A snail crawls at a constant speed.
You are given:
the number of hours the snail crawls
the total distance it crawls in meters
Your task is to:
determine the snail’s speed (meters per hour)
determine how many hours it would take the snail to crawl 36 meters
All values in this problem are integers.

Input
The first line contains an integer a, the number of hours
The second line contains an integer b, the distance crawled (in meters)

Output
Output two lines
Line 1: the snail’s speed (meters per hour)
Line 2: the number of hours needed to crawl 36 meters

Sample Input
3 
9

Sample Output
3
12
"""
a = int(input())      # a hours
b = int(input())      # meters the snail crawls in a hours
speed = b/a
time= 36/speed        # time*speed=distance

print(speed)
print(time)