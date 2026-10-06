"""Ações baseadas em evidências; produto só quando a necessidade é aderente."""
from utils import LABELS, money, number

def priority(economy, coverage):
    if economy>=1000 and coverage>=90: return 'Alta'
    if (economy>=300 and coverage>=60) or (economy>0 and coverage>=90): return 'Média'
    return 'Baixa'

def recommend(df, analysis, benchmark):
    items=[]
    for row in benchmark['table'].to_dict('records'):
        if row['excesso_teorico']<=0: continue
        fuel=row['categoria']=='custo_combustivel'
        item={'problema':f"{LABELS[row['categoria']]} acima da referência simulada: {row['tipo_veiculo']}",
              'evidencia':f"{money(row['custo_observado'])} / {number(row['km_elegiveis'])} km = {number(row['taxa_observada'],4)} R$/km; referência {number(row['referencia_r_por_km'],4)} R$/km.",
              'impacto':f"Excesso teórico {money(row['excesso_teorico'])}; não é desperdício comprovado.",
              'recomendacao':'Conferir preços, abastecimentos, consumo e rotas.' if fuel else 'Revisar ordens de serviço, causas e calendário preventivo; não reduzir manutenção de segurança.',
              'prioridade':priority(row['economia_estimada'],row['cobertura_pct']),
              'economia_estimada':float(row['economia_estimada']),
              'proximo_passo':'Gestor: validar os registros e testar uma ação por 30 dias, comparando custo/km em condições equivalentes.',
              'cobertura_pct':row['cobertura_pct'],
              'aderencia':'Avaliar Multiabastece' if fuel else 'Avaliar Gestão de Manutenção'}
        items.append(item)
    for cat,prio,action,product in [
        ('custo_multas','Alta','Revisar causas, vencimentos e medidas educativas. Não presumir prazo ou infração sem documento.','Avaliar Gestor de Multas'),
        ('custo_pedagio','Média','Conciliar passagens com rotas e cobranças. Verificar o contexto do transporte.','Avaliar Tag Sem Parar ou Vale-Pedágio conforme aderência')]:
        known=df[cat].sum(min_count=1)
        if known>0:
            items.append({'problema':f'Revisão de {LABELS[cat].lower()}',
                'evidencia':f'{money(known)} conhecidos no período; não implica desperdício.',
                'impacto':'Oportunidade qualitativa; economia não quantificada.',
                'recomendacao':action,'prioridade':prio,'economia_estimada':None,
                'proximo_passo':'Gestor: conferir documentos e definir ação, responsável e prazo.',
                'cobertura_pct':float(df[cat].notna().mean()*100),'aderencia':product})
    if analysis['quality']['missing']:
        items.append({'problema':'Lacunas de dados','evidencia':', '.join(analysis['quality']['missing']),
            'impacto':'Parte dos indicadores ou comparações está indisponível.',
            'recomendacao':'Completar os campos e reimportar o arquivo.', 'prioridade':'Média',
            'economia_estimada':None,'proximo_passo':'Responsável pelos dados: conferir fontes, sem preencher ausência com zero.',
            'cobertura_pct':analysis['quality']['percent'],'aderencia':'Sem oferta automática'})
    if any(c<100 for c in benchmark['coverage'].values()):
        items.append({'problema':'Cobertura parcial do benchmark','evidencia':str(benchmark['coverage']),
            'impacto':'O cenário não cobre toda a operação.','recomendacao':'Revisar km zero, campos ausentes e tipos sem referência.',
            'prioridade':'Baixa','economia_estimada':None,'proximo_passo':'Validar a comparabilidade antes de estimar a frota inteira.',
            'cobertura_pct':min(benchmark['coverage'].values()),'aderencia':'Sem oferta automática'})
    order={'Alta':0,'Média':1,'Baixa':2}
    return sorted(items,key=lambda i:(order[i['prioridade']],-(i['economia_estimada'] or 0)))
