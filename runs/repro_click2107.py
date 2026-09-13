import os
import pathlib

import click


def test_path_dash_writes_stdout(tmp_path=None):
    work = "/tmp/dash_probe_dir"
    os.makedirs(work, exist_ok=True)
    lit = os.path.join(work, "-")
    if os.path.exists(lit):
        os.remove(lit)
    cwd = os.getcwd()
    os.chdir(work)
    try:
        f = click.open_file(pathlib.Path("-"), "w")
        f.write("x")
        f.flush()
        assert not os.path.exists(lit), "created literal file '-' instead of stdout!"
    finally:
        os.chdir(cwd)
