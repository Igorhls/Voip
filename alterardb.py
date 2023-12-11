from database_connection import *
def alterar_metas_por_nome(nome, novo_valor_meta):
    # Função para alterar as metas com base nos nomes
    conn = conectar_banco()
    cursor = conn.cursor()

    consulta_sql = "UPDATE indicadores SET meta_atual = %s WHERE nome = %s"
    dados_atualizados = (novo_valor_meta, nome)

    cursor.execute(consulta_sql, dados_atualizados)
    conn.commit()

    print(f'Metas alteradas com sucesso para o nome: {nome}')

    cursor.close()
    conn.close()

alterar_metas_por_nome('Gama', 102)