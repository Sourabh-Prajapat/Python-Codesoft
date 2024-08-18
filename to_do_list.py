l={}

while True:
    print("\n==================================================\n")
    print("1. Add task")
    print("2. View tasks")
    print("3. Update status")
    print("4. Delete task")
    print("5. Exit\n")
    a=int(input("Enter your choice: "))
    if a==5:
        break;
    if a==1:
        n=input("\nEnter name: ")
        if n in l.keys():
            print("\n****Task already in list****")
            continue
        while True:
            print("\nStatus:")
            print("1. Completed")
            print("2. Incomplete\n")
            c=int(input("Enter Status (1/2) : "))
            if c==1:
                l.setdefault(n,"Completed")
                print("\n....Task added successfully.....")
                break
            elif c==2:
                l.setdefault(n,"Incomplete")
                print("\n....Task added successfully.....")
                break
            else:
                print("\n****Invalid choice. Enter again.****")
    elif a==2:
        if len(l)==0:
            print("\n....Empty List.....")
            continue
        else:
            print("\nTasks :-\n")
            for i in l:
                print(i,":",l[i])
    elif a==3:
        if len(l)==0:
            print("\n....Empty List.....")
            continue
        n=input("\nEnter name of the task: ")
        if n not in l.keys():
            print("\n****Task not found****")
            continue
        if l[n]=="Completed":
            print("\n....Task already completed.....")
        else:
            l[n]="Completed"
            print("\n....Status updated successfully.....")
    elif a==4:
        if len(l)==0:
            print("\n....Empty List.....")
            continue
        n=input("\nEnter name of the task: ")
        if n not in l.keys():
            print("\n****Task not found****")
            continue
        l.pop(n)
        print("\n....Task deleted successfully.....")
    else:
        print("\n****Invalid choice. Enter again.****")

print("\n****You Exit Successfully.****\n")
