import pandas as pd
import pytest

# Função isolada que calcula atrasos simulando a lógica do banco
def calcular_atrasos(df):
    df['entregue'] = pd.to_datetime(df['data_entrega'])
    df['estimado'] = pd.to_datetime(df['data_estimada'])
    atrasados = df[df['entregue'] > df['estimado']].shape[0]
    return atrasados

def test_calculo_atraso_entrega():
    # Dado inventado (mock)
    dados_mock = pd.DataFrame({
        'pedido_id': [1, 2, 3],
        'data_entrega': ['2023-10-15', '2023-10-20', '2023-10-25'],
        'data_estimada': ['2023-10-18', '2023-10-19', '2023-10-30']
    })
    
    # O pedido 2 entregou dia 20, mas o estimado era dia 19 (1 atraso)
    resultado = calcular_atrasos(dados_mock)
    
    assert resultado == 1, f"Erro: Esperava 1 atraso, mas a função retornou {resultado}"