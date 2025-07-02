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
        SiegeDuration (int): The duration of the Siege, in months.
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
        self.SiegeRollBonus:int = self.calculate_starting_siege_roll_malus()
        self.BesiegersCasualties:int = 0
        self.DefendersCasualties:int = 0
        self.SiegeDuration:int = 0

    def calculate_starting_siege_roll_malus(self) -> int:
        """
        Function to calculate the starting Siege Roll malus based off of Holdfast Size and Outer Walls DV.

        Returns:
            int: The starting malus to the Siege Rolls.
        """
        if(self.OuterWallsDV > 0):
            return (5 - math.floor(self.OuterWallsDV))
        else:
            return (5 - self.HoldfastSize)
        
    def siege_roll(self):
        """
        Function to make a Siege Roll and add bonuses, calculating effect.

        Returns:
            int: Whether or not the Siege has ended. 1 for surrender, 2 for continue.
        """
        self.SiegeDuration += 1
        BaseSiegeRoll = random.randint(1,20)
        SiegeRoll = BaseSiegeRoll + self.SiegeRollBonus
        if(SiegeRoll <= 4):
            if(BaseSiegeRoll == 1):
                self.BesiegersCasualties += (10 * ((100-self.BesiegersCasualties)/100))
            return 2
        elif(SiegeRoll <= 8):
            self.SiegeRollBonus += 2
            self.DefendersCasualties += (2 * ((100-self.DefendersCasualties)/100))
            return 2
        elif(SiegeRoll <= 15):
            self.SiegeRollBonus += 4
            self.DefendersCasualties += (6 * ((100-self.DefendersCasualties)/100))
            return 2
        elif(SiegeRoll <= 19):
            self.SiegeRollBonus += 8
            self.DefendersCasualties += (10 * ((100-self.DefendersCasualties)/100))
            return 2
        elif(SiegeRoll <= 23):
            self.SiegeRollBonus += 4
            self.DefendersCasualties += (20 * ((100-self.DefendersCasualties)/100))
            return 2
        else:
            return 1
        
    def reset_siege(self):
        """
        Function to reset Siege statistics to beginning values.
        """
        self.SiegeRollBonus = self.calculate_starting_siege_roll_malus()
        self.BesiegersCasualties = 0
        self.DefendersCasualties = 0
        self.SiegeDuration = 0

    def siege(self) -> list[int]:
        """
        Function to simulate a Siege.

        Returns:
            Results (list[int]): The results of the Siege, including duration, besiegers' casualties, and defenders' casualties.
        """
        self.reset_siege()
        SiegeOver = False
        while(not SiegeOver):
            SiegeRollResult = self.siege_roll()
            if(SiegeRollResult == 1):
                SiegeOver = True
        Results:list[int] = [self.SiegeDuration,self.BesiegersCasualties,self.DefendersCasualties]
        return Results
