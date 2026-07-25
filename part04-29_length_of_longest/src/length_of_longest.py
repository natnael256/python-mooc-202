# Write your solution here

def length_of_longest(word_list: list):
    word_count = 0
    for i in word_list:
        if len(i) >= word_count:
            word_count = len(i)
    return word_count


#main
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)
