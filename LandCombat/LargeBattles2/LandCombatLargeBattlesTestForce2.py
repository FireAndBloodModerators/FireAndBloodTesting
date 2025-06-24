# IMPORTS
import math
from LandCombatLargeBattlesTestFlank2 import Flank

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
        self.MaA:int = MaA
        self.Levies:int = Levies
        self.assign_flank_troops(LeftMaA,LeftLevies,CentreMaA,CentreLevies,RightMaA,RightLevies)
        self.LeftFlank:Flank = Flank(self.LeftMaA,self.LeftLevies)
        self.CentreFlank:Flank = Flank(self.CentreMaA,self.CentreLevies)
        self.RightFlank:Flank = Flank(self.RightMaA,self.CentreLevies)
    
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
            self.LeftMaA:int = LeftMaA
        else:
            self.LeftMaA:int = math.floor(self.MaA/3)
        if(LeftLevies is not None):
            self.LeftLevies:int = LeftLevies
        else:
            self.LeftLevies:int = math.floor(self.Levies/3)
        if(CentreMaA is not None):
            self.CentreMaA:int = CentreMaA
        else:
            self.CentreMaA:int = math.floor(self.MaA/3) + (self.MaA % 3)
        if(CentreLevies is not None):
            self.CentreLevies:int = CentreLevies
        else:
            self.CentreLevies:int = math.floor(self.Levies/3) + (self.Levies % 3)
        if(RightMaA is not None):
            self.RightMaA:int = RightMaA
        else:
            self.RightMaA:int = math.floor(self.MaA/3)
        if(RightLevies is not None):
            self.RightLevies:int = RightLevies
        else:
            self.RightLevies:int = math.floor(self.Levies/3)    