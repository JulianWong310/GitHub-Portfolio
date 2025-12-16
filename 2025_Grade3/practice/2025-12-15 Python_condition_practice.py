"""
2025/12/15
🏆 I practiced
1) Basic nested if
2) Nested with values & strings
3) Logic + conditions
4) Multiple rule branches
Final Thought
When you write conditions:
1) > or >= → Big to Small
2) < or <= → Small to Big
3) elif → Stop at the first true condition
"""

"""
Problem 1: Warm or Cold 🌤️
You are given an integer temp.
Rules:
If temp > 30, print "Hot"
Else if temp > 20, print "Warm"
Else if temp > 10, print "Cool"
Else, print "Cold"
👉 Write a program to print the correct message.
"""
tem=int(input())
if tem>30:
    print("Hot")
elif tem>20:
    print("Warm")
elif tem>10:
    print("Cool")
else:
    print("Cold")

"""
Problem 2: Small Number Game 🔢
You are given a number x.
Rules:
If x < 0, print "Negative"
Else if x < 100, print "Medium"
Else if x < 10, print "Small"
Else, print "Large"
"""
x=int(input())
if x<0:
    print("Negative")
elif x<10:
    print ("small")
elif x < 100:
    print("Medium")
else:
    print ("Large")

"""
Problem 3: Sticker Level ⭐
You are given an integer g (number of good stickers).
Rules:
If g >= 3:
  If g == 5, print "Perfect"
  Else, print "Good Job"
Else:
  If g >= 1, print "Keep Trying"
  Else, print "No Stickers"
"""
# Method 1
g=int(input())
if g>=3:
    if g==5:
        print("Perfect")
    else:
        print("Good Job")
else:
    if g>=1:
        print("Keep Trying")
    else:
        print("No Stickers")

# Method 2
g=int(input())
if g==5:
    print("perfect")
elif g>=3:
    print("Good Job")
elif g>=1:
    print("keep trying")
else:
    print("No Sticker")