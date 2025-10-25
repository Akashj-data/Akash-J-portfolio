# 💳 Credit Card Fraud Detection

## Overview
This project focuses on detecting fraudulent credit card transactions using **Logistic Regression** on a highly **imbalanced dataset**.  
It demonstrates fundamental steps in **data preprocessing, sampling, model training, and evaluation** for binary classification problems.

---

## Key Features
- ⚖️ **Handles imbalanced data** via under-sampling to balance normal and fraudulent transactions.
- 🧠 **Logistic Regression Model** trained and evaluated for fraud classification.
- 📊 **Performance Metrics:** Accuracy scores on both training and test data.
- 🔍 **Data Analysis:** Statistical comparison between legitimate and fraudulent transactions.
- 🧪 **Scalable Design:** Can be extended with advanced models like Random Forest, XGBoost, or SMOTE balancing.

---

## Architecture Overview
The workflow follows a structured data science approach: Dataset → Data Cleaning → Sampling → Feature/Target Split
→ Train/Test Split → Logistic Regression Training → Evaluation


### Core Steps
| Step | Description |
|------|--------------|
| **1. Data Loading** | Reads dataset and inspects structure using `pandas`. |
| **2. Data Exploration** | Analyzes missing values, distributions, and imbalance. |
| **3. Under-sampling** | Balances the dataset using an equal number of fraud and non-fraud samples. |
| **4. Model Training** | Trains Logistic Regression with Scikit-learn. |
| **5. Evaluation** | Reports accuracy scores for both train and test sets. |

---

## Tech Stack
`Python` • `Pandas` • `NumPy` • `Scikit-learn` • `Matplotlib`

---

## Setup & Run
```bash
# Clone the repository
git clone https://github.com/Akashj-data/Credit-Card-Fraud-Detection.git
cd Credit-Card-Fraud-Detection

# Install dependencies
pip install pandas numpy scikit-learn matplotlib

# Run the training script
python src/fraud_detection.py

Dataset:

Dataset Source: Kaggle - Credit Card Fraud Detection

Columns include PCA features (V1 … V28), Amount, and Class (0 = Legit, 1 = Fraud)

Total Records: 284,807

Fraudulent Transactions: 492 (~0.17%)

Expected Output:

Training accuracy displayed in console

Test accuracy displayed in console

Fraud class balance statistics

Optional plots for confusion matrix or ROC curve

Future Enhancements:

Implement SMOTE for synthetic oversampling

Add Random Forest & XGBoost models

Introduce threshold tuning based on Precision-Recall tradeoffs

Visualize performance with ROC and Confusion Matrix
