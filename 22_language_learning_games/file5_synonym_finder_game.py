synonyms = {
    "happy": "joyful",
    "fast": "quick",
    "smart": "intelligent"
}

word = input("Enter a word: ").lower()

if word in synonyms:
    print("Synonym:", synonyms[word])
else:
    print("No synonym found.")
