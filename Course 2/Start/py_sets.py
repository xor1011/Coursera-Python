set_a={1,2,3,4,5,6, 6, 6} #the extra 6's won't show up
print (set_a)
set_a.remove(2)
print (set_a)
set_a.add(2)
print (set_a)
set_a.discard(6) # same as remove
print (set_a)

set_b={4,5,6,7,8}
print(set_a.union(set_b)) #{1, 2, 3, 4, 5, 6, 7, 8}
print (set_a | set_b) # prints the same as the union
print ("let;s see an intersection\n")
#intersection gives matches
set_c={2,4,6,8,10,12,14}
set_d={1,2,3,4,5,6,7,8,9,10}
print(set_c.intersection(set_d)) #not permanent
print (set_c)
set_c.intersection_update(set_a) #permanent
print(set_c) 
print (set_c & set_b) # same as intersection

#lets see some differences
set_y={1,2,4,5,6,7}
set_z={0,1,2,3,4,5,6,7,8}
print(set_y.symmetric_difference(set_z)) #0,3,8
print (set_y^set_z)# same as above
#cannot index sets


