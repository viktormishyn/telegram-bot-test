import requests


def cat():
    res = requests.get("https://api.thecatapi.com/v1/images/search")
    cat_url = res.json()[0]['url']

    return cat_url
