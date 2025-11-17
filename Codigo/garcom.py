from profissional import Profissional
from pedido import Pedido

class Garcom(Profissional):
    def __init__(self, nome, email, telefone, Cpf, cargo, Id):
        super().__init__(nome, email, telefone, Cpf, cargo, Id)
        self.mesas_responsavel = []

    def Anotar_pedido(self, cliente, mesa, itens, Id_pedido):
        
        # Cria um pedido pro cliente, com os itens, a mesa e o id
        p = cliente.Fazer_pedido(items=itens, mesa=mesa, Id_pedido=Id_pedido)
        
        # O pedido se torna automaticamente pendente
        p.status = "pendente"
        return p

    def Entregar_pedido(self, pedido):
        
        # Se o status do pedido for "pronto", muda o status pra "entregue" e assina a entrega com o nome do atendente
        if getattr(pedido, "status", "") == "pronto":
            pedido.status = "entregue"
            pedido.entregue_por = self.nome
            return True
        return False