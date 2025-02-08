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

### Data Extraction:
Data was extracted using a TicketMaster API. The raw json file size was too large to request, so a json file with AWS buckets storing the data was requested instead, and code was written in master_data_set.py to extract the csv download link for all US events. 

### Exploratory Data Analysis:

### Libraries, Packages, Modules & Submodules Used:

    a. pandas as pd
    b. matplotlib.pylab as plt
    c. matplotlib.dates as mdates
    d. numpy as np
    e. seaborn as sns
    f. plotly pandas
    g. from random import randint

