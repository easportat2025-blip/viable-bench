import os

import click


def test_atomic_preserves_umask():
    p = "/tmp/t_atomic_perm_check"
    if os.path.exists(p):
        os.remove(p)
    click.open_file(p, "w", atomic=True).close()
    mode = oct(os.stat(p).st_mode)
    assert mode == "0o100644", mode
