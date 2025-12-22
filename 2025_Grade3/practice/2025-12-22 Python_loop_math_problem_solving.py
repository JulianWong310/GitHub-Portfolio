"""
2025/12/22
Problem 1
A machine starts with:
x = 2
The machine repeats this rule 6 times:
	•	If x is less than 10, add 3
	•	If x is 10 or more, add 1
What is the final value of x?
"""
x=2
for i in range(6):
    if x < 10:
        x=x+3
    else:
        x=x+1
print(x)

"""
Problem 2
A counter begins with the value y = 3.
It follows this rule 4 times:
Each time, it multiplies the number by 2.
What is the final value of y after 4 steps?
"""
y=3
for i in range(4):
    y=y*2
print(y)

"""
 Problem 3
A number starts at 20.
It follows this rule:
1) The first time, subtract 1
2) The second time, subtract 2
3) The third time, subtract 3
4) The fourth time, subtract 4 and so on
What is the number after the 5th step?
"""
n=20
for i in range(1,6):
    n=n-i
print(n)

"""
Problem 4
A machine starts with:
x = 5
The machine runs 6 times.
Each time:
Add 3 more than the previous increase.
The add numbers follow this rule:
Start with +4, then each time add 3 more than last time.
So the add sequence is:
+4, +7, +10, +13, +16, +19
What is the final value of x?
"""
x=5
add=4
for i in range(6):
    x=x+add
    add=add+3
print(x)
