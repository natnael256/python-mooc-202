# Write your solution here

def longest_series_of_neighbours(my_list):
    longest = 0


    for i in my_list:
        currnt_num = i 
        next_num = [i + 1]

        if abs(currnt_num - next_num) == 1:
            longest += longest

    return longest  
            
my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbours(my_list))