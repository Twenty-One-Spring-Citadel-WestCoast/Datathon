import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from urllib.request import urlopen
import json

pd.set_option('display.max_columns', 5)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)

educationDataset = pd.read_csv("data/education/Education.csv")
economicDataset = pd.read_csv("data/education/Unemployment.csv")
temperatureDataset = pd.read_csv("data/education/tempData.csv")
urbanizationDataset = pd.read_csv("data/education/pop-urban-pct-historical.csv")
populationDataset = pd.read_csv('data/us_pop.csv')
ageDataset = pd.read_csv('data/education/sc-est2019-agesex-civ.csv')
raceDataset = pd.read_csv('data/education/sc-est2019-alldata5.csv')

### Education dataset cleaning ###
colNames = ["FIPS Code",
            "Percent of adults with less than a high school diploma, 2014-18",
            "Percent of adults with a bachelor's degree or higher, 2014-18",
            "Percent of adults completing some college or associate's degree, 2014-18",
            "Percent of adults with a high school diploma only, 2014-18"]

educationDataset = educationDataset[colNames]

### Unemployment/wealth dataset cleaning ###
colNames = ["fips_txt",
            "State",
            "area_name",
            "Unemployment_rate_2019",
            "Median_Household_Income_2019"]

economicDataset = economicDataset[colNames]
economicDataset = economicDataset.dropna(subset=["Median_Household_Income_2019"])
economicDataset["Median_Household_Income_2019"] = economicDataset["Median_Household_Income_2019"].astype(int)
economicDataset = economicDataset.rename(columns={"fips_txt":"FIPS Code", "area_name": "Area Name"})

### Mean Temperature Dataset ###
temperatureDataset['AverageTemperature'] = round((5/9)*(temperatureDataset['AverageTemperature']-32),2)

### Degree of Urbanization ###
colNames = ["FIPS","Area Name","2010"]

urbanizationDataset = urbanizationDataset[colNames]
urbanizationDataset = urbanizationDataset.rename(columns={"FIPS":"FIPS Code","2010":"Urbanization %","Area Name":"State"})
urbanizationDataset["Urbanization %"] = urbanizationDataset["Urbanization %"].astype(float)

### Population Dataset ###
populationDataset = populationDataset.rename(columns={"state":"State"})

### Age Dataset ###
colNames = ["NAME","AGE","POPEST2019_CIV"]
ageDataset = ageDataset[colNames]

ageDataset = ageDataset.groupby("NAME")
#print(ageDataset.groups)


### Race Dataset ###
colNames = ["NAME","RACE","SEX","POPESTIMATE2019"]
raceDataset = raceDataset[colNames]

singleRaceDataset = raceDataset.loc[raceDataset["SEX"] == 0]
raceGroups = singleRaceDataset.groupby(["NAME","RACE"]).agg(np.sum)
raceGroups = raceGroups["POPESTIMATE2019"].unstack(level=-1)

raceDict = {1:"White",2:"Black",3:"American Native",4:"Asian",5:"Pacific Islander"}
raceGroups = raceGroups.rename(columns=raceDict)
raceGroups["Total"] = np.sum(raceGroups, axis=1)
raceGroups = raceGroups.iloc[:,:-1].div(raceGroups["Total"], axis=0).reset_index()
raceGroups = raceGroups.rename(columns={"NAME":"State"})

### Construct and save merged dataset ###
stateDataset = temperatureDataset.merge(urbanizationDataset, how='left', on="State")
stateDataset = stateDataset.merge(populationDataset, how='left', on="State")
stateDataset = stateDataset.merge(raceGroups, how='left', on="State")
stateDataset["FIPS Code"] = stateDataset["FIPS Code"].astype(str) + "000"
stateDataset["FIPS Code"] = stateDataset["FIPS Code"].astype(int)
stateDataset = stateDataset.drop(columns=["State"])
print(stateDataset)

fullDataset = economicDataset.merge(educationDataset,how='left',on="FIPS Code")
fullDataset = fullDataset.merge(stateDataset,how='left', on ="FIPS Code")

fullDataset.to_csv("data/cleaned/educationDataset.csv")

fullStateDataset = fullDataset.loc[fullDataset["FIPS Code"]%1000 == 0]
fullStateDataset.loc[fullStateDataset["State"]=="DC","AverageTemperature"] = 4.8
fullStateDataset.loc[fullStateDataset["State"]=="DC","Urbanization %"] = 100.0
fullStateDataset = fullStateDataset.dropna()

fullStateDataset.to_csv("data/cleaned/educationStateDataset.csv")










