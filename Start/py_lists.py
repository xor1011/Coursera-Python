list1=[1,2,3,4,5]
list2=['A', 'B', 'C']
list3=['Hello',1,True,40.22]

list4=[1,[2,3,4],5,6] #nested list
print(*list1)#prints the entire list

#add items to a list
list2.insert(len(list2), 'D')
print(list2, sep="-") 
list1.append(6)
print (*list1)
list1.extend(list2)
print(list1)

# remove items from a list
list1.pop(0) #removes the item as index 0
print (list1)
del list1[3] # removes the item at index 3
print (list1)

for n in list4:
    print (n)
print ('enumerate\n')
for i in enumerate(list2):
    print(i)

my_string="abcdefg"
x=iter(my_string)
for y in my_string:
    print(next(x))

print('\n\n\n')
new_list=[1,1,1,1,1]
x=25
for i in range(len(new_list)):
    x-=new_list[i]
print(x)