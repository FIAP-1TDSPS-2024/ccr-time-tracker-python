import csv
import oracledb
import json
from datetime import datetime

def get_conexao():
    return oracledb.connect(user="rm561144", password="130304",
                            dsn="oracle.fiap.com.br/orcl")

def insere_filme(nome_filme, diretor, genero, ano_lancamento):
    #Insere na tabela de relação
    sql =  """
        SELECT nome_filme, ano_lancamento
        FROM t_filme
        WHERE nome_filme = :nome_filme AND ano_lancamento = TO_DATE(:ano_lancamento, 'YYYY')
    """
    
    dados = {
        'nome_filme': nome_filme,
        'ano_lancamento': ano_lancamento
    }
    
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, dados)
            filme_registrado = cur.fetchall()

    if filme_registrado:
        print(f"O filme {nome_filme} já existe")

    else:
        #Insere filme
        sql =  """
            INSERT INTO t_filme (nome_filme, diretor, genero, ano_lancamento)
            VALUES (:nome_filme, :diretor, :genero, TO_DATE(:ano_lancamento, 'YYYY'))
        """

        dados = {
            'nome_filme': nome_filme,
            'diretor': diretor,
            'genero': genero,
            'ano_lancamento': ano_lancamento
        }

        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute(sql, dados)
            con.commit()

        print(f"O filme {nome_filme} foi registrado")

def insere_ator(ator):
    #Insere na tabela de relação
    sql =  """
        SELECT nome_ator
        FROM t_ator
        WHERE nome_ator = :nome_ator
    """
    
    dados = {
            'nome_ator': ator
        }
    
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, dados)
            autor_registrado = cur.fetchall()

    if autor_registrado:
        print(f"O ator {ator} já existe")
    
    else:
        #Insere ator
        sql =  """
            INSERT INTO t_ator (nome_ator)
            VALUES (:nome_ator)
        """

        dados = {
            'nome_ator': ator
        }

        with get_conexao() as con:
            with con.cursor() as cur:
                cur.execute(sql, dados)
            con.commit()

        print(f"O ator {ator} foi registrado")

def insere_filme_ator(ator, nome_filme):
    #Insere na tabela de relação
    sql =  """
        SELECT f.id_filme, a.id_ator
        FROM t_filme f
        JOIN t_ator a ON 1=1
        WHERE f.nome_filme = :nome_filme AND a.nome_ator = :nome_ator
    """
    
    dados = {
            'nome_ator': ator,
            'nome_filme': nome_filme
        }
    
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, dados)
            ids = cur.fetchall()

    #Insere filme_ator
    id_filme = ids[0][0]
    id_ator = ids[0][1]
    
    sql =  """
        INSERT INTO t_filme_ator (id_filme, id_ator)
        VALUES (:id_filme, :id_ator)
    """

    dados = {
        'id_filme': id_filme,
        'id_ator': id_ator
    }

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, dados)
        con.commit()

def consultar_filmes():
    #Insere na tabela de relação
    sql =  """
        SELECT *
        FROM t_filme
    """

    filmes = None
    
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql)
            filmes = cur.fetchall()
    
    return filmes

def consultar_atores():
    #Insere na tabela de relação
    sql =  """
        SELECT *
        FROM t_ator
    """

    atores = None
    
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql)
            atores = cur.fetchall()
    
    return atores

def imprimir_json(info, nome):
    def serializar(obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d')  # ou outro formato que quiser
        return str(obj)  # garante que qualquer outro tipo estranho também seja convertido

    nome = nome + ".json"
    with open(nome, mode="w", encoding="utf8") as arq:
        json.dump(info, arq, indent=4, default=serializar)

def main():
    with open('filmes.csv', 'rt', encoding='utf8') as ficheiro:

        reader = csv.reader(ficheiro, delimiter=':', quoting=csv.QUOTE_NONE)

        for linha in reader:

            lista = linha[0].split(';')

            if len(lista) >= 5:
                nome_filme = lista[0]
                diretor = lista[1]
                genero = lista[2]
                ano_lancamento = lista[3]
                ator = lista[4]

            insere_filme(nome_filme, diretor, genero, ano_lancamento)
            insere_ator(ator)
            insere_filme_ator(ator, nome_filme)

        filmes = consultar_filmes()
        atores = consultar_atores()

        imprimir_json(filmes, "filmes")
        imprimir_json(atores, "atores")

main()

        