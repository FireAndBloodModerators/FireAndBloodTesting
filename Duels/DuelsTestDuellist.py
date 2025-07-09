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

    def __init__(self):
        """
        Initialiser function for a Duels Duellist.
        """
        self.Morale:int = 30
        self.DuelBonus:int = 0
        self.DamageBonus:int = 0
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
    
    def injury_roll_a(self):
        """
        Function to roll 1d100 on Injury Table A after Duellist receives a Critical Strike.
        """
        self.DuelBonus -= 2
        InjuryRoll = random.randint(1,100)
        if(InjuryRoll <= 5):
            self.CriticalInjuries += 1
        elif(InjuryRoll <= 50):
            self.MajorInjuries += 1
        else:
            self.MinorInjuries += 1

    def injury_roll_b(self):
        """
        Function to roll 1d100 on Injury Table B after Duellist is brought to 0 Morale.
        """
        InjuryRoll = random.randint(1,100)
        if(InjuryRoll <= 30):
            self.Deaths += 1
        elif(InjuryRoll <= 40):
            self.CriticalInjuries += 1
        elif(InjuryRoll <= 70):
            self.MajorInjuries += 1
        else:
            self.MinorInjuries += 1