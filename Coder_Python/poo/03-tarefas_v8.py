from datetime import datetime, timedelta

# timedelta é uma diferença entre datas

# criar exceção específica
class TarefaNaoEncontrada(Exception):
    pass


# lista Tarefas passa a ser um atributo da classe projeto
class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    # sobrecarga do operador +=
    # projeto += tarefa
    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    # método p/ listar tarefas
    # C/ iter não precisa mais o .tarefas para iterar
    def listar(self):
        # for tarefa in self.tarefas:
        for tarefa in self:
            print(tarefa)

    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get("vencimento", None)))

    # método p/ add tarefa dentro do projeto
    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = (
            self._add_tarefa
            if isinstance(tarefa, Tarefa)
            else self._add_nova_tarefa
        )
        kwargs["vencimento"] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    # método p/ pegar tarefas pendentes
    # list comprehension p/ se não estiver concluida, entrar na lista.
    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    # método de busca
    # possível indexError erro se a tarefa não existir
    # list comprehension p/ se achar a tarefa traz somente o 1º el encontrado index[0]
    def procurar(self, descricao):
        try:
            # Possível IndexError
            return [
                tarefa
                for tarefa in self.tarefas
                if tarefa.descricao == descricao
            ][0]
        except IndexError as e:
            raise TarefaNaoEncontrada(str(e))

    # método para retornar uma string das tarefas
    def __str__(self):
        return f"{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))"


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento
        self.dono = None

    def concluir(self):
        self.feito = True

    # .days p/ o resultado ser em dias
    def __str__(self):
        status = []
        if self.feito:
            status.append("(Concluída)")
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append("(Vencida)")
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f"(Vence em {dias} dias )")
        return f"{self.descricao} {status}"


# Recebe a classe pai
# dias para recorrência da tarefa
# super() chamar construtor ou FN da classe pai
class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(
            self.descricao, novo_vencimento, self.dias
        )
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa


def main():
    casa = Projeto("Tarefas de Casa")
    # tarefa sem prazo vence na hora q lançar
    casa.add("Passar roupa", datetime.now())
    # add 3 dias p/ tarefa
    casa.add("Lavar prato", datetime.now() + timedelta(days=3))
    print(casa)

    # Localiza e chama fn para concluir tarefa
    casa.procurar("Lavar prato").concluir()

    # SubClasse
    casa.tarefas.append(TarefaRecorrente("Trocar lençóis", datetime.now(), 7))
    casa.tarefas.append(casa.procurar("Trocar lençóis").concluir())

    # sobreCarga do operador
    # projeto já possui dono
    casa += TarefaRecorrente("Passar aspirador", datetime.now(), 7)
    casa.procurar("Passar aspirador").concluir()

    try:
        casa.procurar("Lavar prato - ERRO").concluir()
    except TarefaNaoEncontrada as e:
        print(f'A causa foi "{str(e)}"!')
    finally:
        print("Sempre será executado!")

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
