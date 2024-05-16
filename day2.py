# dictionary methods

#To merge dictonaries

ep1={100:59,102:89,103:77,104:91}

ep2={111:93,109:88}

ep1.update(ep2)
print(ep1)
print("-"*80)
# else block with a loop

for i in range(6):
    print(i+1,end=" ")
else:
    print(f"\nloop executed properly!!")

print("-"*80)


#Exception Handling

try:
    n=int(input("Enter the number: "))
    print("The table of n is given below!")
    for i in range(1,11):
        print(f"{n}*{i}= {n*i}")
except Exception as e :
    print("Enter a valid input!!!")

print(format(((1/24)*100),'.2f'))

print("-"*80)

# n=int(input("Enter the value between 5 to 9: "))
# if(n<5 or n>9):
#     raise ValueError("please enter valid value which should be between 5 to 9 and it is Integer")

print("-"*80)



# single line if else function
a=500
b=300

print(a*b) if a<b else print(format(a/b,'.2f')) if a>b else print(f"{a} and {b} are equal")





