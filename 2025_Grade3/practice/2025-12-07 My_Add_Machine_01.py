"""
2025-12-07
Problem
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


