import Veiculo
class Lancha( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, capacidadeAgua, passageiros ):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Lancha")
        self.capacidadeAgua = capacidadeAgua
        self.passageiros = passageiros
        self.marcha = 0
    def ligar( self ):
        return self.marcha
    def desligar( self ):
        self.marcha = 0
""" Aqui comeca o teste """
Lancha = Lancha('não informado', 'Lanchas Coral', 'MERCRUISER', '2023', '310', 'Dia: 14 | Noite: 4')
print(Lancha.get_tipo())
print(Lancha.passageiros)
print(Lancha.marca)
print(Lancha.modelo)
print(Lancha.ligar())