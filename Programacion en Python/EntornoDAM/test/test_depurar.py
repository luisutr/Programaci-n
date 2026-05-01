import pytest
import depurar as l

@pytest.mark.basic
def test_mayus_ini():
    assert "notable" == l.notas(8)
    assert "sobresaliente" == l.notas(10)
    assert "sobresaliente" == l.notas(9)
    assert "suspenso" == l.notas(3)
    assert "suspenso" == l.notas(-3)
    assert "bien" == l.notas(6)
    assert "La nota introducida es erronea" == l.notas(24)