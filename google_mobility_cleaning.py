import numpy as np
import pandas as pd
import altair as alt

## Google Mobility Data
us_mobility = pd.read_csv("data/google_mobility/2020_US_Region_Mobility_Report.csv")

us_mobility_state = us_mobility.loc[
    (us_mobility["sub_region_2"].isnull() == True) and (us_mobility["sub_region_1"].isnull() == False),
    [
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
us_mobility_state["state"] = us_mobility_state["sub_region_1"]
us_mobility_state = us_mobility_state.drop("sub_region_1", axis=1)
us_mobility_state["non_residential_percent_change_from_baseline"] = us_mobility_state[
    [
        "retail_and_recreation_percent_change_from_baseline",
        "grocery_and_pharmacy_percent_change_from_baseline",
        "parks_percent_change_from_baseline",
        "transit_stations_percent_change_from_baseline",
        "workplaces_percent_change_from_baseline",
    ]
].mean(axis=1)
us_mobility_state.to_csv("data/cleaned/US_mobility_state_cleaned.csv")