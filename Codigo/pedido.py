class Pedido:
    def __init__(self, Id_pedido, mesa, cliente):
        self.Id_pedido = Id_pedido
        self.mesa = mesa
        self.cliente = cliente
        self.itens = []
        self.preco = 0.0
        self.status = "novo"      # status: novo, pendente, preparando, pronto, entregue, pago, cancelado
        self.preparado_por = None
        self.entregue_por = None
        self.preparado_em = None
        self.entregue_em = None

    def Adicionar_item(self, item):
        
        # Essa condicional serve pra ver se o item possui "preco". Caso nao, e considerado um item invalido
        if not hasattr(item, "preco"):
            raise TypeError("item inválido")
        
        # Se passar como item valido, e inserido na lista de itens
        self.itens.append(item)
        
        # O preco e obtido verificando o preco do item individual
        self.preco += float(item.preco)

    def Calcular_total(self):
        
        # Inicia uma variavel com preco = 0
        total = 0.0
        
        # Loopa em todos os itens da lista e soma seus valores 
        for it in self.itens:
            total += float(it.preco)
            
        # atribui a "preco", o valor total
        self.preco = total
        return self.preco
    
    def Exibir_detalhes(self):
        
        # Somente exibe os detalhes 
        return {
            "Id_pedido": self.Id_pedido,
            "mesa": getattr(self.mesa, "numero", None),
            "cliente": getattr(self.cliente, "nome", None),
            "itens": [(i.Id, i.nome, i.preco) for i in self.itens],
            "preco_total": self.preco,
            "status": self.status,
            "preparado_por": self.preparado_por,
            "entregue_por": self.entregue_por
        }