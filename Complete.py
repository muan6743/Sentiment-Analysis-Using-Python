import nltk
from textblob import TextBlob

# Download necessary NLTK data (only needs to be done once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Sample text reviews
reviews = [
    "I absolutely loved this movie! The acting was amazing and the plot was engaging.",
    "The food at this restaurant was terrible. I wouldn't recommend it to anyone.",
    "The weather today is quite pleasant, not too hot or cold.",
    "I had a really bad experience with their customer service. Very disappointed."
]

# Defining a function for sentiment analysis
def analyze_sentiment(text):
    # Create a TextBlob object with the input text
    blob = TextBlob(text)
    
    # Calculate the polarity (-1 to 1) and subjectivity (0 to 1) of the text
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Classify sentiment based on polarity
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    return sentiment, polarity, subjectivity

# Analyze sentiment for each review
for i, review in enumerate(reviews, start=1):
    sentiment, polarity, subjectivity = analyze_sentiment(review)
    print(f"Review {i}:")
    print("Text:", review)
    print("Sentiment:", sentiment)
    print("Polarity:", polarity)
    print("Subjectivity:", subjectivity)
    print("=" * 50)
