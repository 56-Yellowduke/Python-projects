
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = np.array([
    [20, 100000], [21, 110000], [22, 120000],
    [25, 700000], [27, 900000], [29, 800000],
    [23, 150000], [30, 957400], [35, 500000],
    [40, 800000], [19, 50000], [45, 1000000]
])

y = np.array([0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1])

model=DecisionTreeClassifier()
model.fit(X, y)

customers = [[31, 70000], [32, 90000], [37, 991000]]

for student in customers:
   prediction = model.predict([student])
   result= "Buy" if prediction [0] == 1 else "Not Buy"
   print(f"Age: {student[0]},  Income:{student[1]}  {result}")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions) * 100, "%")