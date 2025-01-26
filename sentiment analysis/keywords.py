from collections import Counter
import nltk
from nltk.corpus import stopwords
import pandas as pd
import seaborn as sns
import ast
import matplotlib.pyplot as plt

# Download NLTK stopwords
nltk.download('stopwords')
nltk.download('punkt')

# Load the data
file_path = "C:\\Users\SLala\Desktop\Extras\SRH\Thesis\Code\sentiment analysis\Tweets\Tweets21-20\SA21-20.csv"
df = pd.read_csv(file_path)
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Convert 'Sentiment Scores' column from string to dictionary
df['Sentiment Scores'] = df['Sentiment Scores'].apply(ast.literal_eval)

# Add a new column for sentiment compound score
df['Compound Score'] = df['Sentiment Scores'].apply(lambda x: x['compound'])

# Tokenize the text of tweets
all_words = ' '.join(df['Text'])
tokens = nltk.word_tokenize(all_words)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stop_words]

# Calculate word frequency
word_freq = Counter(filtered_tokens)

# Select top N keywords
top_keywords = word_freq.most_common(10)  # Change 10 to the desired number of keywords

# Extract keywords and their frequencies
keywords, frequencies = zip(*top_keywords)

# Calculate total number of words
total_words = sum(word_freq.values())

# Calculate percentage of each keyword frequency relative to total words
percentages = [(freq / total_words) * 1000 for freq in frequencies]

# Plot keywords with percentages
plt.figure(figsize=(10, 6))
sns.barplot(x=list(keywords), y=list(frequencies))
for i, freq in enumerate(frequencies):
    plt.text(i, freq, f'{percentages[i]:.2f}%', ha='center', va='bottom')
plt.title('Top Keywords in Tweets')
plt.xlabel('Keywords')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.savefig('3.6.png')
