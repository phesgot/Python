import abc


class Conta(abc.ABC):

    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO R${valor:.2f})')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é R${self.saldo:.2f} {msg}')
        print('-'*10)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE R${valor:.2f})')
            return self.saldo

        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO DE R${valor:.2f})')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(
        self, agencia: int, conta: int, saldo: float = 0,
        limite: float = 0
    ):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE R${valor:.2f})')
            return self.saldo

        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO DE R${valor:.2f})')
        return self.saldo

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
            f'{self.limite!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':

    cp1 = ContaPoupanca(111, 222, 0)
    cp1.sacar(1)
    cp1.depositar(100)
    cp1.detalhes()
    cp1.sacar(10)

    print('#'*10)

    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(20)
    cc1.sacar(90)
    cc1.sacar(80)
    cc1.depositar(400)
