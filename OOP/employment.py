class Employees():
    def __init__(self, name, last) -> None:
        self.name=name
        self.last=last


class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password=password

class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for "+str(days)+" days"
adrian=Supervisors("Adrian", "A", "apple")
emily=Chefs("Emily", "E")
julio=Chefs("Julio", "J")
print(emily.leave_request(6))
print(adrian.password)
print(emily.name)