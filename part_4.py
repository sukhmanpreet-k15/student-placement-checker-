

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

# ----------------------------------------------------------------
# 1. Load the labeled data
# ----------------------------------------------------------------
df = pd.read_csv(r"C:\Users\sukhm\OneDrive\Desktop\pydev\project_ml_place_chk\placement_data.csv")

FEATURE_COLUMNS = [
    "cgpa",
    "mcq_score",
    "code_score",
    "project_score",
    "internships",
    "projects_done",
    "backlogs",
]

X = df[FEATURE_COLUMNS]
y = df["placed"]

# ----------------------------------------------------------------
# 2. Split into train/test so we can honestly check accuracy
# ----------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ----------------------------------------------------------------
# 3. Train a Decision Tree Classifier
#    max_depth=5 limits how many questions deep the tree can go -
#    without a limit, it tends to memorize the training data exactly
#    (overfitting) instead of learning patterns that generalize.
# ----------------------------------------------------------------
model = DecisionTreeClassifier(random_state=42, max_depth=5)
model.fit(X_train, y_train)

# ----------------------------------------------------------------
# 4. Check how good it is on data it has NEVER seen
# ----------------------------------------------------------------
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy:.3f}")
print()
print(classification_report(y_test, predictions))

# ----------------------------------------------------------------
# 5. Retrain on ALL the data for the final deployed version
# ----------------------------------------------------------------
final_model = DecisionTreeClassifier(random_state=42, max_depth=5)
final_model.fit(X, y)

# ----------------------------------------------------------------
# 6. Save the trained model to disk using pickle
# ----------------------------------------------------------------
os.makedirs("models", exist_ok=True)
with open("models/placement_model.pkl", "wb") as f:
    pickle.dump(final_model, f)

print("\nSaved trained model to models/placement_model.pkl")