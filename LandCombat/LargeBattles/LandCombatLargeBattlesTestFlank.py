# IMPORTS

# CLASS
class Flank:
    """
    A class representing a Land Combat Force's flank for r/FireAndBlood.

    Attributes:
        MaA (int): The number of Men-at-Arms (MaA) in the flank.
        Levies (int): The number of Levies in the flank.
        Combat_Value (int): The combat strength of troops in the flank.
        Morale (int): The morale/fighting spirit of troops in the flank.
        Retreat_Threshold (int): The morale at which the flank will retreat at.
        Speed (int): The speed at which the flank moves at.
        Casualties (int): Percentage of the flank's troops lost in battle.
        Strength_Bonus (int): The bonus to combat rolls received from the flank having greater strength than the enemy's flank.
        Terrain_Bonus (int): The bonus to combat rolls received from the terrain the flank is fighting in.
        Skill_Bonus (int): The bonus to combat rolls received from the flank's commander.
        Target (Flank|None): The enemy flank the flank is targetting.
        Defeated (bool): Whether or not the flank has been defeated.
    """

    def __init__(self,MaA:int,Levies:int):
        """
        Initialiser function for a Land Combat force's flank.
    
        Arguments:
            MaA (int): The number of Men-at-Arms (MaA) in the flank.
            Levies (int): The number of Levies in the flank.
        """
        self.MaA = MaA
        self.Levies = Levies
        self.Combat_Value = self.calculate_combat_value(self.MaA,self.Levies)
        self.Morale = 100
        self.Retreat_Threshold = 0
        self.Speed = self.calculate_speed(self.MaA,self.Levies)
        self.Casualties = 0
        self.Strength_Bonus = 0
        self.Terrain_Bonus = 0
        self.Skill_Bonus = 0
        self.Target = None
        self.Defeated = False

    def calculate_combat_value(self,MaA:int,Levies:int) -> int:
        """
        Function to calculate combat value (CV) of a flank's troops.
    
        Arguments:
            MaA (int): The number of Men-at-Arms (MaA) in the flank.
            Levies (int): The number of Levies in the flank.
        """
        return (MaA*3) + Levies

    def calculate_speed(self,MaA:int,Levies:int) -> int:
        """
        Function to calculate speed of a flank.
    
        Arguments:
            MaA (int): The number of Men-at-Arms (MaA) in the flank.
            Levies (int): The number of Levies in the flank.
        """
        TotalTroops = MaA + Levies
        if(Levies == 0):
            if(TotalTroops <= 20):
                return 8
            elif(TotalTroops <= 100):
                return 7
            elif(TotalTroops <= 1000):
                return 6
            elif(TotalTroops <= 15000):
                return 5
            elif(TotalTroops <= 30000):
                return 4
            else:
                return 3
        else:
            if(TotalTroops <= 20):
                return 7
            elif(TotalTroops <= 100):
                return 6
            elif(TotalTroops <= 1000):
                return 5
            elif(TotalTroops <= 15000):
                return 4
            elif(TotalTroops <= 30000):
                return 3
            else:
                return 2