import os
import re  # Biblioteca para expressões regulares para validações de formato
import json
import oracledb
import requests

data_json = {
    "funcionarios": {},
    "linhas": {
        "linha_8": {
            "estacoes": [],
            "clima": ""
        },
        "linha_9": {
            "estacoes": [],
            "clima": ""
        }
    }
}

def get_conexao():
    return oracledb.connect(user="rm561144", password="130304",
                            dsn="oracle.fiap.com.br/orcl")


def consultar_linhas(numero_estacao):
    sql =  """
        SELECT * FROM estacao e
        JOIN linha_estacao le ON e.id = le.estacoes_id
        WHERE le.linhas_id = :numero_estacao
    """

    parametros = {'numero_estacao': numero_estacao}

    linhas = []
    
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, parametros)
            columns = [col[0].lower() for col in cur.description]
            linhas = [dict(zip(columns, row)) for row in cur.fetchall()]
    
    return linhas

# Função para validar cada campo individualmente
def validar_campo(valor, tipo):
    if tipo == 'nome':
        # Validação para o nome: permite apenas letras e espaços
        if re.fullmatch(r'[A-Za-zÀ-ÿ ]+', valor):
            return True
        print("Erro: O nome deve conter apenas letras e espaços.")
    
    elif tipo == 'cpf':
        # Validação para o CPF: deve estar no formato "000.000.000-00"
        if re.fullmatch(r'\d{11}', valor):
            return True
        print("Erro: O CPF deve estar no formato 00000000000.")
    
    elif tipo == 'cargo':
        # Validação para o cargo: deve conter apenas letras e espaços
        if re.fullmatch(r'[A-Za-zÀ-ÿ ]+', valor):
            return True
        print("Erro: O cargo deve conter apenas letras.")
    
    elif tipo == 'email':
        # Validação para o email: permite letras e números antes do '@', e deve ter o formato básico
        if re.fullmatch(r'[A-Za-z0-9À-ÿ]+@[A-Za-z]+\.[A-Za-z]+', valor):
            return True
        print("Erro: O email deve ser válido e conter apenas letras e números antes do '@'.")
    
    elif tipo == 'senha':
        # Validação para a senha: pode incluir letras, números e alguns caracteres especiais
        if re.fullmatch(r'[A-Za-z0-9!@#$%^&*(),.?":{}|<>]+', valor):
            return True
        print("Erro: A senha pode conter letras, números e caracteres especiais.")

    elif tipo == 'permissao':
        # Validação para a permissao: valor numérico de um algarismo
        if re.fullmatch(r'\d{1}', valor):
            return True
        print("Erro: A permissao deve ser apenas um número de 0 a 3")
    
    return False  # Retorna False se a validação falhar
# Função para cadastrar um funcionário
def consultar_funcionarios():

    while True:
        sql =  """
            SELECT * FROM funcionario
        """

        funcionarios = []
        
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute(sql)
                columns = [col[0].lower() for col in cur.description]
                funcionarios = [dict(zip(columns, row)) for row in cur.fetchall()]
        
        for i in funcionarios:
            print(f"id: {i['id_funcionario']}, nome: {i['nome']}, cargo: {i['cargo']}")

        data_json['funcionarios'] = funcionarios
   
        # Opção de voltar ao menu principal
        voltar = input('Digite "V" para voltar ao menu principal: ').upper()
        if voltar == 'V':
            break  # Sai do laço e retorna ao menu principal

def consultar_funcionario_id(id):

    while True:
        sql =  """
            SELECT * FROM funcionario where id_funcionario=:id
        """

        dados = {"id": id}
        
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute(sql, dados)
                funcionario = cur.fetchone()
        
        if funcionario != None:
            print("Funcionario encontrado!")
            print(funcionario)
            return True
        
        else:
            print("Funcionário não existe! Selecione um ID válido")
            return False


def deletar_funcionario():

    while True:
        sql =  """
            DELETE FROM funcionario WHERE id_funcionario=:id
        """

        id = input("Digite o id do funcionário a ser deletado")

        parametros = {'id': id}
        
        
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute(sql, parametros)
        

        print("Funcionario deletado com sucesso!")
    
        # Opção de voltar ao menu principal
        voltar = input('Digite "V" para voltar ao menu principal: ').upper()
        if voltar == 'V':
            break  # Sai do laço e retorna ao menu principal


