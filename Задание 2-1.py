from scipy.optimize import linprog
import numpy as np

# Coefficients for the objective function (profit)
c = np.array([-16, -19])  # Negative values since we are maximizing

# Coefficients for the inequality constraints (material usage constraints for product type A)
A_A = np.array([[19, 16]])
b_A = np.array([1121])

# Coefficients for the inequality constraints (material usage constraints for product type B)
A_B = np.array([[31, 9]])
b_B = np.array([706])

# Bounds on the amount of material that can be used
bounds = [(0, 1066), (0, 1066)]

result_A = linprog(c, A_ub=A_A.T, b_ub=b_A, bounds=bounds)
result_B = linprog(c, A_ub=A_B.T, b_ub=b_B, bounds=bounds)

max_profit = -result_A.fun - result_B.fun
print(f'Maximum profit: {max_profit} rubles')
print(f'Amount of Product A: {result_A.x[0]}, Product B: {result_B.x[0]}')