class Lista_espera:
    def __init__(self, maximo_esperando=10):
        self.maximo_esperando = int(maximo_esperando)
        self.clientes_aguardo = []

    def Adicionar_cliente(self, cliente):
        
        # Aqui verifica se a quantidade de clientes em aguardo e maior ou igual a quantidade de clientes maximo esperando. Se for, nao adiciona o cliente
        if len(self.clientes_aguardo) >= self.maximo_esperando:
            return False
        
        # Se nao for, adiciona o cliente a lista de espera
        self.clientes_aguardo.append(cliente)
        return True

    def Remover_cliente(self):
        
        # Se o cliente nao estiver aqui, nada acontece
        if not self.clientes_aguardo:
            return None
        
        # Senao, retira o cliente
        return self.clientes_aguardo.pop(0)

    def Mostrar_lista(self):
        
        # Loopa uma lista mostrando os nomes dos clientes em aguardo
        return [c.nome for c in self.clientes_aguardo]