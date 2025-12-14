"""
2025/12/14
I practiced
1) comparison operators: >, <, ==, >=, <=, !=
2) comparing strings using ASCII order
3) fixing string–number comparisons using int() or str()

Final Thought
Booleans are like light switches: ON (True) and OFF (False).
True → means YES, it is correct!
False → means NO, it is not correct!
"""

# Python Boolean comparison can be written as:
# a > b, a < b, a == b, a >= b, a <= b, a != b
# 🎯 Practice 1 — Number Detective
# Say if each statement is True or False:
# 1) 5 > 2
print(5>2) # True
# 2) 10 < 3
print(10<3) # False
# 3) 9 == 4
print(9==4) # False
# 4) 7 != 7
print(7 != 7) # False
# 5) 1 + 1 == 2
print(1 + 1 == 2) # True
# 6) 100>= 100
print(100>= 100) # True

# 🐶 Practice 2 — Silly Animal Quiz
# Look at the sentence and answer True or False like Python:
# "cat" == "cat"
print( "cat" == "cat") # True
# "dog" == "fish"
print( "dog" == "fish") # False
# "bird" == "Bird" (hint: capital letters matter!)
print( "bird" == "Bird" ) # False
# "cow" != "pig" (≠ means “not the same”)
print("cow" != "pig" ) # True
# "fish" == "fish " (hint: notice the space!)
print("fish" == "fish ") # False

"""
String comparison is based on ASCII values:
0–9 → 48–57
A–Z → 65–90
a–z → 97–122
The computer checks the letters from left to right,
as soon as one letter is bigger, then that whole word is bigger.
"""

# ✨Practice 3 — String Comparison Practice

# 1) "abc" < "abd"
print( "abc" < "abd") # True
# 2) "milk" > "honey"
print("milk" > "honey") # True
# 3) "A" < "a"
print("A" < "a") # True

# 4) "book" == "Book"
print("book" == "Book") # False
# 5) "carrot" != "car"
print("carrot" != "car") # True

# In Python: you cannot compare "text" with a number like 5.
# 🧒Practice 4 — Fix the comparison
# a) "7" < 9
print(int("7") < 9)
# b) "12" == 12
print(int("12")==12)
# c)  5 > "2"
print(str(5)> "2")