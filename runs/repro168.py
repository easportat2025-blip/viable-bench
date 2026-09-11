import json

from starlite import Starlite
from starlite.exceptions import HTTPException


def test_status_code_present_in_handler():
    exc = HTTPException(detail="boom", status_code=404)
    resp = Starlite.default_http_exception_handler(None, None, exc)
    body = json.loads(bytes(resp.body).decode())
    assert body.get("status_code") == 404, body
    assert body.get("detail") == "boom", body
