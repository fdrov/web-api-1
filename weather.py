from typing import List

import requests

cities: List[str] = ['London', 'svo', 'Череповец']


def get_forecast(location: str) -> str:
    url = f'http://wttr.in/{location}'
    payload = {
        'mMnTq': '',
        'lang': 'ru'
    }
    response = requests.get(url=url, params=payload)
    response.raise_for_status()
    return response.text


if __name__ == "__main__":
    for city in cities:
        try:
            forecast = get_forecast(city)
            print(forecast)
        except requests.exceptions.HTTPError as err:
            print('The is an error', err)
