# Write your solution here

def no_vowels(my_string):
    vowels = "aeiou"
    for i in my_string:

        if i in vowels:
           my_string = my_string.replace(i, "")
           
    return my_string




if __name__ == "__main__":
    my_string = "xzcvb"
    print(no_vowels(my_string))




