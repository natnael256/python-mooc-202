# Write your solution here

def all_the_longest (word_list: list[str]):

    longest = max(word_list, key= len)
    new_list = []


    for i in word_list:

        if len(longest) <= len(i):
            new_list.append(i)
    return new_list


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    print (all_the_longest(my_list))
        
