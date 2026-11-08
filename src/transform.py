import sqlite3

def rodar_sql(arquivo_sql, cursor):
    with open(arquivo_sql, 'r', encoding='utf-8') as f:
        query = f.read()
    cursor.execute("DROP TABLE IF EXISTS " + arquivo_sql.split('/')[-1].replace('.sql', ''))
    cursor.execute(query)

def executar_pipeline():
    conn = sqlite3.connect('auto_parts.db')
    cur = conn.cursor()
    
    print("Construindo camada REFINED...")
    rodar_sql('sql/refined/ref_auto_orders.sql', cur)
    
    print("Construindo camada MARTS...")
    rodar_sql('sql/marts/mart_freight_impact.sql', cur)
    rodar_sql('sql/marts/mart_delivery_delay.sql', cur)
    
    conn.commit()
    conn.close()
    print("Pipeline de transformação concluído.")

if __name__ == "__main__":
    executar_pipeline()