import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from urllib.request import urlopen
import json

educationDataset = pd.read_csv("data/education/Education.csv")
economicDataset = pd.read_csv("data/education/Unemployment.csv")

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

### Construct and save merged dataset ###
fullDataset = economicDataset.merge(educationDataset,how='left',on="FIPS Code")

fullDataset.to_csv("data/cleaned/educationDataset.csv")










