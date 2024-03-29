mood = input("Emotion: ")
emojibank = {
    "happy": "😄",
    "sad": "😢",
    "angry": "😠",
    "disgust": "🤢",
    "surprised": "😯",
    "afraid": "😨",
}
output = ''

def emotion(mood,emojibank):
    output = emojibank[mood.lower()] + " "
    return(output)

emotion(mood,emojibank)
print("Today I am "+(emotion(mood,emojibank)))
