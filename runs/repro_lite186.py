from starlette.exceptions import HTTPException

from starlite.utils.exception import get_exception_handler


def h500(request, exc):
    return "h500"


def hhttp(request, exc):
    return "hhttp"


class MyErr(HTTPException):
    def __init__(self):
        super().__init__(404, "x")


def test_mro_beats_500_fallback():
    got = get_exception_handler({500: h500, HTTPException: hhttp}, MyErr())
    assert got is hhttp, got
