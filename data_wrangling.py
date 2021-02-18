# Import modules
import numpy as np
import pandas as pd
import altair as alt

# Read data

## Data provided by Citadel
owid = pd.read_csv("data/1_owid/owid-covid-data.csv")

ecdc_daily = pd.read_csv("data/2_ecdc/dailynotificationeu.csv")
ecdc_weekly = pd.read_csv("data/2_ecdc/weeklynotificationeu.csv")
ecdc_testing = pd.read_csv("data/2_ecdc/testing.csv")
ecdc_admission = pd.read_csv("data/2_ecdc/admissionrates.csv")
ecdc_age = pd.read_csv("data/2_ecdc/agerangenotificationeu.csv")
ecec_response = pd.read_csv("data/2_ecdc/country_response_measures.csv")
ecdc_world = pd.read_csv("data/2_ecdc/notification.csv")

us_national = pd.read_csv("data/3_covidtracking/national-history.csv")

## Google Mobility Data
us_mobility = pd.read_csv("data/google_mobility/2020_US_Region_Mobility_Report.csv")
us_mobility_state = us_mobility.loc[
    us_mobility["sub_region_2"].isnull() == True,
    [
        "country_region_code",
        "sub_region_1",
        "date",
        "retail_and_recreation_percent_change_from_baseline",
        "grocery_and_pharmacy_percent_change_from_baseline",
        "parks_percent_change_from_baseline",
        "transit_stations_percent_change_from_baseline",
        "workplaces_percent_change_from_baseline",
        "residential_percent_change_from_baseline",
    ],
]
## Google Trend Data
