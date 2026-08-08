
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import pickle
import os

# ----------------------------------------------------------------
# 1. Load the labeled data
# ----------------------------------------------------------------
df = pd.read_excel(r"C:\Users\sukhm\OneDrive\Desktop\pydev\project_ml_place_chk\updated_project.xlsx")

FEATURE_COLUMNS = [
    "total_lines",
    "num_functions",
    "num_classes",
    "num_comments",
    "adv_libs",
    "error_handling",
]

X = df[FEATURE_COLUMNS]
y = df["marks"]

# ----------------------------------------------------------------
# 2. Split into train/test so we can honestly check accuracy
#    (test data is held back - the model never sees it while training)
# ----------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------------------------------------------
# 3. Train a Decision Tree Regressor
#    max_depth=6 limits how many questions deep the tree can go -
#    without a limit, a decision tree tends to memorize the training
#    data exactly (overfitting) instead of learning general patterns.
# ----------------------------------------------------------------
model = DecisionTreeRegressor(random_state=42, max_depth=6)
model.fit(X_train, y_train)

# ----------------------------------------------------------------
# 4. Check how good it is on data it has NEVER seen
# ----------------------------------------------------------------
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Mean Absolute Error: {mae:.2f} marks")
print(f"R-squared score:     {r2:.3f}")
print("(R2 close to 1.0 means the model explains the data very well)")

# ----------------------------------------------------------------
# 5. Retrain on ALL the data (not just 80%) for the final deployed
#    version - once we've confirmed accuracy above, we don't want
#    to throw away 20% of our small dataset in the real model.
# ----------------------------------------------------------------
final_model = DecisionTreeRegressor(random_state=42, max_depth=6)
final_model.fit(X, y)

# ----------------------------------------------------------------
# 6. Save the trained model to disk using pickle
#    pickle.dump(object, file) writes the trained model's state to
#    a file. We open the file in "wb" mode - write binary - since
#    pickle saves data as raw bytes, not plain text.
# ----------------------------------------------------------------
os.makedirs("models", exist_ok=True)
with open("models/project_eval_model.pkl", "wb") as f:
    pickle.dump(final_model, f)

print("\nSaved trained model to models/project_eval_model.pkl")