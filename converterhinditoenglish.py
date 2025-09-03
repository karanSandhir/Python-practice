converter_hindi_to_english = {
    "नमस्ते": "Hello",
    "पानी": "Water",
    "किताब": "Book",
    "घर": "House",
    "शिक्षक": "Teacher",
    "विद्यार्थी": "Student",
    "खुशी": "Happiness",
    "बगीचा": "Garden",
    "दोस्त": "Friend",
    "परिवार": "Family"
}
print("Welcome to the Hindi to English Dictionary!")
word = input("Enter a Hindi word to get its English translation: ").strip()

if word in converter_hindi_to_english:
    print(f"The English translation of '{word}' is '{converter_hindi_to_english[word]}'.")
else:
    print(f"Sorry, the word '{word}' is not in the dictionary.")