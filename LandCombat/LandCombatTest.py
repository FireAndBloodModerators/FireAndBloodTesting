# IMPORTS
import pandas as pd
from LandCombatTestForce import Force
from LandCombatTestBattle import Battle

## SET SIMULATIONS COUNT
SimulationCount = 10000

# SIMPLE TEST
print("Simple Sims Start")
## Create list of levy numbers for testing use
SimpleLevyNumbers = [100,200,300,400,500,600,700]

## Create list of retreat thresholds for testing use
SimpleRetreatThresholds = [80,50,0]

## Create column labels for later use
SimpleColumnLabels = [f"{LevyNumber} CV // {RetreatThreshold} RT" for LevyNumber in SimpleLevyNumbers for RetreatThreshold in SimpleRetreatThresholds]
SimpleColumnLabels.insert(0,"")

## Initialise results list
SimpleWinPercentageResults = []
SimpleCasualtyResults = []

## Iterate through the SimpleLevyNumbers and SimpleRetreatThresholds list to create 2 forces and simulate battle between them
for LevyNumber1 in SimpleLevyNumbers:

    for RetreatThreshold1 in SimpleRetreatThresholds:
        #### Create Force 1
        Force1 = Force(0,LevyNumber1,RetreatThreshold1)

        #### Initialise new results lists
        NewWinPercentageResults = [f"{LevyNumber1} CV // {RetreatThreshold1} RT"]
        NewCasualtyPercentageResults = [f"{LevyNumber1} CV // {RetreatThreshold1} RT"]

        for LevyNumber2 in SimpleLevyNumbers:

            for RetreatThreshold2 in SimpleRetreatThresholds:
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
        SimpleWinPercentageResults.append(NewWinPercentageResults)
        SimpleCasualtyResults.append(NewCasualtyPercentageResults)

        #### Checkpoint
        print(f"{LevyNumber1} CV // {RetreatThreshold1} RT simulations complete")

## Save simple results to dataframe
SimpleWinPercentageDataFrame = pd.DataFrame(SimpleWinPercentageResults,columns=SimpleColumnLabels)
SimpleCasualtyDataFrame = pd.DataFrame(SimpleCasualtyResults,columns=SimpleColumnLabels)

## Save simple dataframes to csv file
SimpleWinPercentageDataFrame.to_csv("LandCombat/land_combat_simple_win_percentages.csv",index=False)
SimpleCasualtyDataFrame.to_csv("LandCombat/land_combat_simple_casualties.csv",index=False)
print("Simple Sims End")

print()

# ADVANCED TEST
print("Advanced Sims Start")
## Create list of levy numbers for testing use
AdvancedLevyNumbers = [100,125,150,175,200,225,250,275,300,325,350,375,400,425,450,475,500,525,550,575,600,625,650,675,700]

## Create list of retreat thresholds for testing use
AdvancedRetreatThresholds = [80,70,60,50,40,30,20,10,0]

## Create column labels for later use
AdvancedColumnLabels = [f"{LevyNumber} CV // {RetreatThreshold} RT" for LevyNumber in AdvancedLevyNumbers for RetreatThreshold in AdvancedRetreatThresholds]
AdvancedColumnLabels.insert(0,"")

## Initialise results list
AdvancedWinPercentageResults = []
AdvancedCasualtyResults = []

## Iterate through the AdvancedLevyNumbers and AdvancedRetreatThresholds list to create 2 forces and simulate battle between them
print("Advanced Sims")
for LevyNumber1 in AdvancedLevyNumbers:

    for RetreatThreshold1 in AdvancedRetreatThresholds:
        #### Create Force 1
        Force1 = Force(0,LevyNumber1,RetreatThreshold1)

        #### Initialise new results lists
        NewWinPercentageResults = [f"{LevyNumber1} CV // {RetreatThreshold1} RT"]
        NewCasualtyPercentageResults = [f"{LevyNumber1} CV // {RetreatThreshold1} RT"]

        for LevyNumber2 in AdvancedLevyNumbers:

            for RetreatThreshold2 in AdvancedRetreatThresholds:
                ##### Create Force 2
                Force2 = Force(0,LevyNumber2,RetreatThreshold2)

                ##### Create variables to track wins and casualties
                Force1Wins = 0
                Force1Casualties = 0
                Force2Wins = 0
                Force2Casualties = 0

                ##### Create battle between Force 1 and 2
                TestBattle = Battle(Force1,Force2)

                ##### Run sims
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
        AdvancedWinPercentageResults.append(NewWinPercentageResults)
        AdvancedCasualtyResults.append(NewCasualtyPercentageResults)

        #### Checkpoint
        print(f"{LevyNumber1} CV // {RetreatThreshold1} RT simulations complete")

## Save Advanced results to dataframe
AdvancedWinPercentageDataFrame = pd.DataFrame(AdvancedWinPercentageResults,columns=AdvancedColumnLabels)
AdvancedCasualtyDataFrame = pd.DataFrame(AdvancedCasualtyResults,columns=AdvancedColumnLabels)

## Save Advanced dataframes to csv file
AdvancedWinPercentageDataFrame.to_csv("LandCombat/land_combat_advanced_win_percentages.csv",index=False)
AdvancedCasualtyDataFrame.to_csv("LandCombat/land_combat_advanced_casualties.csv",index=False)
print("Advanced Sims End")