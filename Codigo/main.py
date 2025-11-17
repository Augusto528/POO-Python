
# ---------- Imports ----------

from cliente import Cliente
from administrador import Administrador
from profissional import Profissional
from garcom import Garcom
from chef import Chef
from mesa import Mesa
from reserva import Reserva
from item_cardapio import Item_cardapio
from pedido import Pedido
from pagamento import Pagamento
from lista_espera import Lista_espera

 
# ---------- Variaveis de Controle ----------

# Lista de clientes cadastrados -> iniicalmente 0, pois ninguem usou o sistema ainda (Teste e um cliente teste)
clientes = [Cliente("teste", "assdasfas", 12412, 14134)]

# Lista de profissionais cadastrados -> Inicialmente 0, pois o sistema começa sem ninguem
profissionais = []

# Lista de mesas disponiveis -> Inicialmente 6 mesas, mas mutavel
mesas = [Mesa(1, 6), Mesa(2, 6), Mesa(3, 6), Mesa(4, 6), Mesa(5, 4), Mesa(6, 4)]

# Lista de espera -> Maximo de 10 pessoas na lista de espera
lista_espera = Lista_espera(10)

# Cardapio do restaurante -> Itens e seus preços
cardapio = [
    Item_cardapio(1, "Pizza Pequena", 27.50),
    Item_cardapio(2, "Pizza Media", 35.00),
    Item_cardapio(3, "Pizza Grande", 50.00),
    Item_cardapio(4, "Hambúrguer Artesanal", 28.00),
    Item_cardapio(5, "Miojo", 35.00),
    Item_cardapio(6, "Capeletti", 130.00),
    Item_cardapio(7, "Suco 1L", 8.00),
    Item_cardapio(8, "Refrigerante", 12.00),
    
]

# Administrador padrão -> Um admin geral. O cadastro de mais pessoas com poder de ADM so pode ser feito dentro do sistema
admin = Administrador("Admin Geral", "admin@geral.com", "996053831", "12345678901", senha="1234", credencial="ADM")


# ---------- Funçoes auxiliares ----------

# Lista todos os clientes ja cadastrados - Escolha de qual ira usar o sistema
def escolher_cliente():
    print("\n=== Escolher Cliente ===")
    for i, c in enumerate(clientes):
        print(f"{i+1}. {c.nome} (CPF: {c.Cpf})")
    n = int(input("Escolha um cliente: "))
    return clientes[n-1]

# Funçao para que o profissional possa se logar
def escolher_profissional(cargo=None): #Tem "cargo=None" pra filtrar os cargos

    disponiveis = []
    
    # Loopa entre os profissionais
    for p in profissionais:
        
        # Se o cargo do profissional dentro do loop for "None" (Aqueles que pode ter acontecido um erro de digitaçao) ou o "cargo" selecionado pela situacao, o profissional estara dentro da lista de disponiveis
        if cargo is None or p.cargo.lower() == cargo.lower():
            disponiveis.append(p)

    # Se, no final, nao houverem profissionais disponiveis -> "Nenhum profissional disponivel" e acaba a funçao no "return None"
    if not disponiveis:
        print("Nenhum profissional disponível.")
        return None
    
    # Depois de filtrar os disponiveis, mostra eles por nome e cargo
    for i, p in enumerate(disponiveis):
        print(f"{i+1}. {p.nome} ({p.cargo})")
    
    # Pede pra escolher entre um deles
    escolha = int(input("Escolha: "))
    return disponiveis[escolha - 1]

# Escolha da mesa pelo cliente. Mostra o numero da mesa e se ela esta disponivel
def escolher_mesa():
    print("\n=== Mesas ===")
    for i, m in enumerate(mesas):
        print(f"{i+1}. Mesa {m.numero} - {'Disponível' if m.disponivel else 'Ocupada'}")
    
    escolha = int(input("Escolha uma mesa: "))
    while escolha > len(mesas):
        print("Mesa invalida! Escolha uma das mesas disponiveis, apenas")
        escolha = int(input("Escolha uma mesa: "))
    return mesas[escolha - 1]

# Mostra os itens dentro do cardapio e pede a escolha do cliente
def escolher_item_cardapio():
    print("\n=== Cardápio ===")
    for i, item in enumerate(cardapio):
        print(f"{i+1}. {item.Id} - {item.nome} (R$ {item.preco:.2f})")
    escolha = int(input("Escolha um item: "))
    return cardapio[escolha - 1]

