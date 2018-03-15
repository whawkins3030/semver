# SemVer - simple Semantic Versioning parsing suite

In this directory you'll see the work in progress for a module that supports [Semantic Versioning](https://semver.org/).

Requirements: Python 3.5+

Contents:
* ```semver``` is the start of a Python module that supports a SemVer class with >, <, and = comparison operators. Examples below
* ```tests``` contains a few test cases (WIP)
* ```run.py``` can be used as an executable to handle stdin testing as specified in semver.pdf.

Basic command line usage:
* ```run.py``` Use ```make init``` to make ```run.py``` an executable that you can call like so:

* Invoke tests with ```make test_basic```
*


```semver``` examples with Python3:

```
>>>import semver
>>>sv = semver.SemVer("1.3.6")
```
