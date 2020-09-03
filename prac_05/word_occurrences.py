text = input("Enter text: ").split()

word_count = {}
for word in text:
    word_frequency = word_count.get(word, 0)
    word_count[word] = word_frequency + 1

# Put words in a list and Sort word alphabetically
text = list(word_count.keys())
text.sort()

# Find maximum length of word in text
max_length = 0
for word in text:
    if len(word) > max_length:
        max_length = len(word)


# Print out words, frequency and formatting
for word in text:
    print("{:{}} : {}".format(word, max_length, word_count[word]))
