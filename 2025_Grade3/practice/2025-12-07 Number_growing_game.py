"""
2025-12-07
Problem 1
A machine starts with a number x = 1.
It repeats this rule 5 times:
Each time, it adds 2 to the number.
What is the final value of x after 5 steps?
"""
# first time x = 1 + 2 = 3
# second time x = 3 + 2 =5
# third time x = 5 + 2 =  7
# fourth time x = 7 + 2 = 9
# fifth time x = 9  +  2 = 11

# Method 1
f=1
s=2
g=f+s
b=g+s
y=b+s
w=y+s
q=w+s
print(g)
print(b)
print(y)
print(w)
print(q)

# Method 2
p=1
for i in range(5):
    p=p+2
print(p)

"""
Problem 2
A machine starts with:
x = 5
The machine runs 5 times.
Each time:
	•	Add 1 more than last time starting from 5
The add numbers are:
+,5 +6, +7, +8, +9
What is the final value of x?
"""
# 1st: 5 + 5 = 10
# 2nd:10 + 6 = 16
# 3rd: 16 + 7 = 23
# 4th: 23 + 8  = 31
# 5th: 31 + 9  = 40
x = 5
l=5
for i in range(5):
    x=x+l # 10,16,23,31,40
    l=l+1  # 6, 7, 8, 9, 10
print(x)
print(l)

"""
 Problem 3 : 
A number sequence starts like this:
2, 4, 7, 11, 16, ?
Each new number is made by adding:
+2, then +3, then +4, then +5, then +6 …
Question:
What is the next number?
"""
j=2
q=2
for i in range(5):
    j=j+q
    q=q+1
print(j)
print(q)

