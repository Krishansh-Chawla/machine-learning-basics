import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 40, 50, 55, 65, 70, 78, 90]
}

df = pd.DataFrame(data)

X = df[["Study_Hours"]]
y = df["Marks"]

model = LinearRegression()

model.fit(X, y)

sh=eval(input("Enter study hours:: "))
predicted_marks = model.predict(
    pd.DataFrame({"Study_Hours": [sh]})
)
print(f"Predicted marks for {sh} study hours: {predicted_marks[0]:.2f}")
