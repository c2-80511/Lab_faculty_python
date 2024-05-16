dict={"monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "saturday":5, "Sunday":6}

start_day_of_month=input("Enter the start day of the month: ")
days_of_month=int(input("Enter the days of month: "))

print(f"|Mon Tue Wed Thu Fri Sat Sun|")
print(" ",end="")
for i in range(int(start_day_of_month)):
    print("    ",end="")
itr=7-int(start_day_of_month)
for i in range(days_of_month):
    if i<10:
        print(" ",end="")
        print(i+1,end="  ")
    else:
        print(i + 1, end="  ")
    itr=itr-1
    if itr==0:
        itr=7
        print()
        print(" ", end="")


