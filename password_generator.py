import string
import random

s=string.ascii_letters
d=string.digits
c=string.punctuation
ans='Y'
while ans=='Y' or ans=='y':
    print("Enter 1 for Easy Password.")
    print("Enter 2 for Medium Password.")
    print("Enter 3 for Hard Password.\n")
    a=int(input("Enter: "))
    p=""
    if a==1:
        print("\nEnter 1 for digit password.")
        print("Enter 2 for alphabet password.\n")
        x=int(input("Enter: "))
        if(x==2):
            for i in range(6):
                p+=random.choice(s)
        else:
            for i in range(6):
                p+=random.choice(d)
    elif a==2:
        for i in range(6):
            p+=random.choice(s)
        for i in range(4):
            p+=random.choice(d)
    elif a==3:
        for i in range(6):
            p+=random.choice(s)
        p+=random.choice(c)
        for i in range(5):
            p+=random.choice(d)
        p+=random.choice(c)
    else:
        print("\n***Enter valid choice.***\n")
        continue
    print("\nPassword:=",p)
    ans=input("\nWant to generate password again? (Y/N) : ")
    print("=================================================\n")
