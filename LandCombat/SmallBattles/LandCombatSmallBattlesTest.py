# IMPORTS
import pandas as pd
from LandCombatSmallBattlesTestForce import Force
from LandCombatSmallBattlesTestBattle import Battle

# TEST
## Create list of levy numbers for testing use
LevyNumbers = [100,200,300,400,500,600,700]

## Create list of retreat thresholds for testing use
RetreatThresholds = [95,75,50,25,0]

## Create column labels for later use
ColumnLabels = [f"{LevyNumber} CV // {RetreatThreshold} RT" for LevyNumber in LevyNumbers for RetreatThreshold in RetreatThresholds]
ColumnLabels.insert(0,"")

## Set number of simulations
SimulationCount = 100000

## Initialise results list
WinPercentageResults = []
CasualtyResults = []

## Iterate through the LevyNumbers list to create 2 forces and simulate battle between them
for LevyNumber1 in LevyNumbers:

    for RetreatThreshold1 in RetreatThresholds:
        #### Create Force 1
        Force1 = Force(0,LevyNumber1,RetreatThreshold1)

        #### Initialise new results lists
        NewWinPercentageResults = [f"{LevyNumber1} CV // {RetreatThreshold1} RT"]
        NewCasualtyPercentageResults = [f"{LevyNumber1} CV // {RetreatThreshold1} RT"]

        for LevyNumber2 in LevyNumbers:

            for RetreatThreshold2 in RetreatThresholds:
                ##### Create Force 2
                Force2 = Force(0,LevyNumber2,RetreatThreshold2)

                ##### Create variables to track wins and casualties
                Force1Wins = 0
                Force1Casualties = 0
                Force2Wins = 0
                Force2Casualties = 0

                ##### Create battle between Force 1 and 2
                TestBattle = Battle(Force1,Force2)

                ##### Run sims 10,000 times
                for x in range(SimulationCount):
                    ###### Run battle between Force 1 and 2
                    BattleResult = TestBattle.battle()

                    ###### Increment win count of winner of the battle
                    if(BattleResult == 1):
                        Force1Wins += 1
                    elif(BattleResult == 2):
                        Force2Wins += 1
                    else:
                        pass

                    ###### Increment casualty count of both sides
                    Force1Casualties += Force1.Casualties
                    Force2Casualties += Force2.Casualties

                ##### Calculate win percentage and average casualties of each force
                Force1WinPercentage = round((Force1Wins/SimulationCount)*100,2)
                Force1AverageCasualties = round(Force1Casualties/SimulationCount)
                Force2WinPercentage = round((Force2Wins/SimulationCount)*100,2)
                Force2AverageCasualties = round(Force2Casualties/SimulationCount)

                ##### Save results to New Results lists
                NewWinPercentageResults.append(f"{Force1WinPercentage}% Winrate")
                NewCasualtyPercentageResults.append(f"{Force1AverageCasualties}% Casualties")
        
        #### Save New Results lists to Results list
        WinPercentageResults.append(NewWinPercentageResults)
        CasualtyResults.append(NewCasualtyPercentageResults)

        #### Checkpoint
        print(f"{LevyNumber1} CV // {RetreatThreshold1} RT simulations complete")

    ### Save results to dataframe
    WinPercentageDataFrame = pd.DataFrame(WinPercentageResults,columns=ColumnLabels,)
    CasualtyDataFrame = pd.DataFrame(CasualtyResults,columns=ColumnLabels,)

    ### Save dataframes to csv file
    WinPercentageDataFrame.to_csv("LandCombat/SmallBattles/land_combat_small_battle_win_percentages.csv",index=False)
    CasualtyDataFrame.to_csv("LandCombat/SmallBattles/land_combat_small_battle_casualties.csv",index=False)