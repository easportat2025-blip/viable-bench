import click
from click.testing import CliRunner


@click.command()
@click.option("--opt", default=1)
@click.pass_context
def cli(ctx, opt):
    src = ctx.get_parameter_source("opt")
    click.echo("SRC=%s VAL=%s" % (src, opt))


def test_parameter_source_tracked():
    assert hasattr(click, "ParameterSource"), "no ParameterSource"
    r1 = CliRunner().invoke(cli, [])
    assert "SRC=ParameterSource.DEFAULT" in r1.output, r1.output
    r2 = CliRunner().invoke(cli, ["--opt", "5"])
    assert "SRC=ParameterSource.COMMANDLINE" in r2.output, r2.output
