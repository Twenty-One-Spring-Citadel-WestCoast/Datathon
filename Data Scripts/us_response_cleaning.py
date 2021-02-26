import numpy as np
import pandas as pd

US_response = pd.read_csv(
    "https://raw.githubusercontent.com/OxCGRT/USA-covid-policy/master/data/OxCGRT_US_latest.csv"
)

US_response = US_response[
    [
        "RegionName",
        "RegionCode",
        "Jurisdiction",
        "Date",
        "C1_School closing",
        "C1_Flag",
        "C2_Workplace closing",
        "C2_Flag",
        "C3_Cancel public events",
        "C3_Flag",
        "C4_Restrictions on gatherings",
        "C4_Flag",
        "C5_Close public transport",
        "C5_Flag",
        "C6_Stay at home requirements",
        "C6_Flag",
        "C7_Restrictions on internal movement",
        "C7_Flag",
        "C8_International travel controls",
        "ConfirmedCases",
        "ConfirmedDeaths",
        "StringencyIndex",
        "GovernmentResponseIndex",
        "ContainmentHealthIndex",
    ]
]

US_response["state"] = US_response["RegionName"]
US_response = US_response.drop("RegionName", axis=1)

US_response.to_csv("data/cleaned/US_response_cleaned.csv")