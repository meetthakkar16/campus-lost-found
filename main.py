items = []
next_id = 1

def add_lost_item():

    global next_id

    print ("adding a lost item")

    item_type = input ("Enter item type: ")
    brand = input ("Enter the brand: ")
    colour = input ("Enter the colour: ")
    location = input ("Enter the location: ")
    date = input ("Enter the date: ")
    description = input ("Enter description: ")

    item = {
        "id": next_id,
        "report type": "lost",
        "type": item_type,
        "brand": brand,
        "colour": colour,
        "location": location,
        "date": date,
        "description": description,
        "status": "active"
    }

    items.append(item)
    next_id += 1

    print ("lost item created") 
    print (item)

def add_found_item():

    global next_id

    print ("adding a found items")

    item_type = input ("Enter item type: ")
    brand = input ("Enter the brand: ")
    colour = input ("Enter the colour: ")
    location = input ("Enter the location: ")
    date = input ("Enter the date: ")
    description = input ("Enter description: ")

    item = {
        "id": next_id,
        "report type": "found",
        "type": item_type,
        "brand": brand,
        "colour": colour,
        "location": location,
        "date": date,
        "description": description,
        "status": "active"
    }

    items.append(item)
    next_id += 1

    print ("found item created")
    print (item)

def view_items():
    print ("All reported items")

    if not items:
        print ("No items found")
        return
        
    for item in items:
        print ("\nID:", item["id"])
        print ("Report type:", item["report type"])
        print ("Type:", item["type"])
        print ("Brand:", item["brand"])
        print ("Colour:", item["colour"])
        print ("Location:", item["location"])
        print ("Date:", item["date"])
        print ("Description:", item["description"])
        print ("Status: ", item["status"])

        print ("-------------------------")

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
        add_lost_item()
        
    elif choice == "2":
        add_found_item() 

    elif choice == "3":
        view_items()    

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

