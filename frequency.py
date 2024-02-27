def calculate_word_frequency(text):
    word_frequency = {}
    
    # Split the text into words
    words = text.split()

    # Count the frequency of each word
    for word in words:
        # Remove punctuation marks
        word = word.strip('.,!?;:')
        # Convert the word to lowercase for case-insensitive counting
        word = word.lower()
        
        # If the word is already in the dictionary, increment its count
        if word in word_frequency:
            word_frequency[word] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            word_frequency[word] = 1
    
    return word_frequency

# Example usage:
text = "This is an example sentence. This sentence contains repeated words. Repeated words should be counted."
word_freq = calculate_word_frequency(text)
print(word_freq)