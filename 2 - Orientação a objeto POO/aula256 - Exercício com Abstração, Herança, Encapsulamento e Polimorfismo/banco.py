import contas
import pessoas


class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta: contas.Conta) -> bool:
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    def _checa_cliente(self, cliente: pessoas.Pessoa) -> bool:
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False

    def _checa_conta(self, conta: contas.Conta) -> bool:
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False

    def _checa_se_conta_e_do_cliente(
        self, cliente: pessoas.Cliente, conta: contas.Conta
    ) -> bool:
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False

    def autenticar(
        self, cliente: pessoas.Cliente, conta: contas.Conta
    ) -> bool:
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.contas!r}, {self.clientes!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':

    c1 = pessoas.Cliente('Pedro', 28)
    cc1 = contas.ContaCorrente(111, 222, 100, 100)
    c1.conta = cc1

    c2 = pessoas.Cliente('Maria', 23)
    cp1 = contas.ContaPoupanca(112, 333, 200)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([112, 222])

    if banco.autenticar(c2, cp1):
        cp1.depositar(10)
        c2.conta.depositar(10)
        print(c2.conta)
