import time
from data_json import dados_json
from data_csv import dados_csv
from data_SQLite import dados_sql

# Funções para simular o carregamento dos dados
def carregar_dados_json():
    return dados_json

def carregar_dados_csv():
    return dados_csv

def carregar_dados_sqlite():
    return dados_sql

# Medir tempo de carregamento dos dados JSON
start_time_json = time.perf_counter()
dados_carregados_json = carregar_dados_json()
end_time_json = time.perf_counter()
print(f'Tempo de carregamento dos dados JSON: {end_time_json - start_time_json:.10f} segundos')

# Medir tempo de carregamento dos dados CSV
start_time_csv = time.perf_counter()
dados_carregados_csv = carregar_dados_csv()
end_time_csv = time.perf_counter()
print(f'Tempo de carregamento dos dados CSV: {end_time_csv - start_time_csv:.10f} segundos')

# Medir tempo de carregamento dos dados SQLite
start_time_sqlite = time.perf_counter()
dados_carregados_sqlite = carregar_dados_sqlite()
end_time_sqlite = time.perf_counter()
print(f'Tempo de carregamento dos dados SQLite: {end_time_sqlite - start_time_sqlite:.10f} segundos')
