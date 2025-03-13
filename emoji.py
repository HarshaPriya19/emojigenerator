import re
from textblob import TextBlob
import emoji

emoji_dict = {
    "love": "❤️", "happy": "😊", "sad": "😢", "angry": "😡", "excited": "🤩",
    "coding": "💻", "Python": "🐍", "AI": "🤖", "learning": "📚", "fun": "😂",
    "bugs": "🐞", "coffee": "☕", "sleep": "😴", "fast": "⚡", "slow": "🐢",
    "food": "🍕", "burger": "🍔", "pizza": "🍕", "ice cream": "🍦",
    "music": "🎵", "dance": "💃", "car": "🚗", "bike": "🏍️", "train": "🚆",
    "sick": "🤒", "doctor": "👨‍⚕️", "hospital": "🏥", "money": "💰", "rich": "🤑",
    "work": "🏢", "fire": "🔥", "party": "🎉", "game": "🎮", "smart": "🧠",
    "travel": "✈️", "phone": "📱", "strong": "💪", "rain": "🌧️", "sun": "☀️",
    "moon": "🌙", "cold": "❄️", "hot": "🔥", "dog": "🐶", "cat": "🐱",
    "beautiful": "😍", "awesome": "🤩", "danger": "⚠️", "alert": "🚨",
    "water": "💧", "laugh": "😂", "brilliant": "💡", "tired": "🥱", "dead": "💀",
    "heart": "❤️", "broken": "💔", "money": "💰", "poor": "😢", "winner": "🏆",
    "boss": "🕴️", "robot": "🤖", "cool": "😎", "friend": "👫", "family": "👨‍👩‍👧‍👦",
    "shock": "😱", "fear": "😨", "cry": "😭", "laughing": "🤣", "help": "🆘",
}

def clean_text(text):
    """Removes punctuation and converts text to lowercase."""
    return re.sub(r"[^\w\s]", "", text).lower()

def text_to_emoji(text):
    """Converts text into an emoji-enhanced version with sentiment-based emojis."""
    sentences = text.split(". ")
    converted_sentences = []

    for sentence in sentences:
        cleaned_sentence = clean_text(sentence)
        sentiment = TextBlob(cleaned_sentence).sentiment.polarity
        words = cleaned_sentence.split()

        converted_text = " ".join(emoji_dict.get(word, word) for word in words)

        # Add sentiment-based emojis at the beginning and end of the sentence
        if sentiment > 0.5:
            converted_text = f"🤩 {converted_text} 🤩"
        elif sentiment > 0:
            converted_text = f"😊 {converted_text} 😊"
        elif sentiment < -0.5:
            converted_text = f"😭 {converted_text} 😭"
        elif sentiment < 0:
            converted_text = f"😞 {converted_text} 😞"
        else:
            converted_text = f"😐 {converted_text} 😐"

        converted_sentences.append(converted_text)

    return " ".join(converted_sentences)

# Get user input
user_input = input("Enter your text: ")
print(text_to_emoji(user_input))

