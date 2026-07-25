# Write your solution here

def shortest (my_list: list[str]):
    short = my_list[0] # Start by assuming the first word is the shortest.
    length = len(my_list[0]) # Save the length of the first word for comparison.

    for i in my_list:
        if length > len(i):
            length  = len(i)
            short = i
    return short




if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    print(shortest(my_list))
