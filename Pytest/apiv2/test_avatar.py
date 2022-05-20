import pytest
from apiv2 import github

__resp__wagnerberna = {
    "login": "wagnerberna",
    "id": 72299498,
    "node_id": "MDQ6VXNlcjcyMjk5NDk4",
    "avatar_url": "https://avatars.githubusercontent.com/u/72299498?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/wagnerberna",
    "html_url": "https://github.com/wagnerberna",
    "followers_url": "https://api.github.com/users/wagnerberna/followers",
    "following_url": "https://api.github.com/users/wagnerberna/following{/other_user}",
    "gists_url": "https://api.github.com/users/wagnerberna/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/wagnerberna/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/wagnerberna/subscriptions",
    "organizations_url": "https://api.github.com/users/wagnerberna/orgs",
    "repos_url": "https://api.github.com/users/wagnerberna/repos",
    "events_url": "https://api.github.com/users/wagnerberna/events{/privacy}",
    "received_events_url": "https://api.github.com/users/wagnerberna/received_events",
    "type": "User",
    "site_admin": False,
    "name": "Wagner Berna",
    "company": "null",
    "blog": "",
    "location": "null",
    "email": "null",
    "hireable": "null",
    "bio": "null",
    "twitter_username": "null",
    "public_repos": 7,
    "public_gists": 0,
    "followers": 6,
    "following": 1,
    "created_at": "2020-10-03T09:32:52Z",
    "updated_at": "2021-11-03T20:22:07Z",
}

# class RespMock


def get_mock(user):
    return __resp__wagnerberna


def test_avatar():
    # # setup preparação para o teste
    # # chama o atributo requests com fn get
    assert github.requests.get == get_mock

    # Test
    assert (
        "https://avatars.githubusercontent.com/u/72299498?v=4"
        == github.get_avatar("wagnerberna")
    )