# Função para cadastrar um funcionário
def cadastrar_funcionario():
    funcionario = {}
    os.system('cls')  # função para limpar a tela
    while True:
        print('Vamos cadastrar um usuário!')
        
        # Solicita e valida cada campo individualmente
        while True:
            nome = input('Digite o nome do funcionário: ')
            if validar_campo(nome, 'nome'):
                funcionario.update({"nome": nome})
                break  # Sai do loop se o nome for válido
        
        while True:
            cpf = input('Digite o CPF do funcionário: ')
            if validar_campo(cpf, 'cpf'):
                funcionario.update({"cpf": cpf})
                break  # Sai do loop se o CPF for válido
        
        while True:
            cargo = input('Digite o cargo do funcionário: ')
            if validar_campo(cargo, 'cargo'):
                funcionario.update({"cargo": cargo})
                break  # Sai do loop se o cargo for válido
        
        while True:
            email = input('Digite o email do funcionário: ')
            if validar_campo(email, 'email'):
                funcionario.update({"email": email})
                break  # Sai do loop se o email for válido
        
        while True:
            senha = input('Digite a senha do funcionário: ')
            if validar_campo(senha, 'senha'):
                funcionario.update({"senha": senha})
                break  # Sai do loop se a senha for válida

        while True:
            permissao = input('Digite o nível de permissao do funcionario, de 0 a 3: ')
            if validar_campo(permissao, 'permissao'):
                funcionario.update({"permissao": permissao})
                break  # Sai do loop se a senha for válida

        #criando sql concatenando strings
        sql = """
        INSERT INTO funcionario (nome, cpf, cargo, email, senha, permissao)
        VALUES (:nome, :cpf, :cargo, :email, :senha, :permissao)
        """
        
        funcionario = {
            'nome': nome,
            'cpf': cpf,
            'cargo': cargo,
            'email': email,
            'senha': senha,
            'permissao': permissao
        }
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute(sql, funcionario)
            con.commit()
        
        # Todos os dados foram validados com sucesso
        #print(f'Usuário {nome} cadastrado com sucesso!')
        #data_json.update({"funcionario": funcionario})
        
        # Opção de voltar ao menu principal
        voltar = input('Digite "V" para voltar ao menu principal: ').upper()
        if voltar == 'V':
            break  # Sai do laço e retorna ao menu principal

# Função para cadastrar um funcionário
def atualizar_funcionario():
    funcionario = {}
    os.system('cls')  # função para limpar a tela
    while True:
        print('Vamos atualizar um usuário!')
        
        # Solicita e valida cada campo individualmente
        while True:
            id = input('Digite o id do funcionário: ')
            if consultar_funcionario_id(id):
                funcionario.update({"id": id})
                break  # Sai do loop se o nome for válido

        while True:
            nome = input('Digite o nome do funcionário: ')
            if validar_campo(nome, 'nome'):
                funcionario.update({"nome": nome})
                break  # Sai do loop se o nome for válido
        
        while True:
            cpf = input('Digite o CPF do funcionário: ')
            if validar_campo(cpf, 'cpf'):
                funcionario.update({"cpf": cpf})
                break  # Sai do loop se o CPF for válido
        
        while True:
            cargo = input('Digite o cargo do funcionário: ')
            if validar_campo(cargo, 'cargo'):
                funcionario.update({"cargo": cargo})
                break  # Sai do loop se o cargo for válido
        
        while True:
            email = input('Digite o email do funcionário: ')
            if validar_campo(email, 'email'):
                funcionario.update({"email": email})
                break  # Sai do loop se o email for válido
        
        while True:
            senha = input('Digite a senha do funcionário: ')
            if validar_campo(senha, 'senha'):
                funcionario.update({"senha": senha})
                break  # Sai do loop se a senha for válida

        while True:
            permissao = input('Digite o nível de permissao do funcionario, de 0 a 3: ')
            if validar_campo(permissao, 'permissao'):
                funcionario.update({"permissao": permissao})
                break  # Sai do loop se a senha for válida

        #criando sql concatenando strings
        sql = """
        UPDATE funcionario set nome =:nome, cpf =:cpf, cargo=:cargo, email=:email, senha=:senha, permissao=:permissao
        WHERE id_funcionario =:id
        """
        
        funcionario = {
            'id': id,
            'nome': nome,
            'cpf': cpf,
            'cargo': cargo,
            'email': email,
            'senha': senha,
            'permissao': permissao
        }
        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute(sql, funcionario)
            con.commit()
        
        # Todos os dados foram validados com sucesso
        #print(f'Usuário {nome} cadastrado com sucesso!')
        #data_json.update({"funcionario": funcionario})
        
        # Opção de voltar ao menu principal
        voltar = input('Digite "V" para voltar ao menu principal: ').upper()
        if voltar == 'V':
            break  # Sai do laço e retorna ao menu principal

