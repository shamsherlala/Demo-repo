from bs4 import BeautifulSoup
import requests
import csv


# get html
url = "https://twitter.com/i/lists/1746880937780981814"

# change the user-agent value based on your web browser
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

#get the tweets

tweets = soup.find_all(data_testid="cellInnerDiv")

print(tweets[1])