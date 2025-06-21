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
            Force1Flank2 (Flank): The first force's secondary flank. Default to None.
            Force1Flank3 (Flank): The first force's tertiary flank. Default to None.
            Force2Flank2 (Flank): The second force's secondary flank. Default to None.
            Force2Flank3 (Flank): The second force's tertiary flank. Default to None.
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
    
    def land_combat_roll(self,RollingFlank:Flank) -> int:
        """
        Function to roll 2d50 and add a flank's bonuses.
    
        Arguments:
            RollingFlank (Flank): The flank that is rolling.

        Returns:
            Combat_Roll (int): The 2d50 roll plus a force's bonuses.
        """
        Combat_Roll = random.randint(1,50) + random.randint(1,50) + RollingFlank.Strength_Bonus + RollingFlank.Terrain_Bonus + RollingFlank.Skill_Bonus
        return Combat_Roll
    
    def round_morale_damage(self,DamagedFlank1:Flank,Damage:int,DamagedFlank2:Flank|None=None,DamagedFlank3:Flank|None=None):
        """
        Function to reduce a flank's morale by the damage dealt in a combat round.
    
        Arguments:
            DamagedFlank1 (Flank): The flank that is taking damage.
            Damage (int): The damage dealt in the combat round to the flank.
            DamagedFlank2 (Flank): Secondary flank that is taking damage. Default to None.
            DamagedFlank3 (Flank): Tertiary flank that is taking damage. Default to None.
        """
        DamagedFlank1.Morale -= Damage
        if(DamagedFlank2 is not None):
            DamagedFlank2.Morale -= Damage
        if(DamagedFlank3 is not None):
            DamagedFlank3.Morale -= Damage

    def round_casualties(self,Winner1:Flank,Loser1:Flank,Winner2:Flank|None=None,Winner3:Flank|None=None,Loser2:Flank|None=None,Loser3:Flank|None=None):
        """
        Function to increase a flank's battle casualties based.
    
        Arguments:
            Winner1 (Flank): The flank that won the battle round.
            Loser1 (Flank): The flank that lost the battle round.
        """
        Winner1.Casualties += 1
        if(Winner2 is not None):
            Winner2.Casualties += 1
        if(Winner3 is not None):
            Winner3.Casualties += 1
        Loser1.Casualties += (random.randint(1,3) + 1)
        if(Loser2 is not None):
            Loser2.Casualties += (random.randint(1,3) + 1)
        if(Loser3 is not None):
            Loser3.Casualties += (random.randint(1,3) + 1)

    def attempt_retreat(self,RetreatingFlank:Flank,NonRetreatingFlank:Flank):
        """
        Function to trigger a retreat or a rout for a defeated flank.

        Arguments:
            RetreatingFlank (Flank): The flank that is attempting to retreat.
            NonRetreatingFlank (Flank): The flank that is attempting to retreat.
        """
        if(RetreatingFlank.Morale > 0):
            RetreatThreshold = 10 + NonRetreatingFlank.Speed - RetreatingFlank.Speed
            RetreatRoll = random.randint(1,20)
            if(RetreatRoll < RetreatThreshold):
                RetreatingFlank.Casualties += (random.randint(1,5) + random.randint(1,5))
        else:
            RetreatingFlank.Casualties += (random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + 5)
    
    def reduce_casualties(self,ReducedCasualtiesFlank:Flank):
        """
        Function to reduce a flank's casualties taken based on its Strength Bonus.

        Arguments:
            ReducedCasualtiesFlank (Flank): The flank that is having its casualties reduced.
        """
        CasualtyReductionAmount = (ReducedCasualtiesFlank.Strength_Bonus * 5) if ((ReducedCasualtiesFlank.Strength_Bonus * 5) < 50) else 50
        ReducedCasualtiesFlank.Casualties = round(ReducedCasualtiesFlank.Casualties * (1 - (CasualtyReductionAmount/100)))