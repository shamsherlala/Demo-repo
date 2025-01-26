import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

# Read the Excel file
file_path = "C:\\Users\SLala\Desktop\Extras\SRH\Thesis\Code\sentiment analysis\Excel.xls"  # Replace with the actual path to your Excel file

# Assuming the second column is named 'Text' in your Excel file
df = pd.read_excel(file_path)
texts = df.iloc[:, 2].astype(str)

# Initialize lists to store results
result_texts = []
result_scores = []
result_labels = []

# Analyze sentiment for each row in the second column
for text in texts:
    sentiment_scores = sia.polarity_scores(text)

    if sentiment_scores['compound'] > 0.05:
        sentiment_label = "positive"
    elif sentiment_scores['compound'] < -0.05:
        sentiment_label = "negative"
    else:
        sentiment_label = "neutral"

    # Append results to lists
    result_texts.append(text)
    result_scores.append(sentiment_scores)
    result_labels.append(sentiment_label)

# Create a DataFrame from the results
result_df = pd.DataFrame({
    'Text': result_texts,
    'Sentiment Scores': result_scores,
    'Sentiment Label': result_labels
})

# Save the DataFrame to a CSV file
output_csv_path = "C:\\Users\SLala\Desktop\Extras\SRH\Thesis\Code\sentiment analysis\output.csv"  # Replace with the desired output path
result_df.to_csv(output_csv_path, index=False)

print(f"Results saved to {output_csv_path}")
