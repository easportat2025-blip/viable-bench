from elasticsearch5.exceptions import TransportError


def test_str_with_string_error_body():
    e = TransportError(406, '{"error":"Content-Type header [application/octet-stream] is not supported","status":406}')
    s = str(e)
    assert 'not supported' in s, s
