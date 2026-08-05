import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    "Size": [30, 50, 70, 90, 110, 130],
    "Price": [5, 8, 12, 15, 20, 25]
}

df = pd.DataFrame(data)

X = np.array(df["Size"]).reshape(-1, 1)
y = np.array(df["Price"])

model = LinearRegression()
model.fit(X, y)

plt.scatter(df["Size"], df["Price"], color="blue", label="Actual")
plt.plot(df["Size"], model.predict(X), color="red", label="Prediction line")
plt.title("House Size vs Price")
plt.xlabel("Size (sqm)")
plt.ylabel("Price (millions)")
plt.legend()
plt.show()