# Faz o cliente escolher um de seus pedidos
def escolher_pedido(cliente):
    
    # Se o cliente nao tiver pedidos, fale isso
    if not cliente.pedidos:
        print("Este cliente não tem pedidos.")
        return None

    # Caso tiver, printa esses pedidos nesse loop
    print("\n=== Pedidos ===")
    for i, p in enumerate(cliente.pedidos):
        print(f"{i+1}. Pedido #{p.Id_pedido} - Status: {p.status}")

    # Fazer ele escolher um de seus pedidos
    escolha = int(input("Escolha um pedido: "))
    return cliente.pedidos[escolha - 1]


# Menu Cliente -> Mostra as açoes do cliente que esta utilizando o sistema
def menu_cliente(cliente):
    while True:
        print(f"\n=== Menu do Cliente ({cliente.nome}) ===")
        print("1. Fazer reserva")
        print("2. Ver reservas")
        print("3. Cancelar reserva")
        print("4. Fazer pedido")
        print("5. Ver pedidos")
        print("6. Cancelar pedido")
        print("7. Voltar")

        op = input("Escolha: ")

        if op == "1":
            
            # Escolhe a mesa
            mesa = escolher_mesa()
            
            # E o horario da reserva
            data = input("Data/Hora da reserva: ")
            
            # Cria a reserva com a funcao "Fazer_reserva()"
            reserva = cliente.Fazer_reserva(Id_reserva=1000+len(cliente.reservas), mesa=mesa, data_hora=data)
            
            if reserva.Confirmar():
                print("Reserva confirmada!")
            else:
                print("Mesa indisponível, adicionando cliente à lista de espera.")
                lista_espera.Adicionar_cliente(cliente)

        elif op == "2":
            
            # Printa as reservas do tal cliente
            print("\nReservas:")
            for r in cliente.Exibir_reservas():
                print(f'\nId da reserva: {r["Id_reserva"]}  |  Mesa: {r["mesa"]}  |  Data/Hora: {r["data_hora"]}  |  Status: {r["status"]}')

        elif op == "3":
            
            # Verifica se o cliente tem ou nao reservas. Caso nao, printa "Nenhuma reserva"
            if not cliente.reservas:
                print("Nenhuma reserva para cancelar.")
                continue
            
            # Caso haja reserva, cancela a primeira do cliente
            reserva = cliente.reservas[0]
            cliente.Cancelar_reserva(reserva)
            print("Reserva cancelada.")

        elif op == "4":

           # O cliente precisa ter uma reserva pra pedir
           if not cliente.reservas:
               print("Você precisa ter uma reserva antes de fazer um pedido!")
               continue
            
           # Usa a mesa da última reserva feita
           mesa = cliente.reservas[-1].mesa  
       
           # Escolhe itens dentre os que ha disponivel
           itens = []
           while True:
               item = escolher_item_cardapio()
               itens.append(item)
               cont = input("Adicionar outro item? (s/n): ")
               if cont.lower() != "s":
                   break
                
           # Faz o pedido em "Cliente.Fazer_pedido()"
           pedido = cliente.Fazer_pedido(
               items=itens,
               mesa=mesa,
               Id_pedido=3000 + len(cliente.pedidos)
           )
       
           print("\nPedido criado!")
           print(pedido.Exibir_detalhes())

        elif op == "5":
            
            # Loopa entre os pedidos printando cada um dos feitos e armazenados em "cliente.pedidos"
            for p in cliente.pedidos:
                print(p.Exibir_detalhes())

        elif op == "6":
            
            # Ve qual pedido o cliente quer cancelar e cancela com a opçao ".Cancelar_pedido()"
            pedido = escolher_pedido(cliente)
            if pedido:
                cliente.Cancelar_pedido(pedido)
                print("Pedido cancelado.")

        elif op == "7":
            
            # Volta... Nao ha muito o que comentar aqui....
            break

        else:
            print("Opção inválida.")

