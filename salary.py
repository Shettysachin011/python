print(" Enter Salary " )
salary=int(input())
print(" Enter tenture ")
t=int(input())
if t>=10:
    b=salary+(salary*0.15)
    print(b)
elif t>=5:
    b=salary+(salary*0.1)
    print(b)
elif t>=3:
    b=salary+(salary*0.05)
    print(b)
else:
    print(" Not Eligible ")