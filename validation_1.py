fname = input("Enter your first name \n")
while (not fname.isalpha() or len(fname)<=0 ):
    print(" Not valid")
    fname = input("Enter your first name \n")

sname = input("Enter your Last name \n")
while (not sname.isalpha() or len(sname)<=0 ):
    print(" Not valid")
    sname = input("Enter your Last name \n")

pno = input("Enter your Phone Number \n")
while (not pno.isnumeric() or len(pno)!=10 ):
    print(" Not valid")
    pno = input("Enter your Phone number \n")

age = input("Enter your age \n")
while (not age.isnumeric() or len(age)>3 or len(age)<=0 or int(age)<20):
    print(" Not valid")
    age = input("Enter your age \n")

addr = input("Enter your Address \n")
while (not addr.isalpha() or len(addr)<=0 ):
    print(" Not valid")
    addr = input("Enter your Address \n")

city = input("Enter your City \n")
while (not city.isalpha() or len(city)<=0 ):
    print(" Not valid")
    city = input("Enter your city \n")

dname = input("Enter your Department name \n")
while (not dname.isalpha() or len(dname)<=0 ):
    print(" Not valid")
    dname = input("Enter your Department name \n")

sal = input("Enter your Salary \n")
while (not sal.isnumeric() or len(sal)<=0 or int(sal)<0):
    print(" Not valid")
    sal = input("Enter your salary \n")


print("\nName:", fname+ sname)
print("Phone Number:", pno)
print("Age:", age)
print("Address:", addr)
print("City:", city)
print("Department Name:", dname)
print("Sal:", sal)




   
