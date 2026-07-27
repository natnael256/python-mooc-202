def everything_reversed(my_list: list[str]):

    new_list = []
    word = ""
    for i in my_list:
        word = i[::-1]
        new_list.append(word)
    new_list = new_list[::-1]

    return new_list



if __name__ == '__main__':
    my_list = ["Hi", "there", "example", "one more"]
    print(everything_reversed(my_list))