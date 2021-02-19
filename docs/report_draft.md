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

Many containment policies aim to reduce the physical distances among people and minimize in-person contact between individuals from different households. Therefore, such measures will only work if people do indeed abide by the rules and control their own movement. Here, we utilize Google's COVID-19 Community Mobility Reports to get information about people's physical movement in different geographical locations. We believe that although Google's data is not a representative sample of all people's physical movement, its use is nonethless justified given the high prevelance of cellphone usage in the US. Google provides information about visits to including grocery and pharmacy, parks, transit stations, retail and recreation venues, residential areas and workplaces.

#### Google Trends

To understand the role of misinformation in the pandemic, we want to measure the prevelance of false COVID-19 related conspiracy theories across geographic locations over time. We believe that the ideal approach will be to apply natural language processing (NLP) tools to social media data, where most conspiracy theories disseminate. However, given the very limited time we have to complete this project, we opt to use keyword popularity data provided by Google Trends. For a given keyword and time period, Google Trends provide a popularity score, with maximum scaled to 100, across states and metropolitan areas in the US. We collected monthly popularity scores from March 2020 to January 2021 on the following keywords:

- *covid conspiracy*

- *covid hoax*

- *plandemic*. "Plandemic" is a series of COVID-19 conspiracy theory videos, which claim that COVID-19 is created by "big pharma" to make money.

- *pizzagate*. A conspiracy theory alleging that high level politicians of the U.S. Democratic PArty are involved in human trafficking and child sex. It is unrelated to COVID-19.

- *wuhan lab*. A unsubstantiated theory stating that Wuhan Virology Institute leaked the novel coronavirus.

