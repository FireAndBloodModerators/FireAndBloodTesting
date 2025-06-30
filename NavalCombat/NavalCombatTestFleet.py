# IMPORTS

# CLASS
class Fleet:
    """
    A class representing a Naval Combat Fleet for r/FireAndBlood.

    Attributes:
        Carracks (int): The number of Carracks in the fleet.
        Galleys (int): The number of Galleys in the fleet.
        Ironships (int): The number of Ironships in the fleet.
        Longships (int): The number of Longships in the fleet.
        Cogs (int): The number of Cogs in the fleet.
        Combat_Value (int): The combat strength of ships in the fleet.
        Morale (int): The morale/fighting spirit of ships in the fleet.
        Retreat_Threshold (int): The morale at which the fleet will retreat at.
        Speed (int): The speed at which the fleet moves at.
        Casualties (int): Percentage of ships lost in battle.
        Strength_Bonus (int): The bonus to combat rolls received from the fleet having greater strength than the enemy.
        Skill_Bonus (int): The bonus to combat rolls received from the fleet's commander.
    """

    def __init__(self,Carracks:int,Galleys:int,Ironships:int,Longships:int,Cogs:int,RetreatThreshold:int):
        """
        Initialiser function for a Naval Combat fleet.
    
        Arguments:
            Carracks (int): The number of Carracks in the fleet.
            Galleys (int): The number of Galleys in the fleet.
            Ironships (int): The number of Ironships in the fleet.
            Longships (int): The number of Longships in the fleet.
            Cogs (int): The number of Cogs in the fleet.
            RetreatThreshold (int): The Morale at which the force will retreat.
        """
        self.Carracks:int = Carracks
        self.Galleys:int = Galleys
        self.Ironships:int = Ironships
        self.Longships:int = Longships
        self.Cogs:int = Cogs
        self.Combat_Value:int = self.calculate_combat_value()
        self.Morale:int = 100
        self.Retreat_Threshold:int = RetreatThreshold
        self.Speed:int = self.calculate_speed()
        self.Casualties:int = 0
        self.Strength_Bonus:int = 0
        self.Skill_Bonus:int = 0

    def calculate_combat_value(self) -> int:
        """
        Function to calculate combat value (CV) of a fleet's ships.
        """
        return (self.Carracks*16) + (self.Galleys*6) + (self.Ironships*5) + (self.Longships*2) + self.Cogs

    def calculate_speed(self) -> int:
        """
        Function to calculate speed of a force.
        """
        TotalShips = self.Carracks + self.Galleys + self.Ironships + self.Longships + self.Cogs
        if(self.Cogs == 0):
            if((self.Carracks == 0) & (self.Galleys == 0)):
                if(self.Ironships == 0):
                    if(TotalShips > 100):
                        return 16
                    else:
                        return 32
                else:
                    if(TotalShips > 100):
                        return 14
                    else:
                        return 28
            else:
                if(TotalShips > 100):
                    return 12
                else:
                    return 24
        else:
            if(TotalShips > 100):
                return 8
            else:
                return 16