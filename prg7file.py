# contact block prg

contactlist=[]
def addcontact():
    name=input("enter name")
    address=input("enter address")
    email=input("enter email")
    mobile=input("enter mobile no.")
    data={"name":name,"address":address,"email":email,"mobile":mobile}
    contactlist.append(data)
    print("contact added")

# display
def display():
    if(len(contactlist)==0):
        print("record not found")
    else:
        print("===contactlist===")
        for x in contactlist:
            print("name- ",x["name"])
            print("address- ",x["address"])
            print("email- ",x["email"])
            print("mobile- ",x["mobile"])
            print("================================================================")

while True:
    print("1 for add contact")
    print("2 for display contact")
    print("3 for exit")
    ch=int(input("enter choice:- "))
    if(ch==1):
        addcontact()
    elif(ch==2):
        display()
    elif(ch==3):
        break
    print("Invalid choice")
