from cal import salary


import cal

fname=input("Enter First Name: ")
lname=input("Enter last Name: ")
sa=cal.salary()

print("Total:",(sa+cal.hra(sa)+cal.da(sa)+cal.bonus(sa)))

