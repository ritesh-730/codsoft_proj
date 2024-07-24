contact_book = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")
    contact_book[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact {name} added successfully!")

def view_contact_list():
    if not contact_book:
        print("Contact book is empty!")
    else:
        print("Contact List:")
        for name, details in contact_book.items():
            print(f"{name}: {details['phone']}")

def search_contact():
    query = input("Enter contact name or phone number to search: ")
    for name, details in contact_book.items():
        if query in [name, details["phone"]]:
            print(f"Contact found: {name} - {details['phone']} - {details['email']} - {details['address']}")
            return
    print("Contact not found!") 

def update_contact():
    name = input("Enter contact name to update: ")
    if name in contact_book:
        ch = input("What to update (phone/email/address): ").lower()
        if ch == "phone":
            phone = input("Enter new phone number: ")
            contact_book[name]["phone"] = phone
        elif ch == "email":
            email = input("Enter new email: ")
            contact_book[name]["email"] = email
        elif ch == "address":
            address = input("Enter new address: ")
            contact_book[name]["address"] = address
        else:
            print("Nothing to update.")
        print(f"Contact {name} updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found!")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact_list()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()
