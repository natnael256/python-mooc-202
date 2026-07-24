

list_items_count = int(input("How many items:"))
num_list = []
count  = 1
while list_items_count > 0:
    list_item = int(input(f"Item {count} :"))
    num_list.append(list_item)
    count += 1
    list_items_count -= 1

print(num_list)

    