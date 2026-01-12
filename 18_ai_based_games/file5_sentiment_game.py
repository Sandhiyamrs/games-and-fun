text = input("Type a sentence: ").lower()
if "good" in text:
    print("Positive sentiment 😊")
elif "bad" in text:
    print("Negative sentiment 😞")
else:
    print("Neutral sentiment 😐")
