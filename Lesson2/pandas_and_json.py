import json
import requests
import pprint

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    data = requests.get(url).text
    df = json.loads(data)
    pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(df['topartists']['artist']['rank' == 1]['name'])
    return df['topartists']['artist']['rank' == 1]['name'] # return the top artist in Spain
