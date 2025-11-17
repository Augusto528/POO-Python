from pessoa import Pessoa

class Administrador(Pessoa):
    def __init__(self, nome, email, telefone, Cpf, senha, credencial):
        super().__init__(nome, email, telefone, Cpf)
        self.senha = senha
        self.credencial = credencial
        self.clientes = []
        self.funcionarios = []

    def Cadastro_profissionais(self, profissional):
        
        # Se o funcionario ja estiver cadastrado, nada acontece, mas se nao estiver, ele entra na lista de funcionarios
        if profissional not in self.funcionarios:
            self.funcionarios.append(profissional)
            return True
        return False

    def Remover_profissionais(self, profissional):
        
        # Faz o mesmo que a anterior, mas remove o funcionario, caso ele estiver na lista. Se ele nao estiver, nada acontece
        if profissional in self.funcionarios:
            self.funcionarios.remove(profissional)
            return True
        return False
    
    def Adicionar_cliente(self, cliente):
        
        # Uma copia da funcao pro funcionario, mas com cliente
        if cliente not in self.clientes:
            self.clientes.append(cliente)
            return True
        return False

    def Remover_cliente(self, cliente):
        
        # Mesma coisa, mas remove o cliente "x" da lista de clientes
        if cliente in self.clientes:
            self.clientes.remove(cliente)
            return True
        return False
    
    def Mostrar_lista(self):
        
        # Cria uma lista com os nomes dos funcionarios presentes na lista de funcionarios criada durante a execucao do codigo
        funcionarios = [f.nome for f in self.funcionarios]
        
        # Retorna tal lista
        return {"funcionarios": funcionarios}