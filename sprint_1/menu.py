import os


while True:
    os.system('cls')

    print('Seja bem-vindo ao menu do CaTech!')
    print('1 - Cadastrar Funcionário')
    print('2 - Linhas de Trem')
    print('3 - Tempo Médio de espera')
    print('4 - Sair')

    opcao = input('Digite o número da opção escolhida: ')

    if opcao == '1':
        os.system('cls')

        while True:
            print('Vamos cadastrar um usuário!')
            nome = str(input('Digite o nome do funcionário: '))
            cpf = int(input('Digite o CPF do funcionário: '))
            cargo = str(input('Digite o cargo do funcionário: '))
            email = str(input('Digite o email do funcionário: '))
            senha = str(input('Digite o senha do funcionário: '))
            print(f'Usuário {nome} cadastrado com sucesso!')
            
            voltar = input('Digite "V" para voltar ao menu principal: ').upper()
            if voltar == 'V':
                break

    elif opcao == '2':
        os.system('cls')

        while True:
            print('Escolha a linha de trem que deseja consultar:')
            print('1 - Linha 8')
            print('2 - Linha 9')
            print('3 - Voltar ao menu principal')
            linha = input('Digite o número da linha escolhida: ')
            
            if linha == '1':
                os.system('cls')

                print('A Linha 8 é uma das linhas mais movimentadas da cidade.')
                
            elif linha == '2':
                os.system('cls')

                print('A Linha 9 é uma linha muito movimentada em São Paulo.')
            elif linha == '3':
                os.system('cls')
                break
            else:
                print('Opção inválida. Tente novamente.')

    elif opcao == '3':
        os.system('cls')

        while True:
            print('Tempo médio de espera:')
            print('1 - Linha 8')
            print('2 - Linha 9')
            print('3 - Voltar ao menu principal')
            tempo = input('Digite a opção escolhida: ')
            
            if tempo == '1':
                os.system('cls')                

                print('O tempo médio de espera para a linha 8 é de 2 minutos.')
            elif tempo == '2':
                os.system('cls')

                print('O tempo médio de espera para a linha 9 é de 4 minutos.')
            elif tempo == '3':
                os.system('cls')

                break
            else:
                print('Opção inválida. Tente novamente.')

    elif opcao == '4':
        os.system('cls')

        print('Você optou por sair do app. Obrigado por utilizar o CaTech!')
        break

    else:
        os.system('cls')

        print('Opção inválida, favor tente novamente!')
