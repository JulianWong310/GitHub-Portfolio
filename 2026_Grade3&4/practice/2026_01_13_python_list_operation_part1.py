""""
2026/01/13
Part 1
Python List — All Common Operations
Operation  Modify List? 	Use
append()	      ✅	      build
pop()	          ✅	      simulate
remove()	      ✅	      delete
count()	          ❌	      frequency
sort()	          ✅	      ranking
reverse()	      ✅	      order
len()	          ❌	      loops
in	              ❌	      check
"""

# 1 Create a List
a = [1, 2, 3, 4, 1, 5]
b = []
c = list("ABC") # ['A', 'B', 'C']
print(a,b,c)

# 2 Length of a List
num=len(a)
print(num)

# 3 Access Elements (Indexing)
a = [10, 20, 30]
print(a[0])
print(a[1])
print(a[-1])
print(a[len(a)-1]) # len(a)-1 is the index of the last element
# print(a[len(a)]) # out of range
# ⚠️ Index starts at 0, the last index is len(a)-1,not len(a)

# 4 Modify Elements by Index
a = [5, 6, 7]
a[0] = 100
print(a) # [100, 6,7]
a[2] = 0
print(a) # [100, 6, 0]

# ———— Practice ————
# 1 Create a List
# For each variable below, write YES if it is a list, NO if it is not.
a = [1, 2, 3] # YES
b = "123" # NO
c = [] # YES
d = list("ABC") # YES
e = 10 # YES

# Create a list called nums containing numbers from 1 to 5
nums=[1,2,3,4,5]
# Create an empty list called data
data=[]
# Convert the string "HELLO" into a list of characters
lst=list("HELLO")

# Part 2 — Indexing (VERY IMPORTANT)
# Given a = [10, 20, 30, 40]  Answer the following without running code:
# What is a[0]  10
# What is a[2] 30
# What is a[len(a) - 1]  40

# 2 Modifying by Index
# Given:
a = [5, 6, 7, 8]
# Change the first element to 100
a[0]=100
# Change the last element to 0
a[3]=0

# 3 Index Error Check
# Which of the following lines cause an index error?
a = [1, 2, 3]
a[3] = 10 # Wrong
print(a[-1]) # Correct
print(a[len(a)]) # Wrong