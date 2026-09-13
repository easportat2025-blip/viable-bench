from mimesis.providers.path import Path


def test_home_has_no_trailing_slash():
    assert Path(platform="linux").home() == "/home"
