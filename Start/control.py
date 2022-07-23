bill_total=int(input("What is the total of the bill?: "))
discount1=10
discount2=20
discount3=5
if bill_total>100 and bill_total<200:
    bill_total-=discount1
elif bill_total>=200:
    bill_total-=discount2
else:
    bill_total-=discount3

print("\nBill is {}".format(bill_total))