class Pagamento:
    def __init__(self, metodo, valor, alvo=None):
        self.metodo = metodo
        self.valor = float(valor)
        self.alvo = alvo
        self.processado = False

    def Processar_pagamento(self):
        if self.valor <= 0:
            self.processado = False
            return False

        # "alvo" ve se o produto possui um "Id_pedido", o tornando um pedido
        if hasattr(self.alvo, "Id_pedido"):
            pedido = self.alvo
            
            # Se o que foi pago cobre a conta, marca como pago
            if self.valor >= getattr(pedido, "preco", 0.0):
                pedido.status = "pago"
                self.processado = True
                return True
            else:
                # Se nao pagou tudo, registrar mas não marcar pago
                self.processado = False
                return False

        # se alvo for reserva, marcar como processado
        if hasattr(self.alvo, "Id_reserva"):
            self.processado = True
            return True

        # se não há alvo, faz nada
        self.processado = True
        return True