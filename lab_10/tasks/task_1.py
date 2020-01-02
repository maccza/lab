import requests
from urllib.parse import urljoin

def get_cities_woeid(query: str, timeout: float = 5.):
    API_URL =   'https://www.metaweather.com/api/'
    location_url = urljoin(API_URL, 'location/search')
    params = dict(query = query)
    response = requests.get(location_url, params=params)
    

    return {request["title"]: request["woeid"] for request  in response.json()}


if __name__ == '__main__':
    assert get_cities_woeid('Warszawa') == {}
    assert get_cities_woeid('War') == {
        'Warsaw': 523920,
        'Newark': 2459269,
    }
    try:
        get_cities_woeid('Warszawa', 0.1)
    except Exception as exc:
        isinstance(exc, requests.exceptions.Timeout)
