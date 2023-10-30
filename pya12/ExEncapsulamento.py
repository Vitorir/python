class Ingresso:
    def __init__(self, identificador, preco, titulo):
        self._id = identificador
        self._preco = preco
        self._titulo = titulo

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco < 0:
            raise ValueError("Não pode ser negativo")
        self._preco = novo_preco

    def descricao(self):
        return f"Ingresso para {self._titulo} com preco {self._preco}"
    
    def tipo(self):
        return "Esse ingresso é tal"
    
class IngressoPista(Ingresso):
    def __init__(self, identificador, preco, titulo):
        super().__init__(identificador, preco, titulo)

    def tipo(self):
        return "Esse é o ingresso Pista"
    
class IngressoVIP(Ingresso):
    def __init__(self, identificador, preco, titulo):
        super().__init__(identificador, preco, titulo)

    def tipo(self):
        return 'Esse é ingresso VIP'
    
ip = IngressoPista(1, 100, 'Show A')
print(ip.descricao())
print(ip.tipo())

ip.preco = 50
print(ip.preco)
