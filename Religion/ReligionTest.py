# IMPORTS
import pandas as pd
from ReligionTestConversion import Conversion

# SET SIMULATIONS COUNT
SimulationCount = 10000

# BEGIN TEST
print("Conversion Simulations Start")

# CREATE VARIABLE LISTS
ReligionList = ["Faith of the Seven","Old Gods","Skagosi Old Gods","DrownedGod","DrownedGodII","Mother Rhoyne","Gods of Valyria","R'hllor"]
PopulationList = [1000,50000,100000,150000,200000,250000,300000]
ControlList = [85,90,95,100]
OwnProvinceList = [True,False]

# CREATE COLUMN LABELS
DurationColumnLabels = ["Conversion Type","Duration"]
FailureColumnLabels = ["Conversion Type","% Chance of Failure"]
InjuryColumnLabels = ["Conversion Type","Average Deaths","Average Critical Injuries","Average Major Injuries","AverageMinorInjuries"]

# INITIALISE RESULTS LISTS
ConversionDurationResults = []
ConversionFailureResults = []
ConversionInjuryResults = []

# ITERATE THROUGH EACH LIST TO CREATE CONVERSION OBJECT AND RUN SIMS
for NewReligion in ReligionList:
    for CurrentReligion in ReligionList:
        if(NewReligion != CurrentReligion):
            for Population in PopulationList:
                for Control in ControlList:
                    for OwnProvince in OwnProvinceList:
                        ## Initialise new results lists
                        NewDurationResults = [f"New Religion: {NewReligion}, Current Religion: {CurrentReligion}, Population: {Population}, Control: {Control}, Own Province: {OwnProvince}"]
                        NewFailureResults = [f"New Religion: {NewReligion}, Current Religion: {CurrentReligion}, Population: {Population}, Control: {Control}, Own Province: {OwnProvince}"]
                        NewInjuryResults = [f"New Religion: {NewReligion}, Current Religion: {CurrentReligion}, Population: {Population}, Control: {Control}, Own Province: {OwnProvince}"]

                        ## Create variables to track statistics
                        DurationsSum = 0
                        FailedSimulationsSum = 0
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
                                FailedSimulationsSum += 1
                            DeathsSum += TestConversion.Deaths
                            CriticalInjuresSum += TestConversion.CriticalInjuries
                            MajorInjuriesSum += TestConversion.MajorInjuries
                            MinorInjuriesSum += TestConversion.MinorInjuries

                        ## Calculate statistics
                        if((SimulationCount - FailedSimulationsSum) > 0):
                            NewAverageDuration = round((DurationsSum/(SimulationCount - FailedSimulationsSum)),2)
                        else:
                            NewAverageDuration = "N/A"
                        NewChanceOfFailure = round((FailedSimulationsSum/SimulationCount*100),2)
                        NewAverageDeaths = round((DeathsSum/SimulationCount),2)
                        NewAverageCriticalInjuries = round((CriticalInjuresSum/SimulationCount),2)
                        NewAverageMajorInjuries = round((MajorInjuriesSum/SimulationCount),2)
                        NewAverageMinorInjuries = round((MinorInjuriesSum/SimulationCount),2)

                        ## Save statistics to new results lists
                        NewDurationResults.append(NewAverageDuration)
                        NewFailureResults.append(NewChanceOfFailure)
                        NewInjuryResults.extend([NewAverageDeaths,NewAverageCriticalInjuries,NewAverageMajorInjuries,NewAverageMinorInjuries])

                        ## Save new results lists to results lists
                        ConversionDurationResults.append(NewDurationResults)
                        ConversionFailureResults.append(NewFailureResults)
                        ConversionInjuryResults.append(NewInjuryResults)

                        ## Checkpoint
                        print(f"New Religion: {NewReligion}, Current Religion: {CurrentReligion}, Population: {Population}, Control: {Control}, Own Province: {OwnProvince} simulations complete")

# SAVE RESULTS TO DATAFRAME
ConversionDurationDataFrame = pd.DataFrame(ConversionDurationResults,columns=DurationColumnLabels)
ConversionFailureDataFrame = pd.DataFrame(ConversionFailureResults,columns=FailureColumnLabels)
ConversionInjuryDataFrame = pd.DataFrame(ConversionInjuryResults,columns=InjuryColumnLabels)

## Save simple dataframes to csv file
ConversionDurationDataFrame.to_csv("Religion/religion_average_durations.csv",index=False)
ConversionFailureDataFrame.to_csv("Religion/religion_chance_of_failure.csv",index=False)
ConversionInjuryDataFrame.to_csv("Religion/religion_average_injuries.csv",index=False)

# END TEST
print("Conversion Sims End")

# PRINT AVERAGE VALUES
print()
AverageDuration = 0
for DurationResult in ConversionDurationResults:
    AverageDuration += DurationResult[1]
print(f"Average Duration Overall: {round((AverageDuration/len(ConversionDurationResults)),2)}")
AverageChanceOfFailure = 0
for FailureResult in ConversionFailureResults:
    AverageChanceOfFailure += FailureResult[1]
print(f"Average Chance of Failure Overall: {round((AverageChanceOfFailure/len(ConversionFailureResults)),2)}")
AverageDeaths = 0
AverageCriticalInjuries = 0
AverageMajorInjuries = 0
AverageMinorInjuries = 0
for InjuryResult in ConversionInjuryResults:
    AverageDeaths += InjuryResult[1]
    AverageCriticalInjuries += InjuryResult[2]
    AverageMajorInjuries += InjuryResult[3]
    AverageMinorInjuries += InjuryResult[4]
print(f"Average Deaths Overall: {round((AverageDeaths/len(ConversionInjuryResults)),2)}")
print(f"Average Critical Injuries Overall: {round((AverageCriticalInjuries/len(ConversionInjuryResults)),2)}")
print(f"Average Major Injuries Overall: {round((AverageMajorInjuries/len(ConversionInjuryResults)),2)}")
print(f"Average Minor Injuries Overall: {round((AverageMinorInjuries/len(ConversionInjuryResults)),2)}")