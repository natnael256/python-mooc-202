# Write your solution here
word_list = []


while True:
    input_word = input("Word: ")
    input_word = input_word.lower()

    if input_word in word_list:
        print (f"You typed in {len(word_list)} different words")
        break
    else:
        word_list.append(input_word)
        
