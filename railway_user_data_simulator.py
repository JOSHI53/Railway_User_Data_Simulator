import datetime
x=datetime.datetime.now()        
         
print("\nWELCOME TO TRAIN TICKET BOOKING SYSYTEM\n")
print('\nYOU CAN BOOK YOUR TRAIN TICKETS TO JAMMU BY CHOOSING THE BOOK TICKETS OPTION.\n')

stations = ['DELHI','GWALIOR','CHENNAI','BENGALORE','BOMBAY']
destination=['JAMMU']

lst=list()
for i in range(1,72):
    lst.append(i)

fname=list()
for j in range(1,72):
    fname.append(j)

lname=list()
for k in range(1,72):
    lname.append(k)

agep=list()
for i in range(1,72):
    agep.append(i)
r=1
while r!=0:
    print("1.BOOK TICKET")
    def BOOK_TICKETS():
        print('CHOOSE THE STATION YOU WANT TO BOARD FROM \n OPTIONS ARE: \n DELHI\n GWALIOR \n CHENNAI \n BENGALORE \n BOMBAY')
        boardingStation=input('ENTER THE STATION: ')
        tic=int(input("Enter Seat Number: "))
        
        if boardingStation=='DELHI':
                        
            print("*YOUR TICKET FROM DELHI TO JAMMU IS GETTING PROCESSED PLEASE ENTER THE FOLLOWING DETAILS*")
            if lst[tic-1]==tic: 
                fname1=str(input("Enter Your First Name: \n"))
                lname1=str(input("Enter Your Last Name: \n"))
                age1=int(input("Enter Your age: \n"))
                lst.pop(tic-1)
                fname.pop(tic-1)
                agep.pop(tic-1)
                lst.insert(tic-1,'B')
                fname.insert(tic-1,fname1)
                lname.insert(tic-1,lname1)
                agep.insert(tic-1,age1)
                print("\n **")
                print("your ticket is booked")
                print("**\n")

            else:
                print("\n **")
                print("Seat is already booked try other seat")
                print("**\n")
            print("***********************************************")
            print("TIME OF BOOKING: ",x)
            print("NAME OF PASSENGER: ",fname1,lname1)
            print("AGE: ",age1)
            print("BOARDING STATION: ",boardingStation)
            print("DESTINATION: JAMMU")
            print("***********************************************")
        elif boardingStation=='GWALIOR':
            print("*YOUR TICKET FROM GWALIOR TO JAMMU IS GETTING PROCESSED PLEASE ENTER THE FOLLOWING DETAILS*")
            if lst[tic-1]==tic: 
                fname1=str(input("Enter Your First Name: \n"))
                lname1=str(input("Enter Your Last Name: \n"))
                age1=int(input("Enter Your age: \n"))
                lst.pop(tic-1)
                fname.pop(tic-1)
                agep.pop(tic-1)
                lst.insert(tic-1,'B')
                fname.insert(tic-1,fname1)
                lname.insert(tic-1,lname1)
                agep.insert(tic-1,age1)
                print("\n **")
                print("your ticket is booked")
                print("**\n")

            else:
                print("\n **")
                print("Seat is already booked try other seat")
                print("**\n")
            print("***********************************************")
            print("TIME OF BOOKING: ",x)
            print("NAME OF PASSENGER: ",fname1,lname1)
            print("AGE: ",age1)
            print("BOARDING STATION: ",boardingStation)
            print("DESTINATION: JAMMU")
            print("***********************************************")
        elif boardingStation=='BENGALORE':
            print("*YOUR TICKET FROM BANGALORE TO JAMMU IS GETTING PROCESSED PLEASE ENTER THE FOLLOWING DETAILS*")
            if lst[tic-1]==tic: 
                fname1=str(input("Enter Your First Name: \n"))
                lname1=str(input("Enter Your Last Name: \n"))
                age1=int(input("Enter Your age: \n"))
                lst.pop(tic-1)
                fname.pop(tic-1)
                agep.pop(tic-1)
                lst.insert(tic-1,'B')
                fname.insert(tic-1,fname1)
                lname.insert(tic-1,lname1)
                agep.insert(tic-1,age1)
                print("\n **")
                print("your ticket is booked")
                print("**\n")

            else:
                print("\n **")
                print("Seat is already booked try other seat")
                print("**\n")
            print("***********************************************")
            print("TIME OF BOOKING: ",x)
            print("NAME OF PASSENGER: ",fname1,lname1)
            print("AGE: ",age1)
            print("BOARDING STATION: ",boardingStation)
            print("DESTINATION: JAMMU")
            print("***********************************************")
        elif boardingStation=='CHENNAI':
            print("*YOUR TICKET FROM CHENNAI TO JAMMU IS GETTING PROCESSED PLEASE ENTER THE FOLLOWING DETAILS*")
            if lst[tic-1]==tic: 
                fname1=str(input("Enter Your First Name: \n"))
                lname1=str(input("Enter Your Last Name: \n"))
                age1=int(input("Enter Your age: \n"))
                lst.pop(tic-1)
                fname.pop(tic-1)
                agep.pop(tic-1)
                lst.insert(tic-1,'B')
                fname.insert(tic-1,fname1)
                lname.insert(tic-1,lname1)
                agep.insert(tic-1,age1)
                print("\n **")
                print("your ticket is booked")
                print("**\n")

            else:
                print("\n **")
                print("Seat is already booked try other seat")
                print("**\n")
            print("***********************************************")
            print("TIME OF BOOKING: ",x)
            print("NAME OF PASSENGER: ",fname1,lname1)
            print("AGE: ",age1)
            print("BOARDING STATION: ",boardingStation)
            print("DESTINATION: JAMMU")
            print("***********************************************")
        elif boardingStation=='BOMBAY':
            print("*YOUR TICKET FROM BOMBAY TO JAMMU IS GETTING PROCESSED PLEASE ENTER THE FOLLOWING DETAILS*")
            if lst[tic-1]==tic: 
                fname1=str(input("Enter Your First Name: \n"))
                lname1=str(input("Enter Your Last Name: \n"))
                age1=int(input("Enter Your age: \n"))
                lst.pop(tic-1)
                fname.pop(tic-1)
                agep.pop(tic-1)
                lst.insert(tic-1,'B')
                fname.insert(tic-1,fname1)
                lname.insert(tic-1,lname1)
                agep.insert(tic-1,age1)
                print("\n **")
                print("your ticket is booked")
                print("**\n")

            else:
                print("\n **")
                print("Seat is already booked try other seat")
                print("**\n")
            print("***********************************************")
            print("TIME OF BOOKING: ",x)
            print("NAME OF PASSENGER: ",fname1,lname1)
            print("AGE: ",age1)
            print("BOARDING STATION: ",boardingStation)
            print("DESTINATION: JAMMU")
            print("***********************************************")
        else: print('enter the valid station name')
        
        
        
    print("2.CHECK TICKET STATUS")
    def CHECK_TICKET_STATUS():
        for k in lst:
          print(k,end=" ")
    print("3.CANCEL TICKET")
    def CANCEL_TICKETS():
        tic=int(input("Enter Seat Number:"))
        if lst[tic-1]==tic:
                print("\n**")
                print("This seat is not Booked")
                print("*\n")
        else:
                lst.pop(tic-1)
                lst.insert(tic-1,tic)
                print("\n**")
                print("Your ticket is cancelled")
                print("*\n")
    print("4.CHECK DETAILS OF BOOKED TICKET")
    def CHECK_DETAILS():
        s=int(input("Enter Seat number:\n"))
        s=s-1
        if fname[s]==s+1:
            print("\n**")
            print("This seat is not Booked")
            print("*\n")
        else:
            print("\n**")
            print(f"Customer Name is: {fname[s].title()} {lname[s].title()}  and Age is: {agep[s]}")
            print("*\n")

        
    print("5.EXIT")
    choice = int(input("\n Enter Your Option:"))
    if choice==1:
        BOOK_TICKETS()
        
    elif choice==2:
        CHECK_TICKET_STATUS()
    elif choice==3:
           CANCEL_TICKETS() 
    elif choice==4:
        CHECK_DETAILS()
    elif choice==5:
        r=0
        exit()
    else:
        print("\n**")
        print("You have entered wrong key\n")
        print("*\n")