# Função para consultar as linhas de trem
def consultar_linhas_trem():
    os.system('cls')  
    while True:
        print('Escolha a linha de trem que deseja consultar:')
        print('1 - Linha 8')
        print('2 - Linha 9')
        print('3 - Voltar ao menu principal')
        
        # Ler linha escolhida pelo usuário
        linha = input('Digite o número da linha escolhida: ')
        
        # Exibe informações da linha escolhida
        if linha == '1':
            os.system('cls') 
            for i in consultar_linhas(8):
                print(i['nome'])# Linha 8
            data_json['linhas']['linha_8']['estacoes'] = consultar_linhas(8)
        elif linha == '2':
            os.system('cls')
            for i in consultar_linhas(9):
                print(i['nome']) # Linha 9
            data_json['linhas']['linha_9']['estacoes'] = consultar_linhas(9)
        elif linha == '3':
            os.system('cls')
            break  # Retorna ao menu principal
        else:
            print('Opção inválida. Tente novamente.')  # escolha incorreta

# Função para exibir o tempo médio de espera
def consulta_clima_linha():
    os.system('cls')  
    while True:
        print('Tempo médio de espera:')
        print('1 - Linha 8')
        print('2 - Linha 9')
        print('3 - Voltar ao menu principal')
        
        # Ler o tempo de espera escolhida pelo usuário
        tempo = input('Digite a opção escolhida: ')
        
        # Exibir o tempo de espera da linha escolhida
        if tempo == '1':
            os.system('cls')

            url = "https://api.open-meteo.com/v1/forecast?latitude=-23.52079491059756&longitude=46.73856011334605&hourly=rain&timezone=America%2FSao_Paulo&forecast_days=1"
            
            resposta = requests.get(url)

            chuva = resposta.json()["hourly"]["rain"]

            for i in chuva:
                if(i > 0.0):
                    clima = data_json["linhas"]["linha_8"]["clima"] = "Cuidado! Há previsão de chuva na linha 8 diamante hoje!"
                    print(clima)
                    break

            else:
                clima = data_json["linhas"]["linha_8"]["clima"] = "Pode fazer sua viagem sem problemas! O clima na linha está bom hoje!"
                print(clima)

        elif tempo == '2':
            os.system('cls')

            url = "https://api.open-meteo.com/v1/forecast?latitude=-23.65568480827604&longitude=46.7216246926103&hourly=rain&timezone=America%2FSao_Paulo&forecast_days=1"
            resposta = requests.get(url)

            chuva = resposta.json()["hourly"]["rain"]

            for i in chuva:
                if(i > 0.0):
                    clima = data_json["linhas"]["linha_9"]["clima"] = "Cuidado! Há previsão de chuva na linha 9 esmeralda hoje!"
                    print(clima)
                    break

            else:
                clima = data_json["linhas"]["linha_9"]["clima"] = "Pode fazer sua viagem sem problemas! O clima na linha está bom hoje!"
                print(clima)

            data_json.update({ "tempo":  "A Linha 9 - Esmeralda esta operando normalmente, com intervalos de 6 minutos entre trens"})
            print(data_json["tempo"])
        elif tempo == '3':
            os.system('cls')
            break  
        else:
            print('Opção inválida. Tente novamente.')  # escolha incorreta

# Função para sair do programa
def sair():
    os.system('cls')  
    try:
        with open ("dados.json", "w", encoding='utf-8') as file_json:
                json.dump(data_json, file_json, indent=4)
    except:
        print("Não foi possível escrever o arquivo de relatório")


    print('Você optou por sair do app. Obrigado por utilizar o CaTech!')

# Função principal que exibe o menu 
def menu_principal():
    while True:

        os.system('cls')  
        print('Seja bem-vindo ao menu do CaTech!')
        print('1 - Gerenciar funcionários')
        print('2 - Consultar linhas de Trem')
        print('3 - Consultar clima nas linhas de trem')
        print('4 - Sair')
        
        # Ler opção do usuário
        opcao = input('Digite o número da opção escolhida: ')
        
        # Redireciona para a função escolhida
        if opcao == '1':
            menu_funcionario()
        elif opcao == '2':
            consultar_linhas_trem()
        elif opcao == '3':
            consulta_clima_linha()
        elif opcao == '4':
            sair()
            break  # Sai do programa
        else:
            os.system('cls')
            print('Opção inválida, favor tente novamente!')

def menu_funcionario():
    while True:

        os.system('cls')  
        print('Seja bem-vindo ao menu de gerenciamento de funcionários')
        print('1 - Cadastrar funcionário')
        print('2 - Consultar funcionários existentes')
        print('3 - Atualizar cadastro de funcionário')
        print('4 - Deletar funcionário')
        print('5 - Sair')
        
        # Ler opção do usuário
        opcao = input('Digite o número da opção escolhida: ')
        
        # Redireciona para a função escolhida
        if opcao == '1':
            cadastrar_funcionario()
        elif opcao == '2':
            consultar_funcionarios()
        elif opcao == '3':
            atualizar_funcionario()
        elif opcao == '4':
            deletar_funcionario()
            break  # Sai do programa
        elif opcao == '5':
            sair()
            break  # Sai do programa
        else:
            os.system('cls')
            print('Opção inválida, favor tente novamente!')

# Executa o menu principal
menu_principal()