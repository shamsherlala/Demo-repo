import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read the CSV file
file_path = "C:\\Users\SLala\Desktop\Extras\SRH\Thesis\Code\sentiment analysis\Tweets\Tweets21-20\SA21-20.csv"
df = pd.read_csv(file_path)

# Extract text from the second column (assuming it's named 'Text' in this example)
text_column = 'Text'  # Replace 'Text' with the actual column name
text_data = df[text_column].dropna()  # Drop rows with missing values in the 'Text' column

# Combine all text into a single string
all_text = ' '.join(text_data)

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='hanning')
plt.axis('off')
plt.savefig('wc21.jpg')
