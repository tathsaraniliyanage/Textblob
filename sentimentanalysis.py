from textblob import TextBlob, WordList
import nltk

testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
testimonial.sentiment
Sentiment(polarity=0.39166666666666666, subjectivity=0.4357142857142857)
testimonial.sentiment.polarity


text="good"
blob=TextBlob(text)
sentiment=blob.sentimentprint(sentiment.polarity)

