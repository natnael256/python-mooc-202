# Write your solution here
# You can test your function by calling it within the following block

def spruce(height):

    width = 1
    char = "*"
    cnter = height * 2
    print ("a spruce!")
    while height > 0:

        print((char * width).center(cnter) )
        width += 2
        height -= 1
    print(char.center(width - 1))


if __name__ == "__main__":
    spruce(3)