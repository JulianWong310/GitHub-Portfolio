"""
2025/12/11
🌟FOR LOOP
 Repeat a fixed number of times
🌟 WHILE LOOP
Keep looping until a condition is true
"""

"""
Question 1 — Jumping Jacks 🏃
Do 3 jumping jacks.
Print:
Jump 1
Jump 2
Jump 3
"""
# Method 1
for i in range(3):
    print(f"Jump {i+1}")

# Method 2
for i in range(1,4):
    print(f"Jump {i}")

"""
Question 2 — Watering Flowers 🌸
There are 4 flowers.
Print:
Water flower 1
Water flower 2
Water flower 3
Water flower 4
"""
for i in range(1,5):
    print(f"Watering flower {i}")

"""
Question 3 — Counting Stickers 💖
You have 5 stickers.
Print:
Sticker 1
Sticker 2
Sticker 3
Sticker 4
Sticker 5
"""
for i in range(1,6):
    print(f"Sticker {i}")

"""
Question 4 — Hello 3 Times 👋
Print "Hello!" three times.
"""
for i in range(3):
    print("Hello")

"""
Question 5 — Number Line 📏
Print numbers from 1 to 10.
"""
for i in range(1,11):
    print(f"Number Line {i}")

"""
Question 6 — Filling a Cup 🥤
A cup starts at 0 ml.
It becomes full at 5 ml.
Add 1 ml each time.
When it reaches 5, print "Full!".
"""
cup=0
while cup<5:
    cup=cup+1
    print(f"cup:{cup}ml")
print("Full!")

"""
Question 7 — Counting Down ⏳
Start at 5.
Use a while loop to print:
5
4
3
2
1
Go!
"""
r=6
while r>1:
    r=r-1
    print(r)
print("Go")

"""
Question 8 — Finding Lost Socks 🧦
You look in a basket until you find a blue sock.
Keep printing "Looking..." until found = True.
When you find it, print "Found it!".
"""
found=False
while found==True:
    print("Looking...")
    found=True
print("Found it!")

"""
Question 9 — Balloon Growing 🎈
A balloon starts at size 0.
Blow air until size reaches 3.
Print "Blowing..." each time.
When size is 3, print "Big balloon!".
"""
size=0
while size<3:
    size=size+1
    print("Blowing...")
print("Big balloon!")

"""
Question 10 — Walk Until Door 🚪
Start at step 0.
Walk forward until step 5.
Print "Step" each time.
At 5, print "Reached the door!".
"""
step=0
while step<5:
    step=step+1
    print("step")
print("Reached the door!")