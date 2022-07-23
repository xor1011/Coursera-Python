my_list=[1,2,3]
#functional languages do not alter global variables
#Pure functions make code easier to debug and extend
def add_to_list(lst, item):
    newList=lst.copy()
    newList.append(item)
    return newList
new_list=add_to_list(my_list, 4)
print(my_list)
print(new_list)