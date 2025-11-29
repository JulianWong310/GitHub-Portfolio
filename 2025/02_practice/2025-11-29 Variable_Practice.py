"""
2025/11/29
Practiced About Variables!
1) Reviewing variable-naming rules
2) Changing variables
3) Making a story with variables
4) Printing variables (using commas, +, str(), and f-strings)
Final Thought
Variables are like little boxes in our program.
We can put stuff in them, change what’s inside, and use them to do math or write stories.
"""

# Review: what are Python variable naming rules?
# Start with a letter
# Use letters,numbers or_
# No spaces
# Don't use Python words
# Case sensitive
# Better to be clear and meaningful

# 1) My Name
# Create a variable to store my name and print it.
name_willowway="Julian"
print(name_willowway)

# 2) Favorite Number
# Make a variable that stores my favorite number and print it.
FavouriteNumber=1000
print(FavouriteNumber)

# 3) Changing What’s Inside
# Create a variable called score, set it to 5, then change it to 10.
score=5
print(score)
score=10
print(score)

# 4) Math Result
# Make two variables and add them.
number1=55
number2=101
number3=number1+number2
print(number3)

# 5) Mixed Variables
# Make THREE variables: one with a number,one with a word,one with a math problem.
# Then print all of them.
num=7048407
word="Super Mario 3D World + Bowser's fury"
mathproblem=2862798*826924
# Use comma
print(num,word,mathproblem)
# Use str() to change number to string
print(str(num) + word + str(mathproblem))

# 6) Story Time
# Make variables to store: my character’s name, his age, and his favorite colour.
# Then print a short story using them!
name='Jamie Rusynyk'
age=50
favourite_colour='blue'
# Use comma
print(name, "is" , age,  "years old. His favourite colour is" , favourite_colour,".")
# Use + and str()
print(name+" is "+str (age)+ " years old. His favourite colour is "+ favourite_colour+".")
# Use f-strings
print (f"{name} is {age} years old. His favourite colour is {favourite_colour}.")
# f-strings make code cleaner, shorter, and easier to read than using commas or +.