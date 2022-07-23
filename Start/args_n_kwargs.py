import enum


def sum_of(*args):
    return sum(args)

x=sum_of(4,5,6,7)
print (x)

def how_many(*args):
    c=0
    for x in args:
        c+=1
    return c

xx=how_many(1,1,1,1,1)
print(xx)

def item_sum(**kwargs):
   
    total=0
    for k,v in kwargs.items():
        total+=v
        
    return round(total, 2)


print(item_sum(cake=2.99, pie=3.99, donut=0.37))
