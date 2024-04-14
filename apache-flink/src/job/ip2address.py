import os
import json
import requests

def get_geolocation(ip_address):
    api_url = "https://api.ip2location.io"
    api_key = os.environ.get("IP_CODING_KEY")

    if not api_key:
        print("Warning: IP_CODING_KEY environment variable not found. Limited data may be returned.")

    params = {
        'ip': ip_address
    }

    if api_key:
        params['key'] = api_key  

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return {}

    try:
        data = json.loads(response.text)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
        return {}

    country = data.get('country_code', '')
    state = data.get('region_name', '')
    city = data.get('city_name', '')

    return data


print(get_geolocation("71.198.153.28"))