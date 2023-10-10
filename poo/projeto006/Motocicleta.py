import Veiculo

class Motocicleta( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, cilindrada, numero_rodas ):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Motocicleta")
        self.cilindrada = cilindrada
        self,numero_rodas = numero_rodas
        #Aqui começa o teste
Moto = Motocicleta("5azkg01z12a339037", "Honda", "GG", "2015", 1200, 2)
print(Moto.get_tipo())
print(Moto.numero_rodas())