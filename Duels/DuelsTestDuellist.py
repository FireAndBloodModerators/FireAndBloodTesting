# IMPORTS

# CLASS
class Duellist:
    """
    A class representing a Duels Duellist for r/FireAndBlood.

    Attributes:
        Morale (int): The morale/fighting spirit of the Duellist.
        DuelBonus (int): The Duellist's bonus to Duel Rolls.
        MinorInjuries (int): The number of Minor Injuries the Duellist has taken.
        MajorInjuries (int): The number of Major Injuries the Duellist has taken.
        CriticalInjuries (int): The number of Critical Injuries the Duellist has taken.
        Deaths (int): The number of times the Duellist has died.
    """

    def __init__(self,DuelBonus:int):
        """
        Initialiser function for a Duels Duellist.
    
        Arguments:
            DuelBonus (int): The Duellist's bonus to Duel Rolls.
        """
        self.Morale:int = 30
        self.DuelBonus:int = DuelBonus
        self.MinorInjuries:int = 0
        self.MajorInjuries:int = 0
        self.CriticalInjuries:int = 0
        self.Deaths:int = 0