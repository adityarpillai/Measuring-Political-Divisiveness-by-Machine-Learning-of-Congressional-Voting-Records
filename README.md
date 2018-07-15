# Measuring Political Divisiveness by Machine Learning of Congressional Voting Records
Research Project by Dr. Douglas Fisher and Aditya Pillai

**Abstract:** Common wisdom suggests that we live in highly polarized times, and that reducing the polarity would be beneficial. This paper expands on the first of these beliefs by measuring the degree of political polarization over the years. Our proxy for polarization is the ease with which political party of members of Congress can be predicted from machine learning of their voting records from 1789 through 2017. We measure ‘ease’ of prediction in several different ways.

One class of measures is the amount of training data (i.e., voting records for a given year) required to predict political party over a disjoint test set with specified accuracy and confidence, using a variety of machine learning algorithms. A second family of measures is inspired by decision trees, which are used frequently in classification and diagnosis. Specifically, we calculate the expected number of roll call votes in a year that need to be examined to distinguish political parties from yay and nay votes. 

The measures above characterize divisiveness by ‘ease’ of distinguishing political party. But there are also divisions within parties (e.g., the Democratic Party in 1965, the Republican Party in 2017). An additional class of measures addresses within-party by measuring the distance between all pairs of voting records within a year, regardless of party.

To evaluate the various measures as reasonable proxies of divisiveness, we compare the year by year ratings by each measure, with the divisiveness ratings of political historians, who we surveyed. We judge our measures by their correlations with the yearly averages of historians, as well as the “best fitting” historian for each method.


## Data

Data is retrieved from UCLA's (VoteView)[https://voteview.com/data].

## File Structure

### Data

Within this repository, the raw data is stored in the `data` folder. Within the `data` folder, the two houses of Congress are separated by folder -- `house` and `senate`. In each of these folders, there is the leading character for House (H) and Senate (S), followed by a three digit number corresponding to the session of Congress (e.g. 001 is the 1st Session of Congress which lasted from 1789-1791 and 115 is the 115th Session fo Congress which is the most recent session lasting from 2017 until 2019).

