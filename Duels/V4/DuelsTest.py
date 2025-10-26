# IMPORTS
import pandas as pd
from DuelsTestDuellist import Duellist
from DuelsTestDuel import Duel

## SET SIMULATIONS COUNT
SimulationCount = 100000

# WEAPON TEST
print("Sims Start")
## Create list of number of skills for testing use
NumberOfSkillsList = [0,1,2,3,4,5]

## Create column labels for later use
NumberOfSkillsLabels = [f"Duellist w/ {NumberOfSkills} Personal Combat Skills" for NumberOfSkills in NumberOfSkillsList]
NumberOfSkillsLabels.insert(0,"")

## Initialise results list
NumberOfSkillsWinPercentageResults = []
NumberOfSkillsInjuriesResults = []

## Iterate through the SkillBonuses list to create 2 Duellists and simulate a Duel between them
for NumberOfSkills1 in NumberOfSkillsList:

    #### Create Duellist 1
    Duellist1 = Duellist(NumberOfSkills1)

    #### Initialise new results lists
    NewWinResults = [f"Duellist w/ {NumberOfSkills1} Personal Combat Skills"]
    NewInjuriesResults = [f"Duellist w/ {NumberOfSkills1} Personal Combat Skills"]

    for NumberOfSkills2 in NumberOfSkillsList:

        #### Create Duellist 2
        Duellist2 = Duellist(NumberOfSkills2)

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
        Duellist1WinResults = round((Duellist1Wins/SimulationCount)*100,3)
        Duellist1DeathResults = round((Duellist1Deaths/SimulationCount)*100,3)
        Duellist1CriticalInjuryResults = round((Duellist1CriticalInjuries/SimulationCount)*100,3)
        Duellist1MajorInjuryResults = round((Duellist1MajorInjuries/SimulationCount)*100,3)
        Duellist1MinorInjuryResults = round((Duellist1MinorInjuries/SimulationCount)*100,3)

        ##### Save statistics to new results lists
        NewWinResults.append(f"{Duellist1WinResults}% Winrate")
        NewInjuriesResults.append([f"{Duellist1DeathResults}% Chance of Death",f"{Duellist1CriticalInjuryResults}% Chance of Critical Injury",f"{Duellist1MajorInjuryResults}% Chance of Major Injury",f"{Duellist1MinorInjuryResults}% Chance of Minor Injury"])

    #### Save New Results lists to Results list
    NumberOfSkillsWinPercentageResults.append(NewWinResults)
    NumberOfSkillsInjuriesResults.append(NewInjuriesResults)

    #### Checkpoint
    print(f"Duellist w/ {NumberOfSkills1} Personal Combat SKills simulations complete")

## Save results to dataframe
NumberOfSkillsWinPercentageDataFrame = pd.DataFrame(NumberOfSkillsWinPercentageResults,columns=NumberOfSkillsLabels)
NumberOfSkillsInjuriesDataFrame = pd.DataFrame(NumberOfSkillsInjuriesResults,columns=NumberOfSkillsLabels)

## Save dataframes to csv file
NumberOfSkillsWinPercentageDataFrame.to_csv("Duels/V4/duels_number_of_skills_win_percentages.csv",index=False)
NumberOfSkillsInjuriesDataFrame.to_csv("Duels/V4/duels_number_of_skills_injuries.csv",index=False)
print("Sims End")