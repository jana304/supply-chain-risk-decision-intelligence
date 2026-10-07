# Supply Chain Risk & Operations Decision Intelligence Platform

**Logistics Risk Analytics | Predictive Risk Modeling | Operational Intelligence | SQL | Power BI**

---

## 📌 Project Overview

The **Supply Chain Risk & Operations Decision Intelligence Platform** is an end-to-end analytics project focused on identifying delivery risks, evaluating logistics performance, measuring financial exposure, and supporting operational decision-making.

The project combines **Python, Machine Learning, SQL, and Power BI** to transform supply chain data into actionable business insights.

---

## 🎯 Business Objectives

* Identify high-risk shipping operations
* Analyze delivery and shipping performance
* Compare risk across shipping modes, regions, and markets
* Measure sales exposure associated with delivery risk
* Predict late-delivery risk using Machine Learning
* Identify high-impact operational areas
* Support management with data-driven recommendations

---

## 🛠️ Tools & Technologies

| Technology       | Purpose                           |
| ---------------- | --------------------------------- |
| Python           | Data analysis and automation      |
| Pandas           | Data cleaning and transformation  |
| NumPy            | Numerical analysis                |
| Matplotlib       | Exploratory visualization         |
| Scikit-Learn     | Machine Learning                  |
| MySQL            | Data storage and SQL analysis     |
| SQL              | Business and operational analysis |
| SQLAlchemy       | Database integration              |
| Power BI         | Interactive decision dashboard    |
| Jupyter Notebook | Data analysis                     |
| VS Code          | Development                       |
| Git & GitHub     | Version control                   |

---

## 📊 Dataset

The project uses the **DataCo SMART SUPPLY CHAIN FOR BIG DATA ANALYSIS** dataset.

### Dataset Scale

* **180,519 order items**
* **65,752 unique orders**
* Multi-year supply chain transaction data
* Order history spanning **2015–2018**

### Main Data Areas

* Orders and shipping
* Delivery status
* Products and categories
* Customers and segments
* Sales and profit
* Discounts
* Shipping modes
* Markets and regions
* Departments

### Machine Learning Target

**Late_delivery_risk**

* `1` = At Risk
* `0` = No Risk

---

## 🚚 Supply Chain Risk Analysis

The project analyzes delivery risk across multiple operational dimensions.

### Shipping Mode Risk

| Shipping Mode  | Late Delivery Risk |
| -------------- | -----------------: |
| First Class    |         **95.32%** |
| Second Class   |         **76.63%** |
| Same Day       |         **45.74%** |
| Standard Class |         **38.07%** |

### Financial Exposure

Orders carrying late-delivery risk are associated with approximately **$20.13M in sales exposure**, representing approximately **54.71% of total sales**.

> Financial exposure represents sales associated with orders labeled as at risk; it does not imply that delivery risk caused the sales amount.

### Operational Analysis

The project evaluates:

* Shipping mode performance
* Regional delivery risk
* Market-level risk
* Scheduled vs. actual shipping time
* Shipping delays
* Sales exposure by risk status
* Operational risk priorities

---

## 🤖 Machine Learning

A **Random Forest Classifier** was developed to predict late-delivery risk using order, shipping, product, customer segment, market, and regional features.

Post-outcome variables such as **Delivery Status** and **actual shipping days** were excluded from the prediction features to reduce data leakage.

### Model Performance

| Metric    |     Result |
| --------- | ---------: |
| Accuracy  | **70.04%** |
| Precision | **83.87%** |
| Recall    | **56.16%** |
| F1 Score  | **67.28%** |
| ROC-AUC   | **0.7543** |

---

## 💡 Key Findings

* **First Class** has the highest observed late-delivery risk at **95.32%**.
* **Second Class** shows **76.63%** late-delivery risk.
* **Standard Class** has a lower risk rate but significant financial exposure due to its larger order volume.
* Approximately **54.83%** of order items carry a late-delivery risk label.
* Risk levels across regions are relatively close compared with the differences between shipping modes.
* Combining **risk rate, order volume, and financial exposure** provides a stronger basis for operational prioritization.

---

## 📁 Project Structure

```text
Supply-Chain-Risk-Decision-Intelligence/
│
├── data/
│
├── notebook/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_risk_prediction.ipynb
│   └── 05_load_to_mysql.ipynb
│
├── python/
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── risk_prediction.py
│   └── risk_report.py
│
├── sql/
│   └── 01_supply_chain_analysis.sql
│
├── power bi/
│   └── Dashboard.pbix
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🧠 Skills Demonstrated

* Supply Chain Analytics
* Logistics & Operations Analytics
* Data Cleaning
* Exploratory Data Analysis
* Feature Engineering
* Predictive Modeling
* Classification
* Data Leakage Prevention
* SQL Business Analysis
* MySQL
* Power BI Dashboard Development
* KPI Development
* Financial Exposure Analysis
* Risk Analysis
* Business Decision Support
* Data Storytelling

---

## 🎯 Business Recommendations

Based on the analysis:

1. Investigate the operational causes behind high-risk **First Class and Second Class** shipments.
2. Monitor shipping performance against scheduled expectations.
3. Prioritize operational areas using both **risk percentage and financial exposure**.
4. Closely monitor high-value orders carrying delivery risk.
5. Compare shipping performance across regions and markets.
6. Use predictive risk scores to support proactive operational monitoring.

---

## 👤 Author

**Jana M**

Computer Science Engineering Graduate
