"""
2025/12/10
Key Points for if, elif, and else
1. if can be used alone
2. elif must follow if
3. else is optional
4.elif cannot exist without if
5. elif stops checking after a match
6. if + if keeps checking everything
7. If many rules can happen → use if + if
8.  If only one rule can happen → use if + elif + else
"""

"""
Question 1 — SUPER EASY (Only if + else)
Check if a number is positive or not.
Tom types a number.
If the number is greater than 0, print "Positive".
Otherwise, print "Not Positive".
"""
a=int(input("Enter a number: "))
if a>0:
    print("Positive")
else:
    print("Not Positive")

"""
Question 2 — EASY (if + else)
Even or Odd.
Lucy types a number.
If the number is even, print "Even".
Otherwise, print "Odd".
"""
x=int(input("Enter a number: "))
if x%2==0:
    print("Even")
else:
    print("Odd")

"""
Question 3 — MEDIUM (if + elif + else)
Temperature feeling.
The temperature is a number.
If the temperature is greater than 30, print "Hot"
If the temperature is between 15 and 30 (inclusive), print "Warm"
Otherwise, print "Cold"
"""
k=int(input("Enter a number: "))
if k>30:
    print("Hot")
elif 15<k<=30:
    print("Warm")
else:
    print("Cold")

"""
Question 4 — MEDIUM+ (Score Grade)
School grade system.
A student gets a score from 0 to 100.
If score ≥ 90 → print "A"
If score ≥ 80 → print "B"
If score ≥ 70 → print "C"
Otherwise → print "D"
This one cannot use if + if — must use elif.
"""
p=int(input("Enter your score: "))
if p>=90:
    print("A")
elif p>=80:
    print("B")
elif p>=70:
    print("C")
else:
    print("D")

"""
Question 5 — HARD (Real Life Logic + else)
Weather decision.
You type today’s weather:
If it is "sunny" → print "Go play outside!"
If it is "rainy" → print "Take an umbrella!"
If it is "snowy" → print "Wear warm clothes!"
Otherwise → print "Stay at home!"
"""
o=input("Enter today's weather: ").strip()
if o=="sunny":
    print("Go play outside!")
elif o=="rainy":
    print("Take an umbrella!")
elif o=="snowy":
    print("Wear warm clothes!")
else:
    print("Stay at home!")

