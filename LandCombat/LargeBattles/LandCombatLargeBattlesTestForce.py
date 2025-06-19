# IMPORTS

# CLASS
class Force:
    """
    A class representing a Land Combat Force for r/FireAndBlood.

    Attributes:
        MaA (int): The number of Men-at-Arms (MaA) in the force.
        Levies (int): The number of Levies in the force.
        LeftMaA (int): The number of Men-at-Arms (MaA) predetermined to be in the left flank. Default None.
        LeftLevies (int): The number of Levies predetermined to be in the left flank. Default None.
        CentreMaA (int): The number of Men-at-Arms (MaA) predetermined to be in the centre flank. Default None.
        CentreLevies (int): The number of Levies predetermined to be in the centre flank. Default None.
        RightMaA (int): The number of Men-at-Arms (MaA) predetermined to be in the right flank. Default None.
        RightLevies (int): The number of Levies predetermined to be in the right flank. Default None.
        Morale (int): The morale/fighting spirit of troops in the force.
    """

    def __init__(self,MaA:int,Levies:int,LeftMaA: int|None = None,LeftLevies: int|None = None,CentreMaA: int|None = None,CentreLevies: int|None = None,RightMaA: int|None = None,RightLevies: int|None = None):
        """
        Initialiser function for a Land Combat force.
    
        Arguments:
            MaA (int): The number of Men-at-Arms (MaA) in the force.
            Levies (int): The number of Levies in the force.
            LeftMaA (int): The number of Men-at-Arms (MaA) predetermined to be in the left flank. Default None.
            LeftLevies (int): The number of Levies predetermined to be in the left flank. Default None.
            CentreMaA (int): The number of Men-at-Arms (MaA) predetermined to be in the centre flank. Default None.
            CentreLevies (int): The number of Levies predetermined to be in the centre flank. Default None.
            RightMaA (int): The number of Men-at-Arms (MaA) predetermined to be in the right flank. Default None.
            RightLevies (int): The number of Levies predetermined to be in the right flank. Default None.
        """
        self.MaA = MaA
        self.Levies = Levies