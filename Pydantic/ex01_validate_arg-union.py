from ctypes import Union
from pydantic import validate_arguments
from typing import Union

# Python não valida em tempo de execução, não dá erro, tenta realizar a operação
# validade para em tempo de execução
@validate_arguments
def soma1 (x: int, y: int):
    return x + y

print(soma1(2,3))
# retorna erro:
# print(soma1("a","b"))

# union "OU" permite duas opções de arg.
@validate_arguments
def soma2 (x: Union[int, str], y: Union[int, str]):
    return x + y

print(soma2(2,3))
print(soma2("a","b"))