# IMPORTS
import pandas as pd
from NavalCombatTestFleet import Fleet
from NavalCombatTestBattle import Battle

## SET SIMULATIONS COUNT
SimulationCount = 10000

# SIMPLE TEST
print("Simple Sims Start")
## Create list of cog numbers for testing use
SimpleCogNumbers = [10,30,50,70,90,110,130]

## Create list of retreat thresholds for testing use
SimpleRetreatThresholds = [80,50,0]

## Create column labels for later use
SimpleColumnLabels = [f"{CogNumber} CV // {RetreatThreshold} RT" for CogNumber in SimpleCogNumbers for RetreatThreshold in SimpleRetreatThresholds]
SimpleColumnLabels.insert(0,"")

## Initialise results list
SimpleWinPercentageResults = []
SimpleCasualtyResults = []

## Iterate through the SimpleGalleyNumbers and SimpleRetreatThresholds list to create 2 fleets and simulate battle between them
for CogNumber1 in SimpleCogNumbers:

    for RetreatThreshold1 in SimpleRetreatThresholds:
        #### Create Force 1
        Fleet1 = Fleet(0,0,0,0,CogNumber1,RetreatThreshold1)

        #### Initialise new results lists
        NewWinPercentageResults = [f"{CogNumber1} CV // {RetreatThreshold1} RT"]
        NewCasualtyPercentageResults = [f"{CogNumber1} CV // {RetreatThreshold1} RT"]

        for CogNumber2 in SimpleCogNumbers:

            for RetreatThreshold2 in SimpleRetreatThresholds:
                ##### Create Force 2
                Fleet2 = Fleet(0,0,0,0,CogNumber2,RetreatThreshold2)

                ##### Create variables to track wins and casualties
                Fleet1Wins = 0
                Fleet1Casualties = 0
                Fleet2Wins = 0
                Fleet2Casualties = 0

                ##### Create battle between Force 1 and 2
                TestBattle = Battle(Fleet1,Fleet2)

                ##### Run sims 10,000 times
                for x in range(SimulationCount):
                    ###### Run battle between Force 1 and 2
                    BattleResult = TestBattle.battle()

                    ###### Increment win count of winner of the battle
                    if(BattleResult == 1):
                        Fleet1Wins += 1
                    elif(BattleResult == 2):
                        Fleet2Wins += 1
                    else:
                        pass

                    ###### Increment casualty count of both sides
                    Fleet1Casualties += Fleet1.Casualties
                    Fleet2Casualties += Fleet2.Casualties

                ##### Calculate win percentage and average casualties of each fleet
                Fleet1WinPercentage = round((Fleet1Wins/SimulationCount)*100,2)
                Fleet1AverageCasualties = round(Fleet1Casualties/SimulationCount)
                Fleet2WinPercentage = round((Fleet2Wins/SimulationCount)*100,2)
                Fleet2AverageCasualties = round(Fleet2Casualties/SimulationCount)

                ##### Save results to New Results lists
                NewWinPercentageResults.append(f"{Fleet1WinPercentage}% Winrate")
                NewCasualtyPercentageResults.append(f"{Fleet1AverageCasualties}% Casualties")
        
        #### Save New Results lists to Results list
        SimpleWinPercentageResults.append(NewWinPercentageResults)
        SimpleCasualtyResults.append(NewCasualtyPercentageResults)

        #### Checkpoint
        print(f"{CogNumber1} CV // {RetreatThreshold1} RT simulations complete")

## Save simple results to dataframe
SimpleWinPercentageDataFrame = pd.DataFrame(SimpleWinPercentageResults,columns=SimpleColumnLabels)
SimpleCasualtyDataFrame = pd.DataFrame(SimpleCasualtyResults,columns=SimpleColumnLabels)

## Save simple dataframes to csv file
SimpleWinPercentageDataFrame.to_csv("NavalCombat/naval_combat_simple_win_percentages.csv",index=False)
SimpleCasualtyDataFrame.to_csv("NavalCombat/naval_combat_simple_casualties.csv",index=False)
print("Simple Sims End")

