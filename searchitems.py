def search_things(items):
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