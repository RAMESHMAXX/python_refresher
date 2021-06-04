name = "Maxx"
greeting = "Hello, Maxx"

print(greeting)

name = "Ramesh"

print(greeting)

greeting = f"Hello, {name}"   #here usinf f keyword to format string
print(greeting)

# --

name = "Anne"

# -- Using .format() --

# We can define template strings and then replace parts of it with another value, instead of doing it directly in the string.

greeting = "Hello, {}"
with_name = greeting.format("Ramesh")
print(with_name)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("prince", "Monday") #format() method is used
print(formatted)

#positional argument follows keyword argument
print("I am {} and going to {city} to meet my frind {}".format("prince","Anand",city="simla"))

#formatting float value
x=123.5678898
print("x= {:.2f}".format(x))