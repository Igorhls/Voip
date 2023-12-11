import mysql.connector

def conectar_banco():
    # Função para criar e retornar uma conexão com o banco de dados
    host = '192.168.102.100'
    user = 'container65'
    password = '1F(513050)'
    database = 'ASA65'

    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        charset='utf8'  # ou 'utf8mb4' se preferir
    )

    if conn.is_connected():
        print('Conexão estabelecida com sucesso!')
    else:
        print('Falha ao conectar ao banco de dados.')

    return conn
