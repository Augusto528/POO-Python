from pessoa import Pessoa
from reserva import Reserva
from pedido import Pedido

class Cliente(Pessoa):
    def __init__(self, nome, email, telefone, Cpf):
        super().__init__(nome, email, telefone, Cpf)
        self.reservas = []
        self.pedidos = []

    def Cancelar_pedido(self, pedido):
        
        # Se o pedido que veio como parametro da funcao tiver sido feito pelo cliente, seu status sera cancelado e removido da lista de pedidos de tal cliente
        if pedido in self.pedidos:
            pedido.status = "cancelado"
            self.pedidos.remove(pedido)
            return True
        return False

    def Fazer_pedido(self, items, mesa, Id_pedido):

        # Cria uma variavel padrao
        p = Pedido(Id_pedido=Id_pedido, mesa=mesa, cliente=self)
        
        # Loopa dentro dos itens que foram coloados como o pedido do cliente
        for it in items:
            
            # Adiciona cada pedido a lista de itens do cliente
            p.Adicionar_item(it)
            
        
        p.Calcular_total()
        p.status = "pendente"
        self.pedidos.append(p)
        return p

    def Cancelar_reserva(self, reserva):
        if reserva in self.reservas:
            reserva.Cancelar()
            if reserva in self.reservas:
                self.reservas.remove(reserva)
            return True
        return False

    def Fazer_reserva(self, Id_reserva, mesa, data_hora):
        r = Reserva(Id_reserva=Id_reserva, mesa=mesa, cliente=self, data_hora=data_hora)
        self.reservas.append(r)
        return r
    
    def Exibir_reservas(self):
        lista = []
        for r in self.reservas:
            lista.append({
                "Id_reserva": r.Id_reserva,
                "mesa": r.mesa.numero,
                "data_hora": r.data_hora,
                "status": "confirmada" if not r.mesa.disponivel else "pendente"
            })
        return lista
        
