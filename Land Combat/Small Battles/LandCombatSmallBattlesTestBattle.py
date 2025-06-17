# IMPORTS
import math
import random
from LandCombatSmallBattlesTestForce import Force

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
        self.calculate_strength_bonus(Force1,Force2)

    def calculate_strength_bonus(self,Force1:Force,Force2:Force):
        """
        Function to calculate the stronger force in a battle and that force's strength bonus.
    
        Arguments:
            Force1 (Force): The first Force.
            Force2 (Force): The second Force.
        """
        if(Force1.Combat_Value > Force2.Combat_Value):
            Strength_Percentage = ((Force1.Combat_Value/Force2.Combat_Value)-1)*100
            if(Strength_Percentage >= 5):
                Force1.Strength_Bonus = math.ceil(Strength_Percentage/20)
        if(Force2.Combat_Value > Force1.Combat_Value):
            Strength_Percentage = ((Force2.Combat_Value/Force1.Combat_Value)-1)*100
            if(Strength_Percentage >= 5):
                Force2.Strength_Bonus = math.ceil(Strength_Percentage/20)
        else:
            pass

    def land_combat_roll(self,Force:Force) -> int:
        """
        Function to roll 2d50 and add a force's bonuses.
    
        Arguments:
            Force (Force): The Force that is rolling.

        Returns:
            Combat_Roll (int): The 2d50 roll plus a force's bonuses.
        """
        Combat_Roll = random.randint(1,50) + random.randint(1,50) + Force.Strength_Bonus + Force.Terrain_Bonus + Force.Skill_Bonus
        return Combat_Roll
    
    def round_morale_damage(self,Force:Force,Damage:int):
        """
        Function to reduce a force's morale by the damage dealt in a combat round.
    
        Arguments:
            Force (Force): The Force that is taking damage.
            Damage (int): The damage dealt in the combat round to the force.
        """
        Force.Morale = Force.Morale - Damage

    def round_casualties(self,Winner:Force,Loser:Force):
        """
        Function to increase a force's battle casualties based.
    
        Arguments:
            Force (Force): The Force that is taking damage.
            Damage (int): The damage dealt in the combat round to the force.
        """
        Winner.Casualties = Winner.Casualties + random.randint(1,3)
        Loser.Casualties = Loser.Casualties + random.randint(1,3) + 3

    def reset_forces(self):
        """
        Function to reduce a force's morale by the damage dealt in a combat round.
        """
        self.Force1.Morale = 100
        self.Force1.Casualties = 0
        self.Force2.Morale = 100
        self.Force2.Casualties = 0

    def battle(self) -> int:
        """
        Function to roll a battle between two forces.

        Returns:
            Result (int): Result of the battle, 1 for Force 1 winning, 2 for Force 2 winning, or 0 for errors.
        """
        self.reset_forces()
        while((self.Force1.Morale > 0) & (self.Force2.Morale > 0)):
            Force1Roll = self.land_combat_roll(self.Force1)
            Force2Roll = self.land_combat_roll(self.Force2)
            if(Force1Roll > Force2Roll):
                Damage = Force1Roll - Force2Roll
                self.round_morale_damage(self.Force2,Damage)
                self.round_casualties(self.Force1,self.Force2)
            elif(Force2Roll > Force1Roll):
                Damage = Force2Roll - Force1Roll
                self.round_morale_damage(self.Force1,Damage)
                self.round_casualties(self.Force2,self.Force1)
            else:
                pass
        if((self.Force1.Morale > 0) & (self.Force2.Morale <= 0)):
            Result = 1
            return Result
        elif((self.Force2.Morale > 0) & (self.Force1.Morale <= 0)):
            Result = 2
            return Result
        else:
            print("Error")
            Result = 0
            return Result