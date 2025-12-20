"""
2025/12/12
✅ FOR — Key Points
1) for repeats code a fixed number of times.
2) Use for when the number of loops is known.
3) for stops automatically.
✅ WHILE — Key Points
1) while repeats code while a condition is true.
2) Use while when the number of loops is not known.
3) while must change something inside the loop, otherwise it will loop forever.
"""

"""
Question 1 — for loop
Idea: Count fixed times
📘 Problem: Counting Candies 🍬
Lily eats 1 candy each time.
She will eat candies 5 times.
👉 Use a for loop to print:
Candy 1
Candy 2
Candy 3
Candy 4
Candy 5
"""
for i in range(1,6):
    print(f"Candy {i}")

"""
Question 2 — while loop
📘 Problem: Walking to School 🚶
Tom walks to school.
He walks 1 meter each step
He needs to walk 10 meters to arrive
Start at distance = 0
👉 Use a while loop to add 1 meter each time
👉 Stop when distance >= 10
👉 Print:
Arrived!
✅ You do NOT know how many loops before writing the code
✅ So you must use while
"""
d=0
while d<10:
    d=d+1
    print(d)
print("Arrived")

"""
Question 3 — input + while
📘 Problem: Guess the Secret Number 🎯
The secret number is:
secret = 7
The student keeps typing numbers.
👉 Use a while loop:
If the number is not 7, print:
Try again!
If the number is 7, print:
Correct!
and stop the loop.
✅ You don’t know how many tries → use while
"""
s=int(input())
while s!=7:
    if s!=7:
        print("Try again!")
        s=int(input())

print("Correct!")

"""
Question 4 — nested for (Pattern)
📘 Problem: Classroom Seats 🪑
There are 3 rows of seats.
Each row has 4 seats.
👉 Use nested for loops to print:
Row 1 Seat 1
Row 1 Seat 2
Row 1 Seat 3
Row 1 Seat 4
Row 2 Seat 1
Row 2 Seat 2
Row 2 Seat 3
Row 2 Seat 4
Row 3 Seat 1
Row 3 Seat 2
Row 3 Seat 3
Row 3 Seat 4
✅ for + for
✅ This is the first real nested loop
"""
for R in range(1,4):
    for S in range(1,5):
        print(f"Row {R} Seat{S}")

"""
Question 5 — nested while + for 
📘 Problem: Game Levels 🎮
A game has:
3 levels
Each level has 5 stars
👉 Use:
while for the level
for for the stars
Print like this:
Level 1 Star 1
Level 1 Star 2
...
Level 3 Star 5
"""
l=1
while l<4:
    for s in range(1,6):
        print(f"Level {l} Star {s}")
    l=l+1