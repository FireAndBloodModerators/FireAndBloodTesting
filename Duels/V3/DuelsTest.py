# IMPORTS
import pandas as pd
from DuelsTestDuellist import Duellist
from DuelsTestDuel import Duel

## SET SIMULATIONS COUNT
SimulationCount = 100000

# WEAPON TEST
print("Sims Start")
## Create list of skill bonuses for testing use
SkillBonuses = [0,1,2,3,4,5,6]

## Create column labels for later use
SkillBonusesLabels = [f"Duellist w/ +{SkillBonus}" for SkillBonus in SkillBonuses]
SkillBonusesLabels.insert(0,"")

## Initialise results list
SkillBonusesWinPercentageResults = []
SkillBonusesInjuriesResults = []

## Iterate through the SkillBonuses list to create 2 Duellists and simulate a Duel between them
for SkillBonus1 in SkillBonuses:

    #### Create Duellist 1
    Duellist1 = Duellist(SkillBonus1)

    #### Initialise new results lists
    NewWinResults = [f"Duellist w/ +{SkillBonus1}"]
    NewInjuriesResults = [f"Duellist w/ +{SkillBonus1}"]

    for SkillBonus2 in SkillBonuses:

        #### Create Duellist 2
        Duellist2 = Duellist(SkillBonus2)

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
    SkillBonusesWinPercentageResults.append(NewWinResults)
    SkillBonusesInjuriesResults.append(NewInjuriesResults)

    #### Checkpoint
    print(f"Duellist w/ +{SkillBonus1} simulations complete")

## Save Skill Bonuses results to dataframe
SkillBonusesWinPercentageDataFrame = pd.DataFrame(SkillBonusesWinPercentageResults,columns=SkillBonusesLabels)
SkillBonusesInjuriesDataFrame = pd.DataFrame(SkillBonusesInjuriesResults,columns=SkillBonusesLabels)

## Save Skill Bonuses dataframes to csv file
SkillBonusesWinPercentageDataFrame.to_csv("Duels/V3/duels_skill_bonuses_win_percentages.csv",index=False)
SkillBonusesInjuriesDataFrame.to_csv("Duels/V3/duels_skill_bonuses_injuries.csv",index=False)
print("Sims End")