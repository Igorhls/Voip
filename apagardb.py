from database_connection import *
def apagar_dados_por_nome(nome):
    # Função para apagar dados com base nos nomes
    conn = conectar_banco()
    cursor = conn.cursor()

    consulta_sql = "DELETE FROM indicadores WHERE nome = %s"
    dados_para_apagar = (nome,)

    cursor.execute(consulta_sql, dados_para_apagar)
    conn.commit()

    print(f'Dados apagados com sucesso para o nome: {nome}')

    cursor.close()
    conn.close()

apagar_dados_por_nome('Asbuahduahda')