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
parser.add_argument('-p', '--plot', help='plot the final paths', action='store_true')
parser.add_argument('-n', '--number', help='An integer, default = 1', default=1, type=int)
parser.add_argument('-s', '--string', help='A string, default = Hello', type=str)

args = parser.parse_args()

if args.number is not None:
    print("Number = {}".format(args.number))
if args.string is not None:
    print("String = {}".format(args.string))
