# Write your solution here

def distinct_numbers(numbers: list):
    unique_numbers = []


    for i in numbers: 
        if i not in unique_numbers:
            unique_numbers.append(i)

    return sorted(unique_numbers)




#mail

if __name__ == "__main__":
    
    my_list = [3, 2, 1, 3, 2, 1, 3, 2, 1]

    print (distinct_numbers(my_list))

