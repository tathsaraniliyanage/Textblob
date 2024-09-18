from textblob import TextBlob, WordList
import nltk

# testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
# testimonial.sentiment
# testimonial.sentiment.polarity


text="bad is better than good"
blob=TextBlob(text)
sentiment=blob.sentiment
print(sentiment.polarity)

text="good is better than bad"
blob=TextBlob(text)
sentiment=blob.sentiment
print(sentiment.polarity)

# data set ek tag Kr 
# error clean kr
# algorithm ekkin check kra
