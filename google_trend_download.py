from pytrends.request import TrendReq
from datetime import datetime
from calendar import monthrange

import pandas as pd

TOTAL_DATE_RANGE = "2020-03-01 2021-01-31"

pytrends = TrendReq(hl="en-US", tz=360)

kws = [
    "plandemic",
]

# Create monthly timeframes
def last_day_of_month(date_value):
    return date_value.replace(day=monthrange(date_value.year, date_value.month)[1])


date_ranges = []
for m in range(3, 13, 1):
    date_ranges.append(
        str(datetime(year=2020, month=m, day=1).date())
        + " "
        + str(last_day_of_month(datetime(year=2020, month=m, day=1).date()))
    )

date_ranges.append("2021-01-01 2021-01-31")

# Get data
trend_month_state = dict()
trend_month_DMA = dict()
data_all_time_state = dict()
data_all_time_DMA = dict()

for kw in kws:
    kw_list = [kw]
    data_by_month_state = dict()
    data_by_month_DMA = dict()
    for date_range in date_ranges:

        pytrends.build_payload(kw_list, cat=0, geo="US", timeframe=date_range)
        data_by_month_state[date_range] = month_by_state = pytrends.interest_by_region(
            resolution="REGION", inc_low_vol=True, inc_geo_code=True
        )
        data_by_month_DMA[date_range] = pytrends.interest_by_region(
            resolution="DMA", inc_low_vol=True, inc_geo_code=True
        )
    pytrends.build_payload(kw_list, cat=0, geo="US", timeframe=TOTAL_DATE_RANGE)
    data_all_time_state[kw] = pytrends.interest_by_region(
        resolution="REGION", inc_low_vol=True, inc_geo_code=True
    )
    data_all_time_DMA[kw] = pytrends.interest_by_region(
        resolution="DMA", inc_low_vol=True, inc_geo_code=True
    )
    trend_month_state[kw] = data_by_month_state
    trend_month_DMA[kw] = data_by_month_DMA

# Clean data
month_state_transformed = pd.DataFrame(
    {"geocode": [], "trend_index": [], "keyword": [], "date_range": [], "state": []}
)
month_DMA_transformed = pd.DataFrame(
    {"geocode": [], "trend_index": [], "keyword": [], "date_range": [], "DMA": []}
)
data_all_time_state_transformed = pd.DataFrame(
    {"geocode": [], "trend_index": [], "keyword": [], "date_range": [], "state": []}
)
data_all_time_DMA_transformed = pd.DataFrame(
    {"geocode": [], "trend_index": [], "keyword": [], "date_range": [], "state": []}
)

for kw in kws:
    for date_range in date_ranges:
        trend_month_state[kw][date_range].columns = ["geoCode", "trend_index"]
        trend_month_state[kw][date_range]["keyword"] = kw
        trend_month_state[kw][date_range]["date_range"] = date_range
        trend_month_state[kw][date_range]["state"] = trend_month_state[kw][
            date_range
        ].index
        month_state_transformed = pd.concat(
            [month_state_transformed, trend_month_state[kw][date_range]],
            ignore_index=True,
        )

        trend_month_DMA[kw][date_range].columns = ["geoCode", "trend_index"]
        trend_month_DMA[kw][date_range]["keyword"] = kw
        trend_month_DMA[kw][date_range]["date_range"] = date_range
        trend_month_DMA[kw][date_range]["DMA"] = trend_month_DMA[kw][date_range].index
        month_DMA_transformed = pd.concat(
            [month_DMA_transformed, trend_month_DMA[kw][date_range]], ignore_index=True
        )

    data_all_time_state[kw].columns = ["geoCode", "trend_index"]
    data_all_time_state[kw]["keyword"] = kw
    data_all_time_state[kw]["date_range"] = TOTAL_DATE_RANGE
    data_all_time_state[kw]["state"] = data_all_time_state[kw].index
    data_all_time_state_transformed = pd.concat(
        [data_all_time_state_transformed, data_all_time_state[kw]],
        ignore_index=True,
    )

    data_all_time_DMA[kw].columns = ["geoCode", "trend_index"]
    data_all_time_DMA[kw]["keyword"] = kw
    data_all_time_DMA[kw]["date_range"] = TOTAL_DATE_RANGE
    data_all_time_DMA[kw]["DMA"] = data_all_time_DMA[kw].index
    data_all_time_DMA_transformed = pd.concat(
        [data_all_time_DMA_transformed, data_all_time_DMA[kw]],
        ignore_index=True,
    )

month_state_transformed.to_csv("data/cleaned/trend_month_state.csv")
month_DMA_transformed.to_csv("data/cleaned/trend_month_DMA.csv")
data_all_time_state_transformed.to_csv("data/cleaned/trend_all_time_state.csv")
data_all_time_DMA_transformed.to_csv("data/cleaned/trend_all_time_DMA.csv")
