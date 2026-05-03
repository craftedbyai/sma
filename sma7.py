import pandas as pd
import random
from faker import Faker
import plotly.express as px

# Initialize faker
fake = Faker()

# Lists for hashtags and sentiment
hashtags = ["#AI", "#DataScience", "#MachineLearning", "#Python", "#BigData"]
sentiments = ["Positive", "Negative", "Neutral"]

# Generate simulated social media dataset
data = []

for i in range(100):
    likes = random.randint(10, 500)
    comments = random.randint(5, 200)
    shares = random.randint(1, 100)

    post = {
        "User": fake.user_name(),
        "Post": fake.sentence(),
        "Likes": likes,
        "Comments": comments,
        "Shares": shares,
        "Hashtag": random.choice(hashtags),
        "Sentiment": random.choice(sentiments)
    }

    data.append(post)

# Convert to DataFrame
df = pd.DataFrame(data)

# Create Engagement Metric
df["Engagement"] = df["Likes"] + df["Comments"] + df["Shares"]

# Display dataset sample
print("\nSample Dataset:\n")
print(df.head())

# -----------------------------
# Sentiment Distribution
# -----------------------------
sentiment_counts = df["Sentiment"].value_counts()

fig1 = px.pie(
    values=sentiment_counts.values,
    names=sentiment_counts.index,
    title="Sentiment Distribution"
)

fig1.show()

# -----------------------------
# Trending Hashtags
# -----------------------------
hashtag_counts = df["Hashtag"].value_counts()

fig2 = px.bar(
    x=hashtag_counts.index,
    y=hashtag_counts.values,
    labels={"x": "Hashtag", "y": "Count"},
    title="Trending Hashtags"
)

fig2.show()

# -----------------------------
# Engagement Analysis
# -----------------------------
fig3 = px.scatter(
    df,
    x="Likes",
    y="Shares",
    size="Engagement",
    color="Sentiment",
    title="Engagement Analysis Scatter Plot"
)

fig3.show()

# -----------------------------
# Identify Viral Posts
# -----------------------------
viral_posts = df.sort_values(by="Engagement", ascending=False).head(5)

print("\nTop 5 Viral Posts:\n")
print(viral_posts[["User", "Post", "Engagement"]])

# -----------------------------
# Summary Report
# -----------------------------
print("\nSummary Report\n")

print("Total Posts:", len(df))
print("Average Likes:", round(df["Likes"].mean(), 2))
print("Average Comments:", round(df["Comments"].mean(), 2))
print("Average Shares:", round(df["Shares"].mean(), 2))

print("Most Trending Hashtag:", df["Hashtag"].value_counts().idxmax())
