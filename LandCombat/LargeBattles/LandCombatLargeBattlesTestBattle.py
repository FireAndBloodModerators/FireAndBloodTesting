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
        Initialiser function for Land Combat Large Battles.
    
        Arguments:
            Force1 (Force): The first Force.
            Force2 (Force): The second Force.
        """
        self.Force1:Force = Force1
        self.Force2:Force = Force2

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

    def assign_starting_targets(self):
        """
        Function to assign the starting targets of each force's flanks.
        """
        self.Force1.LeftFlank.Target = self.Force2.RightFlank
        self.Force1.CentreFlank.Target = self.Force2.CentreFlank
        self.Force1.RightFlank.Target = self.Force2.LeftFlank
        self.Force2.LeftFlank.Target = self.Force1.RightFlank
        self.Force2.CentreFlank.Target = self.Force1.CentreFlank
        self.Force2.RightFlank.Target = self.Force1.LeftFlank

    def assign_new_targets(self):
        """
        Function to determine new targets of each force's flanks.
        """
        Force1Flanks = sum([not self.Force1.LeftFlank.Defeated,not self.Force1.CentreFlank.Defeated,not self.Force1.RightFlank])
        Force2Flanks = sum([not self.Force2.LeftFlank.Defeated,not self.Force2.CentreFlank.Defeated,not self.Force2.RightFlank])
        if(self.Force1.LeftFlank.Target.Defeated):
            if((self.Force2.CentreFlank.Target is self.Force1.LeftFlank) | (self.Force2.LeftFlank.Target is self.Force1.LeftFlank)):
                if(self.Force2.CentreFlank.Target is self.Force1.LeftFlank):
                    self.Force1.LeftFlank.Target = self.Force2.CentreFlank
                elif(self.Force2.LeftFlank.Target is self.Force1.LeftFlank):
                    self.Force1.LeftFlank.Target = self.Force2.LeftFlank
            elif(not self.Force2.CentreFlank.Defeated):
                self.Force1.LeftFlank.Target = self.Force2.CentreFlank
                if(self.Force2.CentreFlank.Target.Target is not self.Force2.CentreFlank):
                    self.Force2.CentreFlank.Target = self.Force1.LeftFlank
            elif(not self.Force2.LeftFlank.Defeated):
                self.Force1.LeftFlank.Target = self.Force2.LeftFlank
                if(self.Force2.LeftFlank.Target.Target is not self.Force2.LeftFlank):
                    self.Force2.LeftFlank.Target = self.Force1.LeftFlank
            elif(Force2Flanks == 0):
                pass
            else:
                print("Error in new target for Force 1 Left Flank")
        if(self.Force1.RightFlank.Target.Defeated):
            if((self.Force2.CentreFlank.Target is self.Force1.RightFlank) | (self.Force2.RightFlank.Target is self.Force1.RightFlank)):
                if(self.Force2.CentreFlank.Target is self.Force1.RightFlank):
                    self.Force1.RightFlank.Target = self.Force2.CentreFlank
                elif(self.Force2.RightFlank.Target is self.Force1.RightFlank):
                    self.Force1.RightFlank.Target = self.Force2.RightFlank
            elif(not self.Force2.CentreFlank.Defeated):
                self.Force1.RightFlank.Target = self.Force2.CentreFlank
                if(self.Force2.CentreFlank.Target.Target is not self.Force2.CentreFlank):
                    self.Force2.CentreFlank.Target = self.Force1.RightFlank
            elif(not self.Force2.RightFlank.Defeated):
                self.Force1.RightFlank.Target = self.Force2.RightFlank
                if(self.Force2.RightFlank.Target.Target is not self.Force2.RightFlank):
                    self.Force2.RightFlank.Target = self.Force1.RightFlank
            elif(Force2Flanks == 0):
                pass
            else:
                print("Error in new target for Force 1 Right Flank")
        if(self.Force1.CentreFlank.Target.Defeated):
            if((self.Force2.LeftFlank.Target is self.Force1.CentreFlank) | (self.Force2.RightFlank.Target is self.Force1.CentreFlank)):
                if(self.Force2.LeftFlank.Target is self.Force1.CentreFlank):
                    self.Force1.CentreFlank.Target = self.Force2.LeftFlank
                elif(self.Force2.RightFlank.Target is self.Force1.CentreFlank):
                    self.Force1.CentreFlank.Target = self.Force2.RightFlank
            else:
                if(((self.Force1.LeftFlank.Morale < self.Force1.RightFlank.Morale) & (not self.Force1.LeftFlank.Defeated) & (not self.Force1.RightFlank.Defeated)) | ((not self.Force1.LeftFlank.Defeated) & self.Force1.RightFlank.Defeated)):
                    self.Force1.CentreFlank.Target = self.Force1.LeftFlank.Target
                elif(((self.Force1.RightFlank.Morale < self.Force1.LeftFlank.Morale) & (not self.Force1.RightFlank.Defeated) & (not self.Force1.LeftFlank.Defeated)) | ((not self.Force1.RightFlank.Defeated) & self.Force1.LeftFlank.Defeated)):
                    self.Force1.CentreFlank.Target = self.Force1.RightFlank.Target
                elif(Force2Flanks == 0):
                    pass
                else:
                    print("Error in new target for Force 1 Centre Flank")
        if(self.Force2.LeftFlank.Target.Defeated):
            if((self.Force1.CentreFlank.Target is self.Force2.LeftFlank) | (self.Force1.LeftFlank.Target is self.Force2.LeftFlank)):
                if(self.Force1.CentreFlank.Target is self.Force2.LeftFlank):
                    self.Force2.LeftFlank.Target = self.Force1.CentreFlank
                elif(self.Force1.LeftFlank.Target is self.Force2.LeftFlank):
                    self.Force2.LeftFlank.Target = self.Force1.LeftFlank
            elif(not self.Force1.CentreFlank.Defeated):
                self.Force2.LeftFlank.Target = self.Force1.CentreFlank
                if(self.Force1.CentreFlank.Target.Target is not self.Force1.CentreFlank):
                    self.Force1.CentreFlank.Target = self.Force2.LeftFlank
            elif(not self.Force1.LeftFlank.Defeated):
                self.Force2.LeftFlank.Target = self.Force1.LeftFlank
                if(self.Force1.LeftFlank.Target.Target is not self.Force1.LeftFlank):
                    self.Force1.LeftFlank.Target = self.Force2.LeftFlank
            elif(Force1Flanks == 0):
                pass
            else:
                print("Error in new target for Force 2 Left Flank")
        if(self.Force2.RightFlank.Target.Defeated):
            if((self.Force1.CentreFlank.Target is self.Force2.RightFlank) | (self.Force1.RightFlank.Target is self.Force2.RightFlank)):
                if(self.Force1.CentreFlank.Target is self.Force2.RightFlank):
                    self.Force2.RightFlank.Target = self.Force1.CentreFlank
                elif(self.Force1.RightFlank.Target is self.Force2.RightFlank):
                    self.Force2.RightFlank.Target = self.Force1.RightFlank
            elif(not self.Force1.CentreFlank.Defeated):
                self.Force2.RightFlank.Target = self.Force1.CentreFlank
                if(self.Force1.CentreFlank.Target.Target is not self.Force1.CentreFlank):
                    self.Force1.CentreFlank.Target = self.Force2.RightFlank
            elif(not self.Force1.RightFlank.Defeated):
                self.Force2.RightFlank.Target = self.Force1.RightFlank
                if(self.Force1.RightFlank.Target.Target is not self.Force1.RightFlank):
                    self.Force1.RightFlank.Target = self.Force2.RightFlank
            elif(Force1Flanks == 0):
                pass
            else:
                print("Error in new target for Force 2 Right Flank")
        if(self.Force2.CentreFlank.Target.Defeated):
            if((self.Force1.LeftFlank.Target is self.Force2.CentreFlank) | (self.Force1.RightFlank.Target is self.Force2.CentreFlank)):
                if(self.Force1.LeftFlank.Target is self.Force2.CentreFlank):
                    self.Force2.CentreFlank.Target = self.Force1.LeftFlank
                elif(self.Force1.RightFlank.Target is self.Force2.CentreFlank):
                    self.Force2.CentreFlank.Target = self.Force1.RightFlank
            else:
                if(((self.Force2.LeftFlank.Morale < self.Force2.RightFlank.Morale) & (not self.Force2.LeftFlank.Defeated) & (not self.Force2.RightFlank.Defeated)) | ((not self.Force2.LeftFlank.Defeated) & self.Force2.RightFlank.Defeated)):
                    self.Force2.CentreFlank.Target = self.Force2.LeftFlank.Target
                elif(((self.Force2.RightFlank.Morale < self.Force2.LeftFlank.Morale) & (not self.Force2.RightFlank.Defeated) & (not self.Force2.LeftFlank.Defeated)) | ((not self.Force2.RightFlank.Defeated) & self.Force2.LeftFlank.Defeated)):
                    self.Force2.CentreFlank.Target = self.Force2.RightFlank.Target
                elif(Force1Flanks == 0):
                    pass
                else:
                    print("Error in new target for Force 2 Centre Flank")

    def check_if_flanks_defeated(self):
        """
        Function to determine if a force's flanks are defeated.
        """
        if((not self.Force1.LeftFlank.Defeated) & (self.Force1.LeftFlank.Morale <= self.Force1.LeftFlank.Retreat_Threshold)):
            self.Force1.LeftFlank.Defeated = True
        if((not self.Force1.CentreFlank.Defeated) & (self.Force1.CentreFlank.Morale <= self.Force1.CentreFlank.Retreat_Threshold)):
            self.Force1.CentreFlank.Defeated = True
        if((not self.Force1.RightFlank.Defeated) & (self.Force1.RightFlank.Morale <= self.Force1.RightFlank.Retreat_Threshold)):
            self.Force1.RightFlank.Defeated = True
        if((not self.Force2.LeftFlank.Defeated) & (self.Force2.LeftFlank.Morale <= self.Force2.LeftFlank.Retreat_Threshold)):
            self.Force2.LeftFlank.Defeated = True
        if((not self.Force2.CentreFlank.Defeated) & (self.Force2.CentreFlank.Morale <= self.Force2.CentreFlank.Retreat_Threshold)):
            self.Force2.CentreFlank.Defeated = True
        if((not self.Force2.RightFlank.Defeated) & (self.Force2.RightFlank.Morale <= self.Force2.RightFlank.Retreat_Threshold)):
            self.Force2.RightFlank.Defeated = True
        self.assign_new_targets()
    
    def flank_damage(self):
        """
        Function to have each flank deal damage to its target.
        """
        Force1Flanks = sum([not self.Force1.LeftFlank.Defeated,not self.Force1.CentreFlank.Defeated,not self.Force1.RightFlank])
        Force2Flanks = sum([not self.Force2.LeftFlank.Defeated,not self.Force2.CentreFlank.Defeated,not self.Force2.RightFlank])
        if(Force1Flanks > Force2Flanks):
            if(not self.Force1.LeftFlank.Defeated):
                if(self.Force1.LeftFlank.Target.Target is self.Force1.LeftFlank):
                    if(((self.Force1.CentreFlank.Target is self.Force1.LeftFlank.Target) & (not self.Force1.CentreFlank.Defeated)) & ((self.Force1.RightFlank.Target is self.Force1.LeftFlank.Target) & (not self.Force1.RightFlank.Defeated))):
                        self.calculate_strength_bonus(Force1Flank1=self.Force1.LeftFlank,Force2Flank1=self.Force1.LeftFlank.Target,Force1Flank2=self.Force1.CentreFlank,Force1Flank3=self.Force1.RightFlank)
                        Flank1Roll = self.land_combat_roll(self.Force1.LeftFlank)
                        Flank2Roll = self.land_combat_roll(self.Force1.LeftFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.LeftFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force1.LeftFlank,Loser1=self.Force1.LeftFlank.Target,Winner2=self.Force1.CentreFlank,Winner3=self.Force1.RightFlank)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.LeftFlank,Damage=Damage,DamagedFlank2=self.Force1.CentreFlank,DamagedFlank3=self.Force1.RightFlank)
                            self.round_casualties(Winner1=self.Force1.LeftFlank.Target,Loser1=self.Force1.LeftFlank,Loser2=self.Force1.CentreFlank,Loser3=self.Force1.RightFlank)
                        else:
                            pass
                    elif((self.Force1.CentreFlank.Target is self.Force1.LeftFlank.Target) & (not self.Force1.CentreFlank.Defeated)):
                        self.calculate_strength_bonus(Force1Flank1=self.Force1.LeftFlank,Force2Flank1=self.Force1.LeftFlank.Target,Force1Flank2=self.Force1.CentreFlank)
                        Flank1Roll = self.land_combat_roll(self.Force1.LeftFlank)
                        Flank2Roll = self.land_combat_roll(self.Force1.LeftFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.LeftFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force1.LeftFlank,Loser1=self.Force1.LeftFlank.Target,Winner2=self.Force1.CentreFlank)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.LeftFlank,Damage=Damage,DamagedFlank2=self.Force1.CentreFlank)
                            self.round_casualties(Winner1=self.Force1.LeftFlank.Target,Loser1=self.Force1.LeftFlank,Loser2=self.Force1.CentreFlank)
                        else:
                            pass
                    elif((self.Force1.RightFlank.Target is self.Force1.LeftFlank.Target) & (not self.Force1.RightFlank.Defeated)):
                        self.calculate_strength_bonus(Force1Flank1=self.Force1.LeftFlank,Force2Flank1=self.Force1.LeftFlank.Target,Force1Flank2=self.Force1.RightFlank)
                        Flank1Roll = self.land_combat_roll(self.Force1.LeftFlank)
                        Flank2Roll = self.land_combat_roll(self.Force1.LeftFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.LeftFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force1.LeftFlank,Loser1=self.Force1.LeftFlank.Target,Winner2=self.Force1.RightFlank)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.LeftFlank,Damage=Damage,DamagedFlank2=self.Force1.RightFlank)
                            self.round_casualties(Winner1=self.Force1.LeftFlank.Target,Loser1=self.Force1.LeftFlank,Loser2=self.Force1.RightFlank)
                        else:
                            pass
                    else:
                        self.calculate_strength_bonus(Force1Flank1=self.Force1.LeftFlank,Force2Flank1=self.Force1.LeftFlank.Target)
                        Flank1Roll = self.land_combat_roll(self.Force1.LeftFlank)
                        Flank2Roll = self.land_combat_roll(self.Force1.LeftFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.LeftFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force1.LeftFlank,Loser1=self.Force1.LeftFlank.Target)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.LeftFlank,Damage=Damage)
                            self.round_casualties(Winner1=self.Force1.LeftFlank.Target,Loser1=self.Force1.LeftFlank)
                        else:
                            pass
            if(not self.Force1.CentreFlank.Defeated):
                if(self.Force1.CentreFlank.Target.Target is self.Force1.CentreFlank):
                    if(((self.Force1.LeftFlank.Target is self.Force1.CentreFlank.Target) & (not self.Force1.LeftFlank.Defeated)) & ((self.Force1.RightFlank.Target is self.Force1.CentreFlank.Target) & (not self.Force1.CentreFlank.Defeated))):
                        self.calculate_strength_bonus(Force1Flank1=self.Force1.CentreFlank,Force2Flank1=self.Force1.CentreFlank.Target,Force1Flank2=self.Force1.LeftFlank,Force1Flank3=self.Force1.RightFlank)
                        Flank1Roll = self.land_combat_roll(self.Force1.CentreFlank)
                        Flank2Roll = self.land_combat_roll(self.Force1.CentreFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.CentreFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force1.CentreFlank,Loser1=self.Force1.CentreFlank.Target,Winner2=self.Force1.LeftFlank,Winner3=self.Force1.RightFlank)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.CentreFlank,Damage=Damage,DamagedFlank2=self.Force1.LeftFlank,DamagedFlank3=self.Force1.RightFlank)
                            self.round_casualties(Winner1=self.Force1.CentreFlank.Target,Loser1=self.Force1.CentreFlank,Loser2=self.Force1.LeftFlank,Loser3=self.Force1.RightFlank)
                        else:
                            pass
                    elif((self.Force1.LeftFlank.Target is self.Force1.CentreFlank.Target) & (not self.Force1.LeftFlank.Defeated)):
                        self.calculate_strength_bonus(Force1Flank1=self.Force1.CentreFlank,Force2Flank1=self.Force1.CentreFlank.Target,Force1Flank2=self.Force1.LeftFlank)
                        Flank1Roll = self.land_combat_roll(self.Force1.CentreFlank)
                        Flank2Roll = self.land_combat_roll(self.Force1.CentreFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.CentreFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force1.CentreFlank,Loser1=self.Force1.CentreFlank.Target,Winner2=self.Force1.LeftFlank)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.CentreFlank,Damage=Damage,DamagedFlank2=self.Force1.LeftFlank)
                            self.round_casualties(Winner1=self.Force1.CentreFlank.Target,Loser1=self.Force1.CentreFlank,Loser2=self.Force1.LeftFlank)
                        else:
                            pass
                    elif((self.Force1.RightFlank.Target is self.Force1.CentreFlank.Target) & (not self.Force1.RightFlank.Defeated)):
                        self.calculate_strength_bonus(Force1Flank1=self.Force1.CentreFlank,Force2Flank1=self.Force1.CentreFlank.Target,Force1Flank2=self.Force1.RightFlank)
                        Flank1Roll = self.land_combat_roll(self.Force1.CentreFlank)
                        Flank2Roll = self.land_combat_roll(self.Force1.CentreFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.CentreFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force1.CentreFlank,Loser1=self.Force1.CentreFlank.Target,Winner2=self.Force1.RightFlank)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.CentreFlank,Damage=Damage,DamagedFlank2=self.Force1.RightFlank)
                            self.round_casualties(Winner1=self.Force1.CentreFlank.Target,Loser1=self.Force1.CentreFlank,Loser2=self.Force1.RightFlank)
                        else:
                            pass
                    else:
                        self.calculate_strength_bonus(Force1Flank1=self.Force1.CentreFlank,Force2Flank1=self.Force1.CentreFlank.Target)
                        Flank1Roll = self.land_combat_roll(self.Force1.CentreFlank)
                        Flank2Roll = self.land_combat_roll(self.Force1.CentreFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.CentreFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force1.CentreFlank,Loser1=self.Force1.CentreFlank.Target)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.CentreFlank,Damage=Damage)
                            self.round_casualties(Winner1=self.Force1.CentreFlank.Target,Loser1=self.Force1.CentreFlank)
                        else:
                            pass
            if(not self.Force1.RightFlank.Defeated):
                if(self.Force1.RightFlank.Target.Target is self.Force1.RightFlank):
                    if(((self.Force1.CentreFlank.Target is self.Force1.RightFlank.Target) & (not self.Force1.CentreFlank.Defeated)) & ((self.Force1.LeftFlank.Target is self.Force1.RightFlank.Target) & (not self.Force1.LeftFlank.Defeated))):
                        self.calculate_strength_bonus(Force1Flank1=self.Force1.RightFlank,Force2Flank1=self.Force1.RightFlank.Target,Force1Flank2=self.Force1.CentreFlank,Force1Flank3=self.Force1.LeftFlank)
                        Flank1Roll = self.land_combat_roll(self.Force1.RightFlank)
                        Flank2Roll = self.land_combat_roll(self.Force1.RightFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.RightFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force1.RightFlank,Loser1=self.Force1.RightFlank.Target,Winner2=self.Force1.CentreFlank,Winner3=self.Force1.LeftFlank)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.RightFlank,Damage=Damage,DamagedFlank2=self.Force1.CentreFlank,DamagedFlank3=self.Force1.LeftFlank)
                            self.round_casualties(Winner1=self.Force1.RightFlank.Target,Loser1=self.Force1.RightFlank,Loser2=self.Force1.CentreFlank,Loser3=self.Force1.LeftFlank)
                        else:
                            pass
                    elif((self.Force1.CentreFlank.Target is self.Force1.RightFlank.Target) & (not self.Force1.CentreFlank.Defeated)):
                        self.calculate_strength_bonus(Force1Flank1=self.Force1.RightFlank,Force2Flank1=self.Force1.RightFlank.Target,Force1Flank2=self.Force1.CentreFlank)
                        Flank1Roll = self.land_combat_roll(self.Force1.RightFlank)
                        Flank2Roll = self.land_combat_roll(self.Force1.RightFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.RightFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force1.RightFlank,Loser1=self.Force1.RightFlank.Target,Winner2=self.Force1.CentreFlank)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.RightFlank,Damage=Damage,DamagedFlank2=self.Force1.CentreFlank)
                            self.round_casualties(Winner1=self.Force1.RightFlank.Target,Loser1=self.Force1.RightFlank,Loser2=self.Force1.CentreFlank)
                        else:
                            pass
                    elif((self.Force1.LeftFlank.Target is self.Force1.RightFlank.Target) & (not self.Force1.LeftFlank.Defeated)):
                        self.calculate_strength_bonus(Force1Flank1=self.Force1.RightFlank,Force2Flank1=self.Force1.RightFlank.Target,Force1Flank2=self.Force1.LeftFlank)
                        Flank1Roll = self.land_combat_roll(self.Force1.RightFlank)
                        Flank2Roll = self.land_combat_roll(self.Force1.RightFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.RightFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force1.RightFlank,Loser1=self.Force1.RightFlank.Target,Winner2=self.Force1.LeftFlank)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.RightFlank,Damage=Damage,DamagedFlank2=self.Force1.LeftFlank)
                            self.round_casualties(Winner1=self.Force1.RightFlank.Target,Loser1=self.Force1.RightFlank,Loser2=self.Force1.LeftFlank)
                        else:
                            pass
                    else:
                        self.calculate_strength_bonus(Force1Flank1=self.Force1.RightFlank,Force2Flank1=self.Force1.RightFlank.Target)
                        Flank1Roll = self.land_combat_roll(self.Force1.RightFlank)
                        Flank2Roll = self.land_combat_roll(self.Force1.RightFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.RightFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force1.RightFlank,Loser1=self.Force1.RightFlank.Target)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force1.RightFlank,Damage=Damage)
                            self.round_casualties(Winner1=self.Force1.RightFlank.Target,Loser1=self.Force1.RightFlank)
                        else:
                            pass
        elif(Force2Flanks > Force1Flanks):
            if(not self.Force2.LeftFlank.Defeated):
                if(self.Force2.LeftFlank.Target.Target is self.Force2.LeftFlank):
                    if(((self.Force2.CentreFlank.Target is self.Force2.LeftFlank.Target) & (not self.Force2.CentreFlank.Defeated)) & ((self.Force2.RightFlank.Target is self.Force2.LeftFlank.Target) & (not self.Force2.RightFlank.Defeated))):
                        self.calculate_strength_bonus(Force1Flank1=self.Force2.LeftFlank,Force2Flank1=self.Force2.LeftFlank.Target,Force1Flank2=self.Force2.CentreFlank,Force1Flank3=self.Force2.RightFlank)
                        Flank1Roll = self.land_combat_roll(self.Force2.LeftFlank)
                        Flank2Roll = self.land_combat_roll(self.Force2.LeftFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.LeftFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force2.LeftFlank,Loser1=self.Force2.LeftFlank.Target,Winner2=self.Force2.CentreFlank,Winner3=self.Force2.RightFlank)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.LeftFlank,Damage=Damage,DamagedFlank2=self.Force2.CentreFlank,DamagedFlank3=self.Force2.RightFlank)
                            self.round_casualties(Winner1=self.Force2.LeftFlank.Target,Loser1=self.Force2.LeftFlank,Loser2=self.Force2.CentreFlank,Loser3=self.Force2.RightFlank)
                        else:
                            pass
                    elif((self.Force2.CentreFlank.Target is self.Force2.LeftFlank.Target) & (not self.Force2.CentreFlank.Defeated)):
                        self.calculate_strength_bonus(Force1Flank1=self.Force2.LeftFlank,Force2Flank1=self.Force2.LeftFlank.Target,Force1Flank2=self.Force2.CentreFlank)
                        Flank1Roll = self.land_combat_roll(self.Force2.LeftFlank)
                        Flank2Roll = self.land_combat_roll(self.Force2.LeftFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.LeftFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force2.LeftFlank,Loser1=self.Force2.LeftFlank.Target,Winner2=self.Force2.CentreFlank)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.LeftFlank,Damage=Damage,DamagedFlank2=self.Force2.CentreFlank)
                            self.round_casualties(Winner1=self.Force2.LeftFlank.Target,Loser1=self.Force2.LeftFlank,Loser2=self.Force2.CentreFlank)
                        else:
                            pass
                    elif((self.Force2.RightFlank.Target is self.Force2.LeftFlank.Target) & (not self.Force2.RightFlank.Defeated)):
                        self.calculate_strength_bonus(Force1Flank1=self.Force2.LeftFlank,Force2Flank1=self.Force2.LeftFlank.Target,Force1Flank2=self.Force2.RightFlank)
                        Flank1Roll = self.land_combat_roll(self.Force2.LeftFlank)
                        Flank2Roll = self.land_combat_roll(self.Force2.LeftFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.LeftFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force2.LeftFlank,Loser1=self.Force2.LeftFlank.Target,Winner2=self.Force2.RightFlank)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.LeftFlank,Damage=Damage,DamagedFlank2=self.Force2.RightFlank)
                            self.round_casualties(Winner1=self.Force2.LeftFlank.Target,Loser1=self.Force2.LeftFlank,Loser2=self.Force2.RightFlank)
                        else:
                            pass
                    else:
                        self.calculate_strength_bonus(Force1Flank1=self.Force2.LeftFlank,Force2Flank1=self.Force2.LeftFlank.Target)
                        Flank1Roll = self.land_combat_roll(self.Force2.LeftFlank)
                        Flank2Roll = self.land_combat_roll(self.Force2.LeftFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.LeftFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force2.LeftFlank,Loser1=self.Force2.LeftFlank.Target)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.LeftFlank,Damage=Damage)
                            self.round_casualties(Winner1=self.Force2.LeftFlank.Target,Loser1=self.Force2.LeftFlank)
                        else:
                            pass
            if(not self.Force2.CentreFlank.Defeated):
                if(self.Force2.CentreFlank.Target.Target is self.Force2.CentreFlank):
                    if(((self.Force2.LeftFlank.Target is self.Force2.CentreFlank.Target) & (not self.Force2.LeftFlank.Defeated)) & ((self.Force2.RightFlank.Target is self.Force2.CentreFlank.Target) & (not self.Force2.CentreFlank.Defeated))):
                        self.calculate_strength_bonus(Force1Flank1=self.Force2.CentreFlank,Force2Flank1=self.Force2.CentreFlank.Target,Force1Flank2=self.Force2.LeftFlank,Force1Flank3=self.Force2.RightFlank)
                        Flank1Roll = self.land_combat_roll(self.Force2.CentreFlank)
                        Flank2Roll = self.land_combat_roll(self.Force2.CentreFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.CentreFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force2.CentreFlank,Loser1=self.Force2.CentreFlank.Target,Winner2=self.Force2.LeftFlank,Winner3=self.Force2.RightFlank)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.CentreFlank,Damage=Damage,DamagedFlank2=self.Force2.LeftFlank,DamagedFlank3=self.Force2.RightFlank)
                            self.round_casualties(Winner1=self.Force2.CentreFlank.Target,Loser1=self.Force2.CentreFlank,Loser2=self.Force2.LeftFlank,Loser3=self.Force2.RightFlank)
                        else:
                            pass
                    elif((self.Force2.LeftFlank.Target is self.Force2.CentreFlank.Target) & (not self.Force2.LeftFlank.Defeated)):
                        self.calculate_strength_bonus(Force1Flank1=self.Force2.CentreFlank,Force2Flank1=self.Force2.CentreFlank.Target,Force1Flank2=self.Force2.LeftFlank)
                        Flank1Roll = self.land_combat_roll(self.Force2.CentreFlank)
                        Flank2Roll = self.land_combat_roll(self.Force2.CentreFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.CentreFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force2.CentreFlank,Loser1=self.Force2.CentreFlank.Target,Winner2=self.Force2.LeftFlank)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.CentreFlank,Damage=Damage,DamagedFlank2=self.Force2.LeftFlank)
                            self.round_casualties(Winner1=self.Force2.CentreFlank.Target,Loser1=self.Force2.CentreFlank,Loser2=self.Force2.LeftFlank)
                        else:
                            pass
                    elif((self.Force2.RightFlank.Target is self.Force2.CentreFlank.Target) & (not self.Force2.RightFlank.Defeated)):
                        self.calculate_strength_bonus(Force1Flank1=self.Force2.CentreFlank,Force2Flank1=self.Force2.CentreFlank.Target,Force1Flank2=self.Force2.RightFlank)
                        Flank1Roll = self.land_combat_roll(self.Force2.CentreFlank)
                        Flank2Roll = self.land_combat_roll(self.Force2.CentreFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.CentreFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force2.CentreFlank,Loser1=self.Force2.CentreFlank.Target,Winner2=self.Force2.RightFlank)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.CentreFlank,Damage=Damage,DamagedFlank2=self.Force2.RightFlank)
                            self.round_casualties(Winner1=self.Force2.CentreFlank.Target,Loser1=self.Force2.CentreFlank,Loser2=self.Force2.RightFlank)
                        else:
                            pass
                    else:
                        self.calculate_strength_bonus(Force1Flank1=self.Force2.CentreFlank,Force2Flank1=self.Force2.CentreFlank.Target)
                        Flank1Roll = self.land_combat_roll(self.Force2.CentreFlank)
                        Flank2Roll = self.land_combat_roll(self.Force2.CentreFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.CentreFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force2.CentreFlank,Loser1=self.Force2.CentreFlank.Target)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.CentreFlank,Damage=Damage)
                            self.round_casualties(Winner1=self.Force2.CentreFlank.Target,Loser1=self.Force2.CentreFlank)
                        else:
                            pass
            if(not self.Force2.RightFlank.Defeated):
                if(self.Force2.RightFlank.Target.Target is self.Force2.RightFlank):
                    if(((self.Force2.CentreFlank.Target is self.Force2.RightFlank.Target) & (not self.Force2.CentreFlank.Defeated)) & ((self.Force2.LeftFlank.Target is self.Force2.RightFlank.Target) & (not self.Force2.LeftFlank.Defeated))):
                        self.calculate_strength_bonus(Force1Flank1=self.Force2.RightFlank,Force2Flank1=self.Force2.RightFlank.Target,Force1Flank2=self.Force2.CentreFlank,Force1Flank3=self.Force2.LeftFlank)
                        Flank1Roll = self.land_combat_roll(self.Force2.RightFlank)
                        Flank2Roll = self.land_combat_roll(self.Force2.RightFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.RightFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force2.RightFlank,Loser1=self.Force2.RightFlank.Target,Winner2=self.Force2.CentreFlank,Winner3=self.Force2.LeftFlank)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.RightFlank,Damage=Damage,DamagedFlank2=self.Force2.CentreFlank,DamagedFlank3=self.Force2.LeftFlank)
                            self.round_casualties(Winner1=self.Force2.RightFlank.Target,Loser1=self.Force2.RightFlank,Loser2=self.Force2.CentreFlank,Loser3=self.Force2.LeftFlank)
                        else:
                            pass
                    elif((self.Force2.CentreFlank.Target is self.Force2.RightFlank.Target) & (not self.Force2.CentreFlank.Defeated)):
                        self.calculate_strength_bonus(Force1Flank1=self.Force2.RightFlank,Force2Flank1=self.Force2.RightFlank.Target,Force1Flank2=self.Force2.CentreFlank)
                        Flank1Roll = self.land_combat_roll(self.Force2.RightFlank)
                        Flank2Roll = self.land_combat_roll(self.Force2.RightFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.RightFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force2.RightFlank,Loser1=self.Force2.RightFlank.Target,Winner2=self.Force2.CentreFlank)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.RightFlank,Damage=Damage,DamagedFlank2=self.Force2.CentreFlank)
                            self.round_casualties(Winner1=self.Force2.RightFlank.Target,Loser1=self.Force2.RightFlank,Loser2=self.Force2.CentreFlank)
                        else:
                            pass
                    elif((self.Force2.LeftFlank.Target is self.Force2.RightFlank.Target) & (not self.Force2.LeftFlank.Defeated)):
                        self.calculate_strength_bonus(Force1Flank1=self.Force2.RightFlank,Force2Flank1=self.Force2.RightFlank.Target,Force1Flank2=self.Force2.LeftFlank)
                        Flank1Roll = self.land_combat_roll(self.Force2.RightFlank)
                        Flank2Roll = self.land_combat_roll(self.Force2.RightFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.RightFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force2.RightFlank,Loser1=self.Force2.RightFlank.Target,Winner2=self.Force2.LeftFlank)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.RightFlank,Damage=Damage,DamagedFlank2=self.Force2.LeftFlank)
                            self.round_casualties(Winner1=self.Force2.RightFlank.Target,Loser1=self.Force2.RightFlank,Loser2=self.Force2.LeftFlank)
                        else:
                            pass
                    else:
                        self.calculate_strength_bonus(Force1Flank1=self.Force2.RightFlank,Force2Flank1=self.Force2.RightFlank.Target)
                        Flank1Roll = self.land_combat_roll(self.Force2.RightFlank)
                        Flank2Roll = self.land_combat_roll(self.Force2.RightFlank.Target)
                        if(Flank1Roll > Flank2Roll):
                            Damage = Flank1Roll - Flank2Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.RightFlank.Target,Damage=Damage)
                            self.round_casualties(Winner1=self.Force2.RightFlank,Loser1=self.Force2.RightFlank.Target)
                        if(Flank2Roll > Flank1Roll):
                            Damage = Flank2Roll - Flank1Roll
                            self.round_morale_damage(DamagedFlank1=self.Force2.RightFlank,Damage=Damage)
                            self.round_casualties(Winner1=self.Force2.RightFlank.Target,Loser1=self.Force2.RightFlank)
                        else:
                            pass
        else:
            if(not self.Force1.LeftFlank.Defeated):
                self.calculate_strength_bonus(Force1Flank1=self.Force1.LeftFlank,Force2Flank1=self.Force1.LeftFlank.Target)
                Flank1Roll = self.land_combat_roll(self.Force1.LeftFlank)
                Flank2Roll = self.land_combat_roll(self.Force1.LeftFlank.Target)
                if(Flank1Roll > Flank2Roll):
                    Damage = Flank1Roll - Flank2Roll
                    self.round_morale_damage(DamagedFlank1=self.Force1.LeftFlank.Target,Damage=Damage)
                    self.round_casualties(Winner1=self.Force1.LeftFlank,Loser1=self.Force1.LeftFlank.Target)
                if(Flank2Roll > Flank1Roll):
                    Damage = Flank2Roll - Flank1Roll
                    self.round_morale_damage(DamagedFlank1=self.Force1.LeftFlank,Damage=Damage)
                    self.round_casualties(Winner1=self.Force1.LeftFlank.Target,Loser1=self.Force1.LeftFlank)
                else:
                    pass
            if(not self.Force1.CentreFlank.Defeated):
                self.calculate_strength_bonus(Force1Flank1=self.Force1.CentreFlank,Force2Flank1=self.Force1.CentreFlank.Target)
                Flank1Roll = self.land_combat_roll(self.Force1.CentreFlank)
                Flank2Roll = self.land_combat_roll(self.Force1.CentreFlank.Target)
                if(Flank1Roll > Flank2Roll):
                    Damage = Flank1Roll - Flank2Roll
                    self.round_morale_damage(DamagedFlank1=self.Force1.CentreFlank.Target,Damage=Damage)
                    self.round_casualties(Winner1=self.Force1.CentreFlank,Loser1=self.Force1.CentreFlank.Target)
                if(Flank2Roll > Flank1Roll):
                    Damage = Flank2Roll - Flank1Roll
                    self.round_morale_damage(DamagedFlank1=self.Force1.CentreFlank,Damage=Damage)
                    self.round_casualties(Winner1=self.Force1.CentreFlank.Target,Loser1=self.Force1.CentreFlank)
                else:
                    pass
            if(not self.Force1.RightFlank.Defeated):
                self.calculate_strength_bonus(Force1Flank1=self.Force1.RightFlank,Force2Flank1=self.Force1.RightFlank.Target)
                Flank1Roll = self.land_combat_roll(self.Force1.RightFlank)
                Flank2Roll = self.land_combat_roll(self.Force1.RightFlank.Target)
                if(Flank1Roll > Flank2Roll):
                    Damage = Flank1Roll - Flank2Roll
                    self.round_morale_damage(DamagedFlank1=self.Force1.RightFlank.Target,Damage=Damage)
                    self.round_casualties(Winner1=self.Force1.RightFlank,Loser1=self.Force1.RightFlank.Target)
                if(Flank2Roll > Flank1Roll):
                    Damage = Flank2Roll - Flank1Roll
                    self.round_morale_damage(DamagedFlank1=self.Force1.RightFlank,Damage=Damage)
                    self.round_casualties(Winner1=self.Force1.RightFlank.Target,Loser1=self.Force1.RightFlank)
                else:
                    pass
     
    def flank_retreats(self):
        """
        Function to determine if flanks retreat or are routed.
        """
        if(self.Force1.LeftFlank.Defeated):
            if(not self.Force2.RightFlank.Defeated):
                self.calculate_strength_bonus(self.Force1.LeftFlank,self.Force2.RightFlank)
                self.attempt_retreat(self.Force1.LeftFlank,self.Force2.RightFlank)
        if(self.Force1.CentreFlank.Defeated):
            if(not self.Force2.CentreFlank.Defeated):
                self.calculate_strength_bonus(self.Force1.CentreFlank,self.Force2.CentreFlank)
                self.attempt_retreat(self.Force1.CentreFlank,self.Force2.CentreFlank)
        if(self.Force1.RightFlank.Defeated):
            if(not self.Force2.LeftFlank.Defeated):
                self.calculate_strength_bonus(self.Force1.RightFlank,self.Force2.LeftFlank)
                self.attempt_retreat(self.Force1.RightFlank,self.Force2.LeftFlank)
        if(self.Force2.LeftFlank.Defeated):
            if(not self.Force1.RightFlank.Defeated):
                self.calculate_strength_bonus(self.Force2.LeftFlank,self.Force1.RightFlank)
                self.attempt_retreat(self.Force2.LeftFlank,self.Force1.RightFlank)
        if(self.Force2.CentreFlank.Defeated):
            if(not self.Force1.CentreFlank.Defeated):
                self.calculate_strength_bonus(self.Force2.CentreFlank,self.Force1.CentreFlank)
                self.attempt_retreat(self.Force2.CentreFlank,self.Force1.CentreFlank)
        if(self.Force2.RightFlank.Defeated):
            if(not self.Force1.LeftFlank.Defeated):
                self.calculate_strength_bonus(self.Force2.RightFlank,self.Force1.LeftFlank)
                self.attempt_retreat(self.Force2.RightFlank,self.Force1.LeftFlank)

    def reduce_flank_casualties(self):
        """
        Function to reduce a flank's casualties taken based on its Strength Bonus.
        """
        self.reduce_casualties(self.Force1.LeftFlank)
        self.reduce_casualties(self.Force1.CentreFlank)
        self.reduce_casualties(self.Force1.RightFlank)
        self.reduce_casualties(self.Force2.LeftFlank)
        self.reduce_casualties(self.Force2.CentreFlank)
        self.reduce_casualties(self.Force2.RightFlank)
    
    def battle_winner(self) -> int:
        """
        Function to determine which force won the battle. 1 is Force 1, 2 is Force 2, 0 is error.
        """
        if(
            ((not self.Force1.LeftFlank.Defeated) | (not self.Force1.CentreFlank.Defeated) | (not self.Force1.RightFlank.Defeated))
            &
            ((self.Force2.LeftFlank.Defeated) | (self.Force2.CentreFlank.Defeated) | (self.Force2.RightFlank.Defeated))
        ):
            return 1
        elif(
            ((not self.Force2.LeftFlank.Defeated) | (not self.Force2.CentreFlank.Defeated) | (not self.Force2.RightFlank.Defeated))
            &
            ((self.Force1.LeftFlank.Defeated) | (self.Force1.CentreFlank.Defeated) | (self.Force1.RightFlank.Defeated))
        ):
            return 2
        else:
            print("Error in determining victor")
            return 0
    
    def reset_strength_bonuses(self):
        """
        Function to reset all flanks' Strength Bonus to 0.
        """
        self.Force1.LeftFlank.Strength_Bonus = 0
        self.Force1.CentreFlank.Strength_Bonus = 0
        self.Force1.RightFlank.Strength_Bonus = 0
        self.Force2.LeftFlank.Strength_Bonus = 0
        self.Force2.CentreFlank.Strength_Bonus = 0
        self.Force2.RightFlank.Strength_Bonus = 0

    def base_strength_bonuses(self):
        """
        Function to get Strength Bonuses of each flank, compared to opposite flank.
        """
        self.calculate_strength_bonus(self.Force1.LeftFlank,self.Force2.RightFlank)
        self.calculate_strength_bonus(self.Force1.CentreFlank,self.Force2.CentreFlank)
        self.calculate_strength_bonus(self.Force1.RightFlank,self.Force2.LeftFlank)
    
    def reset_forces(self):
        """
        Function to reset a force's attributes to their original state.
        """
        self.Force1.LeftFlank.Morale = 100
        self.Force1.LeftFlank.Casualties = 0
        self.Force1.LeftFlank.Target = None
        self.Force1.LeftFlank.Defeated = False
        self.Force1.CentreFlank.Morale = 100
        self.Force1.CentreFlank.Casualties = 0
        self.Force1.CentreFlank.Target = None
        self.Force1.CentreFlank.Defeated = False
        self.Force1.RightFlank.Morale = 100
        self.Force1.RightFlank.Casualties = 0
        self.Force1.RightFlank.Target = None
        self.Force1.RightFlank.Defeated = False
        self.Force2.LeftFlank.Morale = 100
        self.Force2.LeftFlank.Casualties = 0
        self.Force2.LeftFlank.Target = None
        self.Force2.LeftFlank.Defeated = False
        self.Force2.CentreFlank.Morale = 100
        self.Force2.CentreFlank.Casualties = 0
        self.Force2.CentreFlank.Target = None
        self.Force2.CentreFlank.Defeated = False
        self.Force2.RightFlank.Morale = 100
        self.Force2.RightFlank.Casualties = 0
        self.Force2.RightFlank.Target = None
        self.Force2.RightFlank.Defeated = False
        self.reset_strength_bonuses()

    def battle(self) -> int:
        """
        Function to roll a Large Battle between two forces.

        Returns:
            Result (int): Result of the battle, 1 for Force 1 winning, 2 for Force 2 winning, or 0 for errors.
        """
        self.reset_forces()
        self.assign_starting_targets()
        while(
            ((not self.Force1.LeftFlank.Defeated) | (not self.Force1.CentreFlank.Defeated) | (not self.Force1.RightFlank.Defeated))
            &
            ((not self.Force2.LeftFlank.Defeated) | (not self.Force2.CentreFlank.Defeated) | (not self.Force2.RightFlank.Defeated))
        ):
            self.reset_strength_bonuses()
            self.check_if_flanks_defeated()
            self.flank_damage()
        self.reset_strength_bonuses()
        self.base_strength_bonuses()
        self.flank_retreats()
        self.reduce_flank_casualties()
        Victor = self.battle_winner()
        return Victor