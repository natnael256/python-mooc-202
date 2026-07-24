# Write your solution here

def even_numbers(num: list):
    new_list = []
    for i in num:
        if i % 2 == 0:
            new_list.append(i)
    return new_list


# main func

if __name__ == "__main__":
    my_list = [1,2,3,4,5]
    
    print (f"original {my_list}")
    print (f"new {even_numbers(my_list)}")