print()

# ADVANCED TEST
print("Advanced Sims Start")
## Create list of cog numbers for testing use
AdvancedCogNumbers = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130]

## Create list of retreat thresholds for testing use
AdvancedRetreatThresholds = [80,70,60,50,40,30,20,10,0]

## Create column labels for later use
AdvancedColumnLabels = [f"{CogNumber} CV // {RetreatThreshold} RT" for CogNumber in AdvancedCogNumbers for RetreatThreshold in AdvancedRetreatThresholds]
AdvancedColumnLabels.insert(0,"")

## Initialise results list
AdvancedWinPercentageResults = []
AdvancedCasualtyResults = []

## Iterate through the AdvancedLevyNumbers and AdvancedRetreatThresholds list to create 2 forces and simulate battle between them
print("Advanced Sims")
for CogNumber1 in AdvancedCogNumbers:

    for RetreatThreshold1 in AdvancedRetreatThresholds:
        #### Create Fleet 1
        Fleet1 = Fleet(0,0,0,0,CogNumber1,RetreatThreshold1)

        #### Initialise new results lists
        NewWinPercentageResults = [f"{CogNumber1} CV // {RetreatThreshold1} RT"]
        NewCasualtyPercentageResults = [f"{CogNumber1} CV // {RetreatThreshold1} RT"]

        for CogNumber2 in AdvancedCogNumbers:

            for RetreatThreshold2 in AdvancedRetreatThresholds:
                ##### Create Fleet 2
                Fleet2 = Fleet(0,0,0,0,CogNumber2,RetreatThreshold2)

                ##### Create variables to track wins and casualties
                Fleet1Wins = 0
                Fleet1Casualties = 0
                Fleet2Wins = 0
                Fleet2Casualties = 0

                ##### Create battle between Fleet 1 and 2
                TestBattle = Battle(Fleet1,Fleet2)

                ##### Run sims
                for x in range(SimulationCount):
                    ###### Run battle between Force 1 and 2
                    BattleResult = TestBattle.battle()

                    ###### Increment win count of winner of the battle
                    if(BattleResult == 1):
                        Fleet1Wins += 1
                    elif(BattleResult == 2):
                        Fleet2Wins += 1
                    else:
                        pass

                    ###### Increment casualty count of both sides
                    Fleet1Casualties += Fleet1.Casualties
                    Fleet2Casualties += Fleet2.Casualties

                ##### Calculate win percentage and average casualties of each force
                Fleet1WinPercentage = round((Fleet1Wins/SimulationCount)*100,2)
                Fleet1AverageCasualties = round(Fleet1Casualties/SimulationCount)
                Fleet2WinPercentage = round((Fleet2Wins/SimulationCount)*100,2)
                Fleet2AverageCasualties = round(Fleet2Casualties/SimulationCount)

                ##### Save results to New Results lists
                NewWinPercentageResults.append(f"{Fleet1WinPercentage}% Winrate")
                NewCasualtyPercentageResults.append(f"{Fleet1AverageCasualties}% Casualties")
        
        #### Save New Results lists to Results list
        AdvancedWinPercentageResults.append(NewWinPercentageResults)
        AdvancedCasualtyResults.append(NewCasualtyPercentageResults)

        #### Checkpoint
        print(f"{CogNumber1} CV // {RetreatThreshold1} RT simulations complete")

## Save Advanced results to dataframe
AdvancedWinPercentageDataFrame = pd.DataFrame(AdvancedWinPercentageResults,columns=AdvancedColumnLabels)
AdvancedCasualtyDataFrame = pd.DataFrame(AdvancedCasualtyResults,columns=AdvancedColumnLabels)

## Save Advanced dataframes to csv file
AdvancedWinPercentageDataFrame.to_csv("NavalCombat/naval_combat_advanced_win_percentages.csv",index=False)
AdvancedCasualtyDataFrame.to_csv("NavalCombat/naval_combat_advanced_casualties.csv",index=False)
print("Advanced Sims End")