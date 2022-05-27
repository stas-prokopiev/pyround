import pyround


def test_version():
    pyround.rtnsd(0.23234, 2)
    assert pyround.rtnsd(0.23234, 2) == 0.23
    assert pyround.rtnsd(0.23534, 2) == 0.24
    assert pyround.rtnsd(105.3, 1) == 100
    assert pyround.rtnsd(125.3, 2) == 130
