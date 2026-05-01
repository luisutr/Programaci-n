import pytest
import pruebas as l

@pytest.mark.basic
def test_mayus_ini():
    assert "How Can Mirrors Be Real If Our Eyes Aren't Rea " == l.mayus_ini("How can mirrors be real if our eyes aren't rea")
