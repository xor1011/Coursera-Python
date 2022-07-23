"""f=open('Files/test.txt', mode='r')
data=f.readline()
print(data)
f.close() """
loc=input("Enter the file location folder/file.txt: ")
try:
    with open(loc, mode='r') as file:
        data=file.readline()
        print(data)
        #automatically closes with block
except FileNotFoundError as e:
    print("Please double check the file location {}".format(e))
except Exception as e:
    print("Something went wrong: ".format(e))
