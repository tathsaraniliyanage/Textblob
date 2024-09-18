from flask import Flask,render_template,request,jsonify
from textblob import TextBlob, WordList

app = Flask(__name__)

@app.route("/",methods=['GET'])
def hello_world():
    # return "<p>Hello, World!</p>"
    return render_template('index.html')


@app.route("/feedback",methods =['POST'])
def feedback():
    text=request.form['text']
    # text="bad is better than good"
    blob=TextBlob(text)
    sentiment=blob.sentiment
    print(sentiment.polarity)

    # return render_template('index.html')
    return render_template('index.html',value=sentiment.polarity)










