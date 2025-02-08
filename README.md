# TicketMasterAPI

### Data Extraction:
Data was extracted using a TicketMaster API. The raw json file size was too large to request, so a json file with AWS buckets storing the data was requested instead, and code was written in master_data_set.py to extract the csv download link for all US events. 

### Exploratory Data Analysis:
The TicketMaster API EDA is exploring Maximum Price (dependent variable) across different independent variables:
    a. Event Type
    b. State
    c. Duration of Sales
    d. Promoters
    e. Event Genres

