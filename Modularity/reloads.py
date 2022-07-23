import filechanges
import importlib

def changes():
    try:
        importlib.reload(filechanges)
        filechanges.print_changes()
    except Exception as e:
        print("something went wrong "+str(e))
        
filechanges.os.system("cls")
for i in range(5):
    changes()
    input("Hit Enter to reload..")


