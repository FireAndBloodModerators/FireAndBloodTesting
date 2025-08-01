# IMPORTS
import pandas as pd
from DuelsTestDuellist import Duellist
from DuelsTestDuel import Duel

## SET SIMULATIONS COUNT
SimulationCount = 10000

# WEAPON TEST
print("Weapon Types Sims Start")
## Create list of weapon types for testing use
WeaponTypes = ["None","FO","MW","MW/FO","VS"]

## Create column labels for later use
WeaponTypesLabels = [f"Duellist w/ {WeaponType}" for WeaponType in WeaponTypes]
WeaponTypesLabels.insert(0,"")

## Initialise results list
WeaponTypesWinPercentageResults = []
WeaponTypesInjuriesResults = []

## Iterate through the WeaponTypes list to create 2 Duellists and simulate a Duel between them
for WeaponType1 in WeaponTypes:

    #### Create Duellist 1
    Duellist1 = Duellist(WeaponType1)

    #### Initialise new results lists
    NewWinResults = [f"Duellist w/ {WeaponType1}"]
    NewInjuriesResults = [f"Duellist w/ {WeaponType1}"]

    for WeaponType2 in WeaponTypes:

        #### Create Duellist 2
        Duellist2 = Duellist(WeaponType2)

        ##### Create variables to track wins and casualties
        Duellist1Wins = 0
        Duellist1Deaths = 0
        Duellist1CriticalInjuries = 0
        Duellist1MajorInjuries = 0
        Duellist1MinorInjuries = 0

        ##### Create Duel  between Duellist 1 and 2
        TestDuel = Duel(Duellist1,Duellist2)

        ##### Run sims
        for x in range(SimulationCount):
            ###### Run Duel between Duellist 1 and 2
            DuelResult = TestDuel.duel()

            ###### Increment win count of winner of the Duel
            if(DuelResult == 1):
                Duellist1Wins += 1
            else:
                pass

            ###### Increment Duellist 1 trackers
            Duellist1Deaths += Duellist1.Deaths
            Duellist1CriticalInjuries += Duellist1.CriticalInjuries
            Duellist1MajorInjuries += Duellist1.MajorInjuries
            Duellist1MinorInjuries += Duellist1.MinorInjuries

        ##### Calculate win percentage and statistics for Duellist 1
        Duellist1WinResults = round((Duellist1Wins/SimulationCount)*100,2)
        Duellist1DeathResults = round((Duellist1Deaths/SimulationCount),2)
        Duellist1CriticalInjuryResults = round((Duellist1CriticalInjuries/SimulationCount),2)
        Duellist1MajorInjuryResults = round((Duellist1MajorInjuries/SimulationCount),2)
        Duellist1MinorInjuryResults = round((Duellist1MinorInjuries/SimulationCount),2)

        ##### Save statistics to new results lists
        NewWinResults.append(f"{Duellist1WinResults}% Winrate")
        NewInjuriesResults.append([f"{Duellist1DeathResults} Average Deaths",f"{Duellist1CriticalInjuryResults} Average Critical Injuries",f"{Duellist1MajorInjuryResults} Average Major Injuries",f"{Duellist1MinorInjuryResults} Average Minor Injuries"])

    #### Save New Results lists to Results list
    WeaponTypesWinPercentageResults.append(NewWinResults)
    WeaponTypesInjuriesResults.append(NewInjuriesResults)

    #### Checkpoint
    print(f"Duellist w/ {WeaponType1} simulations complete")

## Save Weapon Type results to dataframe
WeaponTypeWinPercentageDataFrame = pd.DataFrame(WeaponTypesWinPercentageResults,columns=WeaponTypesLabels)
WeaponTypeInjuriesDataFrame = pd.DataFrame(WeaponTypesInjuriesResults,columns=WeaponTypesLabels)

## Save Weapon Types dataframes to csv file
WeaponTypeWinPercentageDataFrame.to_csv("Duels/V2/duels_weapon_types_win_percentages.csv",index=False)
WeaponTypeInjuriesDataFrame.to_csv("Duels/V2/duels_weapon_types_injuries.csv",index=False)
print("Weapon Types Sims End")