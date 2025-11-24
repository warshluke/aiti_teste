import pytest
from fatorial import fatorial

@pytest.mark.parametrize("n,esperado", [(0,1),(1,1),(2,2),(3,6)])
def test_fatorial(n, esperado):
        assert fatorial(n) == esperado
