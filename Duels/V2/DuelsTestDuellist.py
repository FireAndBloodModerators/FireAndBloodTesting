# IMPORTS
import random

# CLASS
class Duellist:
    """
    A class representing a Duels Duellist for r/FireAndBlood.

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

    def __init__(self,WeaponType:str):
        """
        Initialiser function for a Duels Duellist.

        Arguments:
            WeaponType (str): What weapon the Duellist is wielding, determines DamageBonus.
        """
        self.Morale:int = 30
        self.DuelBonus:int = 0
        self.WeaponType = WeaponType
        self.DamageBonus:int = self.determine_damage_bonus()
        self.MinorInjuries:int = 0
        self.MajorInjuries:int = 0
        self.CriticalInjuries:int = 0
        self.Deaths:int = 0
        self.Defeated:bool = False

    def determine_damage_bonus(self) -> int:
        """
        Function to determine Duellist's Damage Bonus.

        Returns:
            int: The Duellist's Damage Bonus based on their weapon.
        """
        if(self.WeaponType == "VS"):
            return 3
        elif(self.WeaponType == "MW/FO"):
            return 2
        elif(self.WeaponType == "MW"):
            return 1
        elif(self.WeaponType == "FO"):
            return 1
        else:
            return 0

    def duel_roll(self) -> tuple[int,int]:
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
            CriticalStrike = 0
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

    def injury_roll(self):
        """
        Function to make an Injury Roll after a Critical Strike.
        """
        InjuryRoll = random.randint(1,100)
        if(InjuryRoll <= 20):
            self.Deaths += 1
            self.Defeated = True
        elif(InjuryRoll <= 40):
            self.CriticalInjuries += 1
            self.Defeated = True
        elif(InjuryRoll <= 70):
            self.MajorInjuries += 1
            self.DuelBonus -= 2
        else:
            self.MinorInjuries += 1
            self.DuelBonus -= 2

    def reset_duellist(self):
        """
        Function to reset duellist to original values.
        """
        self.Morale:int = 30
        self.DuelBonus:int = 0
        self.DamageBonus:int = self.determine_damage_bonus()
        self.MinorInjuries:int = 0
        self.MajorInjuries:int = 0
        self.CriticalInjuries:int = 0
        self.Deaths:int = 0
        self.Defeated:bool = False