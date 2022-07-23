#str[start:stop:step]
#slice function
trial="reversal"
new_trial=trial[::-1]
print (new_trial)

def rev_string(str):
    if (len(str)==0):
        return str
    else: 
        return rev_string(str[1:])+str[0] #slices from the front
        
new_string=rev_string("My String")
print(new_string)

my_string="MY STRING"
print(my_string[2:]) #MY is removed
print(my_string[:1]) #only M is printed
print (my_string[::2]) #Every other letter is omitted
print (my_string[::3]) #prints MSI
print (my_string[::-4]) #Prints GTM
my_string.replace()