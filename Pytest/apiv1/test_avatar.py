from apiv1.github import get_avatar


def test_avatar():
    assert (
        "https://avatars.githubusercontent.com/u/72299498?v=4"
        == get_avatar("wagnerberna")
    )
