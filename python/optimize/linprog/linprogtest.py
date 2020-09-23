import numpy as np
from scipy.optimize import linprog

# inner product with x for objective
c = np.array([1., 2., 3., 4.])

# Inequality constraints
A_ub = None
b_ub = None

# Equality constraints
A_eq = np.array([[1., 1., 0., 0.],[0., 1., 1., 1.]])
b_eq = np.array([[1., 5.]])

# Design variable bounds
bounds = (0., 5.) # could also be an array

# initial guess
x_guess = np.ones(4)

res = linprog(c, A_eq = A_eq, b_eq = b_eq, bounds = bounds, method = 'interior-point')

print(res)
