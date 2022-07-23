my_list=["One", "Two", "Three"]
rev_list=[]
for x in range(len(my_list)-1, -1, -1):
    rev_list.append(my_list[x])
print (rev_list)