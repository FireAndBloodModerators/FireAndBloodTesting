# IMPORTS
import pandas as pd
from DuelsTestDuellist import Duellist
from DuelsTestDuel import Duel

## SET SIMULATIONS COUNT
SimulationCount = 100000

# WEAPON TEST
print("Sims Start")

## Create list of skill combinations for testing use.
SkillCombinationList = [["NoSkills",0,0,0,0],["T1Warrior",0,1,0,1],["T1Warrior/T2Warrior",0,2,0,2],["T1Warrior/T2Warrior/T3Warrior",0,4,0,3],["T1Warrior/T1Brute/T2Warrior/T3Warrior",0,4,1,4],["T1Warrior/T1Brute/T2Warrior/T2Brute/T3Warrior",0,4,3,5]]

## Create column labels for later use
SkillCombinationLabels = [f"Duellist w/ {SkillCombination[0]}" for SkillCombination in SkillCombinationList]
SkillCombinationLabels.insert(0,"")

## Initialise results list
SkillCombinationDeathCritInjuryResults = []

## Iterate through the SkillCombinationList list to create 2 Duellists and simulate a Duel between them
for SkillCombination1 in SkillCombinationList:

    #### Create Duellist 1
    Duellist1 = Duellist(SkillCombination1[1],SkillCombination1[2],SkillCombination1[3],SkillCombination1[4])

    #### Initialise new results lists
    NewInjuriesResults = [f"Duellist w/ {SkillCombination1[0]}"]

    for SkillCombination2 in SkillCombinationList:

        #### Create Duellist 2
        Duellist2 = Duellist(SkillCombination2[1],SkillCombination2[2],SkillCombination2[3],SkillCombination2[4])

        ##### Create variables to track wins and casualties
        Duellist1Deaths = 0
        Duellist1CriticalInjuries = 0

        ##### Create Duel  between Duellist 1 and 2
        TestDuel = Duel(Duellist1,Duellist2)

        ##### Run sims
        for x in range(SimulationCount):
            ###### Run Duel between Duellist 1 and 2
            DuelResult = TestDuel.duel()

            ###### Increment Duellist 1 trackers
            Duellist1Deaths += Duellist1.Deaths
            Duellist1CriticalInjuries += Duellist1.CriticalInjuries

        ##### Calculate win percentage and statistics for Duellist 1
        Duellist1DeathResults = round((Duellist1Deaths/SimulationCount)*100,3)
        Duellist1CriticalInjuryResults = round((Duellist1CriticalInjuries/SimulationCount)*100,3)

        ##### Save statistics to new results lists
        NewInjuriesResults.append([f"{Duellist1DeathResults}% Chance of Death",f"{Duellist1CriticalInjuryResults}% Chance of Critical Injury"])

    #### Save New Results lists to Results list
    SkillCombinationDeathCritInjuryResults.append(NewInjuriesResults)

    #### Checkpoint
    print(f"Duellist w/ {SkillCombination1[0]} simulations complete")

## Save results to dataframe
SkillCombinationDeathCritInjuryDataFrame = pd.DataFrame(SkillCombinationDeathCritInjuryResults,columns=SkillCombinationLabels)

## Save dataframes to csv file
SkillCombinationDeathCritInjuryDataFrame.to_csv("Duels/V4/duels_skill_combination_death_crit_injury_results.csv",index=False)
print("Sims End")