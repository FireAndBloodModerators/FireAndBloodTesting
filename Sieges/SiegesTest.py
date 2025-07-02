# IMPORTS
import pandas as pd
from SiegesTestSiege import Siege

## SET SIMULATIONS COUNT
SimulationCount = 100000

## CREATE COLUMN LABELS
ColumnLabels = ["","Maximum Siege Duration","Average Siege Duration","Minimum Siege Duration","Average Besiegers Casualties","Average Defenders Casualties"]

## HOLDFASTS TESTS
print("Holdfast Sims Start")

### Create list of Holdfast Sizes
HoldfastSizes = [1,2,3,4,5,6,7,8,9,10]

### Initialise results list
HoldfastResults = []

### Iterate through Holdfast Sizes and generate Siege object
for HoldfastSize in HoldfastSizes:
    TestSiege = Siege(HoldfastSize,0)

    #### Create lists for results
    HoldfastSizeSiegeDurations = []
    HoldfastSizeBesiegersCasualties = []
    HoldfastSizeDefendersCasualties = []

    #### Run sims
    for x in range(SimulationCount):
        ##### Call Siege function to get results
        HoldfastSizeResults = TestSiege.siege()

        ##### Append results to applicable list
        HoldfastSizeSiegeDurations.append(HoldfastSizeResults[0])
        HoldfastSizeBesiegersCasualties.append(HoldfastSizeResults[1])
        HoldfastSizeDefendersCasualties.append(HoldfastSizeResults[2])
    
    #### Calculate end results
    HoldfastNewResults = [f"Holdfast Size {HoldfastSize}",max(HoldfastSizeSiegeDurations),round((sum(HoldfastSizeSiegeDurations)/len(HoldfastSizeSiegeDurations)),1),min(HoldfastSizeSiegeDurations),f"{round((sum(HoldfastSizeBesiegersCasualties)/len(HoldfastSizeBesiegersCasualties)),2)}%",f"{round((sum(HoldfastSizeDefendersCasualties)/len(HoldfastSizeDefendersCasualties)),2)}%"]

    #### Append new results to results list
    HoldfastResults.append(HoldfastNewResults)

    #### Checkpoint
    print(f"Holdfast Size {HoldfastSize} simulations complete")

### Save results to dataframe
HoldfastDataframe = pd.DataFrame(HoldfastResults,columns=ColumnLabels)

### Save dataframe to csv file
HoldfastDataframe.to_csv("Sieges/holdfast_siege_results.csv",index=False)
print("Holdfasts Sims End")

print()

## OUTER WALLS TESTS
print("Outer Walls Sims Start")

### Create list of Outer Walls DVs
OuterWallsDVs = [1.5,2,3,4]

### Initialise results list
OuterWallsResults = []

### Iterate through Outer Walls DVs and generate Siege object
for OuterWallsDV in OuterWallsDVs:
    TestSiege = Siege(0,OuterWallsDV)

    #### Create lists for results
    OuterWallsDVSiegeDurations = []
    OuterWallsDVBesiegersCasualties = []
    OuterWallsDVDefendersCasualties = []

    #### Run sims
    for x in range(SimulationCount):
        ##### Call Siege function to get results
        OuterWallsDVResults = TestSiege.siege()

        ##### Append results to applicable list
        OuterWallsDVSiegeDurations.append(OuterWallsDVResults[0])
        OuterWallsDVBesiegersCasualties.append(OuterWallsDVResults[1])
        OuterWallsDVDefendersCasualties.append(OuterWallsDVResults[2])
    
    #### Calculate end results
    OuterWallsDVNewResults = [f"Outer Walls DV {OuterWallsDV}",max(OuterWallsDVSiegeDurations),round((sum(OuterWallsDVSiegeDurations)/len(OuterWallsDVSiegeDurations)),1),min(OuterWallsDVSiegeDurations),f"{round((sum(OuterWallsDVBesiegersCasualties)/len(OuterWallsDVBesiegersCasualties)),2)}%",f"{round((sum(OuterWallsDVDefendersCasualties)/len(OuterWallsDVDefendersCasualties)),2)}%"]

    #### Append new results to results list
    OuterWallsResults.append(OuterWallsDVNewResults)

    #### Checkpoint
    print(f"Outer Walls DV {OuterWallsDV} simulations complete")

