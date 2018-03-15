#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
usage:
cat tests/test_basic.txt | python3 run.py
'''

import sys
import re

sys.path.append('..')
import semver

# from ..run import *  # Failing to import run.py from root dir; temporarily including copy
from __run_copy import *


def run_tests():
    assert is_empty("")
    assert is_empty(" \t \t  \n")
    assert not is_empty(" d ")

    assert is_valid_input("1.3.6 1.4.2")
    assert not is_valid_input(" 1.3.6 1.4.2")
    assert not is_valid_input("1.7.9 1.3.5 0.0.2")

    print("Success")

    # 1.3.6 1.4.2
    # 1.7.9 1.3.5 0.0.2
    # 4.2.3 - beta    4.2.3 - alpha
    # 1.6 1.6.3


if __name__ == '__main__':
    run_tests()
