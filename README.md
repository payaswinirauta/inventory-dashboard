#  Inventory Insights Dashboard

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Pandas](https://img.shields.io/badge/Library-pandas-green)
![Matplotlib](https://img.shields.io/badge/Charting-matplotlib-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A mini data engineering project that reads inventory data from a CSV file, analyzes category-wise stock levels, detects low-stock products, highlights upcoming restocks, and visualizes trends through a bar chart using Python, Pandas, and Matplotlib.

---

##  Project Overview

- Load and parse structured inventory data (CSV)
- Perform category-wise stock aggregation
- Identify low-stock items (Quantity < 10)
- Predict upcoming restocks (within 7 days)
- Generate a visual summary using bar charts

This project is ideal for supply chain analytics, automated reporting, and business intelligence workflows.

---

## 🛠️ Technologies Used

- Python 3.10+
- Pandas
- Matplotlib
- CSV file handling
- IDE: PyCharm / VS Code

---

## 📁 Project Structure
```
inventory_dashboard_project/
│
├── inventory.csv # Sample inventory dataset
├── main.py # Inventory analytics script
├── inventory_chart.png # Auto-generated bar chart
└── README.md # Project documentation


---
```
## 📊 Sample Output

```plaintext
Total stock by category:
Category
Electronics    22
Fashion        15
Grocery        27

Low stock products:
ProductID     Category  Quantity RestockDate
101        Electronics         5  2025-08-10
104        Electronics         2  2025-08-06
...

Upcoming Restocks in next 7 days:
ProductID     Category  Quantity RestockDate
101        Electronics         5  2025-08-10
...
Bar chart saved automatically as inventory_chart.png.

---
 ```
## How to Run

# Step 1: Clone the repo
git clone git@github.com:payaswinirauta/inventory-dashboard.git
cd inventory-dashboard

# Step 2: Install dependencies
pip install pandas matplotlib

# Step 3: Run the project
python main.py

---
```
💼 Use Case Fit
Inventory Optimization

Demand Forecasting

Supply Chain Analytics

Automated Dashboards

Data Engineering Practice

✨ Future Enhancements
Export reports to Excel/PDF

Live database connectivity

API integration with FastAPI or Flask

Interactive visualizations using Plotly

👩‍💻 Author
Payaswini Rauta
GitHub Profile

📄 License
Licensed under the MIT License.










