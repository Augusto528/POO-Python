class Pessoa:
    def __init__(self, nome, email, telefone, Cpf):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.Cpf = Cpf

    def Exibir_dados(self):
        
        # Somente exibe os detalhes da pessoa
        return {
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "Cpf": self.Cpf
        }
