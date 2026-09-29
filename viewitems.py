def view_items(items):

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