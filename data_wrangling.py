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

## Google Trend Data
