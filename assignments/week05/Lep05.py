#Code
def contact_book():
    contacts = {
        "John Doe": {"phone": "123-456-7890", "email": "john@example.com", "category": "friend"},
        "Jane Smith": {"phone": "987-654-3210", "email": "jane@example.com", "category": "work"},
    }
    
    while True:
        print("\n" + "="*50)
        print("           CONTACT BOOK MANAGER")
        print("="*50)
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contacts")
        print("4. List All Contacts")
        print("5. Update Contact")
        print("6. Delete Contact")
        print("7. Exit")
        print("-"*50)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            print("\n=== Add New Contact ===")
            name = input("Enter contact name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email address: ").strip()
            category = input("Enter category (family/friend/work/other): ").strip().lower()
            contacts[name] = {
                "phone" : phone,
                "email" : email,
                "category" : category
            }
        
            print(f"Contact '{name}' added successfully!")
        
        elif choice == "2":
            print("\n=== View Contact ===")
            if not contacts:
                print("No contacts found!")
                return
        
            name = input("Enter contact name to view: ").strip()
            if name in contacts:
                info = contacts[name]
                print(f"name: {name}")
                print(f"phone: {info['phone']}")
                print(f"email: {info['email']}")
                print(f"cateegory: {info['category']}") 
            else:
                print(f"contacts: '{name}' not found.")

        elif choice == "3":
            print("\n=== Search Contacts ===")
        
            if not contacts:
                print("No contacts found!")
                return
        
            search_term = input("Enter search term (name/phone/email): ").strip().lower()
            found_contacts = []
        
            for name, info in contacts.items():
                if (search_term in name.lower() or
                    search_term in info['phone'].lower() or
                    search_term in info['email'].lower()):
                    found_contacts.append((name, info))

            if found_contacts:
                print(f"\nFound {len(found_contacts)} contact(s):")
            else:
                print("No contacts found matching your search.")

        elif choice == "4":
            print("\n=== All Contacts ===")
        
            if not contacts:
                print("No contacts found!")
                return
        
            print(f"{'Name':<20} {'Phone':<15} {'Email':<25} {'Category':<10}")
            print("-" * 70)
            pass

        elif choice == "5":
            print("\n=== Update Contact ===")
        
            if not contacts:
                print("No contacts found!")
                return
        
            name = input("Enter contact name to update: ").strip()
            pass

        elif choice == "6":
            print("\n=== Delete Contact ===")
        
            if not contacts:
                print("No contacts found!")
                return
        
            name = input("Enter contact name to delete: ").strip()
            pass
       
        elif choice == "7":
            print("Thank you for using Contact Book Manager!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-7.")


if __name__ == "__main__":
    print("Starting Contact Book Manager...")
    
    contact_book()