import pandas as pd
from sqlalchemy import create_engine
import time

# Função para conectar ao banco de dados MySQL na Azure
def conectar_mysql_azure(usuario, senha, host, banco, porta=3306):
    conexao_string = f'mysql+mysqlconnector://{usuario}:{senha}@{host}:{porta}/{banco}'
    engine = create_engine(conexao_string)
    return engine

# Função para ler os dados da planilha e persistir no MySQL na Azure
def persistir_dados_azure(nome_arquivo, tabela_destino, usuario, senha, host, banco, porta):
    # Conectando ao banco de dados MySQL na Azure
    engine = conectar_mysql_azure(usuario, senha, host, banco, porta)
    
    # Lendo os dados da planilha
    df = pd.read_excel(nome_arquivo)
    
    # Iniciando o cronômetro
    inicio = time.time()
    
    # Persistindo os dados no MySQL na Azure
    df.to_sql(tabela_destino, con=engine, if_exists='replace', index=False)
    
    # Parando o cronômetro
    fim = time.time()
    
    # Exibindo o tempo utilizado para a operação
    print(f"Tempo utilizado para a persistência dos dados: {fim - inicio} segundos.")

# Exemplo de uso
nome_arquivo = '..\\assets\\dados_clientes.xlsx'  # Substitua pelo caminho correto da sua planilha
tabela_destino = 'cliente'
usuario = 'usuarioTcc'
senha = 'senhaTcc135'
host = 'tcccesar.mysql.database.azure.com'
porta = '3306'
banco = 'tcccesar'

# Exemplo de uso
# nome_arquivo = 'caminho_para_sua_planilha.xlsx'  # Substitua pelo caminho correto da sua planilha
# tabela_destino = 'nome_da_tabela_no_mysql_azure'
# usuario = 'seu_usuario'
# senha = 'sua_senha'
# host = 'endereco_do_host_azure_mysql'
# banco = 'nome_do_banco'

# Chamando a função para persistir os dados
persistir_dados_azure(nome_arquivo, tabela_destino, usuario, senha, host, banco, porta)
