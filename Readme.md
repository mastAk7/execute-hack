Twitter Sentiment Analysis Dashboard

A web-based dashboard built with Streamlit that fetches live tweets using the Twitter API, performs sentiment analysis using Hugging Face's transformers library, and visualizes the results through interactive charts.

Features

1. Real-time Tweet Fetching: Fetches live tweets based on user input.

2. Sentiment Analysis: Classifies tweets as Positive, Negative, or Neutral using a pre-trained DistilBERT model.

3. Visualizations: Interactive Pie Chart, Bar Graph, and Word Cloud for sentiment insights.

4. Export Data: Download the sentiment analysis results as a CSV file.

Technologies Used

1. Python

2. Streamlit (for the user interface)

3. Tweepy (for accessing the Twitter API)

4. Hugging Face Transformers (for sentiment analysis)

5. Plotly (for interactive charts)

6. Matplotlib and WordCloud (for visualization)

How It Works

1. Input Keyword: Users enter a keyword to fetch relevant tweets.

2. Fetch Tweets: The app fetches recent tweets using Tweepy.

3. Analyze Sentiment: Sentiment analysis is performed using the DistilBERT model.

4. Visualize Results: Sentiments are displayed via pie chart, bar chart, and word cloud.

5. Download Data: Users can export the results as a CSV file.

Screenshots/Demo
   ![image](https://github.com/user-attachments/assets/96636d76-d65f-49b4-9d82-3866357622ab)
   ![image](https://github.com/user-attachments/assets/5ad20aa9-d10b-44c5-9f99-98f8b971d1ad)
![image](https://github.com/user-attachments/assets/ad08df8d-567c-4243-861e-7d44bcab43d9)


Use Cases
 
1. Analyze public opinion on brands, products, or events.
2. Track sentiment trends over time.
3. Use for market research or competitor analysis.

Website - https://execute-hack.vercel.app/

License

This project is open to use.

