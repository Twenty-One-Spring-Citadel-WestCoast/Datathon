# Import modules
import numpy as np
import pandas as pd
import altair as alt
import pyjags as pjs

# Read data
owid = pd.read_csv("data/1_owid/owid-covid-data.csv")
us_national = pd.read_csv("data/3_covidtracking/national-history.csv")

# Sample country: USA
USA_Bayesian = us_national.loc[
    us_national["date"] > "2020-05-31", ["date", "negativeIncrease", "positiveIncrease"]
]
US_pop = owid.loc[owid["iso_code"] == "USA", "population"].mean()
N_days = USA_Bayesian.shape[0]

#
jags_code = """
model{
    for (i in N_days){
        pneg[i] ~ dunif(0, 1)
        ppos[i] = pneg[i]  * (k + 1) / (1 + pneg[i] * k)
        r[i] ~ dbeta(1.5, 30)
        Nneg[i] ~ dnorm (P * (1 - r[i]) * pneg[i], 0.001)
        Npos[i] ~ dnorm (P *  r[i] * ppos[i], 0.001)
        
    }
    k ~ dgamma(5, 1)
}"""

jags_data = {
    "N_days": N_days,
    "P": US_pop,
    "Nneg": USA_Bayesian["negativeIncrease"],
    "Npos": USA_Bayesian["positiveIncrease"],
}

N_samples = 10000
N_thin = 50
model = pjs.Model(code=jags_code, data=jags_data, chains=1, adapt=10000)
samples = model.sample(N_samples, vars=["r", "k"], thin=N_thin)

samples["k"].mean(axis=1)
samples["r"]