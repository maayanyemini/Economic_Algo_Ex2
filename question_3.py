import cvxpy as cp
import numpy as np
from tabulate import tabulate

def compute_egalitarian_allocation(valuation_matrix):
    # Get the number of participants (rows) and number of items (columns)
    num_participants, num_items = valuation_matrix.shape

    # Decision variables:
    # alloc_matrix[i, j] represents how much of item j is given to participant i (0 ≤ alloc ≤ 1)
    alloc_matrix = cp.Variable((num_participants, num_items), nonneg=True)

    # Calculate each participant's utility: sum over all items of (fraction assigned * personal value)
    participant_utilities = []
    for i in range(num_participants):
        weighted_allocation = cp.multiply(alloc_matrix[i, :], valuation_matrix[i, :])
        utility_expr = cp.sum(weighted_allocation)
        participant_utilities.append(utility_expr)

    # Define a variable for the minimum utility across all participants
    min_utility_var = cp.Variable()

    # Build the constraints
    constraints = []

    # Each item must be fully allocated (sum of fractions per column = 1)
    for j in range(num_items):
        constraints.append(cp.sum(alloc_matrix[:, j]) == 1)

    # Each participant's utility must be at least the minimum utility variable
    for utility in participant_utilities:
        constraints.append(utility >= min_utility_var)

    # Define and solve the optimization problem (maximize fairness)
    objective = cp.Maximize(min_utility_var)
    problem = cp.Problem(objective, constraints)
    problem.solve()

    # Extract results
    allocation = alloc_matrix.value
    min_utility_value = min_utility_var.value

    # Prepare headers and rows
    headers = ["Participant"] + [f"Item {j+1}" for j in range(num_items)] + ["Total Utility"]
    rows = []
    for i in range(num_participants):
        row = [f"Participant {i+1}"]
        for j in range(num_items):
            row.append(f"{allocation[i, j]:.4f}")
        row.append(f"{participant_utilities[i].value:.4f}")
        rows.append(row)

    # Use tabulate with double grid
    result_table = tabulate(rows, headers=headers, tablefmt="double_grid")

    # Final result string
    result = f"Egalitarian allocation computed with minimum utility value: {min_utility_value:.8f}\n"
    result += "Allocation Table:\n" + result_table
    return result


if __name__ == "__main__":
    # Example from the question
    valuation1 = np.array([
        [81, 19, 1],
        [70, 1, 29]
    ])

    print("Evaluation Matrix 1-")
    print(valuation1)
    print("\n" + compute_egalitarian_allocation(valuation1))

    # Additional example
    valuation2 = np.array([
        [10, 20, 15],
        [20, 10, 15],
        [15, 20, 10],
        [5, 10, 25]
    ])

    print("\nEvaluation Matrix 2-")
    print(valuation2)
    print("\n" + compute_egalitarian_allocation(valuation2))

    valuation3 = np.array([
        [12, 15, 10],
        [9, 25, 20],
        [10, 10, 30]
    ])

    print("\nEvaluation Matrix 3-")
    print(valuation3)
    print("\n" + compute_egalitarian_allocation(valuation3))
