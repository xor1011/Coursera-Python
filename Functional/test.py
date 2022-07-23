# Using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]
"""
# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)
"""

# Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
for x, y in months_dict.items():
    print("{}:\t{}".format(x,y))

print("\n\n\n")
a = [[96], [69]]

print(''.join(list(map(str, a))))
z = ["alpha","bravo","charlie"]
new_z = [i[0]*2for i in z]
print(new_z)