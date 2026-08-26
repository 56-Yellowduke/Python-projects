import pandas as pd

df = pd.read_csv("fifa_world_cup_2026_player_performance 2.csv")


print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())
print("\nBasic stats:")
print(df.describe())

# Top 10 goal scorers
print("\n=== TOP 10 GOAL SCORERS ===")
top_scorers = df.groupby("player_name")["goals"].sum().sort_values(ascending=False).head(10)
print(top_scorers)

# Top 10 nationalities by number of players
print("\n=== TOP 10 NATIONALITIES ===")
nationalities = df["nationality"].value_counts().head(10)
print(nationalities)

# Average player rating by position
print("\n=== AVERAGE RATING BY POSITION ===")
avg_rating = df.groupby("position")["player_rating"].mean().sort_values(ascending=False)
print(avg_rating)

# Check if Nigeria is in the dataset
print("\n=== NIGERIAN PLAYERS ===")
nigeria = df[df["nationality"] == "Nigeria"]
print(nigeria[["player_name", "position", "player_rating"]].drop_duplicates())


import matplotlib.pyplot as plt

# Chart 1 - Top 10 Goal Scorers
plt.figure(figsize=(10, 6))
top_scorers.plot(kind="bar", color="green")
plt.title("Top 10 Goal Scorers - FIFA World Cup 2026")
plt.xlabel("Player")
plt.ylabel("Goals")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Chart 2 - Top 10 Nationalities
plt.figure(figsize=(10, 6))
nationalities.plot(kind="bar", color="blue")
plt.title("Top 10 Nationalities - FIFA World Cup 2026")
plt.xlabel("Nationality")
plt.ylabel("Number of Players")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Chart 3 - Average Rating by Position
plt.figure(figsize=(8, 5))
avg_rating.plot(kind="bar", color="orange")
plt.title("Average Player Rating by Position")
plt.xlabel("Position")
plt.ylabel("Average Rating")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Select features and target
features = ["goals", "assists", "pass_accuracy", "shots_on_target", "distance_covered_km"]
target = "player_rating"

# Drop rows with missing values
df_clean = df[features + [target]].dropna()

X = df_clean[features]
y = df_clean[target]

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print("\n=== ML MODEL ===")
print("Mean Squared Error:", round(mse, 2))
print("Model Score:", round(model.score(X_test, y_test), 2))