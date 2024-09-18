from textblob import TextBlob, WordList
import nltk
# nltk.download('punkt_tab')
# nltk.download('averaged_perceptron_tagger_eng')



wiki = TextBlob("Python is a high-level, general-purpose programming language.")
# Part-of-speech Tagging
print(wiki.tags)

# Noun Phrase Extraction
print(wiki.noun_phrases)

# wordlists
animals = TextBlob("cat dog octopus")
animals.words
WordList(['cat', 'dog', 'octopus'])
animals.words.pluralize()
WordList(['cats', 'dogs', 'octopodes'])
print(animals)
print(animals.words)
print(animals.words.pluralize())


