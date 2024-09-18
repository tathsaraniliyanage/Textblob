from textblob import TextBlob, WordList
import nltk

monty = TextBlob("We are no longer the Knights who say Ni. "
                    "We are now the Knights who say Ekki ekki ekki PTANG.")
monty.word_counts['ekki']
print(monty.word_counts['ekki'])
print(monty.words.count('ekki', case_sensitive=True))



wiki = TextBlob("Python is a high-level, general-purpose programming language.")
print(wiki.noun_phrases.count('python'))
