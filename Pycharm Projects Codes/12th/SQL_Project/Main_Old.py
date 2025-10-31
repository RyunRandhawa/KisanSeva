import Book

c = 'y'
while c.lower() == 'y':
    print("\n")
    print(" Book Shop Management ".center(89, '='))
    print('1. Register')
    print('2. Login')
    print('3. Exit')
    choice4 = int(input("\nEnter the serial number of your choice : "))
    if choice4 == 1:
        Book.clrscreen()
        Book.add_user()
    elif choice4 == 2:
        Book.clrscreen()
        if Book.login():
            Book.clrscreen
            C = 'y'
            while C.lower() == 'y':
                Book.clrscreen()
                print("\n")
                print(" Book Shop Management ".center(89, '='))
                print("1. Book Stock")
                print("2. Book Selling")
                print("3. Exit")
                choice = int(input("\nEnter the serial number of your choice : "))
                if choice == 1:
                    Book.clrscreen()
                    print("\n")
                    print(" Book Stock ".center(89, '='))
                    print("1. Add a new Stock")
                    print("2. View all Stock")
                    print("3. Update an existing Stock")
                    print("4. Delete a Stock")
                    print("5. Exit")
                    choice2 = int(input("\nEnter the choice : "))
                    if choice2 == 1:
                        Book.clrscreen()
                        Book.add_stock()
                    elif choice2 == 2:
                        Book.clrscreen()
                        Book.view_stock()
                    elif choice2 == 3:
                        Book.clrscreen()
                        Book.update_stock()
                    elif choice2 == 4:
                        Book.delete_stock()
                    elif choice2 == 5:
                        print("\nGood Bye!")
                        break
                    else:
                        print("\nINVALID CHOICE!")
                elif choice == 2:
                    Book.clrscreen()
                    print("\n")
                    print(' Book Selling '.center(89, '='))
                    print('1. Sell a book')
                    print('2. View Sales this month')
                    print("3. Exit")
                    choice3 = int(input("\nEnter your choice : "))
                    if choice3 == 1:
                        Book.clrscreen()
                        Book.sell_book()
                    elif choice3 == 2:
                        Book.clrscreen()
                        Book.view_sales()
                    elif choice3 == 3:
                        print("\nGood Bye!")
                        break
                    else:
                        print("\nINVALID CHOICE!")
                elif choice == 3:
                    print("\nGood Bye!")
                    break
                else:
                    print("\nINVALID CHOICE!")
                C = input("\nDo you want to continue (y/n) : ")
            else:
                print("\nGood Bye!")
        else:
            print("\nEither your Username or Password is incorrect!")
    elif choice4 == 3:
        print("\nGood Bye!")
        break
    else:
        print("\nINVALID CHOICE!")
    c = input("\nDo you want to return to Main Menu (y/n) : ")
else:
    print("\nGood Bye!")