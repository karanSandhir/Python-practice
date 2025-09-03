converter_hindi_to_english = {
    "madad":"help",
    "dost":"friend",
    "billi":"cat",
}
print("Welcome to the Hindi to English Dictionary!")
word = input("Enter a Hindi word to get its English translation: ").strip()

if word in converter_hindi_to_english:
    print(f"The English translation of '{word}' is '{converter_hindi_to_english[word]}'.")
else:
    print(f"Sorry, the word '{word}' is not in the dictionary.")