'''
This module fetches 100 protein-protein interaction data for Homo Sapiens from the STRING database API. 
'''
import requests
import pandas as pd

def fetch_interactions(protein_id, species=9606, limit=100):
    url = f"https://string-db.org/api/json/interactions?identifier={protein_id}&species={species}&limit={limit}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")

    data = response.json()
    interactions = pd.DataFrame(data)
    return interactions