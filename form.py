import datetime

fname = input("Enter the First Name : ")
mname = input("Enter the Middle Name : ")
lname = input("Enter the Last Name : ")
dob = input("Enter your DOB (YYYY-MM-DD): ")
dob = datetime.datetime.strptime(dob,'%Y-%m-%d')
today = datetime.date.today()
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
dob = str(dob)
phone = input("Enter the Telephone Number : ")
email = input("Enter the Email : ")
gender = input("Enter the Gender : ")
company = input("Enter Your Company : ")
address = input("Enter Your Address : ")
retirement = 60 - age

print()

print()

print("NAME : ", fname + " " + mname + " " + lname)
print("DOB : ",dob[:10])
print("AGE : ",age)
print("GENDER : ",gender)
print("PHONE : ",phone)
print("EMAIL : ",email)
print("ADDRESS : ",address)
print("COMPANY : ",company)
print("Service Years Available (Years to Retirement): ",retirement)