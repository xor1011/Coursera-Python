menu=["espresso", "mocha", "latte", "cappccino", "decaf", "americano", "thai", "cortado"]
def find_coffee(coffee):
    if coffee[0]=='c':
        return coffee
"""
map_coffee=map(find_coffee, menu)
print (map_coffee)
for x in map_coffee:
    print(x)
"""
filter_coffee=filter(find_coffee, menu)
for x in filter_coffee:
    print(x)
