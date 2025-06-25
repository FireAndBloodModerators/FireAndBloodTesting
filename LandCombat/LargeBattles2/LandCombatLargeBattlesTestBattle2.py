# IMPORTS
import math
import random
from LandCombatLargeBattlesTestForce2 import Force
from LandCombatLargeBattlesTestFlank2 import Flank

# CLASS
class Battle:
    """
    A class representing Land Combat Battles for r/FireAndBlood.

    Attributes:
        Force1 (Force): The first Force.
        Force2 (Force): The second Force.
        CombatPairs (list[list[Flank]]): The flanks of each force that are actively fighting each other.
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
        self.CombatPairs:list[list[Flank]] = [[self.Force1.LeftFlank,self.Force2.RightFlank],[self.Force1.CentreFlank,self.Force2.CentreFlank],[self.Force1.RightFlank,self.Force2.LeftFlank]]

    def check_if_in_combat_pairs(self,FlankCheck:Flank) -> bool:
        """
        Function to determine new Combat Pairs and supporters.

        Arguments:
            FlankCheck (Flank): The flank being checked in Combat Pairs.

        Returns:
            Result (bool): Result of the check, True for flank is in Combat Pairs, False for flank is not in Combat Pairs.
        """
    
    def set_combat_pairs(self):
        """
        Function to determine new Combat Pairs and supporters.
        """
        if(not self.Force1.LeftFlank.Defeated):
            self.check_if_in_combat_pairs(self.Force1.LeftFlank)
    
    def reset_supporters(self):
        """
        Function to reset a flank's supporters.
        """
        self.Force1.LeftFlank.Supporters = []
        self.Force1.CentreFlank.Supporters = []
        self.Force1.RightFlank.Supporters = []
        self.Force2.LeftFlank.Supporters = []
        self.Force2.CentreFlank.Supporters = []
        self.Force2.RightFlank.Supporters = []
    
    def assign_new_targets(self):
        """
        Function to determine new targets of each force's flanks.
        """
        self.CombatPairs = []
        self.reset_supporters()
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
                elif(not self.Force2.LeftFlank.Defeated):
                    self.Force1.CentreFlank.Target = self.Force2.LeftFlank
                    if(self.Force2.LeftFlank.Target.Target is not self.Force2.LeftFlank):
                        self.Force2.LeftFlank.Target = self.Force1.CentreFlank
                elif(not self.Force2.RightFlank.Defeated):
                    self.Force1.CentreFlank.Target = self.Force2.RightFlank
                    if(self.Force2.RightFlank.Target.Target is not self.Force2.RightFlank):
                        self.Force2.RightFlank.Target = self.Force1.CentreFlank
                elif(Force2Flanks == 0):
                    pass
                else:
                    print("Error in new target for Force 1 Centre Flank")
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
                elif(not self.Force1.LeftFlank.Defeated):
                    self.Force2.CentreFlank.Target = self.Force1.LeftFlank
                    if(self.Force1.LeftFlank.Target.Target is not self.Force1.LeftFlank):
                        self.Force1.LeftFlank.Target = self.Force2.CentreFlank
                elif(not self.Force1.RightFlank.Defeated):
                    self.Force2.CentreFlank.Target = self.Force1.RightFlank
                    if(self.Force1.RightFlank.Target.Target is not self.Force1.RightFlank):
                        self.Force1.RightFlank.Target = self.Force2.CentreFlank
                elif(Force1Flanks == 0):
                    pass
                else:
                    print("Error in new target for Force 2 Centre Flank")
        self.set_combat_pairs()
    
    def check_if_forces_defeated(self):
        """
        Function to determine if all of a force's flanks are defeated.
        """
        if(self.Force1.LeftFlank.Defeated & self.Force1.CentreFlank.Defeated & self.Force1.RightFlank):
            self.Force1.Defeated = True
        if(self.Force2.LeftFlank.Defeated & self.Force2.CentreFlank.Defeated & self.Force2.RightFlank):
            self.Force2.Defeated = True
    
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
        self.check_if_forces_defeated()
        if((not self.Force1.Defeated) & (not self.Force2.Defeated)):
            self.assign_new_targets()
    
    def round_casualties(self,Winner:Flank,Loser:Flank):
        """
        Function to increase a flank's battle casualties based.
    
        Arguments:
            Winner1 (Flank): The flank that won the battle round.
            Loser1 (Flank): The flank that lost the battle round.
        """
        Winner.Casualties += 1
        for Supporter in Winner.Supporters:
            Supporter.Casualties += 1
        Loser.Casualties += (random.randint(1,3) + 1)
        for Supporter in Loser.Supporters:
            Supporter.Casualties += (random.randint(1,3) + 1)
    
    def round_morale_damage(self,DamagedFlank:Flank,Damage:int):
        """
        Function to reduce a flank's morale by the damage dealt in a combat round.
    
        Arguments:
            DamagedFlank (Flank): The flank that is taking damage.
            Damage (int): The damage dealt in the combat round to the flank.
        """
        DamagedFlank.Morale -= Damage
        for Supporter in DamagedFlank.Supporters:
            Supporter.Morale -= Damage
    
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
    
    def calculate_strength_bonus(self,Flank1:Flank,Flank1TotalCombatValue:int,Flank2:Flank,Flank2TotalCombatValue:int):
        """
        Function to calculate the stronger flank in a battle and that flank's Strength Bonus based on total Combat Value of a flank and its supporters.
    
        Arguments:
            Flank1 (Flank): The first flank in the combat pair
            Flank1TotalCombatValue (int): The total Combat Value of Flank 1 and its supporters.
            Flank2 (Flank): The second flank in the combat pair.
            Flank2TotalCombatValue (int): The total Combat Value of Flank 2 and its supporters.
        """
        if(Flank1TotalCombatValue > Flank2TotalCombatValue):
            Strength_Percentage = ((Flank1TotalCombatValue/Flank2TotalCombatValue)-1)*100
            if(Strength_Percentage >= 5):
                Flank1.Strength_Bonus = math.ceil(Strength_Percentage/20) + (len(Flank1.Supporters)*3)
        elif(Flank2TotalCombatValue > Flank1TotalCombatValue):
            Strength_Percentage = ((Flank2TotalCombatValue/Flank1TotalCombatValue)-1)*100
            if(Strength_Percentage >= 5):
                Flank2.Strength_Bonus = math.ceil(Strength_Percentage/20) + (len(Flank2.Supporters)*3)
        else:
            pass
    
    def flank_damage(self):
        """
        Function to have each flank deal damage to its target.
        """
        for CombatPair in self.CombatPairs:
            CombatPairFlank1TotalCombatValue = CombatPair[0].Combat_Value
            for Supporter in CombatPair[0].Supporters:
                CombatPairFlank1TotalCombatValue += Supporter.Combat_Value
            CombatPairFlank2TotalCombatValue = CombatPair[1].Combat_Value
            for Supporter in CombatPair[1].Supporters:
                CombatPairFlank2TotalCombatValue += Supporter.Combat_Value
            self.calculate_strength_bonus(CombatPair[0],CombatPairFlank1TotalCombatValue,CombatPair[1],CombatPairFlank2TotalCombatValue)
            Flank1Roll = self.land_combat_roll(CombatPair[0])
            Flank2Roll = self.land_combat_roll(CombatPair[1])
            if(Flank1Roll > Flank2Roll):
                Damage = Flank1Roll - Flank2Roll
                self.round_morale_damage(DamagedFlank=CombatPair[1],Damage=Damage)
                self.round_casualties(Winner=CombatPair[0],Loser=CombatPair[1])
            elif(Flank2Roll > Flank1Roll):
                Damage = Flank2Roll - Flank1Roll
                self.round_morale_damage(DamagedFlank=CombatPair[0],Damage=Damage)
                self.round_casualties(Winner=CombatPair[1],Loser=CombatPair[0])
            else:
                pass
    
    def reset_combat_pairs(self):
        """
        Function to reset the Combat Pairs of a battle.
        """
        self.CombatPairs:list[list[Flank]] = [[self.Force1.LeftFlank,self.Force2.RightFlank],[self.Force1.CentreFlank,self.Force2.CentreFlank],[self.Force1.RightFlank,self.Force2.LeftFlank]]
    
    def reset_targets(self):
        """
        Function to assign the starting targets of each force's flanks.
        """
        self.Force1.LeftFlank.Target = self.Force2.RightFlank
        self.Force1.CentreFlank.Target = self.Force2.CentreFlank
        self.Force1.RightFlank.Target = self.Force2.LeftFlank
        self.Force2.LeftFlank.Target = self.Force1.RightFlank
        self.Force2.CentreFlank.Target = self.Force1.CentreFlank
        self.Force2.RightFlank.Target = self.Force1.LeftFlank
    
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
    
    def reset_forces(self):
        """
        Function to reset a force's attributes to their original state.
        """
        self.Force1.Defeated = False
        self.Force1.LeftFlank.Morale = 100
        self.Force1.LeftFlank.Casualties = 0
        self.Force1.LeftFlank.Target = None
        self.Force1.LeftFlank.Supporters = []
        self.Force1.LeftFlank.Defeated = False
        self.Force1.CentreFlank.Morale = 100
        self.Force1.CentreFlank.Casualties = 0
        self.Force1.CentreFlank.Target = None
        self.Force1.CentreFlank.Supporters = []
        self.Force1.CentreFlank.Defeated = False
        self.Force1.RightFlank.Morale = 100
        self.Force1.RightFlank.Casualties = 0
        self.Force1.RightFlank.Target = None
        self.Force1.RightFlank.Supporters = []
        self.Force1.RightFlank.Defeated = False
        self.Force2.Defeated = False
        self.Force2.LeftFlank.Morale = 100
        self.Force2.LeftFlank.Casualties = 0
        self.Force2.LeftFlank.Target = None
        self.Force2.LeftFlank.Supporters = []
        self.Force2.LeftFlank.Defeated = False
        self.Force2.CentreFlank.Morale = 100
        self.Force2.CentreFlank.Casualties = 0
        self.Force2.CentreFlank.Target = None
        self.Force2.CentreFlank.Supporters = []
        self.Force2.CentreFlank.Defeated = False
        self.Force2.RightFlank.Morale = 100
        self.Force2.RightFlank.Casualties = 0
        self.Force2.RightFlank.Target = None
        self.Force2.RightFlank.Supporters = []
        self.Force2.RightFlank.Defeated = False
        self.reset_strength_bonuses()
        self.reset_targets()
        self.reset_combat_pairs()
    
    def battle(self) -> int:
        """
        Function to roll a Large Battle between two forces.

        Returns:
            Result (int): Result of the battle, 1 for Force 1 winning, 2 for Force 2 winning, or 0 for errors.
        """
        self.reset_forces()
        while((not self.Force1.Defeated) & (not self.Force2.Defeated)):
            self.reset_strength_bonuses()
            self.flank_damage()
            self.check_if_flanks_defeated()
        self.reset_strength_bonuses()