import numpy as np
import pandas as pd

US_daily = pd.read_csv("data/us_daily/daily.csv")
US_daily = US_daily[
    [
        "date",
        "state",
        "positive",
        "probableCases",
        "negative",
        "pending",
        "totalTestResultsSource",
        "totalTestResults",
        "hospitalizedCurrently",
        "hospitalizedCumulative",
        "inIcuCurrently",
        "inIcuCumulative",
        "onVentilatorCurrently",
        "onVentilatorCumulative",
        "recovered",
        "totalTestsViral",
        "positiveTestsViral",
        "negativeTestsViral",
        "positiveCasesViral",
        "deathConfirmed",
        "deathProbable",
        "totalTestEncountersViral",
        "totalTestsPeopleViral",
        "totalTestsAntibody",
        "positiveTestsAntibody",
        "negativeTestsAntibody",
        "totalTestsPeopleAntibody",
        "positiveTestsPeopleAntibody",
        "negativeTestsPeopleAntibody",
        "totalTestsPeopleAntigen",
        "positiveTestsPeopleAntigen",
        "totalTestsAntigen",
        "positiveTestsAntigen",
        "fips",
        "positiveIncrease",
        "negativeIncrease",
        "total",
        "totalTestResultsIncrease",
        "posNeg",
        "dataQualityGrade",
        "deathIncrease",
        "hospitalizedIncrease",
        "hash",
        "commercialScore",
        "negativeRegularScore",
        "negativeScore",
        "positiveScore",
        "score",
        "grade",
    ]
]
US_daily["state_abb"] = US_daily["state"]
US_daily = US_daily.drop("state", axis=1)

US_state_abb = pd.read_csv("data/US_state_abb.csv")
US_state_abb.columns = ["state", "state_abb"]
US_daily = pd.merge(US_daily, US_state_abb, on="state_abb", how="left")
