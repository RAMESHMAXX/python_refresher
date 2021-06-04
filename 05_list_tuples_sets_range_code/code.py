l = ["Ramesh", "prince", "maxx"]
t = ("Ramesh", "prince", "maxx")
s = {"Ramesh", "prince", "maxx"}

# Access individual items in lists and tuples using the index.

print(l[0])
print(t[0])
# print(s[0]) set is unordered so cannot accessed

# Modyfing

l[0] = "Smith" #list are mutabe means changable  so updated
# t[0] = "Smith"   tuple are unmutable means not changable

print(l)
print(t)

# Add to a list by using `.append`

l.append("Jen")
print(l)
# Tuples cannot be appended to because they are immutable.

# Add to sets by using `.add`

s.add("Jen")
print(s)

# Sets can't have the same element twice.

s.add("Ramesh")
print(s)

#RANGE
print(range(10))  #0 to 10 values

#summary
#list mutable so we can modify it
#tuple are unmutable so cannot updated
#set have unique element and in unorderd.