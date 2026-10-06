from pathlib import Path
from unittest.mock import patch
from io import BytesIO
import pandas as pd
from streamlit.testing.v1 import AppTest

ROOT=Path(__file__).resolve().parents[1]
APP=str(ROOT/'src/app.py')

class Upload(BytesIO):
    def __init__(self,content,name):super().__init__(content);self.name=name

def test_streamlit_example_filters_report():
    at=AppTest.from_file(APP,default_timeout=30).run()
    assert not at.exception
    at.checkbox[0].check().run()
    assert not at.exception
    assert len(at.metric)==4
    assert at.metric[2].value=='8'
    assert at.get('download_button')
    at.selectbox[0].select('CFO / Liderança').run()
    at.multiselect[0].set_value(['2026-01']).run()
    assert not at.exception and at.metric[2].value=='8'
    at.slider[0].set_value(0).run()
    assert at.metric[3].value=='R$ 0,00'
    at.multiselect[0].set_value([]).run()
    assert not at.exception and at.warning

def test_streamlit_csv_upload_path():
    uploaded=Upload((ROOT/'data/frota_exemplo.csv').read_bytes(),'frota_exemplo.csv')
    # AppTest 1.50 não fornece interação nativa com upload: injetar os bytes no widget,
    # mantendo ingestão, validação, cálculo, renderização e download reais.
    with patch('streamlit.file_uploader',return_value=uploaded):
        at=AppTest.from_file(APP,default_timeout=30).run()
    assert not at.exception and len(at.metric)==4
    assert at.metric[2].value=='8'

def test_streamlit_xlsx_upload_path():
    f=BytesIO();pd.read_csv(ROOT/'data/frota_exemplo.csv').to_excel(f,index=False)
    with patch('streamlit.file_uploader',return_value=Upload(f.getvalue(),'example.xlsx')):
        at=AppTest.from_file(APP,default_timeout=30).run()
    assert not at.exception and at.metric[2].value=='8'

def test_streamlit_rejects_bad_upload():
    with patch('streamlit.file_uploader',return_value=Upload(b'wrong\n123','bad.csv')):
        at=AppTest.from_file(APP,default_timeout=30).run()
    assert not at.exception and at.error
    assert len(at.metric)==0

def test_report_contains_numbers_limits_and_actions():
    from app import report
    from ingestion import read_table
    from validation import validate
    from analysis import analyze
    from benchmark import compare
    from recommendations import recommend
    raw=read_table((ROOT/'data/frota_exemplo.csv').read_bytes(),'frota_exemplo.csv')
    v=validate(raw);a=analyze(v.data);b=compare(v.data,pd.read_csv(ROOT/'data/benchmark_simulado.csv'))
    text=report(v.data,a,b,recommend(v.data,a,b),v.received)
    for term in ['Resumo executivo','EMP_DEMO_01','simulados','Premissas','prioridade','proximo_passo','R$']:
        assert term in text
