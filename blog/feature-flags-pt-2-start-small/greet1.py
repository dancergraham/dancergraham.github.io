import sys

personal_flag = "personal" in sys.argv
if personal_flag:
    greeted = input("What's your name? ")
else:
    greeted = "World"
print(f"Hello, {greeted}!")