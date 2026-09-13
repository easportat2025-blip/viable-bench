import datetime

import click


def test_datetime_type_converts():
    assert hasattr(click, "DateTime"), "no DateTime type"
    d = click.DateTime().convert("2021-01-02", None, None)
    assert d == datetime.datetime(2021, 1, 2), d
