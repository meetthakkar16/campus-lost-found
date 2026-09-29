def add_found_item(items, next_id):

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

    return next_id