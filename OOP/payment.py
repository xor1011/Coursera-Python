from http.client import PAYMENT_REQUIRED
from unicodedata import name


class Payslips():
    def __init__(self, name, payment, amount) -> None:
        self.name=name
        self.payment=payment
        self.amount=amount

    def pay(self):
        self.payment="yes"
        
    def status(self):
        if self.payment=="yes":
            return self.name+" is paid "+str(self.amount)
        else:
            return self.name+" is not yet paid"

nate=Payslips("Nathan", "no", 1000)
roger=Payslips("Roger", "no", 3000)

print(nate.status(), "\n", roger.status())
roger.pay()
print(nate.status(), "\n", roger.status())
