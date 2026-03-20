# services/token.py

import requests
from config import APP_ID, APP_SECRET, PAGE_ID, FACEBOOK_API_URL


def get_long_lived_token(short_lived_token: str):
    """
    Exchange short lived token for long lived token (60 days)
    API: GET https://graph.facebook.com/v25.0/oauth/access_token
    """
    url = f"{FACEBOOK_API_URL}/oauth/access_token"

    params = {
        "grant_type": "fb_exchange_token",
        "client_id": APP_ID,
        "client_secret": APP_SECRET,
        "fb_exchange_token": short_lived_token
    }

    response = requests.get(url, params=params)
    result = response.json()

    if "access_token" in result:
        return result["access_token"]
    else:
        raise Exception(f"Failed to get long lived token: {result}")