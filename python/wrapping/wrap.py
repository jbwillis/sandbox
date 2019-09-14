#! /usr/bin/env python3

import numpy as np

def wrap(chi_c, chi):
    """ RRT class function that wraps an angle

    Parameters
    ----------
    chi_c : double
        Angle that will be wrapped

    chi : double
        Reference angle

    Returns
    -------
    chi_c : double
        Returns the wrapped angle
    """
    while chi_c-chi > np.pi:
        chi_c = chi_c - 2.0 * np.pi
    while chi_c-chi < -np.pi:
        chi_c = chi_c + 2.0 * np.pi
    return chi_c - chi


def wrapToPi(x):
    wrap = np.mod(x, 2*np.pi)
    if np.abs(wrap) > np.pi:
        wrap -= 2*np.pi*np.sign(wrap)
    return wrap

def wrapAminusBToPi(A, B):
    diff_wrap = wrapToPi(A - B)
    return diff_wrap


A = 0.0
for B in np.linspace (-2*np.pi, 2*np.pi, 10):
    print("{} - {}".format(A, B))
    print("wrap = ", wrap(A, B))
    print("wrapAminusB = ", wrapAminusBToPi(A, B))

