
![Screen Shot 2019-06-18 at 3 56 27 PM](https://user-images.githubusercontent.com/35629096/59725212-af866380-91e1-11e9-8956-f4000bfcc2c6.png)


## Project Overview

Wikipedia serves more than 400M unique visitors per month. However, less than 1/10 of its editors are female, which in turn has created a biased resource.  One major reason often cited for causing women and other newcomers to be hesitant to become Wikipedia editors is the psychological barrier of not knowing where to start.  I address this issue by creating a pipeline to analyze the entire Wikipedia database with algorithms to suggest high impact, low barrier, and relevant-to-user Wikipedia pages to encourage new people to become first time editors.


## Visualization Output

Click the link for an interactive demo of my project results.
http://www.invitationtoedit.co/

**Dashboard description:** The core features of my product focus on providing a Wikipedia pages that are highly relevent pages to a users interest, as well as impactful pages to edit that require low effort.
  Attached is a screenshot to make it easier to follow along with the dashboard description below.

![Screen Shot 2019-06-25 at 3 51 43 PM](https://user-images.githubusercontent.com/35629096/60139126-96416200-9761-11e9-873e-2e558fb4fdba.png)

**High Relevence** the user can pick a list page specific to their interests by selecting one of the icons located of the top of the dashboard. User also can click multiple icons to view the top lists of results from any customized combination of results they desire.

**High Impact** By analyzing and creating metrics from joined datasets that combined are over 150 million rows: 5 different factors are taken into account when calculating overall impact: an overall Pageview Score, Helpfulness Score, Trending Score, Clickthrough Sum Score, and Click Distribution Score.  Once a user finds a page that that they find interesting, or they are knowledgable about, they can click the page and be directed to the URL on Wikipedia to go ahead and edit. If you hover over the score, you can see more granular metrics I'm referring to.  On the left, a list page receives a reward badge if they are in the top 5% in one of the performance metrics.

**Low Effort** Often the most challenge step of any activity is having the courage to take the first step.  In this case, we have created a low barrier for people to become Wikipedia editors by focusing our analysis to List Pages, as lists can be easily edited by newbies who are less familiar with Wiki markup language.



## Twitter Bot Output
For users who want to constantly be notified about interesting list pages that they can go an edit, a Twitter bot was created that tweets out a new recommended list page to edit every 4 hours.  Each list page that is tweeted achieved an exceptional characteristic about it, being in the top 5% of one of the five metrics that were used to calculated impact score.  Check out the twitter bot here: https:twitter.com/WikiBot5

## Tech Stack

![Screen Shot 2019-06-25 at 3 52 14 PM](https://user-images.githubusercontent.com/35629096/60139096-75790c80-9761-11e9-9106-806d105e2f84.png)

**Tech Stack flow description**
-*Wikipedia database to S3*: Ingested 5 months of clickstream data to S3  
-*S3 to Spark*: Spark reads data from S3 (5 files containing around 30 million rows each) and perfoms aggregate data crunching  
-*Spark to PostGreSQL* Spark sends each of the 5 aggregate DF's to PostGreSQL. Next - an API script is run from the list   titles generated from the aggregate DF to generate a table containing daily pageview data for the same 5 month period  
-*PosGresSQL to TwitterBot* PostGreSQL joins different dataframes. Impact metrics calculated in Pandas. TwitterBot inputs list pages that have exceptional metrics and tweets one of the list every 4 hours  
-*PosGresSQL to Tableau* Tableau reads in the joined, postprocessed df, and a visulation is created  
-*Tableau to Flask* The created dashboard in Tableau is published. Flask takes the embedded code from Tableau to display results on www.invitationtoedit.co  




