from encodings import search_function


print(" Enter Student name ")
s=input()
print(" Classes Attended")
c=int(input())
t=200
avg=(c/t)*100
if(avg>75):
    print(" Eligible ")
else:
    print("Not Eligible")


