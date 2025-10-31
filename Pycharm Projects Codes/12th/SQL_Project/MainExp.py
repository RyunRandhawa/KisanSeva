import Book

def main_menu():
    while True:
        print("\n" + " Book Shop Management ".center(89, "="))
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("\n⚠️ Please enter a valid number!")
            continue

        if choice == 1:
            Book.clrscreen()
            Book.add_user()

        elif choice == 2:
            Book.clrscreen()
            if Book.login():
                Book.clrscreen()
                user_menu()
            else:
                print("\n❌ Invalid username or password!")

        elif choice == 3:
            print("\n👋 Goodbye!")
            break

        else:
            print("\n⚠️ Invalid choice!")

        if input("\nReturn to main menu (y/n): ").lower() != 'y':
            print("\n👋 Goodbye!")
            break


def user_menu():
    while True:
        Book.clrscreen()
        print("\n" + " Book Shop Management ".center(89, "="))
        print("1. Book Stock")
        print("2. Book Selling")
        print("3. Logout")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("\n⚠️ Please enter a valid number!")
            continue

        if choice == 1:
            stock_menu()

        elif choice == 2:
            sales_menu()

        elif choice == 3:
            print("\n🔒 Logged out successfully!")
            break

        else:
            print("\n⚠️ Invalid choice!")

        if input("\nReturn to user menu (y/n): ").lower() != 'y':
            break


def stock_menu():
    while True:
        Book.clrscreen()
        print("\n" + " Book Stock ".center(89, "="))
        print("1. Add New Stock")
        print("2. View All Stock")
        print("3. Update Existing Stock")
        print("4. Delete Stock")
        print("5. Back")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("\n⚠️ Please enter a valid number!")
            continue

        if choice == 1:
            Book.add_stock()
        elif choice == 2:
            Book.view_stock()
        elif choice == 3:
            Book.update_stock()
        elif choice == 4:
            Book.delete_stock()
        elif choice == 5:
            break
        else:
            print("\n⚠️ Invalid choice!")

        input("\nPress Enter to continue...")


def sales_menu():
    while True:
        Book.clrscreen()
        print("\n" + " Book Selling ".center(89, "="))
        print("1. Sell a Book")
        print("2. View Monthly Sales")
        print("3. Back")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("\n⚠️ Please enter a valid number!")
            continue

        if choice == 1:
            Book.sell_book()
        elif choice == 2:
            Book.view_sales()
        elif choice == 3:
            break
        else:
            print("\n⚠️ Invalid choice!")

        input("\nPress Enter to continue...")


# Run program
if __name__ == "__main__":
    main_menu()