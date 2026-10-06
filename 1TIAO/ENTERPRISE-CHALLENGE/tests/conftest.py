from pathlib import Path
import sys
import pandas as pd
import pytest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))

@pytest.fixture
def row():
    return dict(periodo='2026-01',empresa_id='DEMO',veiculo_id='V001',tipo_veiculo='leve',
                km_rodados=1000,litros_combustivel=100,custo_combustivel=900,
                custo_pedagio=0,custo_manutencao=100,custo_multas=0,custo_impostos=0,
                custo_seguro=0,outros_custos=0,custo_total=1000)

@pytest.fixture
def reference():
    return pd.DataFrame([dict(tipo_veiculo='leve',categoria='custo_combustivel',
        referencia_r_por_km=.75,origem='SIMULADO_ACADEMICO',versao=1),
        dict(tipo_veiculo='leve',categoria='custo_manutencao',
        referencia_r_por_km=.10,origem='SIMULADO_ACADEMICO',versao=1)])
