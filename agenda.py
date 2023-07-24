def menu():
    voltarMenu = 's'
    while voltarMenu == 's':
        opcao = input('''
        ===========================================================================================
                                       PROJETO AGENDA EM PYTHON                                                               
        MENU:
        
        [1]CADASTRAR CONTATO
        [2]LISTAR CONTATO
        [3]DELETAR CONTATO
        [4]BUSCAR CONTATO
        [5]ATUALIZAR CONTATO
        [6] SAIR
        
        ===========================================================================================\n ''')
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
            print("ERRO digite uma opção válida! ")
        voltarMenu = input("Deseja voltar ao menu principal? (s/n) ").lower()
    sair()


def salvarContato():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    try:
        agenda = open("agenda.txt","a")
        dados = f'{nome};{telefone};{email} \n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato Salvo com Sucesso!')
    except:
        print("ERRO na Gravação de Contato")

def listarContato():
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        print(contato)
    agenda.close()

def deletarContato():
    nome_deletado = input(f'Digite o nome do contato: ').lower()
    agenda = open("agenda.txt", "r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nome_deletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    print(f'Contato excluído com  sucesso!')
    listarContato()

def buscarContato():
    procura_nome = input(f'Digite o nome do contato: ') .upper()
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        if procura_nome in contato.split(";")[0].upper():
            print(contato)
    agenda.close()

def atualizarContato():
    nome_atualizado = input(f'Digite o nome do contato: ').lower()
    agenda = open("agenda.txt", "r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nome_atualizado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    nome = input("Digite o novo nome: ")
    telefone = input("Digite o novo telefone: ")
    email = input("Digite o novo email: ")
    try:
        agenda = open("agenda.txt","a")
        dados = f'{nome};{telefone};{email} \n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato Atualizado com Sucesso!')
    except:
        print("ERRO na Gravação de Contato")

def sair():
    print(f'Até mais... ')
    exit()

def main():
    menu()

main()