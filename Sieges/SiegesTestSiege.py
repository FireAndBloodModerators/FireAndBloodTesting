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

    def calculate_siege_roll_bonus(self):
        """
        Function to calculate the starting Siege Roll Bonus based off of Holdfast Size and Outer Walls DV.
        """