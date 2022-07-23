num=10
while(num!=0):
    num=int(input("Give me a number between 1 and 4: "))
    match num:
        case 1 | 2:
            print("number is 1 or 2")
        case 3:
            print("number is 3")
        case 4:
            print("number is 4")
        case _:
            print("not an option")