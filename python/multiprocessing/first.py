"""
Simple example of running multiple threads with python
"""

import multiprocessing
from string import ascii_lowercase

def count_to_nxn(n):
    for i in range(n):
        print("Try ", i)
        for j in range(n):
            print("Count ", j)
            # do something to slow it down
            for k in range(n*n):
                l = k+n


def recite_abcs_nx(n):
    for i in range(n):
        print("ABCs {} more times!".format(n-i))
        for l in ascii_lowercase:
            print("Letter ", l)

if __name__ == "__main__":
    
    # create processes
    n = 10
    p1 = multiprocessing.Process(target=count_to_nxn, args=(n,))
    p2 = multiprocessing.Process(target=recite_abcs_nx, args=(n,))

    # start the processes
    print("Starting Process 1")
    p1.start()
    print("Starting Process 2")
    p2.start()

    print("Joining Process 1")
    p1.join()
    print("Joining Process 2")
    p2.join()

    print("Done!")
