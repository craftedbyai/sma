# Experiment 7: Social Media Analytics Dashboard using Data Visualization

## Aim

To design and develop a Social Media Analytics Dashboard using data visualization techniques to analyze user engagement, sentiment distribution, and trending hashtags.

---

# Theory

## Introduction

Social Media Analytics refers to the process of collecting, analyzing, and interpreting data generated from social media platforms such as Twitter, Instagram, and Facebook. It helps organizations understand user behavior, monitor brand reputation, identify trends, and improve marketing strategies.

A Social Media Analytics Dashboard provides a graphical interface that displays key metrics and insights using visualizations such as pie charts, bar graphs, and scatter plots. These dashboards help convert large volumes of raw social media data into meaningful insights that can assist in decision-making.

Organizations use social media analytics dashboards for:

* Monitoring customer feedback
* Understanding audience engagement
* Tracking brand sentiment
* Identifying trending topics
* Improving digital marketing strategies

---

## Social Media Data Representation

Social media data is typically stored in a structured tabular format using a DataFrame. Each row represents a social media post and contains several attributes such as:

* Username
* Post content
* Number of likes
* Number of comments
* Number of shares
* Hashtag used
* Sentiment of the post

This structured representation allows easier processing, analysis, and visualization of the data.

---

## Engagement Metrics

Engagement metrics measure how users interact with social media content. A common way to measure engagement is through an engagement score.

Engagement Score Formula:

Engagement = Likes + Comments + Shares

This score helps in identifying:

* Highly popular posts
* User interaction levels
* Effective marketing content

Businesses use engagement metrics to optimize their content strategy and maximize audience reach.

---

## Data Simulation

In many experiments, real social media APIs are not used because they require authentication and access permissions. Therefore, synthetic data is generated using libraries such as Faker.

The Faker library can generate realistic looking data including:

* Random usernames
* Random sentences representing posts
* Random engagement values
* Random sentiment labels

This simulated dataset behaves similarly to real social media activity and allows experimentation without relying on external APIs.

---

## Sentiment Analysis

Sentiment analysis is a Natural Language Processing (NLP) technique used to determine the emotional tone behind a piece of text. Social media posts can be classified into three main categories:

* Positive
* Negative
* Neutral

Understanding sentiment distribution helps businesses analyze customer feedback, measure brand perception, and detect public opinion trends.

Visualization techniques such as pie charts are commonly used to represent sentiment distribution.

---

## Trending Hashtag Analysis

Hashtags represent keywords or topics associated with social media posts. By analyzing hashtag frequency, we can identify trending topics or discussions.

Trending hashtag analysis helps organizations:

* Identify popular topics
* Improve marketing campaigns
* Increase social media reach

Bar charts are commonly used to visualize the frequency of hashtags.

---

## Engagement Analysis

Engagement analysis studies the relationship between likes, comments, and shares to determine how users interact with posts.

Scatter plots are commonly used to visualize engagement patterns across posts. Bubble sizes can represent engagement levels.

These visualizations help identify high-performing posts and audience interaction patterns.

---

## Viral Content Identification

Posts with extremely high engagement scores are considered viral posts. Viral content can be identified by sorting posts based on engagement score and selecting the top-performing ones.

Identifying viral content helps businesses replicate successful strategies and collaborate with influencers.

---

## Summary Report

A summary report provides key statistics such as:

* Total number of posts
* Average likes, comments, and shares
* Most trending hashtag

Such reports allow quick insights and help decision makers understand overall social media performance.

---

# Python Implementation

## Required Libraries

Install the following libraries before running the code:

```
pip install pandas faker plotly
```

---

## Complete Python Code

```python
import pandas as pd
import random
from faker import Faker
import plotly.express as px

fake = Faker()

hashtags = ["#AI", "#DataScience", "#MachineLearning", "#Python", "#BigData"]
sentiments = ["Positive", "Negative", "Neutral"]

data = []

for i in range(100):
    likes = random.randint(10, 500)
    comments = random.randint(5, 200)
    shares = random.randint(1, 100)

    data.append({
        "User": fake.user_name(),
        "Post": fake.sentence(),
        "Likes": likes,
        "Comments": comments,
        "Shares": shares,
        "Hashtag": random.choice(hashtags),
        "Sentiment": random.choice(sentiments)
    })

# Create DataFrame
df = pd.DataFrame(data)

# Engagement score
df["Engagement"] = df["Likes"] + df["Comments"] + df["Shares"]

print("Sample Dataset:\n")
print(df.head())

# Sentiment Distribution
sentiment_counts = df["Sentiment"].value_counts()

fig1 = px.pie(
    values=sentiment_counts.values,
    names=sentiment_counts.index,
    title="Sentiment Distribution"
)

fig1.show()

# Trending Hashtags
hashtag_counts = df["Hashtag"].value_counts()

fig2 = px.bar(
    x=hashtag_counts.index,
    y=hashtag_counts.values,
    labels={"x": "Hashtag", "y": "Count"},
    title="Trending Hashtags"
)

fig2.show()

# Engagement Analysis
fig3 = px.scatter(
    df,
    x="Likes",
    y="Shares",
    size="Engagement",
    color="Sentiment",
    title="Engagement Analysis"
)

fig3.show()

# Identify Viral Posts
viral_posts = df.sort_values(by="Engagement", ascending=False).head(5)

print("\nTop Viral Posts:\n")
print(viral_posts[["User", "Post", "Engagement"]])

# Summary Report
print("\nSummary Report\n")

print("Total Posts:", len(df))
print("Average Likes:", df["Likes"].mean())
print("Average Comments:", df["Comments"].mean())
print("Average Shares:", df["Shares"].mean())

print("Most Trending Hashtag:", df["Hashtag"].value_counts().idxmax())
```

---

# Result

The Social Media Analytics Dashboard was successfully implemented using Python. The dashboard analyzed engagement metrics, sentiment distribution, and trending hashtags using data visualization techniques.

---

# Conclusion

This experiment demonstrates how data visualization can be used to analyze social media data effectively. By generating simulated data and performing engagement analysis, sentiment analysis, and hashtag trend analysis, useful insights can be obtained for business decision-making and digital marketing strategies.
