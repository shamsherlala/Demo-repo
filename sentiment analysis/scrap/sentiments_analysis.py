from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax

tweet = '@shamsherla today is cold @ Berlin https://twitter.com/home'

#preprocess tweets
tweet_words = []
for word in tweet.split(" "):
    if word.startswith("@") and len(word) > 1:
        word = '@user'
        
    elif word.startswith("http"):
        word = 'http'
        
    tweet_words.append(word)
    
tweet_proc = " ".join(tweet_words)

#print(tweet_proc)
# load model and tokenizer
roberta = "cardiffnlp/twitter-roberta-base-sentiment"

model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ['Negative', 'Neutral', 'Positive']

# sentiment analysis
encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')
output = model(encoded_tweet['input_ids'], encoded_tweet['attention_mask'])
print(output)
