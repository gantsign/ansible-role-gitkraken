def test_gitkraken(Command):
    assert Command('which gitkraken').rc == 0
