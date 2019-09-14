#! /usr/bin/env python3
"""
    tutorial from Small Unmanned Aircraft Supplement
"""
import numpy as np
from scipy.optimize import minimize

# objective function to be minimized
def objective(x, gam):
    J = np.dot(x.T, x) - gam
    return J

# initial guess for the optimum
x0 = np.array([[10, 5, -20, 8]]).T
gam = 3 # parameter passed into objective function

#### Constraints
# first constraint is equality constraint x1 == x2
# second constraint is inequality constraint sin(x3) <= -.5
cons = ({'type': 'eq', 'fun': lambda x: x[0] - x[1],},
        {'type': 'ineq', 'fun': lambda x: np.sin(x[2]) + 0.5})

# solve the minimization problem
res = minimize(objective, 
        x0,
        method='SLSQP',
        args=(gam),
        constraints = cons,
        options = {'ftol': 1e-10, 'disp': True})

xopt = np.array([res.x]).T
print(xopt)

