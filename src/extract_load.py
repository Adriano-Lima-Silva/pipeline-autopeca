import pandas as pd
import sqlite3
import os

def carregar_dados_brutos():
    conn = sqlite3.connect('auto_parts.db')
    
    # Tabelas escolhidas da Olist
    tabelas = {
        'raw_orders': 'data/raw/olist_orders_dataset.csv',
        'raw_order_items': 'data/raw/olist_order_items_dataset.csv',
        'raw_products': 'data/raw/olist_products_dataset.csv'
    }
    
    for nome_tabela, caminho in tabelas.items():
        print(f"Carregando {nome_tabela}...")
        df = pd.read_csv(caminho)
        df.to_sql(nome_tabela, conn, if_exists='replace', index=False)
        
    conn.close()
    print("Camada RAW concluída com sucesso.")

if __name__ == "__main__":
    carregar_dados_brutos()