# ==============================================================================
# Arquivo: config.py
# Autor: Eduardo Daniel
# Data: 27/10/2025
# Descrição: Painel de controle central do sistema Conecta 60+.
# Gerencia variáveis de ambiente, configurações de segurança (chaves API),
# caminhos de diretórios do sistema de arquivos e parâmetros do modelo LLM.
# Implementa o padrão "Single Source of Truth" para configurações.
# ==============================================================================

import os
from pathlib import Path
from dotenv import load_dotenv

# --- Inicialização do Ambiente ---
# Define o caminho absoluto para o arquivo .env na raiz do projeto
# Utiliza a estrutura de diretórios para localizar o arquivo independente de onde o script é executado
BASE_DIR = Path(__file__).parent.parent
DOTENV_PATH = BASE_DIR / '.env'

print(f"🔄 [Config] Carregando variáveis de ambiente de: {DOTENV_PATH}")
load_dotenv(dotenv_path=DOTENV_PATH)

if DOTENV_PATH.exists():
    print("✅ [Config] Arquivo .env encontrado e carregado.")
else:
    print("⚠️ [Config] AVISO: Arquivo .env NÃO encontrado.")

# --- Segurança e Autenticação (OpenAI) ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Fallback de segurança para variáveis do sistema
if not OPENAI_API_KEY:
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Validação crítica: O sistema não deve iniciar sem a chave da API
if not OPENAI_API_KEY:
    raise ValueError(
        "CRÍTICO: A chave da API da OpenAI (OPENAI_API_KEY) não foi detectada. "
        "Verifique o arquivo .env na raiz do projeto."
    )
else:
    # Log de segurança (não exibe a chave, apenas confirmação)
    print("🔒 [Config] Chave de API validada com sucesso.")

# --- Parâmetros do Modelo de IA (LLM) ---
LLM_MODEL = "gpt-3.5-turbo"
TEMPERATURE = 0.7  # Equilibra criatividade e precisão nas respostas

# --- Mapeamento de Diretórios (File System) ---
# Utiliza pathlib para garantir compatibilidade entre Windows, Linux e Mac
DOCS_DIRECTORY = BASE_DIR / 'base'
DB_PERSIST_DIRECTORY = BASE_DIR / 'db'
DB_AMPI_GUIDE_DIRECTORY = BASE_DIR / 'db_ampi_guide'
DATABASE_FILE = BASE_DIR / 'dados_pacientes.csv'

# --- Configurações de Processamento de Dados (RAG) ---
CHUNK_SIZE = 1000    # Tamanho do bloco de texto para vetorização
CHUNK_OVERLAP = 200  # Sobreposição para manter contexto entre blocos
RETRIEVAL_TOP_K = 5  # Número de documentos relevantes a recuperar

# --- Segurança da Aplicação ---
ADMIN_PASSWORD = "admin123"  # Senha de acesso ao Dashboard Administrativo

# --- Engenharia de Prompt ---
# Template base para instruir o comportamento do assistente
PROMPT_TEMPLATE = """Você é o AMPI, um assistente de IA especializado em responder perguntas com base nos documentos fornecidos. 
Use o contexto abaixo para responder à pergunta do usuário de forma clara e precisa.

Contexto:
{context}

Pergunta: {question}

Resposta:"""