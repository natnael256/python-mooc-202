# Write your solution here

num_list = [1,2,3,4,5]

while True:

    index_num = input("index: ")
    if index_num == "-1":
        break
    new_value = input("new value: ")
    index_num = int(index_num)
    new_value = int(new_value)

    num_list[index_num] = new_value
    print(num_list)
    