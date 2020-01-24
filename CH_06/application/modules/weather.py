"""This module gets the weather information from a 
public API using the requests module
"""

from typing import Dict
from argparse import Namespace
import requests


def get(
    weather_api_url: str = None,
    weather_api_key: str = None,
    args: Namespace = None
) -> Dict:
    """Function to call the weatherbit.io external api to get
    the weather information for the passed arguments
    
    Keyword Arguments:
        weather_api_url {str} -- URL of the API (default: {None})
        weather_api_key {str} -- required key to call the API (default: {None})
        args {object} -- passed in arguments collection (default: {None})
    
    Returns:
        Dict -- dictionary of weather information
    """
    url = weather_api_url
    headers = {'Accept': 'application/json'}
    params = {
        'key': weather_api_key,
        'postal_code': args.zipcode,
        'city': args.city,
        'country': 'US',
        'units': args.units
    }
    resp = requests.get(url, params=params, headers=headers)

    # did we get a successful response?
    if resp.status_code == requests.codes.ok:
        return resp.json().get('data', {})[0]
    else:
        return (resp.status_code, resp.reason)
