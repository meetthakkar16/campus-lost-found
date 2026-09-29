def finding_matches(items):
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