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

# Aggregate data

daily_df.to_csv("data/cleaned/US_daily_cleaned.csv")