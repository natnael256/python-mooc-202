# Write your solution here

def remove_smallest(numbers):

    smallest = numbers.index(min(numbers))
    numbers.pop(smallest)

    

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)