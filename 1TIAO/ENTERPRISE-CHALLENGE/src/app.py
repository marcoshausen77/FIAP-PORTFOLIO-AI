"""Bônus acadêmico local. Executar: python -m streamlit run src/app.py."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
import pandas as pd
import streamlit as st
from ingestion import read_table
from validation import validate
from analysis import analyze
from benchmark import compare
from recommendations import recommend
from utils import money, number, safe_text, BENCH_NOTICE

BASE=Path(__file__).resolve().parents[1]

def report(df,result,bench,actions,received):
    m=result['metrics'];q=result['quality']
    lines=['# FleetSave AI — Relatório acadêmico',
        '\n## Resumo executivo',
        f"Empresa: {safe_text(df['empresa_id'].iloc[0])}",
        'Períodos: '+', '.join(map(safe_text,sorted(df['periodo'].unique()))),
        f"Veículos: {m['veiculos']} · Registros: {len(df)}",
        f"Custo total: {money(m['custo_total'])}",
        f"Subtotal conhecido: {money(m['subtotal_conhecido'])}",
        f"Custo/km: {money(m['custo_por_km'])}",
        f"Completude: {q['level']} ({number(q['percent'])}%). Não é confiança estatística.",
        f"Economia no cenário acadêmico: {money(bench['economy'])}",
        f"Excesso teórico: {money(bench['excess'])}; fator de realização: {number(bench['factor']*100)}%.",
        '\n## Categorias',
        '| Categoria | Integral | Subtotal conhecido | Cobertura | Participação |',
        '|---|---:|---:|---:|---:|']
    for r in result['categories'].to_dict('records'):
        integral=None if pd.isna(r['valor_integral']) else r['valor_integral']
        known=None if pd.isna(r['subtotal_conhecido']) else r['subtotal_conhecido']
        lines.append(f"| {r['categoria']} | {money(integral)} | {money(known)} | {number(r['cobertura_pct'])}% | {number(r['participacao_pct'])} |")
    lines+=['\n## Indicadores e limitações']
    for k,v in m.items(): lines.append(f'- {k}: {number(v)}')
    lines+=['Recebidos: '+', '.join(map(safe_text,received)),
        'Ausências (linhas): '+safe_text(q['missing']),
        'Cálculos bloqueados: '+', '.join(k for k,v in m.items() if v is None),
        'Cobertura do benchmark: '+safe_text(bench['coverage']),
        '\n## Diagnóstico e recomendações']
    if not actions: lines.append('Nenhum desvio positivo ou ação adicional pelas regras atuais; isto não comprova eficiência total.')
    for idx,a in enumerate(actions,1):
        lines.append(f"\n### {idx}. {safe_text(a['problema'])}")
        for field in ['evidencia','impacto','recomendacao','prioridade','proximo_passo','aderencia']:
            lines.append(f'- {field}: {safe_text(a[field])}')
        lines.append(f"- Economia estimada: {money(a['economia_estimada'])}; cobertura {number(a['cobertura_pct'])}%")
    lines+=['\n## Premissas',BENCH_NOTICE,
        'Benchmark versão 1. Categorias comparadas: combustível e manutenção. Fórmula: max(0, custo elegível − referência × km elegíveis) × fator.',
        'Oportunidades não garantidas; não incluem investimento de implantação nem comprovam causalidade. Sem extrapolação das linhas excluídas.',
        'MVP sem OCR, IA, persistência e autenticação. Apenas dados fictícios. Perfil visual não é controle de acesso.']
    return '\n\n'.join(lines)+'\n'

def main():
    st.set_page_config(page_title='FleetSave AI',page_icon='📊',layout='wide')
    st.title('FleetSave AI')
    st.caption('Calculadora Inteligente de Redução de Custos de Frota · FIAP / Enterprise Challenge')
    st.info('Demonstração acadêmica local. Use apenas dados fictícios. Benchmark simulado; economia não garantida.')
    with st.sidebar:
        st.header('Análise da operação')
        profile=st.selectbox('Visão',['Gestor de Frota','CFO / Liderança','Sem Parar Empresas'])
        st.caption('A visão muda a apresentação; não é autenticação.')
        uploaded=st.file_uploader('Enviar CSV ou XLSX',type=['csv','xlsx'])
        st.caption('Até 5 MB, 10.000 linhas e 50 colunas. XLSX: primeira aba. Sem PDF/OCR.')
        example=st.checkbox('Carregar exemplo simulado',value=False)
        factor=st.slider('Fator de realização do excesso teórico (%)',0,100,50,5)
    if uploaded is None and not example:
        st.subheader('Comece pelos dados')
        st.write('Carregue o exemplo ou envie uma planilha no modelo. A análise mostrará custos conhecidos, lacunas e ações possíveis.')
        st.download_button('Baixar CSV de exemplo',(BASE/'data/frota_exemplo.csv').read_bytes(),
                           file_name='frota_exemplo.csv',mime='text/csv')
        return
    try:
        if uploaded is not None:
            raw=read_table(uploaded.getvalue(),uploaded.name)
            st.caption('Fonte: arquivo enviado. O upload tem precedência sobre o exemplo.')
        else:
            raw=read_table((BASE/'data/frota_exemplo.csv').read_bytes(),'frota_exemplo.csv')
            st.caption('Fonte: frota fictícia Logística Horizonte Demo.')
        val=validate(raw)
    except Exception as exc:
        st.error(f'Não foi possível ler a entrada: {exc}')
        return
    if val.errors:
        st.error('Análise bloqueada. Corrija as inconsistências abaixo; nenhuma linha foi descartada silenciosamente.')
        for error in val.errors: st.error(error)
        return
    for warning in val.warnings: st.warning(warning)
    df=val.data
    company=st.sidebar.selectbox('Empresa',sorted(df['empresa_id'].unique()))
    df=df.loc[df['empresa_id']==company]
    periods=sorted(df['periodo'].unique())
    selected=st.sidebar.multiselect('Meses',periods,default=periods)
    df=df.loc[df['periodo'].isin(selected)]
    if df.empty:
        st.warning('Selecione ao menos um mês.');return
    result=analyze(df)
    try:
        ref=pd.read_csv(BASE/'data/benchmark_simulado.csv')
        bench=compare(df,ref,factor/100)
    except ValueError as exc:
        st.error(str(exc));return
    actions=recommend(df,result,bench)
    m=result['metrics'];q=result['quality']
    st.subheader('Resumo executivo' if profile=='CFO / Liderança' else 'Visão da operação')
    a,b,c,d=st.columns(4)
    a.metric('Custo total' if m['custo_total'] is not None else 'Subtotal conhecido',
             money(m['custo_total'] if m['custo_total'] is not None else m['subtotal_conhecido']))
    b.metric('Custo por km',money(m['custo_por_km']))
    c.metric('Veículos',m['veiculos'])
    d.metric('Economia no cenário simulado',money(bench['economy']))
    if m['custo_total'] is None:
        st.warning('Custo total indisponível: o subtotal contém apenas valores conhecidos e pode subestimar a operação.')
    st.caption(f"Completude {q['level']}: {number(q['percent'])}% · {len(df)} registros. Cobertura não equivale a certeza estatística.")
    quality,costs,diagnosis,plan=st.tabs(['Qualidade dos dados','Custos e evolução','Benchmark e cenário','Plano de ação'])
    with quality:
        st.write('Campos recebidos:',', '.join(val.received))
        if q['missing']:
            st.dataframe(pd.DataFrame([{'campo':k,'linhas_ausentes':v} for k,v in q['missing'].items()]),hide_index=True)
            st.write('Próximo passo: completar esses campos nas fontes e reimportar; não preencher desconhecido com zero.')
        else: st.success('Campos operacionais completos no recorte.')
        missing_metrics=[k for k,v in m.items() if v is None]
        st.write('Cálculos indisponíveis:',', '.join(missing_metrics) if missing_metrics else 'Nenhum dos indicadores tabulares.')
        st.write('Cálculos possíveis:',', '.join(k for k,v in m.items() if v is not None))
        st.dataframe(df,hide_index=True)
    with costs:
        st.subheader('Custos por categoria')
        st.caption('Barras são subtotais conhecidos; consulte cobertura antes de comparar.')
        table=result['categories']
        st.bar_chart(table.set_index('categoria')['subtotal_conhecido'])
        st.dataframe(table.drop(columns=['campo']),hide_index=True)
        st.subheader('Evolução mensal')
        monthly=result['monthly']
        st.dataframe(monthly,hide_index=True)
        st.line_chart(monthly.set_index('periodo')['custo_total'])
        st.caption('Meses ausentes não são zero. Variação de volume/mix não comprova efeito das ações.')
        st.dataframe(pd.DataFrame([{'indicador':k,'valor':number(v)} for k,v in m.items()]),hide_index=True)
    with diagnosis:
        st.warning(BENCH_NOTICE)
        st.write(f"Excesso teórico: {money(bench['excess'])} · Fator: {factor}% · Cenário: {money(bench['economy'])}")
        st.code('economia = max(0, custo elegível − referência × km elegíveis) × fator de realização')
        st.write('Cobertura por categoria (%):',bench['coverage'])
        if bench['table'].empty: st.info('Sem pares comparáveis. Forneça km positivos, custos e tipo com referência.')
        else: st.dataframe(bench['table'],hide_index=True)
        st.caption('Não extrapola ausências; não inclui custo de implantação; não constitui promessa de economia.')
    with plan:
        if profile=='Sem Parar Empresas':
            st.info('Oportunidades ilustrativas. Sem envio de leads ou compartilhamento automático. Aderência precisa ser validada.')
        if not actions: st.success('Nenhum desvio positivo nas regras atuais. Isso não comprova eficiência total.')
        for a in actions:
            with st.expander(f"{a['prioridade']} · {a['problema']}",expanded=True):
                st.write('Evidência:',a['evidencia']);st.write('Impacto:',a['impacto'])
                st.write('Recomendação:',a['recomendacao'])
                st.write('Economia estimada:',money(a['economia_estimada']))
                st.write('Próximo passo:',a['proximo_passo'])
                st.caption(a['aderencia']+' · Hipótese de aderência, sem garantia de redução.')
    st.download_button('Baixar relatório',report(df,result,bench,actions,val.received),
                       file_name='relatorio_fleetsave.md',mime='text/markdown')
    st.caption('Atualização: carregue um novo arquivo consolidado; o anterior é substituído. Histórico persistente está no roadmap.')

if __name__=='__main__': main()
