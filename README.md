# Project Overview

Encourage people from diverse demographics and backgrounds to become Wikipedia editors by identifying low effort, high impact opportunities.

## Problem statement

Wikipedia is a major source of information for many people, yet it is a biased resource. One of the biases in Wikipedia centers around gender inequality.  For example, only 17% of Wikipedia biographies are about women.  Furthermore, between 8% and 16% of Wikipedia editors are female.  This may beg the question: why don’t more women edit Wiki?  One of the barriers to this relates to phycological barrier to be and editor; the motivation for this project is to lower that physcological barrier.

## Project solution

This project uses a data set containing every Wikipedia article's full text, edit history, and metadata to identify high impact, low effort edit opportunities for first time Wikipedia editors, to create a welcoming inclusive experience that will encourage people from diverse demographics and backgrounds to become Wikipedia editors.  The method for doing this is to calculate an "impact score" for every category page that describes how impactful it would be to become an editor and add an article to it.

## Tech stack


### Calculating Category Impact Score

Monthly page views: the more people that view a category page each month, the higher the impact you will have if you add to it

Click through rate (or "helpfulness"): of the people who view the category page, what percentage of them go on to click on one of the listed articles

Freshness/staleness: how recently it's been updated. If you add to a category page that hasn't been editing in a while, you are having a higher impact.

Number of entries: you will be having more of an impact adding two articles to a list of ten than to a list of 100

Number of editors: if a page has only been edited by a few people, you will impact it by adding your perspective more than if you edit a page that has had hundreds of different editors already


### Calculating Conflict Score

This could be based on things like:
Of all the entries that were ever added to the category page, how many of them were later deleted by someone else
Many entries added and then deleted by others = high conflict
In the editors' comment threads for the page, what is the average sentiment analysis score for the comments (more negative = high conflict)
Conflict score is relevant for inclusion because as it said in the article about the 9 reasons women don't edit wikipedia, some people may not want to engage in "edit wars" or be criticized for their edits


## Visualization Output

A) a dashboard where you can pick any category page and view it's "impact score" and possibly "conflict score" for editing (and all the the different components that go into the scores)
B) A dashboard that shows the top ten category pages that are low hanging fruit for first time editors: high impact, low conflict


## Twitter Bot Output
A daily automated email or tweet that shares three category pages each day that are low hanging fruit for first time editors to add to




