# IMPORTS
import math
import pandas as pd
from LandCombatLargeBattlesTestForce2 import Force
from LandCombatLargeBattlesTestBattle2 import Battle

# TEST
## Create list of levy numbers for testing use
LevyNumbers = [1500,10500]

## Create column labels for later use
ColumnLabels = [f"{math.floor(LevyNumber/3)} CV Left // {math.floor(LevyNumber/3) + (LevyNumber % 3)} CV Centre // {math.floor(LevyNumber/3)} CV Right" for LevyNumber in LevyNumbers]
ColumnLabels.insert(0,"")

## Set number of simulations
SimulationCount = 1000

## Initialise results list
WinPercentageResults = []
CasualtyResults = []

Force1 = Force(0,1500)
Force2 = Force(0,3200)

TestBattle = Battle(Force1,Force2)

WinCount1 = 0
WinCount2 = 0
ErrorCount = 0

for x in range(SimulationCount):
    result = TestBattle.battle()
    if(result == 1):
        WinCount1 += 1
    elif(result == 2):
        WinCount2 += 1
    else:
        ErrorCount += 1

print(f"Force 1 Win %: {round((WinCount1/SimulationCount)*100,2)}%")
print(f"Force 2 Win %: {round((WinCount2/SimulationCount)*100,2)}%")
print(f"Errors %: {round((ErrorCount/SimulationCount)*100,2)}%")