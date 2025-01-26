import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
file_path1 = "C:\\Users\SLala\Desktop\Extras\SRH\Thesis\Code\sentiment analysis\scrap\output_2023.csv"
file_path2 = "C:\\Users\SLala\Desktop\Extras\SRH\Thesis\Code\sentiment analysis\scrap\output_2022.csv"
file_path3 = "C:\\Users\SLala\Desktop\Extras\SRH\Thesis\Code\sentiment analysis\scrap\output_2021.csv"

df1 = pd.read_csv(file_path1)
df1['Year'] = 2023
df1['Date'] = pd.to_datetime(df1['Date'], dayfirst=True)

df2 = pd.read_csv(file_path2)
df2['Year'] = 2022
df2['Date'] = pd.to_datetime(df2['Date'], dayfirst=True)

df3 = pd.read_csv(file_path3)
df3['Year'] = 2021
df3['Date'] = pd.to_datetime(df3['Date'], dayfirst=True)

# Concatenate the dataframes
combined_df = pd.concat([df1, df2, df3])

# Plot the distribution of sentiment labels
plt.figure(figsize=(10, 6))
sns.countplot(x='Sentiment Label', hue='Year', data=combined_df, palette='turbo', alpha=0.7)
plt.ylabel('Tweet Count')

# Create a scatter matrix plot
sns.pairplot(combined_df, hue='Year', palette='viridis')

# Set title and labels
plt.title('Distribution of Sentiment Labels with Scatter Matrix')
plt.xlabel('Sentiment Label')

# Add legend
plt.legend(title='Year', loc='upper right')

plt.savefig('sentiment_distribution_scatter_matrix.png')
#plt.show()
