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

## Example Output

When executed, the script prints a valuation matrix followed by an allocation summary. 
Example:

Valuation Matrix #1:
[[81 19  1]
 [70  1 29]]

Egalitarian allocation computed with minimum utility value: 61.91390727
Allocation Table:

+---------+------------+------------+------------+---------------+
|  Agent  | Resource 1 | Resource 2 | Resource 3 | Total Utility |
+---------+------------+------------+------------+---------------+
| Agent 1 | 0.52980132 | 1.00000000 | 0.00000000 |  61.91390729  |
| Agent 2 | 0.47019868 | 0.00000000 | 1.00000000 |  61.91390728  |
+---------+------------+------------+------------+---------------+

Valuation Matrix #2:
[[10 20 15]
 [20 10 15]
 [15 20 10]
 [ 5 10 25]]

Egalitarian allocation computed with minimum utility value: 14.92537313
Allocation Table:

+---------+------------+------------+------------+---------------+
|  Agent  | Resource 1 | Resource 2 | Resource 3 | Total Utility |
+---------+------------+------------+------------+---------------+
| Agent 1 | 0.00000000 | 0.44402985 | 0.40298507 |  14.92537313  |
| Agent 2 | 0.74626866 | 0.00000000 | 0.00000000 |  14.92537313  |
| Agent 3 | 0.25373134 | 0.55597015 | 0.00000000 |  14.92537313  |
| Agent 4 | 0.00000000 | 0.00000000 | 0.59701493 |  14.92537313  |
+---------+------------+------------+------------+---------------+

Valuation Matrix #3:
[[12 15 10]
 [ 9 25 20]
 [10 10 30]]

Egalitarian allocation computed with minimum utility value: 19.50000000
Allocation Table:

+---------+------------+------------+------------+---------------+
|  Agent  | Resource 1 | Resource 2 | Resource 3 | Total Utility |
+---------+------------+------------+------------+---------------+
| Agent 1 | 1.00000000 | 0.50000000 | 0.00000000 |  19.50000000  |
| Agent 2 | 0.00000000 | 0.50000000 | 0.35000000 |  19.50000000  |
| Agent 3 | 0.00000000 | 0.00000000 | 0.65000000 |  19.50000000  |
+---------+------------+------------+------------+---------------+
## Get Started 🚀
Clone this repo or copy the script into your own environment, install the required packages, and run the code to see egalitarian fairness in action.

