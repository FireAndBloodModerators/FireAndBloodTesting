# IMPORTS
import math
import pandas as pd
from LandCombatLargeBattlesTestForce2 import Force
from LandCombatLargeBattlesTestBattle2 import Battle

TestList = []

TestList.append([1,2])
TestList.append([3,4])
TestList.append([5,6])

exists = False
for Sample in TestList:
    if 3 in Sample:
        exists = True
        break

print(exists)