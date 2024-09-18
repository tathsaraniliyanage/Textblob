from textblob import TextBlob, WordList
import nltk

b = TextBlob("I havv goood speling!")
print(b.correct())


from textblob import Word
w = Word("falibility")
w.spellcheck()
print(w.spellcheck())



