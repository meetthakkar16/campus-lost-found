items = []
next_id = 1

from lostitem import add_lost_item 

from founditem import add_found_item

from viewitems import view_items

from searchitems import search_things

from matching import finding_matches

from status import item_status, status_view


print ("Campus Lost and Found Matcher")
print("--------------------------------")

choice = ""
while choice != "8":
        
    print ("1. Add lost item")
    print ("2. And found item")
    print ("3. View item")
    print ("4. Search item")
    print ("5. Find possible matches")
    print ("6. Update item status")
    print ("7. View status")
    print ("8. Exit")

    choice = input ("Enter your choice: ")

    if choice == "1":
        next_id = add_lost_item (items, next_id) 
        
    elif choice == "2":
        next_id = add_found_item (items, next_id) 

    elif choice == "3":
        view_items(items)    

    elif choice == "4":
        search_things(items)

    elif choice == "5":
        finding_matches(items) 

    elif choice == "6":
        item_status(items) 

    elif choice == "7":
        status_view(items)

    elif choice == "8":
        print ("Exiting\n")

    else:
        print ("Invalid choice. Please enter a number from 1-8\n")

