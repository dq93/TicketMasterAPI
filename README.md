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

## Analsysis Conclusions

### A. Event Type
The four main event types in this dataset are Sports, Music, Film, and Theatre & Arts. Miscellaneous event types were not considered in this analysis. 

Looking at the mean and median of each Event Type, it is clear that all event types display a right skew, with Sports displaying the most extreme skew followed by Music, Arts & Theatre, & Film. This offers a good segwayto examine the density of max prices accross each event type and the information this convey in terms of perceived demand for each event type. 

| Classification |   Mean  | Median |
| -------------- | ------- | ------ |
| Sports         | $366.68 | $70.00 |
| Arts & Theatre | $113.63 | $93.83 |
| Music          | $94.74  | $59.50 |
| Film           | $30.08  | $19.00 |

Due to the extreme outliers and their impact on visualization of max price distribution, a violin plot was used to observe the density of Max Prices per event, filtering out any Max Prices over $300. The plot showed that the highest density of Max Prices for Arts & Theatre hovered at around $100, while the highest density of all other events hovered at the lower end between $20 to $50. This shows that for Arts & Theatre, maximum prices closer to the average of $113 are more common which shows more sustained popularity and demand for the Arts & Theatre events. For the other events, the higher density on the lower price range shows that the majority of events within these categories may not bring much demand. However, there are certain conditions that cause max prices to spike extremely high, as we'll with the outlier and maximum max price analysis below. 



### B. State
There was one lone state with a maximum ticket price that was less than $100, and only 17 states between the $100-$999 range. The upper price ranges of $1000+ dominated the rest of the map, with California, Nevada, Kentucky, New York and Florida leading the pack as the uber-expensive. Exorbitant ticket prices might be explained by new venues, high-end event packages that give the event-goer an unforgettable experience, and loyal fans who will do what it takes to see their favorite performers. However, a deeper dive needs to be done to find out if these prices are indicative of one single ticket sale or packaged ticket sales with extra amenities. I would also be interested in knowing if these are direct ticket sales by Ticketmaster or if they are resales by outside sellers.


### C. Duration of Sales