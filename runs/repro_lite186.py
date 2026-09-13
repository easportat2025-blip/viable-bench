from starlette.exceptions import HTTPException

from starlite.utils.exception import get_exception_handler


def h500(request, exc):
    return "h500"


def hhttp(request, exc):
    return "hhttp"


def test_mro_beats_500_fallback():
    exc = HTTPException(status_code=404)
    got = get_exception_handler({500: h500, HTTPException: hhttp}, exc)
    assert got is hhttp, got
