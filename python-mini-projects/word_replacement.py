def replace_word():
    str = "Hi How are you? Where are you now?"
    word_to_replace = input("Enter the word to replace: ")
    word= input("Enter the word that will be replaced: ")
    print(str.replace(word_to_replace, word))

replace_word()