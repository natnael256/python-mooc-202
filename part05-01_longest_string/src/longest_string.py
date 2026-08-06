# Write your solution here



def longest(my_list: []):

    longest_word = ""

    for i in my_list:
        if len(i) > len(longest_word):
            longest_word = i
    return longest_word


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))