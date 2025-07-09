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
