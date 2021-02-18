# Report

## Technical exposition

### Data sources and manipulation

#### The COVID Tracking Project

To obtain a comprehensive and accurate picture of the prevelance of COVID-19 across US states over time, we collected data from the COVID Tracking Project, a source recommended by Citadel. We utilized its [API](https://covidtracking.com/data/api) here to download historical values for all states.

The COVID Tracking Project data contains a wide range of variables key to the project. Specifically, we have obtained information about:

- Number of new cases (confirmed and probable combined). We have also calculated daily increase in negative and positive test results.

- Number of new hospitalized patients

- Number of new deaths

We believe that the source is largely accurate and unbiased. However, it is ran by *The Atlantic*, which is a left-leaning magazine. We will take into account the party affliation of the federal and state leadership when analyzing our data.

#### Covid-19 Policy Responses

To get an understanding of policy responses to contain the spread of COVID-19, we have also collected data from Covid-19 Policy Responses project the USA state level run by Blavatnik School of Government, Oxford University. The dataset contains topics including school, workplace, and public transport closing, cancellation of events, restrictions on gathering, stay-at-home orders, and restrictions on domestic and international movements.

In addition to these specific policy observations, we also used two composed indices, namely containment and health index and stringency index. 

#### Google Mobility Data

Although many containment policies aim to 