from pynput.keyboard import Key, Listener
def right(s):
    return s[len(s)-1]

print(ord('\''))
documentation=["Welcome to the wonderful world of python\n", \
    "Isn't this fun\n", \
        "Lets write lots of lines\n"]
with open('Files/newfile.txt', 'w') as file:
    file.writelines(documentation)
with open('Files/newfile.txt', 'a') as file:
    data=""
    print("Enter some text, . to quit\n")
    while(data!='.'):
        data=input()
        if (right(data)==';'):
            data=data.replace(";", "\n")           
        file.writelines(data)
f = open("Files/pet_names.txt", "r")
f_content = f.read()
f_content_list = f_content.split("\n")
print(f_content_list[0])
f.close()
