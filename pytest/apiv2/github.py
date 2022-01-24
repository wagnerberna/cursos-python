import requests


def get_avatar(user):
    url = f"https://api.github.com/users/{user}"
    resp = requests.get(url)
    return resp.json()["avatar_url"]
