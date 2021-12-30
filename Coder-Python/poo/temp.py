from datetime import datetime

# lista Tarefas passa a ser um atributo da classe projeto
class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    # método p/ add tarefa dentro do projeto
    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    # método p/ pegar tarefas pendentes
    # list comprehension p/ se não estiver concluida, entrar na lista.
    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    # método de busca
    # possível indexError erro se a tarefa não existir
    # list comprehension p/ se achar a tarefa traz somente o 1º el encontrado index[0]
    def procurar(self, descricao):
        # Possível IndexError
        return [
            tarefa for tarefa in self.tarefas if tarefa.descricao == descricao
        ][0]

    # método para retornar uma string das tarefas
    def __str__(self):
        return f"{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))"


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (" (Concluída)" if self.feito else "")


def main():
    casa = Projeto("Tarefas de Casa")
    casa.add("Passar roupa")
    casa.add("Lavar prato")
    print(casa)

    # casa.procurar("Lavar prato").concluir()
    # for tarefa in casa.tarefas:
    #     print(f"- {tarefa}")
    # print(casa)

    # mercado = Projeto("Compras no mercado")
    # mercado.add("Frutas secas")
    # mercado.add("Carne")
    # mercado.add("Tomate")
    # print(mercado)

    # comprar_carne = mercado.procurar("Carne")
    # comprar_carne.concluir()
    # for tarefa in mercado.tarefas:
    #     print(f"- {tarefa}")
    # print(mercado)


if __name__ == "__main__":
    main()
