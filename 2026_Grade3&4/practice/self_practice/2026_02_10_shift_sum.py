"""
2026/02/10
Problem Description
Julian is studying a special kind of addition called a "Shifty Sum."
Given a starting number N, we "shift" it to the left k times.
Each time we shift the number,
 we add a zero to the end (which is the same as multiplying the number by 10).
 The Shifty Sum is the total sum of the original number plus all the shifted numbers produced.
 Example:If N = 12 and k = 3,
 the calculation is:
 Original number: 12
 Shift 1: 120
 Shift 2: 1,200
 Shift 3: 12,000
 Shifty Sum = $12 + 120 + 1,200 + 12,000 = 13,332.
 Input Specification
 The input will be two integers, each on a new line:
 The first line contains the starting number N.
 The second line contains the number of shifts k (where k >= 0).
 Output Specification
 Output the total Shifty Sum.
 Sample Case #1
 Input:
 12
3
Output:
13332
Sample Case #2
Input:
10
1
Output:
110
"""
n=int(input())
k=int(input())
s=0
for i in range(k+1):
    s = s + n
    n = n * 10


print(s)