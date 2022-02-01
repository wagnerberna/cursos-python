try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
    )
except ImportError:
    raise

from pacote1 import modulo1
from pacote1 import modulo2

# importar módulos de nomes iguais
from pacote2 import modulo1 as modulo1_sub

# Importar direto a FN
from pacote2.modulo1 import subtracao as sub

print(type(modulo1))
print(modulo1.soma(2, 3))
modulo2.teste()
print(modulo1_sub.subtracao(7, 5))
print(sub(7, 5))
