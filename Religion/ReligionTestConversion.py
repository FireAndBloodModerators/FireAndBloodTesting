# IMPORTS
import math
import random

# CLASS
class Conversion:
    """
    A class representing a Religion Conversion for r/FireAndBlood.

    Attributes:
        NewReligion (str): The Religion the Province is being Converted to.
        CurrentReligion (str): The current Religion of the Province.
        Population (int): The total Population of the Province.
        Control (int): The total Control of the Province.
        OwnProvince (bool): Whether or not the Province is owned by the claim Converting it.
        ConversionRollModifier (int): The modifier to the Conversion Roll.
        Deaths (int): The number of deaths characters attempting to Convert the Province has suffered.
        CriticalInjuries (int): The number of Critical Injuries characters attempting to Convert the Province have suffered.
        Major Injuries (int): The number of Major Injuries characters attempting to Convert the Province have suffered.
        MinorInjuries (int): The number of Minor Injuries characters attempting to Convert the Province have suffered.
    """

    def __init__(self,NewReligion:str,CurrentReligion:str,Population:int,Control:int,OwnProvince:bool):
        """
        Initialiser function for a Religion Conversion.

        Arguments:
            NewReligion (str): The Religion the Province is being Converted to.
            CurrentReligion (str): The current Religion of the Province.
            Population (int): The total Population of the Province.
            Control (int): The total Control of the Province.
            OwnProvince (bool): Whether or not the Province is owned by the claim Converting it.
        """
        self.NewReligion:str = NewReligion
        self.CurrentReligion:str = CurrentReligion
        self.Population:int = Population
        self.Control:int = Control
        self.OwnProvince:bool = OwnProvince
        self.ConversionRollModifer:int = self.determine_starting_conversion_modifier()
        self.Deaths:int = 0
        self.CriticalInjuries:int = 0
        self.MajorInjuries:int = 0
        self.MinorInjuries:int = 0

    def determine_new_religion_conversion_modifier(self) -> int:
        """
        Function to determine Conversion Roll modifier for the new Religion.

        Returns:
            int: The modifier to the Conversion Roll from the new Religion.
        """
        if(self.NewReligion == "Skagosi Old Gods"):
            return -4
        elif(self.NewReligion == "DrownedGod"):
            return -2
        elif(self.NewReligion == "DrownedGodInII"):
            return 1
        elif(self.NewReligion == "MotherRhoyne"):
            return -2
        elif(self.NewReligion == "R'hllor"):
            return -1
        else:
            return 0
        
    def determine_current_religion_conversion_modifier(self) -> int:
        """
        Function to determine Conversion Roll modifier for the current Religion.

        Returns:
            int: The modifier to the Conversion Roll from the current Religion.
        """
        if(self.CurrentReligion == "Old Gods"):
            return 1
        elif(self.CurrentReligion == "DrownedGod"):
            return -1
        elif(self.CurrentReligion == "MotherRhoyne"):
            return -1
        else:
            return 0
        
    def determine_population_conversion_modifier(self) -> int:
        """
        Function to determine Conversion Roll modifier based on total Population.

        Returns:
            int: The modifier to the Conversion Roll from the total Population.
        """
        return -(math.floor(self.Population/50000))
    
    def determine_control_conversion_modifier(self) -> int:
        """
        Function to determine Conversion Roll modifier based on Control.

        Returns:
            int: The modifier to the Conversion Roll from the Control.
        """
        if(self.OwnProvince):
            if(self.Control > 85):
                return (math.floor((self.Control-85)/5))
            else:
                return 0
        else:
            if(self.Control > 85):
                return -(math.floor((self.Control-85)/5))
            else:
                return 0
    
    def determine_starting_conversion_modifier(self) -> int:
        """
        Function to determine starting Conversion Roll modifier.

        Returns:
            ConversionRollModifier (int): The starting modifier to the Conversion Roll.
        """
        ConversionRollModifier = 0
        ConversionRollModifier += self.determine_new_religion_conversion_modifier()
        ConversionRollModifier += self.determine_current_religion_conversion_modifier()
        ConversionRollModifier += self.determine_population_conversion_modifier()
        ConversionRollModifier += self.determine_control_conversion_modifier()
        if(ConversionRollModifier < -4):
            ConversionRollModifier = -4
        return ConversionRollModifier
    
    def injury_roll(self):
        """
        Function to make an Injury Roll.
        """
        InjuryRoll = random.randint(1,20)
        if(InjuryRoll <= 2):
            self.Deaths += 1
        elif(InjuryRoll <= 6):
            self.CriticalInjuries += 1
        elif(InjuryRoll <= 12):
            self.MajorInjuries += 1
        else:
            self.MinorInjuries += 1
    
    def conversion_roll(self) -> tuple[bool,bool]:
        """
        Function to make a Conversion Roll plus modifiers.

        Returns:
            ConversionOver (bool): Whether the Conversion had ended.
            ConversionFailed (bool): Whether the Conversion ended in failure.
        """
        ConversionRoll = random.randint(1,20) + self.ConversionRollModifer
        if(ConversionRoll <= 3):
            ConversionOver = True
            ConversionFailed = True
            self.injury_roll()
            return ConversionOver,ConversionFailed
        elif(ConversionRoll <= 6):
            ConversionOver = False
            ConversionFailed = False
            return ConversionOver,ConversionFailed
        elif(ConversionRoll <= 12):
            self.ConversionRollModifer += 1
            ConversionOver = False
            ConversionFailed = False
            return ConversionOver,ConversionFailed
        elif(ConversionRoll <= 16):
            self.ConversionRollModifer += 2
            ConversionOver = False
            ConversionFailed = False
            return ConversionOver,ConversionFailed
        elif(ConversionRoll <= 22):
            self.ConversionRollModifer += 4
            ConversionOver = False
            ConversionFailed = False
            return ConversionOver,ConversionFailed
        elif(ConversionRoll <= 26):
            self.ConversionRollModifer += 6
            ConversionOver = False
            ConversionFailed = False
            return ConversionOver,ConversionFailed
        elif(ConversionRoll <= 29):
            self.ConversionRollModifer += 8
            ConversionOver = False
            ConversionFailed = False
            return ConversionOver,ConversionFailed
        else:
            ConversionOver = True
            ConversionFailed = False
            return ConversionOver,ConversionFailed
    
    def reset_conversion(self):
        """
        Function to reset Conversion statistics to original values.
        """
        self.ConversionRollModifer = self.determine_starting_conversion_modifier()
        self.Deaths = 0
        self.CriticalInjuries = 0
        self.MajorInjuries = 0
        self.MinorInjuries = 0
    
    def conversion(self) -> tuple[int,bool]:
        """
        Function to roll a Conversion for a Province.

        Returns:
            Duration (int): How many years it took to Convert the Province's Religion.
        """
        self.reset_conversion()
        Duration = 0
        ConversionOver = False
        ConversionFailed = False
        while(not ConversionOver):
            Duration += 1
            ConversionOver,ConversionFailed = self.conversion_roll()
        return Duration,ConversionFailed