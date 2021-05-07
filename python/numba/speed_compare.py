#! /usr/bin/env python3

from numba import jit
import numpy as np
import time

@jit
def take_svd_jit(A):
    return np.linalg.svd(A)

def take_svd(A):
    return np.linalg.svd(A)

@jit
def mult_svd_jit(U, S, V):
    return U @ S @ V

def mult_svd(U, S, V):
    return U @ S @ V

def svd_speed_test(n, rows=100, cols=100):
    """ Run a speed  test and average over n times"""

    # cause the jit functions to compile
    Arand = np.random.rand(rows, cols)
    start = time.time()
    U, S, V = take_svd_jit(Arand)
    print(f"SVD with JIT compile:\t\t{time.time()-start}s")
    start = time.time()
    mult_svd_jit(U, S, V)
    print(f"SVD with JIT compile:\t\t{time.time()-start}s")
    
    jit_time_acc = [0., 0.]
    no_time_acc = [0., 0.]

    for i in range(n):
        Arand = np.random.rand(rows, cols)

        start = time.time()
        U, S, V = take_svd_jit(Arand)
        jit_time_acc[0] += (time.time() - start)

        start = time.time()
        mult_svd_jit(U, S, V)
        jit_time_acc[1] += (time.time() - start)

        start = time.time()
        U, S, V = take_svd(Arand)
        no_time_acc[0] += (time.time() - start)

        start = time.time()
        mult_svd_jit(U, S, V)
        no_time_acc[1] += (time.time() - start)

    
    print("SVD with JIT run:\t\t", jit_time_acc[0]/n)
    print("SVD no JIT run:\t\t", no_time_acc[0]/n)

    print("Mult with JIT run:\t\t", jit_time_acc[1]/n)
    print("Mult no JIT run:\t\t", no_time_acc[1]/n)


@jit
def element_mult_jit(A, B):
    # C = A * B
    C = np.empty(A.shape)
    for rr in range(A.shape[0]):
        for cc in range(A.shape[1]):
            C[rr,cc] = A[rr,cc] * B[rr,cc]
    return C

def element_mult(A, B):
    # C = A * B
    C = np.empty(A.shape)
    for rr in range(A.shape[0]):
        for cc in range(A.shape[1]):
            C[rr,cc] = A[rr,cc] * B[rr,cc]
    return C

def element_mult_vectorized(A, B):
    C = A * B
    return C

def element_mult_speed_test(n, rows=100, cols=100):
    """ Run a speed  test and average over n times"""

    # cause the jit functions to compile
    Arand = np.random.rand(rows, cols)
    Brand = np.random.rand(rows, cols)
    start = time.time()
    element_mult_jit(Arand, Brand)
    print(f"Elementwise multiplication with JIT compile:\t\t{time.time()-start}s")
    
    jit_time_acc = 0.
    no_time_acc = 0.
    vec_time_acc = 0.

    for i in range(n):
        Arand = np.random.rand(rows, cols)
        Brand = np.random.rand(rows, cols)

        start = time.time()
        element_mult_jit(Arand, Brand)
        jit_time_acc += (time.time() - start)

        start = time.time()
        element_mult(Arand, Brand)
        no_time_acc += (time.time() - start)

        start = time.time()
        element_mult_vectorized(Arand, Brand)
        vec_time_acc += (time.time() - start)

    print(f"Elementwise multiplication with JIT:\t\t{jit_time_acc/n}s")
    print(f"Elementwise multiplication no JIT:\t\t{no_time_acc/n}s")
    print(f"Elementwise multiplication vectorized:\t\t{vec_time_acc/n}s")


# >>> element_mult_speed_test(100)
"""
Elementwise multiplication with JIT compile:            0.27278709411621094s
Elementwise multiplication with JIT:            5.1927566528320315e-06s
Elementwise multiplication no JIT:              0.003930997848510742s
Elementwise multiplication vectorized:          5.450248718261719e-06s
"""


# >>> svd_speed_test(100)
"""
SVD with JIT compile:           0.5769429206848145s
SVD with JIT compile:           0.3145029544830322s
SVD with JIT run:                0.004079935550689698
SVD no JIT run:          0.004191477298736573
Mult with JIT run:               2.0720958709716796e-05
Mult no JIT run:                 0.003554067611694336
"""
