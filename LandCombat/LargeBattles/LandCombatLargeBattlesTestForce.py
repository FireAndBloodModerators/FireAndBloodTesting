# IMPORTS
import math
from LandCombatLargeBattlesTestFlank import Flank

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
        LeftFlank (Flank): The left flank of the force.
        CentreFlank (Flank): The left flank of the force.
        RightFlank (Flank): The left flank of the force.
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
        self.assign_flank_troops(LeftMaA,LeftLevies,CentreMaA,CentreLevies,RightMaA,RightLevies)
        self.LeftFlank = Flank(self.LeftMaA,self.LeftLevies)
        self.CentreFlank = Flank(self.CentreMaA,self.CentreLevies)
        self.RightFlank = Flank(self.RightMaA,self.CentreLevies)
    
    def assign_flank_troops(self,LeftMaA: int|None,LeftLevies: int|None,CentreMaA: int|None,CentreLevies: int|None,RightMaA: int|None,RightLevies: int|None):
        """
        Function to calculate how many troops are in each flank.
    
        Arguments:
            LeftMaA (int): The number of Men-at-Arms (MaA) predetermined to be in the left flank. Default None.
            LeftLevies (int): The number of Levies predetermined to be in the left flank. Default None.
            CentreMaA (int): The number of Men-at-Arms (MaA) predetermined to be in the centre flank. Default None.
            CentreLevies (int): The number of Levies predetermined to be in the centre flank. Default None.
            RightMaA (int): The number of Men-at-Arms (MaA) predetermined to be in the right flank. Default None.
            RightLevies (int): The number of Levies predetermined to be in the right flank. Default None.
        """
        if(LeftMaA is not None):
            self.LeftMaA = LeftMaA
        else:
            self.LeftMaA = math.floor(self.MaA/3)
        if(LeftLevies is not None):
            self.LeftLevies = LeftLevies
        else:
            self.LeftLevies = math.floor(self.Levies/3)
        if(CentreMaA is not None):
            self.CentreMaA = CentreMaA
        else:
            self.CentreMaA = math.floor(self.MaA/3) + (self.MaA % 3)
        if(CentreLevies is not None):
            self.CentreLevies = CentreLevies
        else:
            self.CentreLevies = math.floor(self.Levies/3) + (self.Levies % 3)
        if(RightMaA is not None):
            self.RightMaA = RightMaA
        else:
            self.RightMaA = math.floor(self.MaA/3)
        if(RightLevies is not None):
            self.RightLevies = RightLevies
        else:
            self.RightLevies = math.floor(self.Levies/3)    