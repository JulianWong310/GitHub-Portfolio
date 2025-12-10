"""
2025/12/09
I practiced
using the Python input function.
turning the input into a number using int()
Final Thought
input() lets the computer ask you a question and then wait for your answer.
It’s like the computer is talking to you!
"""

# 🌟 Practice 1 — Name
# Write a program that:
# Asks the user: “What is your name?”
# Prints: “Nice to meet you, ___!”
name=input("what is your name?")
print(f"Nice to meet you, {name}!")

# 🌟 Practice 2 — Color
# Asks the user: “What is your favourite color?”
# prints: "I like ____ too!"
colour=input("What is your favourite color?")
print(f"I like {colour} too! ")

# 🌟 Practice 3 — Age
# Asks the user "How old are you?"
# Prints:"Next year, you will be ____ years old!"
age=input("How old are you?")
print(f"Next year, you will be {age} years old.")

# 🌟 Practice 4 — Add two numbers
# You will need to turn the input into a number using int().
# Asks the user 2 numbers
# Prints:" The total is ____"
a =int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("The total is",a+b)

# 🌟 Practice 5 — Create a Monster
# Ask the user for the monster’s name, size, and special power.
# After they answer, create a sentence that includes all of this information.
name=input("what is the monster’s name?")
size =input("what is the monster's size?")
special_power=input("what is the monster's special power?")
print(f"The monster is {name}, the size is {size} and the special power is {special_power} ")


