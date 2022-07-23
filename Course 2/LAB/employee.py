employee_name = ["Mario", "Maria"]
age = "55"
title = "owner"

def details():
    print("Employee name is:  ", employee_name)
    print("Employee age is: ", age)
    print("Employee title is:  ", title)

name={key:value for (key,value) in zip('first_name', employee_name)}
print (name)