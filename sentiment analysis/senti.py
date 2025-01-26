import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

#nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

file_path = "C:\\Users\SLala\Desktop\Extras\SRH\Thesis\Code\sentiment analysis\Tweets\Tweets2023\Sorted\Sorted2023.csv"

df = pd.read_csv(file_path)
texts = df.iloc[:, 2].astype(str)

result_texts = []
result_scores = []
result_labels = []

for text in texts:
    sentiment_scores = sia.polarity_scores(text)

    if sentiment_scores['compound'] > 0.05:
        sentiment_label = "positive"
    elif sentiment_scores['compound'] < -0.05:
        sentiment_label = "negative"
    else:
        sentiment_label = "neutral"

    result_texts.append(text)
    result_scores.append(sentiment_scores)
    result_labels.append(sentiment_label)

result_df = pd.DataFrame({
    'Text': result_texts,
    'Sentiment Scores': result_scores,
    'Sentiment Label': result_labels
})

output_csv_path = "C:\\Users\SLala\Desktop\Extras\SRH\Thesis\Code\sentiment analysis\Tweets\Tweets2023\Sorted\Senti_analysis2023.csv"
result_df.to_csv(output_csv_path, index=False)

print(f"Results saved to {output_csv_path}")
