import Veiculo

class Motocicleta( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, potencia, tipoCarro ):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Carro")
        self.potencia = potencia
        self.tipoCarro = tipoCarro