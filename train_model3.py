import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load dataset
df = pd.read_csv(
    "Paris 2024 Olympics Medals and Sports by Country.csv",
    encoding="latin1"
)

# Create Rank based on medals
df = df.sort_values(
    by=["Gold", "Silver", "Bronze"],
    ascending=False
).reset_index(drop=True)

df["Rank"] = df.index + 1

# Inputs
X = df[["Gold", "Silver", "Bronze"]]

# Output
y = df["Rank"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model3.pkl", "wb"))

print("Rank Prediction Model Trained Successfully")