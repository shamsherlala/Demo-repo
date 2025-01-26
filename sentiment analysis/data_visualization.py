from collections import Counter
import nltk
from nltk.corpus import stopwords
import pandas as pd
import seaborn as sns
import ast
import matplotlib.pyplot as plt

# Load the data
file_path = "C:\\Users\SLala\Desktop\Extras\SRH\Thesis\Code\sentiment analysis\Tweets\Tweets23-22\SA23-22.csv"
df = pd.read_csv(file_path)
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Convert 'Sentiment Scores' column from string to dictionary
df['Sentiment Scores'] = df['Sentiment Scores'].apply(ast.literal_eval)

# Add a new column for sentiment compound score
df['Compound Score'] = df['Sentiment Scores'].apply(lambda x: x['compound'])

# Download NLTK stopwords
nltk.download('stopwords')

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

# Plot keywords
plt.figure(figsize=(10, 6))
sns.barplot(x=list(keywords), y=list(frequencies))
plt.title('Top Keywords in Tweets')
plt.xlabel('Keywords')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()


# Plot the distribution of sentiment labels
plt.figure(figsize=(8, 6))
order = df['Sentiment Label'].value_counts().index
sns.countplot(x='Sentiment Label', hue='Sentiment Label', data=df, palette='viridis', order=order, legend=False)
plt.title('Distribution of Sentiment Labels - 2022-2023')
plt.xlabel('Sentiment Label')
plt.ylabel('Tweet Count')
#plt.savefig('sentiment_distribution.png')
plt.savefig('1.1.png')

# Time series plot of sentiment scores over time
plt.figure(figsize=(12, 8))
sns.lineplot(x='Date', y='Compound Score', data=df)
plt.title('Sentiment Compound Score Over Time - 2022-2023')
plt.xlabel('Date')
plt.ylabel('Compound Score')
#plt.savefig('sentiment_timeseries.png')
plt.savefig('2.1.png')

# Box plot of sentiment scores by sentiment label
plt.figure(figsize=(6, 8))
order = df['Sentiment Label'].value_counts().index
sns.boxplot(x='Sentiment Label', y='Compound Score', data=df, order=order)
plt.title('Sentiment Scores by Sentiment Label - 2022-2023')
plt.xlabel('Sentiment Label')
plt.ylabel('Sentiment Score')
plt.ylim(-1, 1)
#plt.savefig('sentiment_boxplot.png')
plt.savefig('3.1.png')

# Visualize sentiment compound score distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Compound Score'], bins=20, kde=True, color='skyblue')
plt.title('Sentiment Compound Score Distribution - 2022-2023')
plt.xlabel('Compound Score')
plt.ylabel('Frequency')
#plt.savefig('sentiment_score.png')
plt.savefig('4.1.png')

# Plotting sentiment distribution over time
plt.figure(figsize=(12, 6))
#order = df['Sentiment Label'].value_counts().index
sns.countplot(x=df['Date'].dt.strftime('%Y-%m'), hue='Sentiment Label', data=df, palette='viridis')
plt.title('Sentiment Distribution Over Time - 2022-2023')
plt.xlabel('Date')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Sentiment')
#plt.savefig('sentiment_time.png')
plt.savefig('5.1.png')

'''
#NEED TO PLAY WITH TEXT!!!
# Scatter plot of sentiment scores vs. tweet length
sns.scatterplot(x='Date', y='Compound Score', data=df)
plt.title('Sentiment Scores vs. Sentiment Label')
plt.xlabel('Sentiment Label')
plt.ylabel('Sentiment Score')
plt.savefig('sentiment_scatterplot23.png')
'''

'''
# Word cloud for each sentiment label
from wordcloud import WordCloud

for label in df['Sentiment Label'].unique():
    text = ' '.join(df[df['Sentiment Label'] == label]['Text'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.imshow(wordcloud, interpolation='gaussian')
    #plt.title(f'Word Cloud for {label} Sentiment')
    plt.axis('off')
    plt.savefig('666.png')
'''

'''
# Extracting sentiment scores from dictionary objects
df['Sentiment Scores'] = df['Sentiment Scores'].apply(lambda x: x['compound'])

# Grouping data by date and aggregating sentiment scores
sentiment_trends = df.groupby(df['Date'].dt.date)['Sentiment Scores'].mean()

# Plotting sentiment trends over time
plt.figure(figsize=(12, 6))
sentiment_trends.plot(marker='o', color='orange')
plt.title('Sentiment Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Average Sentiment Score')
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig('scores.png')
'''