import Veiculo
class Caminhao ( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, numero_rodas, tracao, transmissao, cabines ):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Caminhao")
        self.numero_rodas = numero_rodas
        self.tracao = tracao
        self.transmissao = transmissao
        self.cabines = cabines
        self.marcha = 0
    def ligar( self ):
        return self.marcha
    def desligar( self ):
        self.marcha = 0
""" Aqui comeca o teste """
Caminhao = Caminhao("Cavalo Mecânico", "VOLVO", " FH 480", "2009", "6", "Traçado 6x4", "Automatizada", "Leito Baixo")
print(Caminhao.get_tipo())
print(Caminhao.numero_rodas)
print(Caminhao.marca)
print(Caminhao.tracao)
print(Caminhao.ligar())