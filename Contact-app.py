#Contact Book App

#Empty dictionary to store contacts

contacts = {}

while True:
    # Main Menu
    print('\nContact Book App')
    print('1. Create contact')
    print('2. View contact')
    print('3. Update contact')
    print('4. Delete contact')
    print('5. Search contact')
    print('6. Count contacts')
    print('7. Exit')

    # User choice
    choice = input("Enter your choice = ")

    if choice == '1':
        # Create new contact
        name = input("Enter your name = ")
        if name in contacts:
            print(f"Contact name {name} already exists")
        else:
            age = input("Enter your age = ")
            email = input("Enter your email = ")
            phone = input("Enter your phone number = ")
            contacts[name] = {'age': age, 'email': email, 'phone': phone}
            print(f"Contact name {name} has been created successfully")

    elif choice == '2':
        # View contact details
        name = input("Enter contact name to view = ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}, Age: {contact['age']}, Mobile: {contact['phone']}, Email: {contact['email']}")
        else:
            print("Contact not found!")

    elif choice == '3':
        # Update contact details
        name = input("Enter name to update contact = ")
        if name in contacts:
            age = input("Enter your new age = ")
            email = input("Enter your new email = ")
            phone = input("Enter your new phone number = ")
            contacts[name] = {'age': age, 'email': email, 'phone': phone}
            print(f"Contact {name} has been updated successfully!")
        else:
            print("Contact not found!")

    elif choice == '4':
        # Delete contact
        name = input("Enter contact name to delete = ")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} has been deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == '5':
        # Search contact by name
        search_name = input("Enter contact name to search = ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found - Name: {name}, Age: {contact["age"]}, Mobile: {contact["phone"]}, Email: {contact["email"]}')
                found = True
        if not found:
            print("No contact found with that name!")

    elif choice == '6':
        # Count total contacts
        print(f"Total contacts in your book: {len(contacts)}")

    elif choice == '7':
        # Exit the program
        print("Goodbye.... Closing the program")
        break

    else:
        # Invalid input
        print("Invalid input! Please try again.")
