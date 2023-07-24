def menu():
    voltarMenu = 's'
    while voltarMenu == 's':
        print('''
        ===========================================================================================
                                       PROJETO AGENDA EM PYTHON                                                               
        MENU:
        
        [1]CADASTRAR CONTATO
        [2]LISTAR CONTATO
        [3]DELETAR CONTATO
        [4]BUSCAR CONTATO
        [5]ATUALIZAR CONTATO
        [6]SAIR
        
        ===========================================================================================\n''')
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            salvarContato()
        elif opcao == "2":
            listarContato()
        elif opcao == "3":
            deletarContato()
        elif opcao == "4":
            buscarContato()
        elif opcao == "5":
            atualizarContato()
        elif opcao == "6":
            sair()
        else:
            print("ERRO: Digite uma opção válida!")
        voltarMenu = input("Deseja voltar ao menu principal? (s/n) ").lower()
    sair()

def salvarContato():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    try:
        with open("agenda.txt", "a") as agenda:
            dados = f'{nome};{telefone};{email}\n'
            agenda.write(dados)
        print(f'Contato Salvo com Sucesso!')
    except IOError:
        print("ERRO na Gravação de Contato")

def listarContato():
    try:
        with open("agenda.txt", "r") as agenda:
            print("LISTA DE CONTATOS:")
            for i, contato in enumerate(agenda, 1):
                contato_formatado = contato.replace(";", " | ")
                print(f"{i}. {contato_formatado}")
    except FileNotFoundError:
        print("ERRO: Arquivo da agenda não encontrado.")
    except IOError:
        print("ERRO na Leitura da Agenda")


def deletarContato():
    nome_deletado = input("Digite o nome do contato: ").lower()
    try:
        with open("agenda.txt", "r") as agenda:
            contatos = agenda.readlines()
        with open("agenda.txt", "w") as agenda:
            for contato in contatos:
                if nome_deletado not in contato.lower():
                    agenda.write(contato)
        print(f'Contato excluído com sucesso!')
    except FileNotFoundError:
        print("ERRO: Arquivo da agenda não encontrado.")
    except IOError:
        print("ERRO na Leitura ou Escrita da Agenda")

def buscarContato():
    procura_nome = input("Digite o nome do contato: ").upper()
    try:
        with open("agenda.txt", "r") as agenda:
            for contato in agenda:
                if procura_nome in contato.split(";")[0].upper():
                    print(contato)
    except FileNotFoundError:
        print("ERRO: Arquivo da agenda não encontrado.")
    except IOError:
        print("ERRO na Leitura da Agenda")

def atualizarContato():
    nome_atualizado = input("Digite o nome do contato: ").lower()
    try:
        with open("agenda.txt", "r") as agenda:
            contatos = agenda.readlines()
        with open("agenda.txt", "w") as agenda:
            for contato in contatos:
                if nome_atualizado not in contato.lower():
                    agenda.write(contato)
        nome = input("Digite o novo nome: ")
        telefone = input("Digite o novo telefone: ")
        email = input("Digite o novo email: ")
        with open("agenda.txt", "a") as agenda:
            dados = f'{nome};{telefone};{email}\n'
            agenda.write(dados)
        print(f'Contato Atualizado com Sucesso!')
    except FileNotFoundError:
        print("ERRO: Arquivo da agenda não encontrado.")
    except IOError:
        print("ERRO na Leitura ou Escrita da Agenda")

def sair():
    print(f'Até mais... ')
    exit()

def main():
    menu()

main()
