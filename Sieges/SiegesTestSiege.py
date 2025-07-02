# IMPORTS
import math
import random

# CLASS
class Siege:
    """
    A class representing Sieges for r/FireAndBlood.

    Attributes:
        HoldfastSize (int): The Size of the Holdfast being besieged.
        OuterWallsDV (int): The DV of the Outer Walls being besieged.
        SiegeRollBonus (int): The bonus to the Siege's Siege Roll.
        BesiegersCasualties (int): The casualty percentage taken by the besiegers.
        DefendersCasualties (int): The casualty percentage taken by the defenders.
    """

    def __init__(self,HoldfastSize:int,OuterWallsDV:int):
        """
        Initialiser function for Sieges.
    
        Arguments:
            HoldfastSize (int): The Size of the Holdfast being besieged.
            OuterWallsDV (int): The DV of the Walls being besieged.
        """
        self.HoldfastSize:int = HoldfastSize
        self.OuterWallsDV:int = OuterWallsDV
        self.SiegeRollBonus:int = self.calculate_siege_roll_bonus()
        self.BesiegersCasualties:int = 0
        self.DefendersCasualties:int = 0

    def calculate_siege_roll_bonus(self) -> int:
        """
        Function to calculate the starting Siege Roll Bonus based off of Holdfast Size and Outer Walls DV.

        Returns:
            int: The starting bonus to the Siege Rolls.
        """
        if(self.OuterWallsDV > 0):
            return math.floor(self.OuterWallsDV)
        else:
            return math.floor(self.HoldfastSize/2)
        
    def siege_roll(self):
        """
        Function to make a Siege Roll and add bonuses, calculating effect.

        Returns:
            int: Whether or not the Siege has ended. 1 for surrender, 2 for continue.
        """
        BaseSiegeRoll = random.randint(1,20)
        SiegeRoll = BaseSiegeRoll + self.SiegeRollBonus
        if(SiegeRoll <= 6):
            if(BaseSiegeRoll == 1):
                self.BesiegersCasualties += (10 * ((100-self.BesiegersCasualties)/100))
            return 2
        elif(SiegeRoll <= 15):
            self.SiegeRollBonus += 2
            self.DefendersCasualties += (2 * ((100-self.DefendersCasualties)/100))
            return 2
        elif(SiegeRoll <= 19):
            self.SiegeRollBonus += 4
            self.DefendersCasualties += (6 * ((100-self.DefendersCasualties)/100))
            return 2
        elif(SiegeRoll <= 22):
            self.SiegeRollBonus += 8
            self.DefendersCasualties += (10 * ((100-self.DefendersCasualties)/100))
            return 2
        elif(SiegeRoll <= 27):
            self.SiegeRollBonus += 4
            self.DefendersCasualties += (20 * ((100-self.DefendersCasualties)/100))