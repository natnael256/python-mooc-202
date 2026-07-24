# Write your solution here
def first_word(sentence):
    return sentence.split()[0]

def second_word(sentence):
    return sentence.split()[1]

def last_word(sentence):
    return sentence.split()[-1]

def mid_word(sentence: str):
    words = sentence.split()
    mid_index = len(words) // 2
    mid_index -= 1
    return sentence.split()[mid_index]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
    print(mid_word(sentence))