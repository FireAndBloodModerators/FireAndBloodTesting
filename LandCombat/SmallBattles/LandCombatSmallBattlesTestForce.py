# IMPORTS

# CLASS
class Force:
    """
    A class representing a Land Combat Force for r/FireAndBlood.

    Attributes:
        MaA (int): The number of Men-at-Arms (MaA) in the force.
        Levies (int): The number of Levies in the force.
        Combat_Value (int): The combat strength of troops in the force.
        Morale (int): The morale/fighting spirit of troops in the force.
        Retreat_Threshold (int): The morale at which the force will retreat at.
        Speed (int): The speed at which the force moves at.
        Casualties (int): Percentage of troops lost in battle.
        Strength_Bonus (int): The bonus to combat rolls received from the force having greater strength than the enemy.
        Terrain_Bonus (int): The bonus to combat rolls received from the terrain the force is fighting in.
        Skill_Bonus (int): The bonus to combat rolls received from the force's commander.
    """

    def __init__(self,MaA:int,Levies:int,RetreatThreshold:int):
        """
        Initialiser function for Land Combat Forces.
    
        Arguments:
            MaA (int): The number of Men-at-Arms (MaA) in the force.
            Levies (int): The number of Levies in the force.
            RetreatThreshold (int): The Morale at which the force will retreat.
        """
        self.MaA = MaA
        self.Levies = Levies
        self.Combat_Value = self.calculate_combat_value(self.MaA,self.Levies)
        self.Morale = 100
        self.Retreat_Threshold = RetreatThreshold
        self.Speed = self.calculate_speed(self.MaA,self.Levies)
        self.Casualties = 0
        self.Strength_Bonus = 0
        self.Terrain_Bonus = 0
        self.Skill_Bonus = 0

    def calculate_combat_value(self,MaA:int,Levies:int) -> int:
        """
        Function to calculate combat value (CV) of a force's troops.
    
        Arguments:
            MaA (int): The number of Men-at-Arms (MaA) in the force.
            Levies (int): The number of Levies in the force.
        """
        return (MaA*3) + Levies

    def calculate_speed(self,MaA:int,Levies:int) -> int:
        """
        Function to calculate speed of a force.
    
        Arguments:
            MaA (int): The number of Men-at-Arms (MaA) in the force.
            Levies (int): The number of Levies in the force.
        """
        TotalTroops = MaA + Levies
        if(Levies == 0):
            if(TotalTroops <= 20):
                return 16
            elif(TotalTroops <= 100):
                return 14
            elif(TotalTroops <= 1000):
                return 12
            elif(TotalTroops <= 15000):
                return 10
            elif(TotalTroops <= 30000):
                return 8
            else:
                return 6
        else:
            if(TotalTroops <= 20):
                return 14
            elif(TotalTroops <= 100):
                return 12
            elif(TotalTroops <= 1000):
                return 10
            elif(TotalTroops <= 15000):
                return 8
            elif(TotalTroops <= 30000):
                return 6
            else:
                return 4