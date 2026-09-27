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

def search_things():
    search_type = input ("Enter the type of item to search: ")

    found = False

    for item in items:
        if item["type"] == search_type:
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
            found = True

    if not found:
        print("No matching items found")

def finding_matches():
    print ("finding possible matches")

    for item in items:
        if item["report type"] == "lost":
            for found_item in items: 
                if found_item["report type"] == "found":
                    if item ["type"] == found_item ["type"]:
                        print ("possible matches:")

                        print ("\nLost item:")
                        print ("ID:", item["id"])
                        print ("Report type:", item["report type"])
                        print ("Type:", item["type"])
                        print ("Brand:", item["brand"])
                        print ("Colour:", item["colour"])
                        print ("Location:", item["location"])
                        print ("Date:", item["date"])
                        print ("Description:", item["description"])
                        print ("Status: ", item["status"])

                        print ("\nFound item:")
                        print ("ID:", found_item["id"])
                        print ("Report type:", found_item["report type"])
                        print ("Type:", found_item["type"])
                        print ("Brand:", found_item["brand"])
                        print ("Colour:", found_item["colour"])
                        print ("Location:", found_item["location"])
                        print ("Date:", found_item["date"])
                        print ("Description:", found_item["description"])
                        print ("Status: ", found_item["status"])
                        print ("-----------------------------------------")

def item_status():
    print ("updating item status")
    input_item = int (input ("Enter item ID: "))

    for item in items:
        if item ["id"] == input_item:
            print ("Item found")
            status_change = input ("What do you want to change status too (active/finished): ")
            item["status"] = status_change
            print ("Status changed to: ", item["status"]) 
            break

    else:
        print ("item not found")
            


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
        search_things()

    elif choice == "5":
        finding_matches() 

    elif choice == "6":
        item_status() 

    elif choice == "7":
        print ("Viewing statistics\n")

    elif choice == "8":
        print ("Exiting\n")

    else:
        print ("Invalid choice. Please enter a number from 1-8\n")

