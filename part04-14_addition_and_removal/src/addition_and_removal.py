# Write your solution here

num_list = []
item_num = 1
while True: 

    print(f"The list is now {num_list}")
    comand = input("a(d)d, (r)emove or e(x)it: ")

    if comand == "x":
        print("Bye!")
        break
    elif comand == "d":
        num_list.append(item_num)
        item_num += 1
    elif comand == "r":
        num_list.pop(len(num_list)-1)
        item_num -= 1