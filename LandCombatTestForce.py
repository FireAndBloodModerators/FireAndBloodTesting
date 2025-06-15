class Force:
    """
    A class representing an Land Combat Force for r/FireAndBlood.

    Attributes:
        MaA (int): The number of Men-at-Arms (MaA) in the force.
        Levies (str): The number of Levies in the force.
    """

    def __init__(self,MaA,Levies):
        """
        Initialiser function for Land Combat Forces.
    
        Arguments:
            MaA (int): The number of Men-at-Arms (MaA) in the force.
            Levies (str): The number of Levies in the force.
        """
        self.MaA = MaA
        self.Levies = Levies
        self.calculate_combat_value(self.MaA,self.Levies)

    def calculate_combat_value(self,MaA,Levies):
        """
        Function to calculate combat value (CV) of a force's troops.
    
        Arguments:
            MaA (int): The number of Men-at-Arms (MaA) in the force.
            Levies (str): The number of Levies in the force.
        """
        self.combat_value = (MaA*3) + Levies