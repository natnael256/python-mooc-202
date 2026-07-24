# Write your solution here

def greatest_number(number1, number2, number3):

    while True:
        big_number = max(number1, number2, number3)
        return big_number
    


# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(3, 5, 7)
    print(greatest)