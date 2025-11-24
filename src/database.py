# ==============================================================================
# Arquivo: database.py
# Autor: João
# Data: 20/11/2025
# Descrição: Camada de persistência de dados do Conecta 60+.
#            Gerencia o armazenamento histórico dos pacientes em formato CSV,
#            garantindo a integridade dos dados e fornecendo funções otimizadas
#            para leitura, escrita e geração de estatísticas em tempo real.
#            Atua como o "Backend Database" simplificado da aplicação.
# ==============================================================================

import pandas as pd
import os
from datetime import datetime
import config

def salvar_paciente(dados_pessoais, respostas, analise):
    """
    Persiste os dados completos do atendimento no banco de dados (CSV).
    Realiza o tratamento e formatação dos dados brutos antes da escrita.
    
    Args:
        dados_pessoais (dict): Informações demográficas.
        respostas (dict): Respostas coletadas no questionário.
        analise (dict): Resultados do processamento da IA/Algoritmo.
        
    Returns:
        tuple: (bool: sucesso, df/str: resultado ou mensagem de erro)
    """
    # Normalização dos dados para registro
    registro = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # Log temporal preciso
        'nome': dados_pessoais.get('nome', ''),
        'idade': dados_pessoais.get('idade', 0),
        'cidade': dados_pessoais.get('cidade', ''),
        'sexo': dados_pessoais.get('sexo', 'N/A'), # Adicionado campo sexo
        'filhos': dados_pessoais.get('filhos', 0),
        'especialidade_recomendada': analise['especialidade'],
        'urgencia': analise['urgencia'],
        'pontuacao_total': analise['pontuacao_total'],
        # Converte lista para string para salvar no CSV
        'categorias_problema': ', '.join(analise.get('categorias_problema', [])),
        'recomendacao': analise['recomendacao']
    }
    
    # Mapeamento dinâmico das respostas do questionário
    # Isso permite que o banco cresça horizontalmente se novas perguntas forem adicionadas
    for id_pergunta, resposta in respostas.items():
        registro[f'pergunta_{id_pergunta}'] = resposta
    
    # Recupera o caminho do arquivo do módulo de configuração
    arquivo = str(config.DATABASE_FILE)
    
    try:
        # Lógica de Persistência: Append ou Create
        if os.path.exists(arquivo):
            # Se o banco já existe, carrega e anexa o novo registro
            df = pd.read_csv(arquivo)
            df_novo = pd.DataFrame([registro])
            df = pd.concat([df, df_novo], ignore_index=True)
        else:
            # Se é o primeiro registro, cria o DataFrame inicial
            df = pd.DataFrame([registro])
        
        # Escrita atômica no disco com encoding UTF-8 para suportar acentuação
        df.to_csv(arquivo, index=False, encoding='utf-8')
        return True, df
        
    except Exception as e:
        # Tratamento de erro robusto para não quebrar a aplicação
        return False, str(e)


def carregar_dados():
    """
    Recupera a base histórica completa para análise.
    Implementa tratamento de exceção para arquivos corrompidos ou inexistentes.
    
    Returns:
        pd.DataFrame: Dataset completo ou vazio em caso de falha.
    """
    arquivo = str(config.DATABASE_FILE)
    
    if os.path.exists(arquivo):
        try:
            return pd.read_csv(arquivo, encoding='utf-8')
        except Exception as e:
            print(f"ERRO CRÍTICO: Falha ao ler banco de dados: {e}")
            return pd.DataFrame()
    else:
        return pd.DataFrame()


def get_estatisticas():
    """
    Gera KPIs (Key Performance Indicators) em tempo real para o Dashboard.
    Processa o DataFrame bruto para extrair métricas de negócio.
    
    Returns:
        dict: Dicionário contendo as métricas calculadas.
    """
    df = carregar_dados()
    
    # Retorno padrão para base vazia (Cold Start)
    if df.empty:
        return {
            'total_pacientes': 0,
            'idade_media': 0,
            'atendimentos_hoje': 0
        }
    
    hoje = datetime.now().strftime("%Y-%m-%d")
    
    # Cálculo das métricas analíticas
    stats = {
        'total_pacientes': len(df),
        # Tratamento seguro para cálculo de média (evita erro se coluna não existir)
        'idade_media': df['idade'].mean() if 'idade' in df.columns else 0,
        'atendimentos_hoje': 0
    }
    
    # Filtro temporal para métrica diária
    if 'timestamp' in df.columns:
        try:
            # Filtra registros que contém a data de hoje no timestamp
            atendimentos_hoje = len(df[df['timestamp'].str.contains(hoje, na=False)])
            stats['atendimentos_hoje'] = atendimentos_hoje
        except:
            stats['atendimentos_hoje'] = 0
    
    return stats