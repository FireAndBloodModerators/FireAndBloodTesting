# IMPORTS
import pandas as pd
from LandCombatLargeBattlesTestFlank import Flank
from LandCombatLargeBattlesTestForce import Force
from LandCombatLargeBattlesTestBattle import Battle

# TEST
TestForce1 = Force(0,1500)
TestForce2 = Force(0,3000)
TestBattle = Battle(TestForce1,TestForce2)
TestBattle.battle()