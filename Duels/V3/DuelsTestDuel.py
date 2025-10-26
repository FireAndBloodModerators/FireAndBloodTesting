# IMPORTS
from DuelsTestDuellist import Duellist

# CLASS
class Duel:
    """
    A class representing a Duel for r/FireAndBlood.

    Attributes:
        Duellist1 (Duellist): The first Duellist in the Duel.
        Duellist2 (Duellist): The first Duellist in the Duel.
        DuelOver (bool): Whether or not the duel is over.
    """

    def __init__(self,Duellist1:Duellist,Duellist2:Duellist):
        """
        Initialiser function for a Duel.

        Arguments:
            Duellist1 (Duellist): The first Duellist in the Duel.
            Duellist2 (Duellist): The first Duellist in the Duel.
        """
        self.Duellist1:Duellist = Duellist1
        self.Duellist2:Duellist = Duellist2
        self.DuelOver:bool = False


    def reset_duellists(self):
        """
        Function to reset Duellist statistics to original values.
        """
        self.Duellist1.reset_duellist()
        self.Duellist2.reset_duellist()
        self.DuelOver = False

    def duel(self) -> int:
        """
        Function to roll a Duel between two Duellists.

        Returns:
            DuelResult (int): The winner of the Duel. 1 for Duellist 1, 2 for Duellist 2, 0 for error.
        """
        self.reset_duellists()
        while(not self.DuelOver):
            Duellist1Roll = self.Duellist1.duel_roll()
            Duellist2Roll = self.Duellist2.duel_roll()
            if(Duellist1Roll > Duellist2Roll):
                DuelRollDifference = Duellist1Roll - Duellist2Roll
                if(DuelRollDifference >= 16):
                    self.Duellist2.injury_roll()
                    self.Duellist2.Morale -= self.Duellist1.damage_roll()
                else:
                    self.Duellist2.Morale -= self.Duellist1.damage_roll()
            elif(Duellist2Roll > Duellist1Roll):
                DuelRollDifference = Duellist2Roll - Duellist1Roll
                if(DuelRollDifference >= 16):
                    self.Duellist1.injury_roll()
                    self.Duellist1.Morale -= self.Duellist2.damage_roll()
                else:
                    self.Duellist1.Morale -= self.Duellist2.damage_roll()
            else:
                pass
            if(self.Duellist1.Morale <= 0):
                self.Duellist1.Defeated = True
            elif(self.Duellist2.Morale <= 0):
                self.Duellist2.Defeated = True
            if(self.Duellist1.Defeated | self.Duellist2.Defeated):
                self.DuelOver = True
        if(self.Duellist1.Defeated & (not self.Duellist2.Defeated)):
            DuelResult = 2
            return DuelResult
        elif(self.Duellist2.Defeated & (not self.Duellist1.Defeated)):
            DuelResult = 1
            return DuelResult
        else:
            print("Error in determining Duel victor.")
            return 0