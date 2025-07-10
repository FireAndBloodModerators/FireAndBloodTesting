# IMPORTS
import pandas as pd
from DuelsTestDuellist import Duellist

## SET SIMULATIONS COUNT
SimulationCount = 10000

# WEAPON TEST
print("Weapon Sims Start")
## Create list of weapon types for testing use
WeaponTypes = ["None","FO","MW","MW/FO","VS"]

## Create column labels for later use
WeaponTypesLabels = [f"Duellist w/ {WeaponType}" for WeaponType in WeaponTypes]
WeaponTypesLabels.insert(0,"")

## Initialise results list
WeaponTypesWinPercentageResults = []
WeaponTypeDeathsResults = []
WeaponTypeCriticalInjuriesResults = []
WeaponTypeMajorInjuriesResults = []
WeaponTypeMinorInjuriesResults = []

## Iterate through the WeaponTypes list to create 2 Duellists and simulate a Duel between them
for WeaponType1 in WeaponTypes:

    #### Create Duellist 1
    Duellist1 = Duellist(WeaponType1)

    #### Initialise new results lists
    NewWinResults = [f"Duellist w/ {WeaponType1}"]
    NewDeathsResults = [f"Duellist w/ {WeaponType1}"]
    NewCriticalInjuriesResults = [f"Duellist w/ {WeaponType1}"]
    NewMajorInjuriesResults = [f"Duellist w/ {WeaponType1}"]
    NewMinorInjuriesResults = [f"Duellist w/ {WeaponType1}"]

    for WeaponType2 in WeaponTypes:

        #### Create Duellist 2
        Duellist2 = Duellist(WeaponType2)

        ##### Create variables to track wins and casualties
        Duellist1Wins = 0
        Duellist1Deaths = 0
        Duellist1CriticalInjuries = 0
        Duellist1MajorInjuries = 0
        Duellist1MinorInjuries = 0
        Duellist2Wins = 0
        Duellist2Deaths = 0
        Duellist2CriticalInjuries = 0
        Duellist2MajorInjuries = 0
        Duellist2MinorInjuries = 0