"""
2025-12-16
🔑 If / Elif vs Nested If — Summary
✅ Use elif for Classification
1)You are choosing one result from many options
2) Conditions are mutually exclusive
3) Order matters: most specific first
4) Once one condition is true, the program stops checking

✅ Use Nested if for Process / Flow
One decision depends on a previous decision
You must check condition A before condition B
The program follows steps, not categories
Later checks are inside earlier checks

🏆Final Thought
Classification problem → if / elif / else
Step-by-step logic → nested if
"""

# elif review
"""
Problem 1: Game Score 🎮
You are given an integer score.
Rules:
If score ≥ 50:
  If score ≥ 80, print "Level A"
  Else, print "Level B"
Else:
  If score ≥ 30, print "Level C"
  Else, print "Level D"
"""
score=int(input())
if score >= 80:
    print("Level A")
elif score >= 50:
    print("Level B")
elif score >=30:
    print("Level C")
else:
    print("Level D")

# Nested if
"""
 Problem 2: Game Time 🎮
You are given:
homework (string: "done" or "not done")
weekend (string: "yes" or "no")
Rules:
If homework is "done":
    If weekend is "yes",print "Mario Time"
    Else,print "Play Chess for 1 Hour "
Else:
    print "No Games"
"""
hw=input()
weekend=input()
if hw=="done":
    if weekend=="yes":
        print("Mario Time")
    else:
        print("Play Chess for 1 Hour ")
else:
    print( "No Games")

# determine to use if/elif or nested if
"""
Problem 3: Robot Energy 🤖
Rules:
You are given energy.
if energy >10,print "Full Power"
Else energy <= 0, print "Stop"
Else energy <= 5, print "Low Energy"
Else energy <= 10:
    If energy is even, print "Move Fast"
    Else, print "Move Slow"
"""

# Method 1
r = int(input())
if r>10:
    print("Full Power")
elif r<=0:
    print("Stop")
elif r<=5:
    print("Low Energy")
elif r%2==0:
    print("Move Fast")
else:
    print("Move Slow")

# Method 2
r=int(input())
if  r<=0:
    print("Stop")
elif r<=5:
    print("Low Energy")
elif r<=10:
    if r%2==0:
        print("Move Fast")
    else:
        print("Move Slow")
else:
    print("Full Power")

