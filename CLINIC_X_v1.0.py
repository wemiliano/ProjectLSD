from datetime import datetime

data_hoj = datetime.now()

def cad_cliente (cad_cli):
    cad_cli = []
    n_us = input("Digite o número do Usúario:\n")
    nome = input("Digite o nome:\n")
    idade = input("Idade:\n")
    tel = input("Telefone com DDD:\n")
    cad_cli.append(n_us)
    cad_cli.append(nome)
    cad_cli.append(idade)
    cad_cli.append(tel)
    listas.append(cad_cli)

def cad_user(cad_us):
    cad_us = []
    n_us = input("Digite o número do Usúario:\n")
    sen_us = input("Digite a Senha do Usúario:\n")
    nome = input("Digite o nome:\n")
    idade = input("Idade:\n")
    tel = input("Telefone com DDD:\n")
    cad_us.append(n_us)
    cad_us.append(sen_us)
    cad_us.append(nome)
    cad_us.append(idade)
    cad_us.append(tel)
    listas.append(cad_us)

def listar (listas):
    print(listas)

def cria_agend (agend):
    agend = []
    print("\x1b[2J")
    print("Gerenciar Agendamentos: \n")
    nome_a = input("Digite o Nome do cliente: \n")
    tel_a = input("Digite o telefone do cliente com DDD: \n")
    dat_a = input(" Digite a data separada por espaços DD MM AA: \n")
    hor_a = input("Digite o horário no formato de 24 horas: \n")
    agend.append(nome_a)
    agend.append(tel_a)
    agend.append(dat_a)
    agend.append(hor_a)
    listas.append(agend)
def menu ():
    print("Seja bem vindo Usuario Administrador - Escolha uma opção para prosseguir...\n")
    print("1 - GERENCIAR CLIENTES")
    print("2 - GERENCIAR USÚARIOS")
    print("3 - GERENCIAR AGENDAMENTOS")
    print("4 - CONSULTAS")
    print("5 - ENCERRAR APLICAÇÃO")

    opcao = int(input('Digite o número da opção desejada: \n '))

    if opcao == 1:
        cad_cli = []
        cad_cliente(cad_cli)
        menu()

    elif opcao == 2:
        cad_us = []
        cad_user(cad_us)
        menu()

    elif opcao == 3:
        agend = []
        cria_agend(agend)
        menu()

    elif opcao == 4:
        print("\x1b[2J")
        listar(listas)
        menu()

    elif opcao == 5:
        print("Encerrando...")
def menu_medic ():
    print("Seja bem vindo Dr. X - Escolha uma opção para prosseguir...\n")
    print("1 - GERENCIAR CLIENTES")
    print("2 - GERENCIAR AGENDAMENTOS")
    print("3 - CONSULTAS")
    print("4 - ENCERRAR APLICAÇÃO")
    op = input("Digite a opção desejada:\n")
    if op == "1":
        print("\x1b[2J")
        cad_cli = []
        n_us = input("Digite o número do Usúario:\n")
        nome = input("Digite o nome:\n")
        idade = input("Idade:\n")
        tel = input("Telefone com DDD:\n")
        cad_cli.append(n_us)
        cad_cli.append(nome)
        cad_cli.append(idade)
        cad_cli.append(tel)
        listas.append(cad_cli)
        menu_medic()

    elif op == "2":
        agend = []
        print("\x1b[2J")
        cria_agend(agend)
        menu_medic()

    elif op == "3":
        listar(listas)
        menu_medic()
    elif op == "4":
        print("Saindo")


print("Clinica X -", data_hoj)
user = input(str("Digite seu Usúario:\n "))
sen = input(str("Senha: \n"))
opcao = 0
listas = [[]]
if user != "admin" and user != "medic":
    print("Usúario invalido")
else:
    if user == "admin" and sen == "1234":
        print("\x1b[2J")
        menu()
    if user == "medic" and sen == "4321":
        menu_medic()
    else:
        print("Sair")







