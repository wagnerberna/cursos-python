# Dicionário {chave: valor} "Objeto"
# indexado normalmente por uma string
pessoa1 = {"nome": "Aline", "idade": 20}
# lista dentro do dicionário
pessoa2 = {"nome": "Wagner", "idade": 40, "cursos": ["udemy", "trybe"]}
pessoa3 = {"nome": "Aline", 123: "teste"}
quant_chaves_p1 = len(pessoa1)
quant_chaves_p2 = len(pessoa2)

# normalmente não se usa variáveis, mas funciona
chave1 = "nome"
chave2 = "idade"
valor1 = "Bruce"
valor2 = "30"
pessoa3 = {chave1: valor1, chave2: valor2}

# Acesso
# index (chave)
print(pessoa1["nome"])
# chave / lista
print(pessoa2["cursos"][1])

# keys (Chaves)
print(pessoa2.keys())
# values (Valores)
print(pessoa2.values())
# items (pares de Chave e Valores)
print(pessoa2.items())
# get (retorna valor, pode retornar valor default)
print(pessoa1.get("idade"))
print(pessoa1.get("chave_nao_existe", []))

pessoa4 = {"nome": "Cris", "idade": 30, "cursos": ["udemy"]}
# Add append
pessoa4["cursos"].append("React")
# Alterando valores
pessoa4["nome"] = "Aline Flores"
# update (atualizar ou add)
pessoa4.update({"nome": "Cris", "idade": 30, "cursos": ["podóloga"]})
pessoa4.update({"nome": "Cristiane", "sexo": "F"})
# Remover chave:
# pop (remove e lê o valor da chave removida)
idade_cris = pessoa4.pop("idade")
# del (Deletar chave)
del pessoa4["cursos"]
