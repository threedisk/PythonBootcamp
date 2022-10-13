# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def line():
    print("=================")
line()

print("Function without Inputs")
def greet():
    print("Hello buddies")
    print("How are you today?")
    print("See ya later")
greet()
line()

print("Function with Inputs")
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you today, {name}?")
greet_with_name("Tris")
line()

print("Function with Input: Positional Arguments")
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"You from {location}")
greet_with("Tris","Ngawi")
greet_with("Ngawi","Tris")
line()

print("Function with Input: Keyword Arguments")
def greet_with_key(name,location):
    print(f"Hello {name}")
    print(f"You from {location}")
greet_with_key(name="Tris", location="Ngawi")
greet_with_key(location="Ngawi", name="Tris")
