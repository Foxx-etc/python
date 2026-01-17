#contact book : edit, add, delete, show the list, search, etc.

contact = {}

while True:
    print("(e)dit (a)dd (d)elete (sh)ow (s)earch")
    user = input("Enter : ").lower()


    if user == 'a':                             #add
        while True:
            try:
                add = int(input("Enter New Contact Number : "))
                break         
            except:
                print("ENTER NUMBER!")
 
        name = input("Enter New Contact Name : ")
        contact.__setitem__(name, add)
        print("NEW CONTACT ADDED SUCCESSFULLY!\n\n")



    elif user == 'd':                                           #delete      
        name = input("Enter The Contact Name To Delete : ")      
        if name in contact:
            contact.__delitem__(name)
            print("CONTACT DELETED SUCCESSFULLY, TRY AGAIN!\n")
        else:
            print("NO SUCH CONTACT NAME REGISTERED!\n\n")



    elif user == "sh":
        if contact == {}:
            print("NOTHING TO SHOW!\n\n")
        else:
            for i in contact.keys():
                print(i)
        print("\n")


    elif user == "s":
        search = input("Enter The Name Of The Contact : ")
        print(search , contact.get(search) , "\n\n")



    elif user == 'q':                                 #quit
        break

    else:                                           
        print("INVALID INPUT, TRY AGAIN!\n\n")
