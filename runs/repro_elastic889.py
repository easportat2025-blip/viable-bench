from elasticsearch5.exceptions import TransportError


def test_str_with_string_error_body():
    info = {"error": "Content-Type header [application/octet-stream] is not supported", "status": 406}
    e = TransportError(406, "Content-Type header [application/octet-stream] is not supported", info)
    s = str(e)
    assert 'not supported' in s, s
