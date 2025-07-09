# IMPORTS
import random

# CLASS
class Duellist:
    """
    A class representing a Duels Duellist for r/FireAndBlood.

    Attributes:
        Morale (int): The morale/fighting spirit of the Duellist.
        DuelBonus (int): The Duellist's bonus to Duel Rolls.
        DamageBonus (int): The Duellist's bonus to Damage Rolls.
        MinorInjuries (int): The number of Minor Injuries the Duellist has taken.
        MajorInjuries (int): The number of Major Injuries the Duellist has taken.
        CriticalInjuries (int): The number of Critical Injuries the Duellist has taken.
        Deaths (int): The number of times the Duellist has died.
    """

    def __init__(self,DuelBonus:int,DamageBonus:int):
        """
        Initialiser function for a Duels Duellist.
    
        Arguments:
            DuelBonus (int): The Duellist's bonus to Duel Rolls.
            DamageBonus (int): The Duellist's bonus to Damage Rolls.
        """
        self.Morale:int = 30
        self.DuelBonus:int = DuelBonus
        self.DamageBonus:int = DamageBonus
        self.MinorInjuries:int = 0
        self.MajorInjuries:int = 0
        self.CriticalInjuries:int = 0
        self.Deaths:int = 0

    def duel_roll(self) -> tuple[int,int|None]:
        """
        Function to roll 1d20 plus Duellist's Duel Bonus and return result and whether it was a Critical Strike.
    
        Returns:
            DuelRoll (int): The Duellist's Duel Roll.
            CriticalStrike (int|None): The Duellist's bonus to Damage Rolls.
        """
        DuelRoll = random.randint(1,20)
        if(DuelRoll == 20):
            CriticalStrike = 20
        elif(DuelRoll == 1):
            CriticalStrike = 1
        else:
            CriticalStrike = None
        DuelRoll += self.DuelBonus
        return DuelRoll,CriticalStrike
    
    def damage_roll(self) -> int:
        """
        Function to roll 2d5 plus Duellist's Damage Bonus and return result.

        Returns:
            DamageRoll (int): The Duellist's Damage Roll.
        """
        DamageRoll = random.randint(1,5) + random.randint(1,5) + self.DamageBonus
        return DamageRoll