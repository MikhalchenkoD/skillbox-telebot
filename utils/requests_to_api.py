import requests

HEADERS = {
    "X-RapidAPI-Key": "7f93a9da02msh519358376923efap10c7b8jsna45885a8c9f5",
    "X-RapidAPI-Host": "realtor26.p.rapidapi.com"
}


def get_location(city):
    url = "https://realtor26.p.rapidapi.com/locations"
    querystring = {"location": {city}}

    response = requests.get(url, headers=HEADERS, params=querystring)

    return response.json()


def get_house(data):
    sort_dict = {
        'high': 'highest-price',
        'low': 'lowest-price',
    }
    querystring = None

    if data['method'] == 'custom':
        querystring = {
            "locationKey": data['city'],
            "type": "all",
            "maxPrice": data['max_price'],
            "minPrice": data['min_price']
        }
    else:
        querystring = {
            "locationKey": data['city'],
            "sort": sort_dict[data['method']]
        }

    url = "https://realtor26.p.rapidapi.com/properties/rent"
    response = requests.get(url, headers=HEADERS, params=querystring)
    return response.json()
