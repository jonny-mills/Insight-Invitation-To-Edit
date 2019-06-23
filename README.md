
![Screen Shot 2019-06-18 at 3 56 27 PM](https://user-images.githubusercontent.com/35629096/59725212-af866380-91e1-11e9-8956-f4000bfcc2c6.png)


## Project Overview

Wikipedia serves more than 400M unique visitors per month. However, less than 1/10 of its editors are female, which in turn has created a biased resource.  One major reason often cited for causing women and other newcomers to be hesitant to become Wikipedia editors is the psychological barrier of not knowing where to start.  I address this issue by creating a pipeline to analyze the entire Wikipedia database with algorithms to suggest high impact, low barrier, and relevant-to-user Wikipedia pages to encourage new people to become first time editors.

## Solution strategy

Develop a pipeline that creates engaging invitations for first-time Wikipedia editors by identifying  edit opportunities that are low effort, high impact, and highly relevant to the user’s interests.

## Tech stack
![Screen Shot 2019-06-18 at 3 55 12 PM](https://user-images.githubusercontent.com/35629096/59725158-7f3ec500-91e1-11e9-84b0-bb3546fb6afe.png)

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




