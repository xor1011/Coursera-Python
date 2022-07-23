with open('Files/test.txt', 'r') as f:
    print(f.read())
    print(type(f.read()))
print ("\n")
with open('Files/test.txt', 'r') as f:
    print(f.readlines())
    print(type(f.read()))
my_list=[]
with open('Files/test.txt', 'r') as f:
    for data in f:
        my_list.append(data)
print("\n")
print(my_list)
