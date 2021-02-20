# Import modules
import numpy as np
import pandas as pd
import altair as alt

# Read data

## US daily COVID-19 features
US_daily = pd.read_csv("data/cleaned/US_daily_cleaned.csv", index_col=0)
US_daily["date"] = pd.to_datetime(US_daily["date"], format="%Y%m%d")

## US mobility
US_mobility = pd.read_csv("data/cleaned/US_mobility_state_cleaned.csv", index_col=0)
US_mobility["date"] = pd.to_datetime(US_mobility["date"], format="%Y-%m-%d")

daily_df = pd.merge(US_daily, US_mobility, on=["state", "date"], how="left")

## US_response
US_response = pd.read_csv("data/cleaned/US_response_cleaned.csv", index_col=0)
US_response["date"] = pd.to_datetime(US_response["Date"], format="%Y%m%d")
US_response = US_response.drop("Date", axis=1)

daily_df = pd.merge(daily_df, US_response, on=["state", "date"], how="left")

## US_state_pop
pop = pd.read_csv("data/us_pop.csv")
pop.columns = ["state", "pop_2019"]

daily_df = pd.merge(daily_df, pop, on=["state"], how="left")

# US_state_gdp
gdp = pd.read_csv("data/us_gdp.csv")
gdp = gdp.loc[gdp["LineCode"] == 1, ["GeoName", "2019"]]
gdp.columns = ["state", "GDP_2019"]

daily_df = pd.merge(daily_df, gdp, on=["state"], how="left")

# US_state_education
education = pd.read_csv("data/cleaned/educationStateDataset.csv", index_col=0)
education.columns = [
    "FIPS_Code",
    "state_code",
    "state",
    "Unemployment_rate_2019",
    "Median_Household_Income_2019",
    "Percent_less_than_high_school",
    "Percent_bachelor_or_higher",
    "Percent_some_college_or_associate",
    "Percent_high_school_only",
    "AverageTemperature",
    "Urbanization_rate",
    "Pop_2019",
    "White",
    "Black",
    "American_Native",
    "Asian",
    "Pacific_Islander",
]
education = education[
    [
        "state_code",
        "state",
        "Unemployment_rate_2019",
        "Median_Household_Income_2019",
        "Percent_less_than_high_school",
        "Percent_bachelor_or_higher",
        "Percent_some_college_or_associate",
        "Percent_high_school_only",
        "AverageTemperature",
        "Urbanization_rate",
        "White",
        "Black",
        "American_Native",
        "Asian",
        "Pacific_Islander",
    ]
]

daily_df = pd.merge(daily_df, education, on=["state"], how="left")
# Aggregate data

daily_df.to_csv("data/cleaned/daily_df.csv")