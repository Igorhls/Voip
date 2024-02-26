from database_connection import *
def adicionar_nova_linha(matricula, nome, meta_atual):
    # Função para adicionar uma nova linha à tabela
    conn = conectar_banco()
    cursor = conn.cursor()

    consulta_sql = "INSERT INTO indicadores (matricula, nome, meta_atual) VALUES (%s, %s, %s)"
    dados_nova_linha = (matricula, nome, meta_atual)

    cursor.execute(consulta_sql, dados_nova_linha)
    conn.commit()

    print('Nova linha adicionada com sucesso!')

    cursor.close()
    conn.close()

adicionar_nova_linha(254782, 'Asbuahduahda', 13)