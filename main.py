print ("Campus Lost and Found Matcher")
print("--------------------------------")

choice = ""
while choice != "8":
        
    print ("1. Add lost item")
    print ("2. And found item")
    print ("3. View item")
    print ("4. Search item")
    print ("5. Find possible matches")
    print ("6. Update iterm status")
    print ("7. View status")
    print ("8. Exit")

    choice = input ("Enter your choice: ")

    if choice == "1":
        print ("Adding a lost item\n")
        
    elif choice == "2":
        print ("Adding a found item\n")

    elif choice == "3":
        print ("Viewing items\n")        

    elif choice == "4":
        print ("Searching items\n")

    elif choice == "5":
        print ("Finding possible matches\n")

    elif choice == "6":
        print ("Updating item status\n")

    elif choice == "7":
        print ("Viewing statistics\n")

    elif choice == "8":
        print ("Exiting\n")

    else:
        print ("Invalid choice. Please enter a number from 1-8\n")

