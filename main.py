# load libraries
from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from google.cloud import storage
import gcsfs
import json

# predict sentiment
def sentiment_prd(sentence):
    translator = Translator()
    translations = translator.translate(sentence, dest='en')
    trans_text = translations.text
    analyser = SentimentIntensityAnalyzer()
    result = analyser.polarity_scores(trans_text)
    
    res = ''
    if(result["compound"] < 0):
        res = "Negative"

    if(result["compound"] == 0):
        res = "Netural"

    if(result["compound"] > 0):
        res="Positive"
    return res
 
if __name__ == "__main__":
  text = "I had a great day"
  print(sentiment_prd(text))
