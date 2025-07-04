# Fair Resource Allocation with CVXPY

This project provides a Python-based tool to perform **egalitarian allocation** of resources among multiple individuals based on their personal valuations. The approach ensures fairness by maximizing the **minimum utility** any individual receives. It utilizes convex optimization via the `cvxpy` library and produces clear output tables showing the final distribution.

---

## 📁 File Description

- `question_3.py`  
  The core script that defines the allocation algorithm and demonstrates it on various valuation matrices. The script includes:
  - A function that calculates fair (egalitarian) allocations.
  - Several predefined examples illustrating the algorithm's behavior.
  - Structured result printing using tables.

---

## 🛠 Requirements

To run the project, ensure you have the following installed:

- Python 3.x → [Download](https://www.python.org/)
- NumPy → `pip install numpy`
- CVXPY → `pip install cvxpy`
- Tabulate → `pip install tabulate`

---

## ▶️ Running the Script

Navigate to the folder where the file is located and run it via terminal or command prompt:

python question_3.py

✅ What the Script Does :
Given a matrix where each row represents a person and each column represents a resource, with values indicating how much each person values each resource — the algorithm:

-Defines allocation variables for how much of each resource each person receives.
-Computes each person’s total utility based on their allocation.
-Sets up constraints:
-Every resource must be 100% allocated.
-Each person must receive at least the minimum utility value.
-Maximizes that minimum utility, ensuring the fairest possible distribution.
-Outputs results in a well-formatted table.

## Get Started 
Clone this repo or copy the script into your own environment, install the required packages, and run the code to see egalitarian fairness in action.
