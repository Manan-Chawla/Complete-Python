# 🚀 Customer Churn Prediction using Cross-Validation

## 📌 Project Objective

Customer churn (customers leaving a service) is a **real-world business problem** faced by telecom, banking, SaaS, and subscription-based companies.

In this project, we:

* Build a **customer churn prediction model**
* Focus deeply on **Cross-Validation** to ensure the model is reliable and generalizable
* Explain **every step**, **why it is used**, and **how it helps in real life**

This project is ideal for **LinkedIn & GitHub**, showing strong fundamentals and industry-ready thinking.

---

## 🧠 Real-Life Business Problem

> Acquiring a new customer costs **5x more** than retaining an existing one.

**Goal:**
Predict whether a customer is likely to churn so the company can:

* Offer discounts
* Improve service
* Take preventive action

---

## 🗂 Dataset Description (Simulated Telecom Data)

| Feature           | Meaning                          |
| ----------------- | -------------------------------- |
| `tenure`          | Months customer stayed           |
| `monthly_charges` | Monthly bill amount              |
| `total_charges`   | Total amount paid                |
| `contract_type`   | Monthly / Yearly                 |
| `support_calls`   | Number of customer support calls |
| `churn`           | Target (1 = left, 0 = stayed)    |

---

## 🔹 Step 1: Import Required Libraries

```python
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
```

### Why?

* `pandas & numpy`: Data handling
* `Pipeline`: Prevents data leakage
* `StratifiedKFold`: Maintains class balance in CV
* `cross_val_score`: Performs cross-validation

---

## 🔹 Step 2: Create / Load Dataset

```python
np.random.seed(42)

n = 500

data = pd.DataFrame({
    'tenure': np.random.randint(1, 60, n),
    'monthly_charges': np.random.randint(300, 1500, n),
    'total_charges': np.random.randint(1000, 80000, n),
    'support_calls': np.random.randint(0, 10, n),
    'churn': np.random.choice([0, 1], size=n, p=[0.7, 0.3])
})

X = data.drop('churn', axis=1)
y = data['churn']
```

### Why?

* Mimics **real telecom churn data**
* Imbalanced classes reflect real business scenarios

---

## 🔹 Step 3: Train-Test Split (Baseline)

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
```

### Why?

* Keeps final unseen data for honest evaluation
* `stratify=y` preserves churn ratio

---

## 🔹 Step 4: Build a Pipeline

```python
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])
```

### Why Pipeline is CRITICAL?

* Scaling happens **inside each fold**
* Prevents **data leakage**
* Industry best practice

---

## 🔹 Step 5: Cross-Validation (CORE OF PROJECT)

```python
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

cv_scores = cross_val_score(
    pipeline,
    X_train,
    y_train,
    cv=cv,
    scoring='accuracy'
)

print("CV Accuracy per fold:", cv_scores)
print("Average CV Accuracy:", cv_scores.mean())
```

### What happens internally?

* Train on 4 folds, validate on 1 fold
* Repeat 5 times
* Average gives **stable performance estimate**

---

## 🔹 Step 6: Train Final Model & Evaluate

```python
pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)

print("Test Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

### Why this step?

* CV selects reliable model
* Test set confirms **real-world performance**

---

## 📊 Key Insights

* Cross-validation prevents overconfidence
* Stratified CV handles class imbalance
* Pipeline ensures clean ML workflow
* Model generalizes well to unseen customers

---

## 🧩 Why Cross-Validation Matters in Business

| Without CV       | With CV               |
| ---------------- | --------------------- |
| Lucky results    | Stable results        |
| Overfitting risk | Reduced risk          |
| Poor decisions   | Data-driven decisions |

---

## 🛠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Logistic Regression
* Cross-Validation (StratifiedKFold)

---

## 👤 Author

**Manan Chawla**
FOUNDER @BYTEEDU | COLUMBIA UNIVERSITY 

⭐ If you like this project, don’t forget to star the repo and connect on LinkedIn
