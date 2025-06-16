# IMPORTS
from LandCombatTestForce import Force
from LandCombatTestBattle import Battle

# TEST
## Create list of levy numbers for testing use
LevyNumbers = [100,200,300,400,500,600]

## Iterate through the LevyNumbers list to create 2 forces and simulate battle between them
for LevyNumber1 in LevyNumbers:
    for LevyNumber2 in LevyNumbers:
        ### Create Force 1
        print(LevyNumber1)
        Force1 = Force(0,LevyNumber1)
        print(LevyNumber2)
        ### Create Force 2
        Force2 = Force(0,LevyNumber2)

        ### Create variables to track wins and casualties
        Force1Wins = 0
        Force1Casualties = 0
        Force2Wins = 0
        Force2Casualties = 0

        ### Create battle between Force 1 and 2
        TestBattle = Battle(Force1,Force2)

        ### Run sims 10,000 times
        for x in range(10000):
            ### Run battle between Force 1 and 2
            BattleResult = TestBattle.battle()

            ### Increment win count of winner of the battle
            if(BattleResult == 1):
                Force1Wins = Force1Wins + 1
            elif(BattleResult == 2):
                Force2Wins = Force2Wins + 1
            else:
                pass

            ### Increment casualty count of both sides
            Force1Casualties = Force1Casualties + Force1.Casualties
            Force2Casualties = Force2Casualties + Force2.Casualties

        ### Calculate win percentage and average casualties of each force
        Force1WinPercentage = round((Force1Wins/10000)*100,2)
        Force1AverageCasualties = round(Force1Casualties/10000)
        Force2WinPercentage = round((Force2Wins/10000)*100,2)
        Force2AverageCasualties = round(Force2Casualties/10000)

        ### Print results
        print(f"""{LevyNumber1} CV vs. {LevyNumber2} CV
              
              {LevyNumber1} CV Win Percentage: {Force1WinPercentage}%
              {LevyNumber1} CV Average Casualties: {Force1AverageCasualties}
              
              {LevyNumber2} CV Win Percentage: {Force2WinPercentage}%
              {LevyNumber2} CV Average Casualties: {Force2AverageCasualties}""")