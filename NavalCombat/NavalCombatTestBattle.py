# IMPORTS
import math
import random
from NavalCombatTestFleet import Fleet

# CLASS
class Battle:
    """
    A class representing Naval Combat Battles for r/FireAndBlood.

    Attributes:
        Fleet1 (Fleet): The first Fleet.
        Fleet2 (Fleet): The second Fleet.
    """

    def __init__(self,Fleet1:Fleet,Fleet2:Fleet):
        """
        Initialiser function for Naval Combat Battles.
    
        Arguments:
            Fleet1 (Fleet): The first Fleet.
            Fleet2 (Fleet): The second Fleet.
        """
        self.Fleet1:Fleet = Fleet1
        self.Fleet2:Fleet = Fleet2
        self.calculate_strength_bonus()

    def calculate_strength_bonus(self):
        """
        Function to calculate the stronger fleet in a battle and that fleet's strength bonus.
        """
        if(self.Fleet1.Combat_Value > self.Fleet2.Combat_Value):
            Strength_Percentage = ((self.Fleet1.Combat_Value/self.Fleet2.Combat_Value)-1)*100
            if(Strength_Percentage >= 5):
                self.Fleet1.Strength_Bonus = math.ceil(Strength_Percentage/40)
        if(self.Fleet2.Combat_Value > self.Fleet1.Combat_Value):
            Strength_Percentage = ((self.Fleet2.Combat_Value/self.Fleet1.Combat_Value)-1)*100
            if(Strength_Percentage >= 5):
                self.Fleet2.Strength_Bonus = math.ceil(Strength_Percentage/40)
        else:
            pass

    def land_combat_roll(self,RollingFleet:Fleet) -> int:
        """
        Function to roll 2d50 and add a fleet's bonuses.
    
        Arguments:
            RollingFleet (Fleet): The Fleet that is rolling.

        Returns:
            Combat_Roll (int): The 2d50 roll plus a fleet's bonuses.
        """
        Combat_Roll = random.randint(1,50) + random.randint(1,50) + RollingFleet.Strength_Bonus + RollingFleet.Skill_Bonus
        return Combat_Roll
    
    def round_morale_damage(self,DamagedFleet:Fleet,Damage:int):
        """
        Function to reduce a fleet's morale by the damage dealt in a combat round.
    
        Arguments:
            DamagedFleet (Fleet): The Fleet that is taking damage.
            Damage (int): The damage dealt in the combat round to the Fleet.
        """
        DamagedFleet.Morale -= Damage

    def round_casualties(self,Winner:Fleet,Loser:Fleet):
        """
        Function to increase a Fleet's battle casualties based.
    
        Arguments:
            Winner (Fleet): The Fleet that won the battle round.
            Loser (Fleet): The Fleet that lost the battle round.
        """
        Winner.Casualties += 1
        Loser.Casualties += (random.randint(1,3) + 1)

    def reduce_casualties(self,ReducedCasualtiesFleet:Fleet):
        """
        Function to reduce a fleet's casualties taken based on its Strength Bonus.

        Arguments:
            ReducedCasualtiesFleet (Fleet): The Fleet that is having its casualties reduced.
        """
        CasualtyReductionAmount = (ReducedCasualtiesFleet.Strength_Bonus * 5) if ((ReducedCasualtiesFleet.Strength_Bonus * 5) < 50) else 50
        ReducedCasualtiesFleet.Casualties = round(ReducedCasualtiesFleet.Casualties * (1 - (CasualtyReductionAmount/100)))

    def attempt_retreat(self,RetreatingFleet:Fleet,NonRetreatingFleet:Fleet):
        """
        Function to trigger a retreat or a rout for a defeated Fleet.

        Arguments:
            RetreatingFleet (Fleet): The Fleet that is attempting to retreat.
            NonRetreatingFleet (Fleet): The Fleet that is attempting to pursue.
        """
        if(RetreatingFleet.Morale > 0):
            RetreatThreshold = 8 + (NonRetreatingFleet.Speed/2) - (RetreatingFleet.Speed/2)
            RetreatRoll = random.randint(1,20)
            if(RetreatRoll < RetreatThreshold):
                RetreatingFleet.Casualties += (random.randint(1,5) + random.randint(1,5) + 5)
        else:
            RetreatingFleet.Casualties += (random.randint(1,20) + random.randint(1,20) + 10)

    def reset_fleets(self):
        """
        Function to reset a Fleet's attributes to their original state.
        """
        self.Fleet1.Morale = 100
        self.Fleet1.Casualties = 0
        self.Fleet2.Morale = 100
        self.Fleet2.Casualties = 0

    def battle(self) -> int:
        """
        Function to roll a Battle between two Fleets.

        Returns:
            Result (int): Result of the battle, 1 for Fleet 1 winning, 2 for Fleet 2 winning, or 0 for errors.
        """
        self.reset_fleets()
        while((self.Fleet1.Morale > self.Fleet1.Retreat_Threshold) & (self.Fleet2.Morale > self.Fleet2.Retreat_Threshold)):
            Fleet1Roll = self.land_combat_roll(self.Fleet1)
            Fleet2Roll = self.land_combat_roll(self.Fleet2)
            if(Fleet1Roll > Fleet2Roll):
                Damage = Fleet1Roll - Fleet2Roll
                self.round_morale_damage(self.Fleet2,Damage)
                self.round_casualties(self.Fleet1,self.Fleet2)
            elif(Fleet2Roll > Fleet1Roll):
                Damage = Fleet2Roll - Fleet1Roll
                self.round_morale_damage(self.Fleet1,Damage)
                self.round_casualties(self.Fleet2,self.Fleet1)
            else:
                pass
        if((self.Fleet1.Morale > self.Fleet1.Retreat_Threshold) & (self.Fleet2.Morale <= self.Fleet2.Retreat_Threshold)):
            self.attempt_retreat(self.Fleet2,self.Fleet1)
            if(self.Fleet1.Strength_Bonus > self.Fleet2.Strength_Bonus):
                self.reduce_casualties(self.Fleet1)
            elif(self.Fleet2.Strength_Bonus > self.Fleet1.Strength_Bonus):
                self.reduce_casualties(self.Fleet2)
            else:
                pass
            Result = 1
            return Result
        elif((self.Fleet2.Morale > self.Fleet2.Retreat_Threshold) & (self.Fleet1.Morale <= self.Fleet1.Retreat_Threshold)):
            self.attempt_retreat(self.Fleet1,self.Fleet2)
            if(self.Fleet1.Strength_Bonus > self.Fleet2.Strength_Bonus):
                self.reduce_casualties(self.Fleet1)
            elif(self.Fleet2.Strength_Bonus > self.Fleet1.Strength_Bonus):
                self.reduce_casualties(self.Fleet2)
            else:
                pass
            Result = 2
            return Result
        else:
            print("Error")
            Result = 0
            return Result