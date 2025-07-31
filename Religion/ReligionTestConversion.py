# IMPORTS
import random

# CLASS
class Conversion:
    """
    A class representing a Religion Conversion for r/FireAndBlood.

    Attributes:
        Morale (int): The morale/fighting spirit of the Duellist.
        DuelBonus (int): The Duellist's bonus to Duel Rolls.
        WeaponType (str): The weapon the Duellist is wielding.
        DamageBonus (int): The Duellist's bonus to Damage Rolls.
        MinorInjuries (int): The number of Minor Injuries the Duellist has taken.
        MajorInjuries (int): The number of Major Injuries the Duellist has taken.
        CriticalInjuries (int): The number of Critical Injuries the Duellist has taken.
        Deaths (int): The number of times the Duellist has died.
        Defeated (bool): Whether or not the Duellist is defeated.
    """

    def __init__(self):
        """
        Initialiser function for a Religion Conversion.

        Arguments:
            WeaponType (str): What weapon the Duellist is wielding, determines DamageBonus.
        """
        self.Morale:int = 30
        self.DuelBonus:int = 0
        self.DamageBonus:int = self.determine_damage_bonus()
        self.MinorInjuries:int = 0
        self.MajorInjuries:int = 0
        self.CriticalInjuries:int = 0
        self.Deaths:int = 0
        self.Defeated:bool = False
