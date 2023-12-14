from database_connection import *
def consultar_metas_por_nome_ou_todos(nome=None):
    # Função para consultar as metas atuais com base nos nomes ou mostrar todos
    conn = conectar_banco()
    cursor = conn.cursor()

    if nome and nome.lower() != 'todos':
        # Consultar por um nome específico
        consulta_sql = "SELECT nome, meta_atual FROM indicadores WHERE nome = %s"
        dados_para_consultar = (nome,)
        cursor.execute(consulta_sql, dados_para_consultar)
    else:
        # Consultar todos
        consulta_sql = "SELECT nome, meta_atual FROM indicadores"
        cursor.execute(consulta_sql)

    resultados = cursor.fetchall()

    if resultados:
        for linha in resultados:
            print(f'Nome: {linha[0]}, Metas Atuais: {linha[1]}')
    else:
        if nome:
            print(f'Nenhum registro encontrado para o nome: {nome}')
        else:
            print('Nenhum registro encontrado. Por favor, insira um nome ou digite "todos".')

    cursor.close()
    conn.close()

consultar_metas_por_nome_ou_todos('todos')