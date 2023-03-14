# Approach 1
from IPL import venue

venue.printStadium()
venue.printVenue()

# Approach 2
from IPL.venue import printStadium

printStadium()

# ----------------------------------------------------------
# Approach 1
from IPL.KKR import venue

venue.printStadium()
venue.printVenue()

# Approach 2
from IPL.KKR.venue import printStadium

printStadium()

# ----------------------------------------------------------
# Alias
from IPL2020 import venue
from IPL2020.RCB import venue as RCBModule
from IPL2020.KKR import venue as KKRModule

venue.printStadium()
venue.printVenue()

RCBModule.printStadium()
RCBModule.printVenue()

# Approach 2
from IPL2020.venue import printStadium as ds
from IPL2020.KKR.venue import printStadium as kkrs
from IPL2020.RCB.venue import printStadium as rcbs

ds()
kkrs()
rcbs()

# ----------------------------------------------------------

import math

print(math.factorial(5))

# ----------------------------------------------------------

from math import factorial

print(factorial(10))

# Recommended Approach
# Performance wise, there is no change
# Only loading time would improve
# Execution time remains same across both the approaches.

# ----------------------------------------------------------
# Approach 1

import MyMathUtility
MyMathUtility.printRomanValue(2)

# Approach 2
from MyMathUtility import printRomanValue

printRomanValue(5)
