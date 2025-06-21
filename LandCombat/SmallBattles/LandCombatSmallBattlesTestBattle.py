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

    def land_combat_roll(self,RollingForce:Force) -> int:
        """
        Function to roll 2d50 and add a force's bonuses.
    
        Arguments:
            Force (Force): The Force that is rolling.

        Returns:
            Combat_Roll (int): The 2d50 roll plus a force's bonuses.
        """
        Combat_Roll = random.randint(1,50) + random.randint(1,50) + RollingForce.Strength_Bonus + RollingForce.Terrain_Bonus + RollingForce.Skill_Bonus
        return Combat_Roll
    
    def round_morale_damage(self,DamagedForce:Force,Damage:int):
        """
        Function to reduce a force's morale by the damage dealt in a combat round.
    
        Arguments:
            DamagedForce (Force): The Force that is taking damage.
            Damage (int): The damage dealt in the combat round to the force.
        """
        DamagedForce.Morale -= Damage

    def round_casualties(self,Winner:Force,Loser:Force):
        """
        Function to increase a force's battle casualties based.
    
        Arguments:
            Winner (Force): The force that won the battle round.
            Loser (Force): The force that lost the battle round.
        """
        Winner.Casualties += 1
        Loser.Casualties += (random.randint(1,3) + 1)

    def reduce_casualties(self,ReducedCasualtiesForce:Force):
        """
        Function to reduce a force's casualties taken based on its Strength Bonus.

        Arguments:
            ReducedCasualtiesForce (Force): The force that is having its casualties reduced.
        """
        CasualtyReductionAmount = (ReducedCasualtiesForce.Strength_Bonus * 5) if ((ReducedCasualtiesForce.Strength_Bonus * 5) < 50) else 50
        ReducedCasualtiesForce.Casualties = round(ReducedCasualtiesForce.Casualties * (1 - (CasualtyReductionAmount/100)))

    def attempt_retreat(self,RetreatingForce:Force,NonRetreatingForce:Force):
        """
        Function to trigger a retreat or a rout for a defeated force.

        Arguments:
            RetreatingForce (Force): The force that is attempting to retreat.
        """
        if(RetreatingForce.Morale > 0):
            RetreatThreshold = 8 + NonRetreatingForce.Speed - RetreatingForce.Speed
            RetreatRoll = random.randint(1,20)
            if(RetreatRoll < RetreatThreshold):
                RetreatingForce.Casualties += (random.randint(1,5) + random.randint(1,5))
        else:
            RetreatingForce.Casualties += (random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + 5)

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
        while((self.Force1.Morale > self.Force1.Retreat_Threshold) & (self.Force2.Morale > self.Force2.Retreat_Threshold)):
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
        if((self.Force1.Morale > self.Force1.Retreat_Threshold) & (self.Force2.Morale <= self.Force2.Retreat_Threshold)):
            self.attempt_retreat(self.Force2,self.Force1)
            if(self.Force1.Strength_Bonus > self.Force2.Strength_Bonus):
                self.reduce_casualties(self.Force1)
            elif(self.Force2.Strength_Bonus > self.Force1.Strength_Bonus):
                self.reduce_casualties(self.Force2)
            else:
                pass
            Result = 1
            return Result
        elif((self.Force2.Morale > self.Force2.Retreat_Threshold) & (self.Force1.Morale <= self.Force1.Retreat_Threshold)):
            self.attempt_retreat(self.Force1,self.Force2)
            if(self.Force1.Strength_Bonus > self.Force2.Strength_Bonus):
                self.reduce_casualties(self.Force1)
            elif(self.Force2.Strength_Bonus > self.Force1.Strength_Bonus):
                self.reduce_casualties(self.Force2)
            else:
                pass
            Result = 2
            return Result
        else:
            print("Error")
            Result = 0
            return Result