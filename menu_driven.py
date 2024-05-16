
def resturant():
    print("Enter 1 for Pepsi")
    print("Enter 2 for Coca-Cola")
    print("Enter 3 for Mirinda")
    print("Enter 4 for Slice")
    print("Enter 5 to Exit")
    while(True):
        choice=input(" Enter the values: ")

        if(choice=='1'):
            print("Please Take your Pepsi")
            for i in range(2):
                print("-"*80)
        elif(choice=='2'):
            print("Please Take your  Coca-Cola")
            for i in range(2):
                print("-"*80)
        elif(choice=='3'):
            print("Please Take your  Mirinda")
            for i in range(2):
                print("-"*80)
        elif (choice =='4'):
            print("Please Take your  Slice")
            for i in range(2):
                print("-"*80)
        elif (choice =='5'):
            print()
            print("_"*25)
            print("| Thanks for Visiting!! |")
            print("-" * 25)
            break
        else:
            print("Please Enter valid choice!!!!!")
            for i in range(2):
                print("-"*80)