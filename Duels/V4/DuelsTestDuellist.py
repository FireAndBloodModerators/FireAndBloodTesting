# IMPORTS
import random

# CLASS
class Duellist:
    """
    A class representing a Duels Duellist for r/FireAndBlood.

    Attributes:
        Morale (int): The morale/fighting spirit of the Duellist.
        OriginalMorale (int): The original morale/fighting spirit of the Duellist, for resetting stats.
        DuelBonus (int): The Duellist's bonus to Duel Rolls.
        OriginalDuelBonus (int) The Duellist's original bonus to Duel Rolls, for resetting stats.
        WeaponType (str): The weapon the Duellist is wielding.
        DamageBonus (int): The Duellist's bonus to Damage Rolls.
        MinorInjuries (int): The number of Minor Injuries the Duellist has taken.
        MajorInjuries (int): The number of Major Injuries the Duellist has taken.
        CriticalInjuries (int): The number of Critical Injuries the Duellist has taken.
        Deaths (int): The number of times the Duellist has died.
        Defeated (bool): Whether or not the Duellist is defeated.
    """

    def __init__(self,MoraleBonus:int,DuelBonus:int,NumberOfSkills:int):
        """
        Initialiser function for a Duels Duellist.

        Arguments:
            WeaponType (str): What weapon the Duellist is wielding, determines DamageBonus.
        """
        self.Morale:int = 30 + MoraleBonus
        self.OriginalMorale:int = 30 + MoraleBonus
        self.DuelBonus:int = DuelBonus
        self.OriginalDuelBonus:int = DuelBonus
        self.WeaponType = "None"
        self.DamageBonus:int = self.determine_damage_bonus()
        self.MinorInjuries:int = 0
        self.MajorInjuries:int = 0
        self.CriticalInjuries:int = 0
        self.Deaths:int = 0
        self.Defeated:bool = False
        self.InjuryRollBonus = NumberOfSkills

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

    def duel_roll(self) -> tuple[int,bool]:
        """
        Function to roll 1d20 plus Duellist's Duel Bonus and return result and whether it was a Critical Strike.
    
        Returns:
            DuelRoll (int): The Duellist's Duel Roll.
            CriticalStrike (bool): The Duellist's bonus to Damage Rolls.
        """
        DuelRoll = random.randint(1,20)
        if(DuelRoll == 20):
            CriticalStrike = True
        else:
            CriticalStrike = False
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
        Function to make a Duel Injury Roll after a Critical Strike.
        """
        InjuryRoll = random.randint(1,20) + self.InjuryRollBonus
        if(InjuryRoll <= 1):
            self.Deaths += 1
            self.Defeated = True
        elif(InjuryRoll <= 3):
            self.CriticalInjuries += 1
            self.Defeated = True
        elif(InjuryRoll <= 8):
            self.MajorInjuries += 1
            self.DuelBonus -= 2
        else:
            self.MinorInjuries += 1
            self.DuelBonus -= 2

    def reset_duellist(self):
        """
        Function to reset duellist to original values.
        """
        self.Morale = self.OriginalMorale
        self.DuelBonus = self.OriginalDuelBonus
        self.DamageBonus = self.determine_damage_bonus()
        self.MinorInjuries = 0
        self.MajorInjuries = 0
        self.CriticalInjuries = 0
        self.Deaths = 0
        self.Defeated = False