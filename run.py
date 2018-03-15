#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
usage:
cat tests/test_basic.txt | python3 run.py
'''

import sys
import re

import semver

# Possible bug: \s contains \n --> [ \t\n\r\f\v]
line_re = re.compile('^([^\s]+)([\s]*)([^\s]+)([\s]*)$')


# First pass test for line validity
def is_valid_input(line):
    match = line_re.match(line)
    return bool(match)


def is_empty(line):
    if line.strip() == "":
        return True
    else:
        return False


def createSemVers(line):
    match = line_re.match(line)
    left_str = match.groups()[0]
    right_str = match.groups()[2]

    leftSV = semver.SemVer(left_str)
    rightSV = semver.SemVer(right_str)

    return leftSV, rightSV


def process(line):
    if is_empty(line):
        return  # ignore case

    if not is_valid_input(line):
        print("invalid")  # invalid case (first pass)
        return

    leftSV, rightSV = createSemVers(line)

    try:
        leftSV, rightSV = createSemVers(line)
    except:
        print("invalid")  # invalid case (improper syntax)
        return

    if leftSV < rightSV:
        print("before")
    elif leftSV > rightSV:
        print("after")
    else:
        print("equal")


if __name__ == '__main__':
    for line in sys.stdin.readlines():
        process(line)