### Save results to dataframe
OuterWallsDataframe = pd.DataFrame(OuterWallsResults,columns=ColumnLabels)

### Save dataframe to csv file
OuterWallsDataframe.to_csv("Sieges/outer_walls_siege_results.csv",index=False)
print("Outer Walls Sims End")

print()

## OUTER WALLS & HOLDFAST TESTS
print("Outer Walls & Holdfast Sims Start")

### Create list of Outer Walls DVs
OuterWallsDVs = [1.5,2,3,4]

### Create list of applicable Holdfast Sizes
HoldfastSizesAdjusted = [1,2,3,4,5,6]

### Initialise results list
OuterWallsHoldfastResults = []

### Iterate through Outer Walls DVs and generate Siege object
for OuterWallsDV in OuterWallsDVs:

    for HoldfastSizeAdjusted in HoldfastSizesAdjusted:
        #### Check if Holdfast Size is too big for Outer Walls
        if((OuterWallsDV == 1.5) & (HoldfastSizeAdjusted > 2)):
            break
        if((OuterWallsDV == 2) & (HoldfastSizeAdjusted > 4)):
            break
        if((OuterWallsDV == 3) & (HoldfastSizeAdjusted > 5)):
            break
        
        #### Create Siege object
        TestSiege = Siege(HoldfastSizeAdjusted,OuterWallsDV)

        #### Create lists for results
        OuterWallsDVHoldfastSizeAdjustedSiegeDurations = []
        OuterWallsDVHoldfastSizeAdjustedBesiegersCasualties = []
        OuterWallsDVHoldfastSizeAdjustedDefendersCasualties = []

        #### Run sims
        for x in range(SimulationCount):
            ##### Call Siege function to get results
            OuterWallsDVHoldfastSizeAdjustedResults = TestSiege.double_siege()

            ##### Append results to applicable list
            OuterWallsDVHoldfastSizeAdjustedSiegeDurations.append(OuterWallsDVHoldfastSizeAdjustedResults[0])
            OuterWallsDVHoldfastSizeAdjustedBesiegersCasualties.append(OuterWallsDVHoldfastSizeAdjustedResults[1])
            OuterWallsDVHoldfastSizeAdjustedDefendersCasualties.append(OuterWallsDVHoldfastSizeAdjustedResults[2])
        
        #### Calculate end results
        OuterWallsDVHoldfastSizeAdjustedNewResults = [f"Outer Walls DV {OuterWallsDV} // Holdfast Size {HoldfastSizeAdjusted}",max(OuterWallsDVHoldfastSizeAdjustedSiegeDurations),round((sum(OuterWallsDVHoldfastSizeAdjustedSiegeDurations)/len(OuterWallsDVHoldfastSizeAdjustedSiegeDurations)),1),min(OuterWallsDVHoldfastSizeAdjustedSiegeDurations),f"{round((sum(OuterWallsDVHoldfastSizeAdjustedBesiegersCasualties)/len(OuterWallsDVHoldfastSizeAdjustedBesiegersCasualties)),2)}%",f"{round((sum(OuterWallsDVHoldfastSizeAdjustedDefendersCasualties)/len(OuterWallsDVHoldfastSizeAdjustedDefendersCasualties)),2)}%"]

        #### Append new results to results list
        OuterWallsHoldfastResults.append(OuterWallsDVHoldfastSizeAdjustedNewResults)

        #### Checkpoint
        print(f"Outer Walls DV {OuterWallsDV} // Holdfast Size {HoldfastSizeAdjusted} simulations complete")

### Save results to dataframe
OuterWallsHoldfastDataframe = pd.DataFrame(OuterWallsHoldfastResults,columns=ColumnLabels)

### Save dataframe to csv file
OuterWallsHoldfastDataframe.to_csv("Sieges/outer_walls_and_holdfast_siege_results.csv",index=False)
print("Outer Walls & Holdfast Sims End")