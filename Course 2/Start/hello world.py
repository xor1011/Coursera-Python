for i in range (1, 20, 2):
    print (str(i)+" hello world")

x=(1+3) \
    *4
print (str(x)+" is 1+3*4")

my_string="Once upon "\
    "a time in "\
        "a land "\
            "far far away.\n"
print (my_string)
print("\n"+my_string[5])
print(len(my_string))
#name=input("enter your name: ")
#print("hello "+name)
print(type(str(45)))
print(float(10))
print(type(float('12.2')))

def addup(numbers):
    x=eval(numbers)
    return x

#n=input("Type an equation:\n")
#x=addup(n)
#print(x)
str1='Martin is'
str2='years old'
age=2022-1986
print ('Hi, {} {} {}'.format(str1, age, str2))
