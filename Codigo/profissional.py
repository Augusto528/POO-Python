from pessoa import Pessoa

class Profissional(Pessoa):
    def __init__(self, nome, email, telefone, Cpf, cargo, Id):
        super().__init__(nome, email, telefone, Cpf)
        self.cargo = cargo
        self.Id = Id
        self.lista_pontos = []
        self.ponto_atual = None

    def Registrar_ponto(self, entrada):
        
        # Insere o valor dado como horario de entrada na lista de banco de ponto do funcionario
        self.lista_pontos.append(entrada)
        self.ponto_atual = entrada
        return True