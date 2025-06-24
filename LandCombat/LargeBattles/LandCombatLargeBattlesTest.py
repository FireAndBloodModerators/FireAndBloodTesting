# IMPORTS
import math
import pandas as pd
from LandCombatLargeBattlesTestForce import Force
from LandCombatLargeBattlesTestBattle import Battle

# TEST
## Create list of levy numbers for testing use
LevyNumbers = [100,200,300,400,500,600,700]

## Create column labels for later use
ColumnLabels = [f"{math.floor(LevyNumber/3)} CV Left // {math.floor(LevyNumber/3) + (LevyNumber % 3)} CV Centre // {math.floor(LevyNumber/3)} CV Right" for LevyNumber in LevyNumbers]
ColumnLabels.insert(0,"")

## Set number of simulations
SimulationCount = 100

## Initialise results list
WinPercentageResults = []
CasualtyResults = []

Force1 = Force(0,200)
Force2 = Force(0,100)

TestBattle = Battle(Force1,Force2)

WinCount1 = 0
WinCount2 = 0
ErrorCount = 0

SimRange = 100000

for x in range(SimRange):
    result = TestBattle.battle()
    print(result)
    if(result == 1):
        WinCount1 += 1
    elif(result == 2):
        WinCount2 += 1
    else:
        ErrorCount += 1

print(f"Force 1 Win %: {round((WinCount1/SimRange)*100,2)}%")
print(f"Force 2 Win %: {round((WinCount2/SimRange)*100,2)}%")
print(f"Errors %: {round((ErrorCount/SimRange)*100,2)}%")

# ## Iterate through the LevyNumbers list to create 2 forces and simulate battle between them
# for LevyNumber1 in LevyNumbers:
#     ### Create Force 1
#     Force1 = Force(0,LevyNumber1)

#     ### Initialise new results lists
#     NewWinPercentageResults = [f"{math.floor(LevyNumber1/3)} CV Left // {math.floor(LevyNumber1/3) + (LevyNumber1 % 3)} CV Centre // {math.floor(LevyNumber1/3)} CV Right"]
#     NewCasualtyPercentageResults = [f"{math.floor(LevyNumber1/3)} CV Left // {math.floor(LevyNumber1/3) + (LevyNumber1 % 3)} CV Centre // {math.floor(LevyNumber1/3)} CV Right"]

#     for LevyNumber2 in LevyNumbers:
#         #### Create Force 2
#         Force2 = Force(0,LevyNumber2)

#         #### Create variables to track wins and casualties
#         Force1Wins = 0
#         Force1LeftFlankCasualties = 0
#         Force1CentreFlankCasualties = 0
#         Force1RightFlankCasualties = 0
#         Force2Wins = 0
#         Force2LeftFlankCasualties = 0
#         Force2CentreFlankCasualties = 0
#         Force2RightFlankCasualties = 0

#         #### Create battle between Force 1 and 2
#         TestBattle = Battle(Force1,Force2)

#         #### Run sims X times
#         for x in range(SimulationCount):
#             ##### Run battle between Force 1 and 2
#             BattleResult = TestBattle.battle()

#             ##### Increment win count of winner of the battle
#             if(BattleResult == 1):
#                 Force1Wins += 1
#             elif(BattleResult == 2):
#                 Force2Wins += 1
#             else:
#                 pass

#             ##### Increment casualty count of both sides
#             Force1LeftFlankCasualties += Force1.LeftFlank.Casualties
#             Force1CentreFlankCasualties += Force1.CentreFlank.Casualties
#             Force1RightFlankCasualties += Force1.RightFlank.Casualties
#             Force2LeftFlankCasualties += Force2.LeftFlank.Casualties
#             Force2CentreFlankCasualties += Force2.CentreFlank.Casualties
#             Force2RightFlankCasualties += Force2.RightFlank.Casualties

#         ##### Calculate win percentage and average casualties of each force
#         Force1WinPercentage = round((Force1Wins/SimulationCount)*100,2)
#         Force1LeftFlankAverageCasualties = round(Force1LeftFlankCasualties/SimulationCount)
#         Force1CentreFlankAverageCasualties = round(Force1CentreFlankCasualties/SimulationCount)
#         Force1RightFlankAverageCasualties = round(Force1RightFlankCasualties/SimulationCount)
#         Force2WinPercentage = round((Force2Wins/SimulationCount)*100,2)
#         Force2LeftFlankAverageCasualties = round(Force2LeftFlankCasualties/SimulationCount)
#         Force2CentreFlankAverageCasualties = round(Force2CentreFlankCasualties/SimulationCount)
#         Force2RightFlankAverageCasualties = round(Force2RightFlankCasualties/SimulationCount)

#         ##### Save results to New Results lists
#         NewWinPercentageResults.append(f"{Force1WinPercentage}% Winrate")
#         NewCasualtyPercentageResults.append(f"{Force1LeftFlankAverageCasualties}% Left Casualties // {Force1CentreFlankAverageCasualties}% Centre Casualties // {Force1RightFlankAverageCasualties}% Right Casualties")

#     ### Save New Results lists to Results list
#     WinPercentageResults.append(NewWinPercentageResults)
#     CasualtyResults.append(NewCasualtyPercentageResults)

#     ### Checkpoint
#     print(f"{math.floor(LevyNumber1/3)} CV Left // {math.floor(LevyNumber1/3) + (LevyNumber1 % 3)} CV Centre // {math.floor(LevyNumber1/3)} CV Right simulations complete")

# ## Save results to dataframe
# WinPercentageDataFrame = pd.DataFrame(WinPercentageResults,columns=ColumnLabels)
# CasualtyDataFrame = pd.DataFrame(CasualtyResults,columns=ColumnLabels)

# ### Save dataframes to csv file
# WinPercentageDataFrame.to_csv("LandCombat/LargeBattles/land_combat_large_battle_win_percentages.csv",index=False)
# CasualtyDataFrame.to_csv("LandCombat/LargeBattles/land_combat_small_large_casualties.csv",index=False)