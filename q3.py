//seongjun
def wordCount(t):
    # Initialize a dictionary
    word_dict = {}
    
    with open(t, 'r') as file:
        for line_number, line in enumerate(file, 1):

            words = line.strip().split()
            for word in words:
                    # Otherwise, add the word to the dictionary with the current line number
                word_dict[word] = [line_number]
    
    return word_dict

wordCount('words.txt')

