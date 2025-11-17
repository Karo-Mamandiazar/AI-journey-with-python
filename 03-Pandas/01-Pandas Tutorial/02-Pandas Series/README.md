---

📄 README.md

# Pandas Series & DataFrame Introduction

This project is a beginner-friendly introduction to Pandas Series, two of the most fundamental data structures in the Pandas library.


---

## 📌 What is a Pandas Series?

- A Pandas Series is like a column in a table.
- It is a one-dimensional array holding data of any type.
- Each value in a Series has an index label (default: 0, 1, 2 …).
- You can also create custom labels for easier access.

### Example:
```python
import pandas as pd

a = [1, 7, 2]
my_var = pd.Series(a)
print(my_var)


---

📌 Labels in Series

• By default, Pandas assigns numeric indexes.
• You can access values using these indexes or create your own labels.


Example with custom labels:

a = [1, 7, 2]
my_var = pd.Series(a, index=["x", "y", "z"])
print(my_var["y"])  # Access by label


---

📌 Series from Dictionary

• You can create a Series directly from a dictionary.
• Keys become labels, and values become data.


calories = {"day1": 420, "day2": 380, "day3": 390}
my_var = pd.Series(calories)
print(my_var)


• You can also select specific keys using the index argument.


---

🚀 How to Run

1. Install Python (>=3.8).
2. Install Pandas:pip install pandas
3. Run the script:python pandas_series_intro.py


---

🎯 Project Goal

This project demonstrates the basics of Pandas Series.
It is designed for beginners in Python and Data Science to understand how data is stored, labeled, and manipulated using Pandas.


---
