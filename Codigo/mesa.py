class Mesa:
    def __init__(self, numero, capacidade, disponivel=True):
        self.numero = numero
        self.capacidade = capacidade
        self.disponivel = disponivel
        self.cliente_atual = None
        self.reservas = []

    def Reservar(self, cliente):
        
        # Se a mesa estiver disponivel...
        if self.disponivel:
            
            # Ela nao fica mais disponivel
            self.disponivel = False
            
            # O cliente toma a mesa pra si
            self.cliente_atual = cliente
            return True
        return False

    def Liberar(self):
        
        # Da um set no cliente pra "None", retirando todos que estiverem reservando a mesa
        self.cliente_atual = None
        
        # Faz a mesa estar disponivel de novo
        self.disponivel = True
        return True