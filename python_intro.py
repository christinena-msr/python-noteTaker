# intro to python
print("Hello World!")

# conditional with numbers
if 3 > 2:
    print("3 is greater than 2")
else: 
    print("3 is not greater than 2")

# conditional with strings
def sayHi(name):
    print("Hi " + name + "!")

# functions
def hi():
    print("hello there!")
    print("how you is tho?")

# hi()
# sayHi("Kou")

# loops
girls = ["Futaba", "Yuuri", "Shuuko"]
for name in girls:
    sayHi(name)
    print("next girl")