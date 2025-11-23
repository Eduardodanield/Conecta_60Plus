"""
Sistema de extração de perguntas 100% GRATUITO.
Usa apenas HuggingFace (sem OpenAI).
"""

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import config
import random
import re
from typing import List, Dict


class GeradorPerguntasGratuito:
    """
    Gerador de perguntas usando apenas ferramentas gratuitas.
    """
    
    def __init__(self):
        """Inicializa com HuggingFace."""
        print("🆓 Inicializando sistema 100% gratuito...")
        
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )
        
        self.vector_store = Chroma(
            persist_directory=str(config.DB_PERSIST_DIRECTORY),
            embedding_function=self.embeddings
        )
        
        print("✅ Sistema carregado sem custos!")
    
    def buscar_perguntas_no_pdf(self, categoria: str, k: int = 5) -> List[str]:
        """Busca trechos do PDF sobre a categoria."""
        queries = [
            f"perguntas sobre {categoria} em idosos",
            f"avaliação de {categoria} geriátrica"
        ]
        
        todos_trechos = []
        for query in queries:
            docs = self.vector_store.similarity_search(query, k=k)
            todos_trechos.extend([doc.page_content for doc in docs])
        
        return todos_trechos
    
    def extrair_perguntas_do_texto(self, texto: str) -> List[str]:
        """Extrai perguntas do texto."""
        padroes = [
            r'[0-9]+\.\s+([^?]+\?)',
            r'•\s+([^?]+\?)',
        ]
        
        perguntas_encontradas = []
        
        for padrao in padroes:
            matches = re.findall(padrao, texto, re.MULTILINE)
            perguntas_encontradas.extend(matches)
        
        # Limpar
        perguntas_limpas = []
        for p in perguntas_encontradas:
            p = p.strip()
            # FILTRO RIGOROSO
            if (len(p) > 30 and len(p) < 200 and 
                p.endswith('?') and 
                not p.lower().startswith('de ') and
                not p.lower().startswith('ou ') and
                'imagem' not in p.lower() and
                'original' not in p.lower()):
                perguntas_limpas.append(p)
        
        return list(set(perguntas_limpas))
    
    def gerar_pergunta_por_categoria(self, categoria: str) -> Dict:
        """Gera pergunta por categoria."""
        # SEMPRE usar template - mais confiável!
        return self._gerar_pergunta_template(categoria)
    
    def _gerar_pergunta_template(self, categoria: str) -> Dict:
        """
        Templates com perguntas de QUALIDADE.
        Opções SEMPRE adequadas à pergunta!
        """
        templates = {
            "mobilidade": {
                "pergunta": "Você consegue caminhar sem ajuda por pelo menos 100 metros?",
                "opcoes": ["Sim, sem dificuldade", "Sim, com dificuldade", "Apenas com apoio", "Não consigo"],
                "especialidades": {"ortopedia": 3, "geriatria": 2, "fisioterapia": 1}
            },
            "cognitivo": {
                "pergunta": "Você tem dificuldade para lembrar de compromissos ou datas importantes?",
                "opcoes": ["Não", "Às vezes", "Frequentemente", "Sempre"],
                "especialidades": {"neurologia": 3, "geriatria": 2, "psiquiatria": 1}
            },
            "cardiovascular": {
                "pergunta": "Você sente falta de ar ao subir escadas ou fazer esforços?",
                "opcoes": ["Não", "Em esforços grandes", "Em esforços moderados", "Em esforços leves"],
                "especialidades": {"cardiologia": 4, "geriatria": 1}
            },
            "nutricional": {
                "pergunta": "Você perdeu peso sem querer nos últimos 6 meses?",
                "opcoes": ["Não", "Menos de 3 kg", "De 3 a 5 kg", "Mais de 5 kg"],
                "especialidades": {"nutricao": 3, "geriatria": 2, "gastroenterologia": 1}
            },
            "emocional": {
                "pergunta": "Com que frequência você se sente triste ou desanimado?",
                "opcoes": ["Nunca", "Raramente", "Às vezes", "Frequentemente"],
                "especialidades": {"psiquiatria": 3, "geriatria": 2}
            },
            "sono": {
                "pergunta": "Quantas horas você dorme por noite em média?",
                "opcoes": ["Mais de 7 horas", "5 a 7 horas", "3 a 5 horas", "Menos de 3 horas"],
                "especialidades": {"neurologia": 2, "psiquiatria": 2, "geriatria": 1}
            },
            "visao": {
                "pergunta": "Você tem dificuldade para enxergar ou ler mesmo usando óculos?",
                "opcoes": ["Não", "Um pouco", "Moderada", "Muita dificuldade"],
                "especialidades": {"oftalmologia": 3, "geriatria": 1}
            },
            "audicao": {
                "pergunta": "Você tem dificuldade para ouvir conversas em ambientes barulhentos?",
                "opcoes": ["Não", "Um pouco", "Moderada", "Muita dificuldade"],
                "especialidades": {"otorrinolaringologia": 3, "geriatria": 1}
            },
            "quedas": {
                "pergunta": "Você sofreu alguma queda nos últimos 6 meses?",
                "opcoes": ["Não", "Uma vez", "Duas vezes", "Três ou mais vezes"],
                "especialidades": {"ortopedia": 2, "neurologia": 2, "geriatria": 3}
            },
            "medicamentos": {
                "pergunta": "Quantos medicamentos diferentes você toma por dia?",
                "opcoes": ["Nenhum", "1 a 3", "4 a 6", "Mais de 6"],
                "especialidades": {"geriatria": 3, "farmacia_clinica": 2}
            },
            "urinario": {
                "pergunta": "Você tem perda involuntária de urina?",
                "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
                "especialidades": {"urologia": 3, "geriatria": 2}
            },
            "equilibrio": {
                "pergunta": "Você sente tontura ou desequilíbrio ao se levantar?",
                "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
                "especialidades": {"neurologia": 2, "otorrinolaringologia": 2, "geriatria": 1}
            },
            "peso": {
                "pergunta": "Como está seu apetite atualmente?",
                "opcoes": ["Normal", "Levemente reduzido", "Moderadamente reduzido", "Muito reduzido"],
                "especialidades": {"geriatria": 2, "endocrinologia": 2, "nutricao": 2}
            },
            "digestivo": {
                "pergunta": "Você tem problemas intestinais como prisão de ventre ou diarreia?",
                "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
                "especialidades": {"gastroenterologia": 3, "geriatria": 1}
            },
            "pele": {
                "pergunta": "Você tem feridas ou machucados que demoram a cicatrizar?",
                "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
                "especialidades": {"dermatologia": 2, "geriatria": 1}
            }
        }
        
        pergunta_dict = templates.get(categoria, {
            "pergunta": f"Como você avalia sua saúde em relação a {categoria}?",
            "opcoes": ["Muito boa", "Boa", "Regular", "Ruim"],
            "especialidades": {"geriatria": 2}
        })
        
        pergunta_dict["categoria"] = categoria
        return pergunta_dict
    
    def gerar_questionario_completo(
        self, 
        num_perguntas: int = 10,
        categorias: List[str] = None
    ) -> List[Dict]:
        """
        Gera questionário com EXATAMENTE num_perguntas.
        SEM REPETIÇÃO!
        """
        if categorias is None:
            categorias = [
                "mobilidade", "cognitivo", "cardiovascular", "nutricional",
                "emocional", "sono", "visao", "audicao", "quedas",
                "medicamentos", "urinario", "equilibrio", "peso", 
                "digestivo", "pele"
            ]
        
        # Garantir que não pede mais categorias do que existe
        num_perguntas = min(num_perguntas, len(categorias))
        
        # Selecionar categorias ÚNICAS
        categorias_selecionadas = random.sample(categorias, num_perguntas)
        
        print(f"\n🔍 Gerando {num_perguntas} perguntas...")
        
        perguntas_geradas = []
        perguntas_usadas = set()  # Evitar duplicatas
        
        for i, categoria in enumerate(categorias_selecionadas, 1):
            print(f"⏳ [{i}/{num_perguntas}] {categoria}")
            
            try:
                pergunta = self.gerar_pergunta_por_categoria(categoria)
                
                # Verificar se já foi usada
                if pergunta['pergunta'] not in perguntas_usadas:
                    pergunta["id"] = i
                    perguntas_geradas.append(pergunta)
                    perguntas_usadas.add(pergunta['pergunta'])
                    print(f"   ✅ {pergunta['pergunta'][:60]}...")
                else:
                    print(f"   ⚠️ Pergunta duplicada, pulando...")
                
            except Exception as e:
                print(f"   ❌ Erro: {e}")
        
        print(f"\n✨ {len(perguntas_geradas)} perguntas prontas!")
        
        # GARANTIR que retorna EXATAMENTE o número pedido
        return perguntas_geradas[:num_perguntas]


# Cache global
_cache_perguntas_free = None

def get_perguntas_gratuitas(num_perguntas: int = 10, forcar_regenerar: bool = False) -> List[Dict]:
    """
    Função principal para obter perguntas.
    """
    global _cache_perguntas_free
    
    # SEMPRE REGENERAR para evitar cache com perguntas ruins
    gerador = GeradorPerguntasGratuito()
    perguntas = gerador.gerar_questionario_completo(num_perguntas=num_perguntas)
    
    return perguntas