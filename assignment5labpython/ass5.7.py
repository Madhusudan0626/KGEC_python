def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]

    modified_sentence = ' '.join(capitalized_words)

    return modified_sentence
user_input = input("Enter a sentence: ")

result = capitalize_words(user_input)
print("Modified Sentence:", result)
