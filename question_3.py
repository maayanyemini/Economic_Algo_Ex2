import cvxpy as cp
import numpy as np
from tabulate import tabulate

def compute_egalitarian_allocation(valuation_matrix):
    # Get the number of agents (rows) and number of resources (columns)
    num_agents, num_resources = valuation_matrix.shape

    # Decision variables:
    # alloc_matrix[i, j] represents how much of resource j is given to agent i (0 ≤ alloc ≤ 1)
    alloc_matrix = cp.Variable((num_agents, num_resources), nonneg=True)

    # Calculate each agent's utility: sum over all resources of (fraction assigned * personal value)
    agent_utilities = []
    for i in range(num_agents):
        weighted_allocation = cp.multiply(alloc_matrix[i, :], valuation_matrix[i, :])
        utility_expr = cp.sum(weighted_allocation)
        agent_utilities.append(utility_expr)

    # Define a variable for the minimum utility across all agents
    min_utility_var = cp.Variable()

    # Build the constraints
    constraints = []

    # Each resource must be fully allocated (sum of fractions per column = 1)
    for j in range(num_resources):
        constraints.append(cp.sum(alloc_matrix[:, j]) == 1)

    # Each agent's utility must be at least the minimum utility variable
    for utility in agent_utilities:
        constraints.append(utility >= min_utility_var)

    # Define and solve the optimization problem (maximize fairness)
    objective = cp.Maximize(min_utility_var)
    problem = cp.Problem(objective, constraints)
    problem.solve()

    # Extract results
    allocation = alloc_matrix.value
    min_utility_value = min_utility_var.value

    # Prepare the output table
    headers = ["Agent"] + [f"Resource {j+1}" for j in range(num_resources)] + ["Total Utility"]
    rows = []

    for i in range(num_agents):
        row = [f"Agent {i+1}"]
        for j in range(num_resources):
            row.append(f"{allocation[i, j]:.8f}")
        row.append(f"{agent_utilities[i].value:.8f}")
        rows.append(row)

    result_table = tabulate(rows, headers=headers, tablefmt="pretty")

    # Final formatted result
    result = f"Egalitarian allocation computed with minimum utility value: {min_utility_value:.8f}\n"
    result += "Allocation Table:\n" + result_table

    return result


if __name__ == "__main__":
    # Example from the question - keep unchanged
    valuation1 = np.array([
        [81, 19, 1],
        [70, 1, 29]
    ])

    print("Valuation Matrix #1:")
    print(valuation1)
    print("\n" + compute_egalitarian_allocation(valuation1))

    # Additional example
    valuation2 = np.array([
        [10, 20, 15],
        [20, 10, 15],
        [15, 20, 10],
        [5, 10, 25]
    ])

    print("\nValuation Matrix #2:")
    print(valuation2)
    print("\n" + compute_egalitarian_allocation(valuation2))

    valuation3 = np.array([
        [12, 15, 10],
        [9, 25, 20],
        [10, 10, 30]
    ])

    print("\nValuation Matrix #3:")
    print(valuation3)
    print("\n" + compute_egalitarian_allocation(valuation3))
