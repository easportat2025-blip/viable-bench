import click
from click.testing import CliRunner


@click.command()
@click.option("--answer", flag_value=42)
def main(answer):
    click.echo(repr(answer))


def test_flag_value_keeps_int():
    r = CliRunner().invoke(main, ["--answer"])
    assert r.output.strip() == "42", repr(r.output)
