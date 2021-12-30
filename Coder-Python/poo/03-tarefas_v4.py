from datetime import datetime, timedelta

# timedelta é uma diferença entre datas

# lista Tarefas passa a ser um atributo da classe projeto
class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    # método p/ listar tarefas
    # C/ iter não precisa mais o .tarefas para iterar
    def listar(self):
        # for tarefa in self.tarefas:
        for tarefa in self:
            print(tarefa)

    # método p/ add tarefa dentro do projeto
    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

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
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append("(Concluída)")
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append("(Vencida)")
            else:
                # .days p/ o resultado ser em dias
                dias = (self.vencimento - datetime.now()).days
                status.append(f"(Vence em {dias} dias )")
        return f"{self.descricao} {status}"


def main():
    casa = Projeto("Tarefas de Casa")
    # tarefa sem prazo vence na hora q lançar
    casa.add("Passar roupa", datetime.now())
    # add 3 dias p/ tarefa
    casa.add("Lavar prato", datetime.now() + timedelta(days=3))
    print(casa)
    # Localiza e chama fn para concluir tarefa
    casa.procurar("Lavar prato").concluir()
    casa.listar()

    mercado = Projeto("Compras no mercado")
    mercado.add("Frutas secas")
    mercado.add("Carne")
    mercado.add("Tomate", datetime.now() + timedelta(days=3, minutes=12))
    print(mercado)

    # iter não precisa mais usar o projeto.tarefas para iterar
    comprar_carne = mercado.procurar("Carne")
    comprar_carne.concluir()
    # for tarefa in mercado.tarefas:
    for tarefa in mercado:
        print(f"- {tarefa}")
    print(mercado)


main()
