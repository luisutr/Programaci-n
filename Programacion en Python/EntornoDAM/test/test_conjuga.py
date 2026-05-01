import pytest
from conjuga import *

@pytest.mark.basic
def test_canjuga():
    assert [] == conjuga("")
    assert ['perdo', 'perdes', 'perde', 'perdemos', 'perdeis', 'perden'] == conjuga("perder")
    assert ['salto', 'saltas', 'salta', 'saltamos', 'saltais', 'saltan'] == conjuga("saltar")
    assert ['valoro', 'valoras', 'valora', 'valoramos', 'valorais', 'valoran'] == conjuga("valorar")
    assert ['conjugo', 'conjugas', 'conjuga', 'conjugamos', 'conjugais', 'conjugan'] == conjuga("conjugar")
    assert ['programo', 'programas', 'programa', 'programamos', 'programais', 'programan'] == conjuga("programar")
    assert ['perdo', 'perdes', 'perde', 'perdemos', 'perdeis', 'perden'] == conjuga('perder')
    assert ['vivo', 'vives', 'vive', 'vivimos', 'vivis', 'viven'] == conjuga('vivir')
    assert ['teno', 'tenes', 'tene', 'tenemos', 'teneis', 'tenen'] == conjuga('tener')
    assert ['sobrevivo', 'sobrevives', 'sobrevive', 'sobrevivimos', 'sobrevivis', 'sobreviven'] == conjuga('sobrevivir')
    assert ['bebo', 'bebes', 'bebe', 'bebemos', 'bebeis', 'beben'] == conjuga('beber')
    assert ["corro", "corres", "corre", "corremos", "correis", "corren"] == conjuga("correr")
    assert ["amo", "amas", "ama", "amamos", "amais", "aman"] == conjuga("amar")
    #assert ["sirvo", "sirves", "sirve", "servimos", "servis", "sirven"] == conjuga("servir")

