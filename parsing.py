from textblob import TextBlob, WordList
import nltk

b = TextBlob("And now for something completely different.")
print(b.parse())