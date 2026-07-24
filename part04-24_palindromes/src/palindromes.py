# Write your solution here
def palindromes(word):
    return word == word[::-1] #This will return True of False by it silf. 


# Note, that at this time the main program should not be written inside

while True: 
    word = input("Please type in a palindrome: ").strip()

    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
    
    
