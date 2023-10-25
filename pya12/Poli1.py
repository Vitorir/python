class Automovel:
    def __init__(self, nome_veiculo, qtd_motores, tem_rodas):
        self.nome_veiculo = nome_veiculo
        self.qtd_motores = qtd_motores
        self.tem_rodas = tem_rodas
    
    def buzinar(self):
        pass
    
class Carro(Automovel):
    def __init__(self, nome_veiculo, qtd_motores, tem_rodas):
        super().__init__(nome_veiculo, qtd_motores, tem_rodas)

    def buzinar(self):
        return 'Biii'
    
class Barco(Automovel):
    def __init__(self, nome_veiculo, qtd_motores, tem_rodas):
        super().__init__(nome_veiculo, qtd_motores, tem_rodas)

    def buzinar(self):
        return "Foom"

class Aviao(Automovel):
    def __init__(self, nome_veiculo, qtd_motores, tem_rodas):
        super().__init__(nome_veiculo, qtd_motores, tem_rodas)

    def buzinar(self):
        return 'Tem buzina?'