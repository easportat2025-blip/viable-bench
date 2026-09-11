from pelican.settings import configure_settings


def test_siteurl_trailing_slash_stripped():
    s = configure_settings({'SITEURL': 'http://example.com/blog/', 'PATH': '.'})
    assert not s['SITEURL'].endswith('/'), s['SITEURL']
    assert s.get('FEED_DOMAIN') == 'http://example.com/blog', s.get('FEED_DOMAIN')
