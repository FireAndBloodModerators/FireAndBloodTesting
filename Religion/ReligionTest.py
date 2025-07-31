# IMPORTS
import pandas as pd
from ReligionTestConversion import Conversion

# SET SIMULATIONS COUNT
SimulationCount = 10000

# BEGIN TEST
print("Conversion Simulations Start")

# CREATE VARIABLE LISTS
ReligionList = ["Faith of the Seven","Old Gods","Skagosi Old Gods","DrownedGod","DrownedGodII","Mother Rhoyne","Gods of Valyria","R'hllor"]
PopulationList = [1000,25000,50000,75000,100000,125000,150000,175000,200000,225000,250000,275000,300000]
ControlList = [75,80,85,90,95,100]
OwnProvinceList = [True,False]

# CREATE COLUMN LABELS
DurationColumnLabels = ["Conversion Type","Duration"]
InjuryColumnLabels = ["Conversion Type","Average Deaths","Average Critical Injuries","Average Major Injuries","AverageMinorInjuries"]

# INITIALISE RESULTS LISTS
ConversionDurationResults = []
ConversionInjuryResults = []

# ITERATE THROUGH EACH LIST TO CREATE CONVERSION OBJECT AND RUN SIMS
for NewReligion in ReligionList:
    for CurrentReligion in ReligionList:
        for Population in PopulationList:
            for Control in ControlList:
                for OwnProvince in OwnProvinceList:
                    ## Initialise new results lists
                    NewDurationResults = [f"New Religion: {NewReligion}, Current Religion: {CurrentReligion}, Population: {Population}, Control: {Control}, Own Province: {OwnProvince}"]
                    NewInjuryResults = [f"New Religion: {NewReligion}, Current Religion: {CurrentReligion}, Population: {Population}, Control: {Control}, Own Province: {OwnProvince}"]

                    ## Create variables to track statistics
                    NonFailedSimulations = SimulationCount
                    DurationsSum = 0
                    DeathsSum = 0
                    CriticalInjuresSum = 0
                    MajorInjuriesSum = 0
                    MinorInjuriesSum = 0

                    ## Create Conversion object
                    TestConversion = Conversion(NewReligion,CurrentReligion,Population,Control,OwnProvince)

                    ## Run simulations
                    for x in range(SimulationCount):
                        ### Run conversion
                        NewDuration,ConversionFailed = TestConversion.conversion()

                        ### Save statistics
                        if(not ConversionFailed):
                            DurationsSum += NewDuration
                        else:
                            NonFailedSimulations -= 1
                        DeathsSum += TestConversion.Deaths
                        CriticalInjuresSum += TestConversion.CriticalInjuries
                        MajorInjuriesSum += TestConversion.MajorInjuries
                        MinorInjuriesSum += TestConversion.MinorInjuries

                    ## Calculate statistics
                    if(NonFailedSimulations > 0):
                        NewAverageDuration = round((DurationsSum/NonFailedSimulations),2)
                    else:
                        NewAverageDuration = "N/A"
                    NewAverageDeaths = round((DeathsSum/SimulationCount),2)
                    NewAverageCriticalInjuries = round((CriticalInjuresSum/SimulationCount),2)
                    NewAverageMajorInjuries = round((MajorInjuriesSum/SimulationCount),2)
                    NewAverageMinorInjuries = round((MinorInjuriesSum/SimulationCount),2)

                    ## Save statistics to new results lists
                    NewDurationResults.append(NewAverageDuration)
                    NewInjuryResults.extend([NewAverageDeaths,NewAverageCriticalInjuries,NewAverageMajorInjuries,NewAverageMinorInjuries])

                    ## Save new results lists to results lists
                    ConversionDurationResults.append(NewDurationResults)
                    ConversionInjuryResults.append(NewInjuryResults)

                    ## Checkpoint
                    print(f"New Religion: {NewReligion}, Current Religion: {CurrentReligion}, Population: {Population}, Control: {Control}, Own Province: {OwnProvince} simulations complete")

# SAVE RESULTS TO DATAFRAME
ConversionDurationDataFrame = pd.DataFrame(ConversionDurationResults,columns=DurationColumnLabels)
ConversionInjuryDataFrame = pd.DataFrame(ConversionInjuryResults,columns=InjuryColumnLabels)

## Save simple dataframes to csv file
ConversionDurationDataFrame.to_csv("Religion/religion_average_durations.csv",index=False)
ConversionInjuryDataFrame.to_csv("Religion/religion_average_injuries.csv",index=False)

# END TEST
print("Conversion Sims ENd")