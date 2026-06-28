# Write your solution here
# You can test your function by calling it within the following block

def line (count, icon):

    if len(icon) > 0:
        print(count * icon[0])
    else:
        print(count * "*")



if __name__ == "__main__":
    line(5, "x")




