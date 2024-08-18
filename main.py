# Now that you have been introduced to web scraping and TextBlob, let's target a website that contains quotes and perform sentiment analysis. We will scrape the website for quotes and analyze their sentiment using TextBlob.
import requests
from textblob import TextBlob
from bs4 import BeautifulSoup

# Grab text from quotes web page
data = requests.get("http://quotes.toscrape.com/tag/inspirational/")

# Parse the contents of the page with BeautifulSoup
data_scraping = BeautifulSoup(data.content, "html.parser")
spans = data_scraping.select(".text")

# Loop through the data and perform sentiment analysis
for span in spans:
    quote = TextBlob(span.text)  # Create a TextBlob object for each quote
    quoteScore = round(quote.sentiment.polarity, 2)  # Calculate and round the sentiment polarity to 2 decimal places
    print(span.text, "\n")  # Print the quote
    print("The sentiment analysis for this quote is: {}\n\n".format(quoteScore))  # Print the sentiment analysis result
