import pytest


def soma_1(numero):
    return int(numero) + 1


# teste:
def test_soma_1():
    assert soma_1(41) == 42


def test_soma_1_numero_como_string():
    assert soma_1("41") == 42


# raises só passa se ao executar retorna um erro
# mas não verifica o tipo do erro
def test_soma_1_com_palavra():
    with pytest.raises(ValueError):
        assert soma_1("wagner")
