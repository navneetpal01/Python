# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]


name = "Bro Code"

first_name = name[0:3]  # The first index is inclusive and the stopping index is exclusive
# first_name = name[:3] Python will assume that the starting index is zero
last_name = name[4:]
# normally step is 1 by default
funky_name = name[0:8:2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = "https://google.com"
website2 = "https://wikipedia.com"
slice1 = slice(8, -4)
slice2 = slice(8, -4)


print(website1[slice1])
print(website2[slice2])
