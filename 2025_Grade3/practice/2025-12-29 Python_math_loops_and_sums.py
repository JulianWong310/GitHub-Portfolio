"""
2025/12/29

Problem 1  --- review
Start with:
x = 4
The machine runs 5 times.
Rules:
	•	If x is odd, add 5
	•	If x is even and less than 10, add 2
	•	If x is even and 10 or more, subtract 3
What is the final value of x?
"""
x=4
for i in range(5):
    if x%2==1:
        x=x+5
    elif x%2==0 and x<10:
        x=x+2
    elif x%2==0 and x>=10:
        x=x-3
print(x)

"""
 Problem 2 --- review
All numbers from 1 to 20 are checked.
A number is called special if:
	•	It is even
	•	And it is greater than 10
👉 Question:
How many special numbers are there?
"""
count=0
for i in range (1,21):
    if i%2==0 and i >10:
        count=count+1
print(count)

"""
Problem 3 — Counting by Steps 🚶‍♂️
Description
Tom walks forward in equal steps.
He starts at 0 and walks forward n times.
Each step moves him forward by k units.
Print Tom’s position after each step.

Input
One integer n (number of steps)
One integer k (distance per step)

Output
Print n lines
Each line shows Tom’s position after that step
"""
n=int(input())
k=int(input())
for i in range(1,n+1):
    print(i*k)

"""
Problem 4 — Even Score Sum 🎯
Description
A game gives out scores.
You are given a number n.
From 1 to n, add up only the even numbers.

Input
One integer n

Output
Print one integer, the sum of all even numbers from 1 to n
"""
n=int(input())
s=0
for i in range(1,n+1):
    if i%2==0:
        s=s+i
print(s)

"""
Problem 5 — Candy Sharing 🍬
Description
A teacher has c candies.
She gives candies to students one by one.
Each student receives 2 candies.
Stop when there are not enough candies for the next student.
Print:
how many students received candies
how many candies are left

Input
One integer c

Output
Line 1: number of students
Line 2: candies left
"""
c=int(input())
student=c//2
candy_left=c%2
print(student)
print(candy_left)

"""
Problem 6 — Multiplication Path ✖️
Description
A number path starts at 1.
You are given a number n.
Starting from 1, multiply the current number by n each time.
Print the value after each multiplication,
until the value becomes greater than 100.

Input
Input
One integer n (n > 1)

Output
Print each value on a new line
"""
n=int(input())
current_num=1
while current_num<=100:
        current_num=current_num*n
        print(current_num)

"""
Problem 7 — Saving for a Toy 🧸
Description
A child saves money every week.
In week 1, the child saves a dollars
Every week after that, the saved amount increases by b dollars
The child wants to buy a toy costing T dollars.
Print how many weeks it takes to save at least T dollars.

Input
One integer a (first week savings)
One integer b (increase each week)
One integer T (toy cost)

Output
One integer: number of weeks needed
"""
a=int(input())
b=int(input())
T=int(input())
S=0
count=0
add=a
while S<T:
    S=S+add
    add=add+b
    count=count+1
print(count)


