# -- Difference between two sets --

friends = {"Prince", "Maxx", "Adam","difference"}
abroad = {"Adam", "Maxx"}

# local_friends = ...
# If there are 3 friends, and 2 are abroad, that means that 1 friend is local.
#.difference
local = friends.difference(abroad)
print(local)

print(abroad.difference(friends))  # This returns an empty set

# -- Union of two sets --

local = {"Roxy"}
abroad = {"priti", "Amanda"}

# friends = ...
# If we have 1 local friend and 2 abroad friends, we could calculate the total friends by using `.union`

friends = local.union(abroad)
print(friends)

# -- Intersection of two sets --

art = {"Boby", "Jeny", "Roxy", "Charlie"}
science = {"Boby", "Jeny", "Adam", "Anne"}

# Given these two sets of students, we can calculate those who do both art and science by using `.intersection`

both = art.intersection(science)
print(both)