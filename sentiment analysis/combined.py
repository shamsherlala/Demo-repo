import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
file_path1 = "C:\\Users\SLala\Desktop\Extras\SRH\Thesis\Code\sentiment analysis\Tweets\Tweets23-22\SA23-22.csv"
file_path2 = "C:\\Users\SLala\Desktop\Extras\SRH\Thesis\Code\sentiment analysis\Tweets\Tweets22-21\SA22-21.csv"
file_path3 = "C:\\Users\SLala\Desktop\Extras\SRH\Thesis\Code\sentiment analysis\Tweets\Tweets21-20\SA21-20.csv"

df1 = pd.read_csv(file_path1)
df1['Year'] = "2022-2023"

df2 = pd.read_csv(file_path2)
df2['Year'] = "2021-2022"

df3 = pd.read_csv(file_path3)
df3['Year'] = "2020-2021"

# Convert 'Sentiment Scores' column from string to dictionary
df['Sentiment Scores'] = df['Sentiment Scores'].apply(ast.literal_eval)

# Add a new column for sentiment compound score
df['Compound Score'] = df['Sentiment Scores'].apply(lambda x: x['compound'])

# Concatenate the dataframes
combined_df = pd.concat([df1, df2, df3])

# Plot the distribution of sentiment labels
plt.figure(figsize=(10, 6))
sns.countplot(x='Sentiment Label', hue='Year', data=combined_df, palette='viridis')
plt.title('Distribution of Sentiment Labels')
plt.xlabel('Sentiment Label')
plt.ylabel('Tweet Count')
plt.legend(title='Year')
plt.savefig('sentiment_distribution_combined.png')


# Box plot of sentiment scores by sentiment label
plt.figure(figsize=(10, 6))
sns.boxplot(x='Sentiment Label', y='Sentiment Scores', hue='Year', data=combined_df, palette='viridis')
plt.title('Sentiment Scores by Sentiment Label')
plt.xlabel('Sentiment Label')
plt.ylabel('Compound Score')
plt.ylim(-1, 1)  # Set the y-axis limit if necessary
plt.legend(title='Year')
plt.savefig('sentiment_boxplot_combined.png')
