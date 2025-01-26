import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

text = "today is wednesday. Wednesdays are usually very boring."

sentiment_scores = sia.polarity_scores(text)

if sentiment_scores['compound'] > 0.05:
    sentiment_label = "positive"
elif sentiment_scores['compound'] < -0.05:
    sentiment_label = "negative"
else:
    sentiment_label = "neutral"
    
print("Text:", text)
print("Sentiment Scores:", sentiment_scores)
print("Sentiment Label:", sentiment_label)
