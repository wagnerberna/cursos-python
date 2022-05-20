import pytest


def soma(n, n2):
    return n + n2


# assert
def test_soma():
    assert soma(2, 5) == 7


# parametrize passa lista de parâmetros para var
# roda 3 testes
@pytest.mark.parametrize("x", [1, 2, 3])
def test_soma2(x):
    resultado = soma(x, 3)
    assert resultado - x == 3


# roda 3 x 3  = 9 testes
# se extrair o x têm de resultar no x
@pytest.mark.parametrize("x", [1, 2, 3])
@pytest.mark.parametrize("y", [1, 2, 3])
def test_soma3(x, y):
    resultado = soma(x, y)
    assert resultado - x == y
