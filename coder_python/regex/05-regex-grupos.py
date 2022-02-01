# Meta caracteres: ^ $
# ()     \1
# () ()  \1 \2
# (())()   \1 \2 \3
import re
from pprint import pprint

texto = """
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
"""
