mood = input("Emotion> ")
emojibank = {
    "happy": "😄",
    "sad": "😢",
    "angry": "😠",
    "disgust": "🤢",
    "surprised": "😯",
    "afraid": "😨",
}
output = ''

for word in mood.split():
    if word.lower() in emojibank:
        output += emojibank[word.lower()] + " "
        print("Today, I am " + (output))
    else:
        print("Emoji does not exist yet!")