import random
ans='Y'
u=c=0
l=["Stone","Paper","Scissor"]
while (ans!='N' and ans!='n'):
    a=random.randint(1,3)
    print("Enter 1 for stone.")
    print("Enter 2 for paper.")
    print("Enter 3 for scissor.\n")
    b=int(input("Enter your choice: "))
    if b!=1 and b!=2 and b!=3:
        print("\nEnter valid choice.\n")
        continue;
    
    print("\nYou := ",l[b-1])
    print("Computer := ",l[a-1])
    if a==b:
        print("\nMatch tie.\n")
    elif a==1 and b==2 or a==2 and b==3 or a==3 and b==1:
        print("\nYou wins.\n")
        u+=1
    else:
        print("\nComputer wins.\n")
        c+=1
    ans=input("Want to play again? (Y/N): ")
    print('=================================\n')

print("Your score: ",u)
print("Computer score: ",c)
