from profissional import Profissional

class Chef(Profissional):
    def __init__(self, nome, email, telefone, Cpf, cargo, Id, especialidade):
        super().__init__(nome, email, telefone, Cpf, cargo, Id)
        self.especialidade = especialidade

    def Preparar_pedido(self, pedido):
        
        # Pega o pedido que tiver o status "pendente" ou "preparando" e o transforma em "pronto". Bem arcaico e instantaneo, mas e o que ha
        if getattr(pedido, "status", None) in ("pendente", "preparando"):
            pedido.status = "preparando"
            pedido.status = "pronto"
            pedido.preparado_por = self.nome
            return True
        return False