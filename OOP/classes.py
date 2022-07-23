class MyClass:
  #  pass prevents errors
  a=5
  num_students=30
  num_desks=30
  def pay(self, rate):
    cost=rate*self.num_students
    return cost
  def hello(self):
    print("Hello classes")

myclass=MyClass() #myclass is a new instance
#method object
print(myclass.hello())
yourclass=MyClass() 
yourclass.num_students=22
print("Number of students: {}\n"\
    "Number of desks: {}".format(myclass.num_students, myclass.num_desks))
print("Number of students: {}\n"\
    "Number of desks: {}".format(yourclass.num_students, yourclass.num_desks))
#teacher paid by student
teacher_1=myclass.pay(20)
teacher_2=yourclass.pay(20)
print("Teacher 1 is paid {}\n" \
    "and teacher 2 is paid {}".format(teacher_1, teacher_2))