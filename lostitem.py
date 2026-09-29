def add_lost_item(items,next_id):

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

    return next_id