from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluido = False
        self.criacao = datetime.now()

    def concluir(self):
        self.concluido = True

    def __str__(self):
        return f'{self.descricao} {"(Concluída)" if self.concluido else ""}'


def main():
    # lista armazenar os objetos criados pela classe tarefa
    casa = []
    casa.append(Tarefa("Lavar louça"))
    casa.append(Tarefa("Passar aspirador"))
    # list comprehension p/ concluir quando a tarefa for lavar louça
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == "Lavar louça"]
    for tarefa in casa:
        print(f"-{tarefa}")


main()
