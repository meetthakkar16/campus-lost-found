def item_status(items):
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
            
def status_view(items):
    active_count = 0
    finished_count = 0

    for item in items:
        if item ["status"] == "active":
            active_count += 1
    print ("active: ", active_count)

    for item in items:
        if item ["status"] == "finished":
            finished_count += 1
    print ("finished", finished_count)  