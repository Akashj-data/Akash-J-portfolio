import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv('data/creditcard.csv')

# Separate fraudulent and legitimate transactions
fraud = data[data['Class'] == 1]
legit = data[data['Class'] == 0]

# Downsample legitimate transactions to match fraud count
legit_sample = legit.sample(n=len(fraud))
balanced_data = pd.concat([legit_sample, fraud], axis=0)

# Features and target
X = balanced_data.drop(columns=['Class'])
y = balanced_data['Class']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Accuracy
train_acc = accuracy_score(y_train, y_pred_train)
test_acc = accuracy_score(y_test, y_pred_test)

print("Training Accuracy:", round(train_acc, 3))
print("Testing Accuracy:", round(test_acc, 3))