import requests
import json

#sourced from this website: https://developer.ticketmaster.com/products-and-docs/apis/discovery-feed/#json-feed-response
#scrape page
api_key = 'your api key'
url = f"https://app.ticketmaster.com/discovery-feed/v2/events?apikey={api_key}"

#request page
page = requests.get(url)
if page.status_code == 200:
    print('True')

#convert object to json object
data = page.json()

#save json object file
save_file = open("data/json/ticketMaster.json", "w")
json.dump(data, save_file, indent = 6)
save_file.close()

#load json file
with open("data/json/ticketMaster.json") as f:
    data = json.load(f)
    f.close()

print("On your mac, press 'command' and click on this link to download the csv: \n" + data['countries']["US"]["CSV"]["uri"]) 

