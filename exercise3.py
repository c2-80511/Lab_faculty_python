import random
import string

text=input("Enter the string to be encypted: ")
flag=False
if len(text)<3:
    # text[::-1] This means start walking backward (it starts from the last of string)
    text=text[::-1]
    flag=True
    print(f"The Encrypted test is : {text}")
else:
    ch=text[0]
    text=text[1:len(text)]
    text+=ch
    s1=''.join(random.choices(string.ascii_letters,k=3))
    s2 = ''.join(random.choices(string.ascii_letters, k=3))
    text=s1+text+s2

    print(f"The Encrypted test is : {text}")

decypted_text=text[len(text)-4]+text[3:len(text)-4]

if flag==True:
    print(f"The Decrypted test is : {text[::-1]}")
else:
    print(f"The Decrypted test is : {decypted_text}")

