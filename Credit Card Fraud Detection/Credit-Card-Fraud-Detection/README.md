# 💳 Credit Card Fraud Detection

## Overview
This project focuses on detecting fraudulent credit card transactions using **Logistic Regression** on a highly **imbalanced dataset**.  
It demonstrates fundamental steps in **data preprocessing, sampling, model training, and evaluation** for binary classification problems.

---

## Key Features
- ⚖️ Handles imbalanced data via under-sampling to balance normal and fraudulent transactions.
- 🧠 Logistic Regression model trained and evaluated for fraud classification.
- 📊 Performance metrics: Training and Testing accuracy scores.
- 🔍 Statistical comparison between legitimate and fraudulent transactions.
- 🧪 Easily extendable to advanced models (Random Forest, XGBoost, SMOTE).

---

## Workflow
```
Dataset → Data Cleaning → Sampling → Feature/Target Split
→ Train/Test Split → Logistic Regression Training → Evaluation
```

---

## Tech Stack
`Python` • `Pandas` • `NumPy` • `Scikit-learn`

---

## Setup & Run
```bash
pip install pandas numpy scikit-learn

# Run script
python src/fraud_detection.py
```

Ensure your dataset is placed under `data/creditcard.csv`

---

## Expected Output
- Console metrics showing training and testing accuracy.
- Balanced dataset with equal fraud and non-fraud samples.

---

## Future Enhancements
- Implement SMOTE for synthetic oversampling.
- Add Random Forest & XGBoost models.
- Visualize performance with Confusion Matrix & ROC curve.

---

## Outcome
The project highlights the application of **Machine Learning** to detect fraudulent activities efficiently, minimizing false negatives while maintaining robust model performance.