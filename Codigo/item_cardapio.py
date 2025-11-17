# item_cardapio.py
class Item_cardapio:
    def __init__(self, Id, nome, preco):
        self.Id = Id
        self.nome = nome
        self.preco = float(preco)

    def Emite_recibo(self):
        
        # Retorna o id, o nome e o preco de determinado item... Basico
        return f"Item {self.Id}: {self.nome} - R$ {self.preco:.2f}"
