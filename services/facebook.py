# services/facebook.py

import requests
from config import PAGE_ID, LONG_LIVED_TOKEN, FACEBOOK_API_URL


def post_image(image_url: str, caption: str):
    """
    Post image to Facebook Page using long lived token
    """
    url = f"{FACEBOOK_API_URL}/{PAGE_ID}/photos"

    payload = {
        "url": image_url,
        "caption": caption,
        "access_token": LONG_LIVED_TOKEN,
        "published": True
    }

    response = requests.post(url, data=payload)
    return response.json()