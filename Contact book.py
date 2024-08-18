import mysql.connector as sqlcon

mycon=sqlcon.connect(host="localhost",user="root",password="root",database="contact_book")
cursor=mycon.cursor()

def add_contact():
    ans='Y'
    while ans=='Y' or ans=='y':
        name=input("\nEnter Name: ")
        while(name==''):
            name=input()
        phno=input("Enter Phone Number: ")
        while(phno==''):
            phno=input()
        cursor.execute("select count(*) from contact where Phone_Number='%s'"%phno)
        data=cursor.fetchone()
        if(data[0]>0):
            print("\n***Unable to add contact becuase phone number already exist.***\n")
            continue
        email=input("Enter Email: ")
        while(email==''):
            email=input()
        address=input("Enter Address: ")
        while(address==''):
            address=input()
        cursor.execute("insert into contact values('%s','%s','%s','%s')"%(name,phno,email,address))
        print("\n.....Contact added successfully......")
        print("\n-----------------------------------------------------------------------\n")
        
        ans=input("Want to add another contact? (Y/N) : ")
        print("\n-----------------------------------------------------------------------\n")
        
def update():
    cursor.execute("select * from contact")
    data=cursor.fetchall()
    if not data:
        print("\n***List is empty.***")
        return
    ph=input("\nEnter Phone Number: ")
    cursor.execute("select count(*) from contact where Phone_Number='%s'"%ph)
    data=cursor.fetchone()
    if data[0]==0:
        print("\n***Contact does not exist.***")
        return
    cursor.execute("select * from contact where Phone_Number='%s'\n"%ph)
    data=cursor.fetchone()
    print(data)
    name=input("\nEnter Name: ")
    while(name==''):
        name=input()
    phno=input("Enter Phone Number: ")
    while(phno==''):
        phno=input()
    cursor.execute("select count(*) from contact where Phone_Number='%s'"%phno)
    data=cursor.fetchone()
    if(phno!=ph and data[0]>0):
        print("\n***Unable to update contact becuase phone number already exist.***\n")
        print("\n-----------------------------------------------------------------------\n")
        return
    email=input("Enter Email: ")
    while(email==''):
        email=input()
    address=input("Enter Address: ")
    while(address==''):
        address=input()
    cursor.execute("update contact set Name='%s',Phone_Number='%s',Email='%s',Address='%s' where Phone_Number='%s'" %(name,phno,email,address,ph))
    print("\n.....Updated Successfully......")

def search():
    cursor.execute("select * from contact")
    data=cursor.fetchall()
    if not data:
        print("\n***List is empty.***")
        return
    print("\nEnter 1 for search by Name.")
    print("Enter 2 for search by Phone Number.")
    a=input("\nEnter: ")
    while a=='':
        a=input()
    a=int(a)
    if a==2:
        b=input("\nEnter Phone Number: ")
        cursor.execute("select * from contact where Phone_Number='%s'"%b)
    elif a==1:
        b=input("\nEnter Name: ")
        cursor.execute("select * from contact where Name='%s'"%b)
    else:
        print("\n*****Enter valid choice.*****")
        search()
        return
    data=cursor.fetchall()
    if not data:
        print("\n***Contact does not exist.***")
        return
    print("\n-----------------------------------------------------------------------\n")
    print("(Name , Phone Number , Email Id , Address)\n")
    for i in data:
        print(i)

def view():
    cursor.execute("select * from contact")
    data=cursor.fetchall()
    if not data:
        print("\n***List is empty.***")
        return
    print("\n-----------------------------------------------------------------------\n")
    print("[Name, Phone Number, Email Id, Address]\n")
    for i in data:
        print(i)

def delete():
    cursor.execute("select * from contact")
    data=cursor.fetchall()
    if not data:
        print("\n***List is empty.***")
        return
    a=input("\nEnter name: ")
    cursor.execute("select count(*) from contact where Name='%s'"%a)
    data=cursor.fetchone()
    if data[0]==0:
        print("\n***Contact does not exist.***")
        return
    if data[0]==1:
        cursor.execute("delete from contact where Name='%s'"%a)
    else:
        print("\nMore than one contact has same name.\n")
        b=input("Enter Phone Number: ")
        cursor.execute("select count(*) from contact where Phone_Number='%s'"%b)
        data=cursor.fetchone()
        if data[0]==0:
            print("\n***Contact does not exist.***")
            return
        cursor.execute("delete from contact where Phone_Number='%s'"%b)
    print("\n.....Contact deleted successfully......")

    
print("\n=========================================================================\n")

while True:
    print("Enter 1 for add contact.")
    print("Enter 2 for view contact list.")
    print("Enter 3 for update contact.")
    print("Enter 4 for search contact.")
    print("Enter 5 for delete contact.")
    print("Enter 6 for exit.\n")
    a=input("Enter : ")
    while a=='':
        a=input()
    a=int(a)
    if a==1:
        add_contact()
    elif a==2:
        view()
    elif a==3:
        update()
    elif a==4:
        search()
    elif a==5:
        delete()
    elif a==6:
        break
    else:
        print("\n*****Enter valid choice.*****\n")
        continue

    print("\n=========================================================================\n")

print("\n.....Exit successfully......")
mycon.commit()

mycon.close()
