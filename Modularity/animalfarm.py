def d():
    animal="elephant" #1
    def e():
        nonlocal animal 
        animal="giraffe" #2,3
        print("inside nested function "+animal) #2
    print("Before calling function: "+animal) #1
    e()
    print("After nested function: "+animal) #3

animal="camel" #4
d()
print("Global animal: "+animal) #4