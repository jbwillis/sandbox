#! /usr/bin/env python3

""" argparseTest.py
    program for learning how to take advantage of argparse for
    argument parsing

    I referenced the python3 argparse tutorial on the python docs
    to learn how to do this. 
"""


import argparse

parser = argparse.ArgumentParser(description='A program for testing argument parsing')


parser.add_argument('--video', help='enable writing a video to file')


parser.parse_args()
