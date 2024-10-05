# Contact-Book-App-in-Python

Project Description: Contact Book App

Objective:

The Contact Book App is a simple, text-based Python application designed to manage contact information. It allows users to perform various CRUD (Create, Read, Update, Delete) operations on contacts stored in a dictionary. This project focuses on applying core Python concepts such as dictionaries, loops, conditional statements, and formatted strings to create a functional contact management system.

Key Features:
Create Contacts: Users can add new contacts by providing a name, age, email, and phone number. If the contact name already exists, the app prevents duplication.

View Contacts: Users can view details of a specific contact by entering the contact name. The app retrieves the details (name, age, phone number, and email) of the stored contact.

Update Contacts: Users can update the details of an existing contact by modifying the contact's age, email, or phone number.

Delete Contacts: Users can delete a contact by entering the contact name. If the contact exists, it will be permanently removed from the contact book.

Search Contacts: Users can search for contacts by name. The app provides partial matching and case-insensitive search results to make it easier to find contacts.

Count Contacts: The app provides the total number of contacts stored in the contact book.

Exit: Users can exit the application, which safely terminates the program.

Knowledge Required:
Dictionaries: To store and manage the contact information.
Loops: To continuously display the menu and allow users to interact with the app.
Conditional Statements: To make decisions based on user input, such as whether a contact exists or which operation to perform.
Input Statements: To take input from the user for various operations (e.g., adding or updating contacts).
Formatted Strings: To display contact information in a user-friendly format.
Project Structure:
The contact information is stored in a dictionary, where the keys are the contact names and the values are sub-dictionaries containing the contact's age, email, and phone number.

How to Use the Project:
1. Launch the Program: When the program starts, it will display a menu with the following options:

Create a new contact
View an existing contact
Update a contact
Delete a contact
Search for a contact
Count the total number of contacts
Exit the program
2. Choose an Option: Enter the number corresponding to the operation you want to perform.
3. Create a Contact: If you choose option 1, you will be prompted to enter a contact name, age, email, and phone number. The app will then store this contact in the dictionary.
4. View a Contact: To view a contact, choose option 2, then enter the contact's name. If the contact exists, the app will display the contact's details.
5. Update a Contact: To update a contact, choose option 3, enter the contact's name, and update the contact’s age, email, or phone number.
6.Delete a Contact: To delete a contact, select option 4 and enter the name of the contact to remove.
7.Search for a Contact: Choose option 5 to search for a contact by name. The app supports partial matches, so you don’t need to remember the exact name.
8.Count Contacts: Option 6 will show you the total number of contacts stored in the contact book.
9.Exit: To exit the program, select option 7. The app will display a goodbye message and terminate the program.

Example Usage:

Contact Book App
1. Create contact
2. View contact
3. Update contact
4. Delete contact
5. Search contact
6. Count contacts
7. Exit

Enter your choice = 1
Enter your name = Rohit Rajput
Enter your age = 23
Enter your email = rajputrohitsingh998@gmail.com
Enter your phone number = 9065039396
Contact name Rohit Rajput has been created successfully
