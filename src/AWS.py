import pandas as pd
from sqlalchemy import create_engine
import time

# Função para conectar ao banco de dados MySQL
def conectar_mysql(usuario, senha, host, banco, porta=3306):
    conexao_string = f'mysql+mysqlconnector://{usuario}:{senha}@{host}:{porta}/{banco}'
    engine = create_engine(conexao_string)
    return engine

# Função para ler os dados da planilha e persistir no MySQL
def persistir_dados(nome_arquivo, tabela_destino, usuario, senha, host, porta, banco):
    # Conectando ao banco de dados
    engine = conectar_mysql(usuario, senha, host, banco, porta)
    
    # Lendo os dados da planilha
    df = pd.read_excel(nome_arquivo)
    
    # Iniciando o cronômetro
    inicio = time.time()
    
    # Persistindo os dados no MySQL
    df.to_sql(tabela_destino, con=engine, if_exists='replace', index=False)
    
    # Parando o cronômetro
    fim = time.time()
    
    # Exibindo o tempo utilizado para a operação
    print(f"Tempo utilizado para a persistência dos dados: {fim - inicio} segundos.")

# Exemplo de uso
nome_arquivo = '..\\assets\\dados_clientes.xlsx'  # Atualize para o caminho correto da planilha
tabela_destino = 'cliente'
usuario = 'root'
senha = 'Cesar280197'
host = 'tcccesar.cf4uqsaw2by1.us-east-2.rds.amazonaws.com'
porta = '3306'
banco = 'tcccesar'

# nome_arquivo = 'caminho_para_sua_planilha.xlsx'  # Atualize para o caminho correto da planilha
# tabela_destino = 'nome_da_tabela_no_mysql'
# usuario = 'seu_usuario'
# senha = 'sua_senha'
# host = 'endereco_do_host_aws'
# porta = 'porta'
# banco = 'tccCesar'

# Chamando a função para persistir os dados
persistir_dados(nome_arquivo, tabela_destino, usuario, senha, host, porta, banco)
