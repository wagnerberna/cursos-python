# Interpolação Substituir valores da string

# !!!Método mais Antigo!!!
# Criação 2 var na mesma linha
nome, media = "Wagner", 7.99
# "$s" substituir tipo string
# "%f" float C/ 2 casas decimais / Arredondando
# "%d" substituir float por inteiros "int" corta final
# "%r" true ou false
print("Aluno: %s Media Final: %.2f " % (nome, media))
print("Aluno: %s Media Final: %.1f " % (nome, media))
print("Aluno: %s Media Final: %d " % (nome, media))
print("Aprovado: %r" % (True))
print("conversão booleano %d e %d" % (True, False))

# !!!Método mais atual!!!
# valores em ordem ou indexados ou C/ nome var
print("Aluno: {} Media Final: {} ".format(nome, media))
print("Aluno: {0} Media Final: {1} ".format(nome, media))
print("Aluno: {1} Media Final: {0} ".format(nome, media))
# "f" (format) C/ nome var / aceita expressão
print(f"Aluno: {nome} Media Final: {media} extra: {media -7} ")
# ou
print(f"Aluno: {nome} Media Final: {media} extra:", media - 7)
print("Aprovado: {}".format(True))
