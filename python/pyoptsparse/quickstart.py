#! /usr/bin/env python3

"""
pyOptSparse Quickstart
From: https://mdolab-pyoptsparse.readthedocs-hosted.com/en/latest/quickstart.html
"""

from pyoptsparse import Optimization, OPT

def objconfunc(xdict):
    x = xdict["xvars"]
    funcs = {}
    funcs["obj"] = -x[0] * x[1] * x[2]
    convec = [0]*2
    convec[0] = x[0] + 2.0 * x[1] + 2.0 * x[2] - 72.0
    convec[1] = -x[0] - 2.0 * x[1] - 2.0 * x[2]
    funcs["con"] = convec
    fail = False

    return funcs, fail

optProb = Optimization("Quickstart - TP037 Constraint Problem", objconfunc)

optProb.addVarGroup("xvars", 3, "c", lower =[0, 0, 0], upper=[42, 42, 42], value=10)

optProb.addConGroup("con", 2, lower=None, upper=0.0)

optProb.addObj("obj")

print(optProb)

optOptions = {"iPrint": -1}
opt = OPT("SNOPT", options=optOptions)

sol = opt(optProb, sens="FD")

print(sol)
