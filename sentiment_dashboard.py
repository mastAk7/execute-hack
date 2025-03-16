import pandas as pd
import torch
from transformers import pipeline
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import tweepy
import os
import time
import streamlit as st

# Set up Tweepy client
def create_twitter_client():
    bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
    return tweepy.Client(bearer_token=bearer_token)

# Sentiment Analysis Model
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Fetch Real Tweets
def fetch_tweets(keyword, max_results=10):
    client = create_twitter_client()
    tweets = []

    while len(tweets) < max_results:
        try:
            response = client.search_recent_tweets(query=keyword, max_results=10, tweet_fields=["text"])
            if response.data:
                tweets.extend([tweet.text for tweet in response.data])
            else:
                break
            time.sleep(15)  # Increased delay to avoid rate limiting
        except tweepy.TooManyRequests:
            st.warning("Rate limit reached. Waiting for 60 seconds...")
            time.sleep(60)
        except Exception as e:
            st.error(f"Error fetching tweets: {e}")
            break

    return tweets[:max_results]

# Analyze Sentiment
def analyze_sentiment(tweets):
    results = sentiment_pipeline(tweets)
    return [result["label"] for result in results]

# Visualize Sentiment
def plot_sentiment(df):
    sentiment_count = df["Sentiment"].value_counts().reset_index()
    sentiment_count.columns = ["Sentiment", "Count"]

    fig = px.pie(sentiment_count, names="Sentiment", values="Count", title="Sentiment Distribution")
    st.plotly_chart(fig)

    fig_bar = px.bar(sentiment_count, x="Sentiment", y="Count", color="Sentiment", title="Sentiment Breakdown")
    st.plotly_chart(fig_bar)

# Generate Word Cloud
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(text))
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(plt)

# CSV Export
def export_csv(df):
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "sentiment_analysis.csv", "text/csv")

# Main Execution
if __name__ == "__main__":
    st.title("Twitter Sentiment Analysis Dashboard")

    keyword = st.text_input("Enter a keyword to analyze:")

    if st.button("Analyze Sentiment"):
        if keyword:
            st.info("Fetching tweets and analyzing...")
            try:
                tweets = fetch_tweets(keyword)
                if not tweets:
                    st.error("No tweets found. Try another keyword.")
                else:
                    sentiments = analyze_sentiment(tweets)

                    df = pd.DataFrame({"Tweet": tweets, "Sentiment": sentiments})

                    st.subheader("Sample Tweets")
                    st.dataframe(df.head(10))

                    plot_sentiment(df)

                    st.subheader("Word Cloud")
                    generate_wordcloud(tweets)

                    export_csv(df)
                    st.success("CSV exported successfully.")

            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter a keyword.")