# Menu Administrador -> Mostra as açoes que o ADM pode tomar
def menu_admin(admin):
    while True:
        print(f"\n=== Menu do Administrador ({admin.nome}) ===")
        print("1. Cadastrar cliente")
        print("2. Remover cliente")
        print("3. Cadastrar profissional")
        print("4. Remover profissional")
        print("5. Mostrar listas")
        print("6. Voltar")

        op = input("Escolha: ")

        if op == "1":

            # Cadastra um cliente (como o proprio cliente pode fazer...)
            nome = input("Nome: ")
            email = input("Email: ")
            tel = input("Telefone: ")
            cpf = input("CPF: ")
            c = Cliente(nome, email, tel, cpf)
            clientes.append(c)
            print("Cliente cadastrado!")

        elif op == "2":
            
            # Ve se o cliente que ele quer retirar esta na lista de clientes e o remove, caso sim
            c = escolher_cliente()
            if c in clientes:
                clientes.remove(c)
                print("Cliente removido!")

        elif op == "3":
            
            # Cadastro de profissional com os dados do profissional
            nome = input("Nome: ")
            email = input("Email: ")
            tel = input("Telefone: ")
            cpf = input("CPF: ")
            cargo = input("Cargo (Garçom / Chef): ").strip().lower()

            # Caso o cargo seja "garçom", vira garçom
            if cargo == "garçom" or cargo == "garcom":
                p = Garcom(nome, email, tel, cpf, cargo, Id=len(profissionais)+1)
            
            # Se  for "chef", vira chef... Simples
            elif cargo == "chef":
                esp = input("Especialidade: ")
                p = Chef(nome, email, tel, cpf, cargo, Id=len(profissionais)+1, especialidade=esp)
            
            # Se houver erro de digitaçao na hora do cadastro do cargo, ele para aqui, onde seu cargo nap e definido
            else:
                print("Cargo invalido. Profissional sera generico")
                p = Profissional(nome, email, tel, cpf, cargo, Id=len(profissionais)+1)

            # Insere o funcionario na lista interna de funcionarios (para melhor gerenciamento)
            profissionais.append(p)
            print("Profissional cadastrado!")

        elif op == "4":
            
            # Bem parecido com cliente... Ve se eel esta na lista de funcionarios e, se estiver, o remove
            p = escolher_profissional()
            if p in profissionais:
                profissionais.remove(p)
                print("Profissional removido.")

        elif op == "5":
            
            # Printa a lista com os nomes dos clientes
            print("\nClientes:")
            for c in clientes:
                print("-", c.nome)
                
            # Printa a lista com os nomes dos funcionarios
            print("\nProfissionais:")
            for p in profissionais:
                print("-", p.nome)

        elif op == "6":
            
            # Volta.....
            break

        else:
            print("Opção inválida.")

# Main
def main():
    while True:
        print("\n=== SISTEMA DO RESTAURANTE ===")
        print("1. Entrar como Cliente")
        print("2. Cadastrar novo Cliente")
        print("3. Administrador")
        print("4. Garçom")
        print("5. Chef")
        print("6. Sair")
        op = input("Escolha: ")

        # 1. Cliente ja Cadastrado
        if op == "1":
            if not clientes:
                print("Nenhum cliente cadastrado. Cadastre-se primeiro!")
            else:
                cliente = escolher_cliente()
                menu_cliente(cliente)

        # 2. Autocadastro Cliente
        elif op == "2":
            
            # Menu de dados para cadastro de novo cliente
            print("\n=== Cadastro de Cliente ===")
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            cpf = input("CPF: ")

            # Cria o novo cliente com o tipo "Cliente" (com as informaçoes fornecidas pelo  ´´roprio cliente)
            novo_cliente = Cliente(nome, email, telefone, cpf)
            
            # Insere na nossa lista interna de clientes, o novo cliente
            clientes.append(novo_cliente)

            print(f"\nCliente {nome} cadastrado com sucesso!")
            print("Você já pode usar o menu de Cliente!\n")

        # 3. Login ADM
        elif op == "3":
            
            # Pede a senha (por ser apenas um ADM, fica mais facil)
            # Caso seja a senha certa, vai pro menu do ADM
            senha = input("Senha do administrador: ")
            if senha == admin.senha:
                menu_admin(admin)
            else:
                print("Senha incorreta.")

        # 4. Coloca os profissionais para jogo (os garçons)
        elif op == "4":
            
            # Ve quais garçons tem e mostra seus nomes
            g = escolher_profissional(cargo="Garçom")
            if g:
                print(f"\nGarçom {g.nome} logado. (Funções específicas podem ser expandidas)")
            else:
                print("Nenhum garçom encontrado.")

        # 5. Faz o mesmo da opçao anterior: Coloca os profissionais pra jogo (os chefs)
        elif op == "5":
            
            # A mesma coisa do anterior..., mas pra chefs
            c = escolher_profissional(cargo="Chef")
            if c:
                print(f"\nChef {c.nome} logado. (Funções específicas podem ser adicionadas depois)")
            else:
                print("Nenhum Chef encontrado.")

        # 6. SAIR DO PROGRAMA
        elif op == "6":
            
            # sai........
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

main()