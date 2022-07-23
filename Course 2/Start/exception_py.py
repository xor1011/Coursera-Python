x, y=[float(a) for a in input("Enter two numbers separated by a space ").split()]
try:
    z=x/y
    print("{}/{}={}".format(x,y,z))
except Exception as e:
    print("Sorry you cannot do that: {}".format(e))
