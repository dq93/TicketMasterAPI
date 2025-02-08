# TicketMasterAPI Exploratory Data Analysis

The TicketMasterAPI EDA is exploring **Maximum Price** (dependent variable) across different independent variables:

    a. Event Type
        -exploring how different event types impact maximum ticket prices
    b. State
        -analyzing price variations across the United States
    c. Duration of Sales
        -examining the effect of ticket sale duration on maximum price
    d. Promoters
        -investigating how different promoters influence ticket prices
    e. Event Genres
        -comparing maximum price trends across different event genres

## Data Extraction:
Data was extracted using a TicketMaster API. The raw json file size was too large to request, so a json file with AWS buckets storing the data was requested instead, and code was written in master_data_set.py to extract the csv download link for all US events. 

## Exploratory Data Analysis:

### Libraries, Packages, Modules & Submodules Used:

    a. pandas as pd
    b. matplotlib.pylab as plt
    c. matplotlib.dates as mdates
    d. numpy as np
    e. seaborn as sns
    f. plotly pandas
    g. from random import randint

## Analysis Conclusions

### A. Event Type
The four main event types in this dataset are Sports, Music, Film, and Theatre & Arts. Miscellaneous event types were not considered in this analysis. 

Looking at the mean and median of each Event Type, it is clear that all event types display a right skew, with Sports displaying the most extreme skew followed by Music, Arts & Theatre, & Film. This offers a good segwayto examine the density of max prices accross each event type and the information this convey in terms of perceived demand for each event type. 

| Classification |   Mean  | Median |
| -------------- | ------- | ------ |
| Sports         | $366.68 | $70.00 |
| Arts & Theatre | $113.63 | $93.83 |
| Music          | $94.74  | $59.50 |
| Film           | $30.08  | $19.00 |

Due to the extreme outliers and their impact on visualization of max price distribution, a violin plot was used to observe the density of Max Prices per event, filtering out any Max Prices over $500 based on the max upper limit for Sports. The plot showed that the highest density of Max Prices for Arts & Theatre hovered at around $100, while the highest density of all other events hovered at the lower end between $20 to $50. This shows that for Arts & Theatre, maximum prices closer to the average of $113 are more common indicating more sustained popularity and demand for the Arts & Theatre events. For the other events, the higher density on the lower price range shows that the majority of events within these categories may not bring much demand. Instead, there may be select events for each of the remaining classifications that drive high maximum ticket prices due to event-specific popularity and wide-interest.  

From the outlier data below, we can see that Sports displays the higher upper limit and a significant amount of 15% of all events have max ticket prices above this limit. Although Film shows a high number of outlier events, the Max Price upper limit is at a more humble price of $31.50, six times less than Sports. Arts & Theatre and Music also have a high upper limit, but still lie at nearly half of Sports' upper limit. This indicates that several sports events have a perceived high demand that results in extreme ticket prices going for sale. 

#### Outliers
| Classification |	Total Number of Events | Number of Outliers	| % Outliers from Total Events	| Upper Limit |
| -------------- | ------- | ------ | ------ | ------ |
| Sports |	7,720 |	1,125 |	15%	| $505.00 |
| Arts & Theatre |	22,759	| 1,369 |	6%	| $258.30 |
| Music	| 19,437 |	1,551 |	8%	| $208.25 |
| Film | 202 |	42 | 21%	| $31.50 |

Finally, taking a look at the specific events with the maximum max prices for each classification, we see some extreme prices for sports and music. For future analysis, it would be valuable to breakdown the certain characteristics of each "Event Name" and the max ticket prices distributed based on those characteristics (ex. music genre, sports team, film directors, etc.). For now, we can takeaway that Sports and Music events display a wide range of max prices that may correlate to the perceived demand of what extreme fans might be willing to pay for a seat in the venue. However, Arts & Theatre events show a more consistent and sustained demand with less extreme ticket prices. Additionally, film ticket prices remain on the lower end in comparison to the other three classifications. 

#### Maximums
| Classification |   Event Name  | Max Price |
| -------------- | ------- | ------ |
| Sports         | LA Clippers vs. Los Angeles Lakers | $21,000 |
| Music | Free Beer (the Band) Florida's #1 Party Band (A Tribute to The Rooster! Marcus Outzen former QB for FSU) | $10,000 |
| Arts & Theatre          | Kevin James: Owls Don't Walk  | $1,041 |
| Film           | STOP MAKING SENSE: A Film by Jonathan Demme and Talking Heads  | $179 |


### B. State
There was one lone state with a maximum ticket price that was less than $100, and only 17 states between the $100-$999 range. The upper price ranges of $1000+ dominated the rest of the map, with California, Nevada, Kentucky, New York and Florida leading the pack as the uber-expensive. Exorbitant ticket prices might be explained by new venues, high-end event packages that give the event-goer an unforgettable experience, and loyal fans who will do what it takes to see their favorite performers. However, a deeper dive needs to be done to find out if these prices are indicative of one single ticket sale or packaged ticket sales with extra amenities. I would also be interested in knowing if these are direct ticket sales by Ticketmaster or if they are resales by outside sellers.


### C. Duration of Sales