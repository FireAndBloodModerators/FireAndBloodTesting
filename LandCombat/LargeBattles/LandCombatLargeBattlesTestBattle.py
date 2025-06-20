# IMPORTS
import math
import random
from LandCombatLargeBattlesTestForce import Force
from LandCombatLargeBattlesTestFlank import Flank

# CLASS
class Battle:
    """
    A class representing Land Combat Battles for r/FireAndBlood.

    Attributes:
        Force1 (Force): The first Force.
        Force2 (Force): The second Force.
    """

    def __init__(self,Force1:Force,Force2:Force):
        """
        Initialiser function for Land Combat Battles.
    
        Arguments:
            Force1 (Force): The first Force.
            Force2 (Force): The second Force.
        """
        self.Force1 = Force1
        self.Force2 = Force2

    def calculate_strength_bonus(self,Force1Flank1:Flank,Force2Flank1:Flank,Force1Flank2:Flank|None=None,Force1Flank3:Flank|None=None,Force2Flank2:Flank|None=None,Force2Flank3:Flank|None=None):
        """
        Function to calculate the stronger flank in a battle and that flank's Strength Bonus, as well as any additional flanks.
    
        Arguments:
            Force1Flank1 (Flank): The first force's primary flank.
            Force2Flank1 (Flank): The second force's primary flank.
            Force1Flank2 (Flank): The first force's secondary flank.
            Force1Flank3 (Flank): The first force's tertiary flank.
            Force2Flank2 (Flank): The second force's secondary flank.
            Force2Flank3 (Flank): The second force's tertiary flank.
        """
        if(Force1Flank2 is not None):
            if(Force1Flank3 is not None):
                TotalForce1CombatValue = Force1Flank1.Combat_Value + Force1Flank2.Combat_Value + Force1Flank3.Combat_Value
                if(TotalForce1CombatValue > Force2Flank1.Combat_Value):
                    Strength_Percentage = ((TotalForce1CombatValue/Force2Flank1.Combat_Value)-1)*100
                    if(Strength_Percentage >= 5):
                        Force1Flank1.Strength_Bonus = math.ceil(Strength_Percentage/20) + 6
                elif(Force2Flank1.Combat_Value > TotalForce1CombatValue):
                    Strength_Percentage = ((Force2Flank1.Combat_Value/TotalForce1CombatValue)-1)*100
                    if(Strength_Percentage >= 5):
                        Force2Flank1.Strength_Bonus = math.ceil(Strength_Percentage/20)
                else:
                    pass
            else:
                TotalForce1CombatValue = Force1Flank1.Combat_Value + Force1Flank2.Combat_Value
                if(TotalForce1CombatValue > Force2Flank1.Combat_Value):
                    Strength_Percentage = ((TotalForce1CombatValue/Force2Flank1.Combat_Value)-1)*100
                    if(Strength_Percentage >= 5):
                        Force2Flank1.Strength_Bonus = math.ceil(Strength_Percentage/20) + 3
                elif(Force2Flank1.Combat_Value > TotalForce1CombatValue):
                    Strength_Percentage = ((Force2Flank1.Combat_Value/TotalForce1CombatValue)-1)*100
                    if(Strength_Percentage >= 5):
                        Force2Flank1.Strength_Bonus = math.ceil(Strength_Percentage/20)
                else:
                    pass
        else:
            if(Force2Flank2 is not None):
                if(Force2Flank3 is not None):
                    TotalForce2CombatValue = Force2Flank1.Combat_Value + Force2Flank2.Combat_Value + Force2Flank3.Combat_Value
                    if(TotalForce2CombatValue > Force1Flank1.Combat_Value):
                        Strength_Percentage = ((TotalForce2CombatValue/Force1Flank1.Combat_Value)-1)*100
                        if(Strength_Percentage >= 5):
                            Force2Flank1.Strength_Bonus = math.ceil(Strength_Percentage/20) + 6
                    elif(Force1Flank1.Combat_Value > TotalForce2CombatValue):
                        Strength_Percentage = ((Force1Flank1.Combat_Value/TotalForce2CombatValue)-1)*100
                        if(Strength_Percentage >= 5):
                            Force1Flank1.Strength_Bonus = math.ceil(Strength_Percentage/20)
                    else:
                        pass
                else:
                    TotalForce2CombatValue = Force2Flank1.Combat_Value + Force2Flank2.Combat_Value
                    if(TotalForce2CombatValue > Force1Flank1.Combat_Value):
                        Strength_Percentage = ((TotalForce2CombatValue/Force1Flank1.Combat_Value)-1)*100
                        if(Strength_Percentage >= 5):
                            Force2Flank1.Strength_Bonus = math.ceil(Strength_Percentage/20) + 3
                    elif(Force1Flank1.Combat_Value > TotalForce2CombatValue):
                        Strength_Percentage = ((Force1Flank1.Combat_Value/TotalForce2CombatValue)-1)*100
                        if(Strength_Percentage >= 5):
                            Force1Flank1.Strength_Bonus = math.ceil(Strength_Percentage/20)
                    else:
                        pass
            else:
                if(Force1Flank1.Combat_Value > Force2Flank1.Combat_Value):
                    Strength_Percentage = ((Force1Flank1.Combat_Value/Force2Flank1.Combat_Value)-1)*100
                    if(Strength_Percentage >= 5):
                        Force1Flank1.Strength_Bonus = math.ceil(Strength_Percentage/20)
                if(Force2Flank1.Combat_Value > Force1Flank1.Combat_Value):
                    Strength_Percentage = ((Force2Flank1.Combat_Value/Force1Flank1.Combat_Value)-1)*100
                    if(Strength_Percentage >= 5):
                        Force2Flank1.Strength_Bonus = math.ceil(Strength_Percentage/20)
                else:
                    pass