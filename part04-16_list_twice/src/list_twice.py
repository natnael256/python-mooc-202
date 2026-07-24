# Write your solution here

num_list = []

while True:

    list_item = int(input("New item: "))

    if list_item == 0:
        print("Bye!")
        break
    else:
        num_list.append(list_item)
        print(f"The list now: {num_list}")
        print(f"The list in order: {sorted(num_list)}")
    

    