from random import sample


sample_dict={1:'Coffee', 2:'Tea', 3:'Juice'}
print (sample_dict[1])# reference the key
sample_dict[2]='Black Tea'
print (sample_dict[3])
print('\n')
print (sample_dict)
del sample_dict[1] #deletes Coffee
print (sample_dict)
sample_dict[4]='Water' #add water to the dictionary
print(sample_dict)
#iteration methods
print('\n\n')
my_d={1:'Test', 'Name':'Jim'}
print (my_d['Name']+'\n') #you can mix keys and values
for key, value in my_d.items(): #allows you to iterate through both keys and values in a dictionary
    print("{} : {}".format(key, value))

print (my_d['Name'][0])


