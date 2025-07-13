# IMPORTS
from DuelsTestDuellist import Duellist

# CLASS
class Duel:
    """
    A class representing a Duel for r/FireAndBlood.

    Attributes:
        Duellist1 (Duellist): The first Duellist in the Duel.
        Duellist2 (Duellist): The first Duellist in the Duel.
    """

    def __init__(self,Duellist1:Duellist,Duellist2:Duellist):
        """
        Initialiser function for a Duel.

        Arguments:
            Duellist1 (Duellist): The first Duellist in the Duel.
            Duellist2 (Duellist): The first Duellist in the Duel.
        """
        self.Duellist1 = Duellist1
        self.Duellist2 = Duellist2

    def reset_duellists(self):
        """
        Function to reset Duellist statistics to original values.
        """
        self.Duellist1.Morale = 30
        self.Duellist1.DuelBonus = 0
        self.Duellist1.MinorInjuries = 0
        self.Duellist1.MajorInjuries = 0
        self.Duellist1.CriticalInjuries = 0
        self.Duellist1.Deaths = 0
        self.Duellist1.Defeated = False
        self.Duellist2.Morale = 30
        self.Duellist2.DuelBonus = 0
        self.Duellist2.MinorInjuries = 0
        self.Duellist2.MajorInjuries = 0
        self.Duellist2.CriticalInjuries = 0
        self.Duellist2.Deaths = 0
        self.Duellist2.Defeated = False

    def duel(self) -> int:
        """
        Function to roll a Duel between two Duellists.

        Returns:
            DuelResult (int): The winner of the Duel. 1 for Duellist 1, 2 for Duellist 2, 0 for error.
        """
        self.reset_duellists()
        while((not self.Duellist1.Defeated) & (not self.Duellist2.Defeated)):
            Duellist1Roll,Duellist1CriticalStrike = self.Duellist1.duel_roll()
            Duellist2Roll,Duellist2CriticalStrike = self.Duellist2.duel_roll()
            if(Duellist1Roll > Duellist2Roll):
                if((Duellist1CriticalStrike == 20) & (Duellist2CriticalStrike == 1)):
                    self.Duellist2.Defeated = True
                    break
                elif((Duellist1CriticalStrike == 20) | (Duellist2CriticalStrike == 1)):
                    self.Duellist2.injury_roll_a()
                    self.Duellist2.Morale -= self.Duellist1.damage_roll()
                else:
                    self.Duellist2.Morale -= self.Duellist1.damage_roll()
            elif(Duellist2Roll > Duellist1Roll):
                if((Duellist2CriticalStrike == 20) & (Duellist1CriticalStrike == 1)):
                    self.Duellist1.Defeated = True
                    break
                elif((Duellist2CriticalStrike == 20) | (Duellist1CriticalStrike == 1)):
                    self.Duellist1.injury_roll_a()
                    self.Duellist1.Morale -= self.Duellist2.damage_roll()
                else:
                    self.Duellist1.Morale -= self.Duellist2.damage_roll()
            else:
                pass
            if(self.Duellist1.Morale <= 0):
                self.Duellist1.Defeated = True
            elif(self.Duellist2.Morale <= 0):
                self.Duellist2.Defeated = True
            else:
                pass
        if(self.Duellist1.Defeated & (not self.Duellist2.Defeated)):
            if(self.Duellist1.Morale <= 0):
                self.Duellist1.injury_roll_b()
            DuelResult = 2
            return DuelResult
        elif(self.Duellist2.Defeated & (not self.Duellist1.Defeated)):
            if(self.Duellist2.Morale <= 0):
                self.Duellist2.injury_roll_b()
            DuelResult = 1
            return DuelResult
        else:
            print("Error in determining Duel victor.")
            return 0