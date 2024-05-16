info={"name":"Prasad","Age":24,"eligible_for_vote":True}

for key in info.keys():
    print(key,end=f": {info[key]}\n")
for i in range (3):
    print()
for key,values in info.items():
    print(key,end=f": {values}  ")



for i in range (3):
    print()
prasad="abcdackbbdcskk"

no_of_character=dict()
for i in prasad:
    if i in no_of_character:
        no_of_character[i]+=1
    else:
        no_of_character[i]=1
my_answer=list()
for key,frequency in no_of_character.items():
    if frequency > 2:
        my_answer.append(key)

    print(key,end=f": {frequency}  ")
print()
print("-"*80)
print(my_answer)