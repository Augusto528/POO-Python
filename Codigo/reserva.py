class Reserva:
    def __init__(self, Id_reserva, mesa, cliente, data_hora):
        self.Id_reserva = Id_reserva
        self.mesa = mesa
        self.cliente = cliente
        self.data_hora = data_hora
        self.confirmada = False

    def Confirmar(self):
        
        # Se o status da mesa nao for "disponivel", da erro, pois ela ja estara com outra pessoa
        if not hasattr(self.mesa, "disponivel"):
            raise TypeError("mesa inválida")
        
        # Se o cliente verificado nao tiver reservas tambem da erro...
        if not hasattr(self.cliente, "reservas"):
            raise TypeError("cliente inválido")

        # So entra se a mesa estiver disponivel
        if self.mesa.disponivel:
            
            # Reserva pro cliente em questao
            self.mesa.Reservar(self.cliente)
            
            # Confirma a reserva do cliente
            self.confirmada = True
            
            # Verifica se a reserva ja nao essta na lista de reservas
            if self not in getattr(self.mesa, "reservas", []):
                
                # Se nao estiver, a adiciona
                self.mesa.reservas.append(self)
                
            # Mesma logica, mas pra cliente. Se o cliente nao for duplicado pra aquela reserva...
            if self not in self.cliente.reservas:
                
                # Inclui esse cliente na reserva
                self.cliente.reservas.append(self)
            return True
        return False

    def Cancelar(self):
        # Se o cliente atual da mesa for o proprio cliente da reserva
        if getattr(self.mesa, "cliente_atual", None) == self.cliente:
            
            # Libera a reserva
            self.mesa.Liberar()
        
        # Se o cliente tiver uma reserva, remove ela
        if self in getattr(self.cliente, "reservas", []):
            self.cliente.reservas.remove(self)
            
        # Se nada fora verdade, ela e liberada de qualquer forma
        self.confirmada = False
        return True

    def Remarcar(self, nova_mesa, nova_data_hora):
        
        # Se estiver confirmada
        if self.confirmada:
            # E se o cliente for o cliente atual da mesa
            if getattr(self.mesa, "cliente_atual", None) == self.cliente:
                
                # Libera a mesa
                self.mesa.Liberar()
                
            # Se houver alguma reserva, a remove tambem
            if self in getattr(self.mesa, "reservas", []):
                self.mesa.reservas.remove(self)
            self.confirmada = False

        # Atribui a nova mesa e data pro cliente
        self.mesa = nova_mesa
        self.data_hora = nova_data_hora

        # Roda uma confirmacao na mesa
        return self.Confirmar()
