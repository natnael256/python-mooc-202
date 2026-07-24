# Write your solution here

def sum_of_positives(numbers: list):
    sum = 0
    for i in numbers:
        if i > 0:
            sum = sum + i
    
    return sum


if __name__ == "__main__":
    my_list = [1,-2,3,-4,5]
    print(f"The result is {sum_of_positives(my_list)}")


    