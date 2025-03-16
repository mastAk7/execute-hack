Twitter Sentiment Analysis Dashboard

A web-based dashboard built with Streamlit that fetches live tweets using the Twitter API, performs sentiment analysis using Hugging Face's transformers library, and visualizes the results through interactive charts.

Features

Real-time Tweet Fetching: Fetches live tweets based on user input.

Sentiment Analysis: Classifies tweets as Positive, Negative, or Neutral using a pre-trained DistilBERT model.

Visualizations: Interactive Pie Chart, Bar Graph, and Word Cloud for sentiment insights.

Export Data: Download the sentiment analysis results as a CSV file.

Technologies Used

Python

Streamlit (for the user interface)

Tweepy (for accessing the Twitter API)

Hugging Face Transformers (for sentiment analysis)

Plotly (for interactive charts)

Matplotlib and WordCloud (for visualization)

How It Works

Input Keyword: Users enter a keyword to fetch relevant tweets.

Fetch Tweets: The app fetches recent tweets using Tweepy.

Analyze Sentiment: Sentiment analysis is performed using the DistilBERT model.

Visualize Results: Sentiments are displayed via pie chart, bar chart, and word cloud.

Download Data: Users can export the results as a CSV file.

Contributions

Feel free to open issues and pull requests to contribute to the project.

License

This project is open to use.

