# Election_Analysis
# Election_Analysis

## Overview

The Election Audit analysis was performed to get the Election Results from a CSV file that contained the Election County, Votes, and Candidate Names. This audit will be presented to the election commission for review of the winner and other statistics pulled from the data file such as County turnout and percent of votes per county and candidate. The audit also displays the county with the highest turn out and number of votes broken down per county. All of the results are then printed on the "election_analysis.txt" file in the analysis folder.


## Election Audit Results

    - There were a total of 369,711 votes 
    
    - Denver had the highest number of votes (306,055)

    - The winner of the election is Diana DeGette coming in with 272,892 votes which made up 73.8% of the votes
    
    
    - Number of votes, percentage of total votes for each candidate, and total votes for each county is as follows:

![](Resources/Screen%20Shot%202020-08-08%20at%202.38.50%20PM.png)



## Summary

This code can be used for any upcoming election with a few modifications.
The first modification would be to adjust the paths where the data is coming and going to:

For example- In the picture below you would want to create a seperate file for the .txt in order to record the data from the election results into different files in order to keep track and not overwrite any file.


Also, since this script intakes a CSV file and records data from that sheet the first modification is to make sure the code will pull the right data when assinging it to the list. 

For example:
