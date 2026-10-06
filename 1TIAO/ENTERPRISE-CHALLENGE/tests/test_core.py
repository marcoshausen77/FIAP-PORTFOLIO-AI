from io import BytesIO
from pathlib import Path
import pandas as pd
import pytest
from ingestion import read_table
from validation import validate
from analysis import analyze
from benchmark import compare
from recommendations import recommend, priority
from utils import COSTS

ROOT=Path(__file__).resolve().parents[1]

def good(rows):
    v=validate(pd.DataFrame(rows))
    assert not v.errors,v.errors
    return v.data

def test_total_and_cost_per_km(row):
    row.pop('custo_total')
    m=analyze(good([row]))['metrics']
    assert m['custo_total']==1000
    assert m['custo_por_km']==1
    assert m['litros_por_100km']==10

def test_weighted_aggregation_not_mean_of_ratios(row):
    other={**row,'veiculo_id':'V2','km_rodados':9000,'custo_combustivel':1900,'custo_total':2000}
    m=analyze(good([row,other]))['metrics']
    assert m['custo_por_km']==pytest.approx(.3)
    assert m['custo_por_veiculo']==1500

def test_missing_required(row):
    del row['empresa_id']
    assert 'obrigatórios' in validate(pd.DataFrame([row])).errors[0]

def test_missing_km_blocks_ratio_and_benchmark(row,reference):
    row['km_rodados']=None
    df=good([row]);a=analyze(df);b=compare(df,reference)
    assert a['metrics']['custo_total']==1000
    assert a['metrics']['custo_por_km'] is None
    assert b['economy'] is None
    assert a['quality']['missing']['km_rodados']==1

def test_missing_cost_not_zero(row):
    row['custo_seguro']=None;row['custo_total']=None
    a=analyze(good([row]))
    assert a['metrics']['custo_total'] is None
    assert a['metrics']['subtotal_conhecido']==1000
    assert a['categories'].set_index('campo').loc['custo_seguro','cobertura_pct']==0

def test_total_supplied_with_partial_categories(row):
    row['custo_seguro']=None
    a=analyze(good([row]))
    assert a['metrics']['custo_total']==1000
    cat=a['categories'].set_index('campo').loc['custo_seguro']
    assert pd.isna(cat['participacao_pct'])

@pytest.mark.parametrize('field,value',[('custo_total',800),('custo_combustivel',-1),('km_rodados','inf'),('periodo','2026-13'),('litros_combustivel','abc'),('custo_total','NaN')])
def test_invalid_data_blocks(row,field,value):
    row[field]=value
    assert validate(pd.DataFrame([row])).errors

def test_inconsistent_partial_total(row):
    row['custo_seguro']=None;row['custo_total']=50
    assert validate(pd.DataFrame([row])).errors

def test_duplicate_key_blocks(row):
    assert any('duplicada' in e for e in validate(pd.DataFrame([row,row])).errors)

def test_type_conflict_blocks(row):
    assert validate(pd.DataFrame([row,{**row,'periodo':'2026-02','tipo_veiculo':'van'}])).errors

def test_zero_denominator_no_infinity(row,reference):
    row['km_rodados']=0
    df=good([row]);assert analyze(df)['metrics']['custo_por_km'] is None
    assert compare(df,reference)['economy'] is None

def test_all_zero_costs_are_valid(row):
    for c in COSTS+['custo_total']:row[c]=0
    a=analyze(good([row]))
    assert a['metrics']['custo_por_km']==0
    assert a['categories']['participacao_pct'].isna().all()

def test_benchmark_economy_numeric_example(row,reference):
    b=compare(good([row]),reference,.5)
    assert b['excess']==pytest.approx(150)
    assert b['economy']==pytest.approx(75)
    assert b['table'].iloc[0]['taxa_observada']==pytest.approx(.9)

def test_no_negative_savings(row,reference):
    row['custo_combustivel']=600;row['custo_total']=700
    assert compare(good([row]),reference)['economy']==0

def test_aggregate_before_positive_difference(row,reference):
    other={**row,'veiculo_id':'V2','custo_combustivel':600,'custo_total':700}
    assert compare(good([row,other]),reference)['economy']==0

