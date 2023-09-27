import requests
headers = {
    'User-Agent': 'Flipping tools - Rugg - Discord Rugg#4267'
}
def get_latest_prices():
    response = requests.get(
        "https://prices.runescape.wiki/api/v1/osrs/latest", 
        headers = headers,
    )
    instantResults = response.json()['data']
    return instantResults

def get_mapping():
    response = requests.get(
        "https://prices.runescape.wiki/api/v1/osrs/mapping", 
        headers = headers)
    data = response.json()
    return data

def get_id_to_name_mapping(map):
    return {data['id']: data['name'] for data in map}

def get_name_to_id_mapping(map):
    return {data['name']: data['id'] for data in map}

def get_1h_prices():
    response = requests.get(
        "https://prices.runescape.wiki/api/v1/osrs/1h", 
        headers = headers)
    data = response.json()['data']
    return data

def get_guide_prices(item_ids):
    base_url = "https://api.weirdgloop.org/exchange/history/osrs/latest"
    split_lists = [item_ids[i:i+100] for i in range(0, len(item_ids), 100)]
    results = {}
    for section in split_lists:
        response = requests.get(
            base_url, 
            params = {
                "id": '|'.join(map(str, section)),
                'lang': 'en'
            })
        data = response.json()
        for id, entry in data.items():
            results[id] = entry
    return results