dict={"monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "saturday":5, "Sunday":6}

start_day_of_month=input("Enter the start day of the month: ")
days_of_month=int(input("Enter the days of month: "))
check=int(start_day_of_month)

if (check<7 and (days_of_month<32 and days_of_month>27)):
    print(f"|Mon Tue Wed Thu Fri Sat Sun|")
    print(" ",end="")
    for i in range(int(start_day_of_month)):
        print("    ",end="")
    itr=7-int(start_day_of_month)
    for i in range(days_of_month):
        if i<9:
            print(" ",end="")
            print(i+1,end="  ")
        else:
            print(i + 1, end="  ")
        itr=itr-1
        if itr==0:
            itr=7
            print()
            print(" ", end="")
else:
    print("-"*80)
    print("Please eneter Valid Input!!!!")