def test_unknown_type_no_fallback(row,reference):
    row['tipo_veiculo']='onibus'
    b=compare(good([row]),reference)
    assert b['economy'] is None and b['coverage']['custo_combustivel']==0

def test_partial_coverage_not_extrapolated(row,reference):
    other={**row,'veiculo_id':'V2','km_rodados':None}
    b=compare(good([row,other]),reference)
    assert b['economy']==75 and b['coverage']['custo_combustivel']==50

@pytest.mark.parametrize('factor',[-.1,1.1,float('nan')])
def test_invalid_factor(row,reference,factor):
    with pytest.raises(ValueError):compare(good([row]),reference,factor)

def test_invalid_benchmark(row,reference):
    with pytest.raises(ValueError): compare(good([row]),pd.concat([reference,reference]))
    reference.loc[0,'referencia_r_por_km']=0
    with pytest.raises(ValueError): compare(good([row]),reference)

def test_recommendation_evidence_and_adherence(row,reference):
    df=good([row]);a=analyze(df);b=compare(df,reference);r=recommend(df,a,b)
    assert len(r)==1
    assert r[0]['economia_estimada']==75
    assert r[0]['aderencia']=='Avaliar Multiabastece'
    assert r[0]['prioridade']=='Média'
    for k in ['problema','evidencia','impacto','recomendacao','prioridade','proximo_passo']:assert r[0][k]

def test_fines_have_no_fabricated_saving(row,reference):
    row['custo_multas']=200;row['custo_total']=1200
    df=good([row]);r=recommend(df,analyze(df),compare(df,reference))
    fine=next(x for x in r if x['aderencia']=='Avaliar Gestor de Multas')
    assert fine['economia_estimada'] is None and fine['prioridade']=='Alta'

def test_priority_thresholds():
    assert priority(1000,100)=='Alta'
    assert priority(5000,50)=='Baixa'
    assert priority(400,80)=='Média'

def test_multiple_companies_require_selection(row):
    df=good([row,{**row,'empresa_id':'OTHER'}])
    with pytest.raises(ValueError):analyze(df)

def test_csv_example_and_xlsx_roundtrip():
    raw=read_table((ROOT/'data/frota_exemplo.csv').read_bytes(),'example.csv')
    df=good(raw.to_dict('records'));assert len(df)==48
    assert df['custo_total'].sum()==pytest.approx(df[COSTS].sum().sum())
    f=BytesIO()
    raw.to_excel(f,index=False)
    x=read_table(f.getvalue(),'example.xlsx')
    assert len(x)==48 and not validate(x).errors

def test_brazilian_csv_decimal(row):
    content=pd.DataFrame([row]).to_csv(index=False,sep=';',decimal=',').encode()
    assert not validate(read_table(content,'br.csv')).errors

@pytest.mark.parametrize('content,name',[(b'a,a\n1,2\n','dup.csv'),(b'a,b\n1\n','ragged.csv'),(b'a,b\n','empty.csv'),(b'%PDF','x.pdf'),(b'bad','x.xlsx')])
def test_bad_uploads(content,name):
    with pytest.raises(ValueError):read_table(content,name)

def test_xlsx_formula_rejected():
    from openpyxl import Workbook
    wb=Workbook();wb.active.append(['cost']);wb.active.append(['=1+1']);f=BytesIO();wb.save(f)
    with pytest.raises(ValueError,match='fórmulas'):read_table(f.getvalue(),'formula.xlsx')

def test_upload_size_limit():
    with pytest.raises(ValueError,match='5 MB'):read_table(b'x'*(5*1024*1024+1),'large.csv')

def test_month_order_and_unique_vehicle_count(row):
    a=analyze(good([{**row,'periodo':'2026-03'},row]))
    assert a['monthly']['periodo'].tolist()==['2026-01','2026-03']
    assert a['metrics']['veiculos']==1


def test_financial_display_rounds_half_up():
    from utils import money
    assert money(12062.445)=='R$ 12.062,45'
    assert money(1.005)=='R$ 1,01'
