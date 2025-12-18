"""
2025-12-17
Continued practicing conditions 😊
"""
"""
Problem 1: Number Checker 🔍
You are given an integer n.
Rules:
If n is divisible by 3:
  If n is divisible by 2, print "Divisible by 6"
  Else, print "Divisible by 3 only"
Else:
  If n is divisible by 2, print "Divisible by 2 only"
  Else, print "Not divisible by 2 or 3"
"""
n=int(input())
if n % 3==0:
    if n%2 ==0:
        print("Divisible by 6")
    else:
        print("Divisible by 3 only")
else:
    if n%2==0:
        print("Divisible by 2 only")
    else:
        print("Not divisible by 2 or 3")

"""
Problem 2: Balloon Control 🎈
You are given an integer size.
Rules:
If size < 5:
  If size is even, print "Blow Slowly"
  Else, print "Blow Carefully"
Else:
  If size > 10, print "Too Big"
  Else, print "Stop Blowing"
"""
s=int(input())
if s<5:
    if s%2==0:
        print("Blow Slowly")
    else:
        print("Blow Carefully")
else:
    if s>10:
        print("Too Big")
    else:
        print("Stop Blowing")

"""
Problem 3: Homework Checker 📚
You are given:
finished (integer)
missing (integer)
Rules:
If finished >= 4:
    If missing == 0, print "Excellent"
    Else,print "Good"
Else:
    If missing >= 2, print "Warning"
    Else,print "Needs Improvement"
"""
f=int(input())
m=int(input())
if f>=4:
    if m==0:
        print("Excellent")
    else:
        print("Good")
else:
    if m>=2:
        print("Warning")
    else:
        print("Needs Improvement")

"""
Problem 4: Game Character Status 🧙
health (integer)
shield (string: "yes" or "no")
Rules:
If health <= 0, print "Game Over"
Else if health > 50 and shield == "yes", print "Strong"
Else if shield == "yes", print "Protected"
Else if health > 20, print "Weak"
Else, print "Critical"
"""
h=int(input())
s=input()
if h <= 0:
    print("Game Over")
elif h > 50 and s=="yes":
    print("Strong")
elif s=="yes":
    print("Protected")
elif h > 20:
    print("Weak")
else:
    print("Critical")

"""
Problem 5: Bus Monitor 🚌
You are given:
on_time (integer)
late (integer)
Rules:
If on_time >= 5:
  If late == 0, print "Excellent"
  Else, print "Good"
Else:
  If late >= 3, print "Warning"
  Else, print "Needs Improvement"
"""
o=int(input())
l=int(input())
if o >= 5:
    if l==0:
        print( "Excellent")
    else:
        print("Good")
else:
    if l>=3:
        print("Warning")
    else:
        print("Needs Improvement")