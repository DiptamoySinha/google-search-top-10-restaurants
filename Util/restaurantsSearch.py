import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
api = os.getenv('API')

params = {
    "engine": "google_local",
    "q": "top+10+restaurants+for+best+food",
    "location": "Delhi",
    "gl": "in",
    "hl": "en",
    "api_key": API_KEY
}

def search(city: str):
    params['location'] = city
    response = requests.get(api, params=params)
    results = []

    if response.status_code != 200:
        print('something went wrong')
    else:
        print('fetching....')
        results = response.json()['local_results'] #get the retaurants details as list

    #sort the restaurants by reviews in decending order
    results.sort(key= lambda x: (-x['reviews']))

    #get the top 10 restaurants above 4 rating 
    results = list(filter(lambda x : x['rating'] > 4, results))[:10]

    # res is our list which will hold the restaurants name as key (rating and review ) as values
    res = []
    for r in results:
        key = dict()
        value = dict()
        value['rating'] = r['rating']
        value['reviews'] = r['reviews']

        key[r['title']] = value

        res.append(key)
    return res

def dumpFile(folder, res):
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = os.path.join(folder, "extract.json")


    # dir_path = os.path.dirname(os.path.abspath(__file__))
    # file_path = dir_path +'/extractData/top10restaurants.json'
    # os.path.abspath("top10restaurants.json")

    with open(file_path, 'w') as json_file:
        json.dump(res, json_file, indent=4)
