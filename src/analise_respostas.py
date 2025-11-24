# src/analise_respostas.py

def analisar_respostas(perguntas_respondidas, respostas):
    """
    Analisa as respostas e retorna especialidade recomendada.
    COMPATÍVEL com o sistema de perguntas do perguntas_conecta60.py
    
    Args:
        perguntas_respondidas: Lista de perguntas que foram feitas
        respostas: Dicionário com as respostas {id_pergunta: resposta_escolhida}
    
    Returns:
        dict com especialidade, urgencia e detalhes
    """
    scores = {}
    detalhes_categorias = {}
    
    for pergunta in perguntas_respondidas:
        pergunta_id = pergunta['id']
        resposta = respostas.get(pergunta_id, "")
        
        # Contar categorias
        categoria = pergunta.get('categoria', 'geral')
        if categoria not in detalhes_categorias:
            detalhes_categorias[categoria] = 0
        
        # Calcular pontos baseado na resposta
        # Lógica: Quanto maior o índice da opção, pior a situação
        # Exemplo: ["Não", "Às vezes", "Frequentemente"]
        # "Não" = índice 0 (melhor) = 0 pontos
        # "Às vezes" = índice 1 = 1 ponto
        # "Frequentemente" = índice 2 (pior) = 2 pontos
        
        try:
            indice_resposta = pergunta['opcoes'].index(resposta) if resposta in pergunta['opcoes'] else 0
        except (ValueError, KeyError):
            indice_resposta = 0
        
        # Somar pontos para cada especialidade baseado no peso
        especialidades = pergunta.get('especialidades', {})
        
        for especialidade, peso in especialidades.items():
            if especialidade not in scores:
                scores[especialidade] = 0
            
            # Quanto pior a resposta (índice maior), mais pontos
            # Multiplicado pelo peso da especialidade
            scores[especialidade] += peso * indice_resposta
        
        # Contar problemas por categoria
        if indice_resposta > 0:  # Se não for a primeira opção (geralmente "Não" ou "Nenhum")
            detalhes_categorias[categoria] += 1
    
    # Encontrar especialidade com maior pontuação
    if not scores or all(score == 0 for score in scores.values()):
        # Se não há pontuação ou todas são zero = paciente saudável!
        return {
            'especialidade': 'geriatria',
            'urgencia': 'baixa',
            'scores': {'geriatria': 0, 'clinico_geral': 0},
            'categorias_problema': [],
            'recomendacao': 'Excelente! Suas respostas indicam boa saúde geral. Continue com check-ups de rotina.',
            'pontuacao_total': 0
        }
    
    especialidade_principal = max(scores, key=scores.get)
    pontuacao_maxima = scores[especialidade_principal]
    
    # Determinar urgência baseada na pontuação
    if pontuacao_maxima >= 15:
        urgencia = 'alta'
        recomendacao = 'Recomendamos agendar consulta o mais breve possível'
    elif pontuacao_maxima >= 8:
        urgencia = 'média'
        recomendacao = 'Recomendamos agendar consulta nas próximas semanas'
    else:
        urgencia = 'baixa'
        recomendacao = 'Consulta de acompanhamento recomendada'
    
    # Categorias com problemas
    categorias_problema = [cat for cat, count in detalhes_categorias.items() if count > 0]
    
    # Top 3 especialidades
    top_especialidades = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
    
    return {
        'especialidade': especialidade_principal,
        'urgencia': urgencia,
        'scores': dict(top_especialidades),
        'categorias_problema': categorias_problema,
        'recomendacao': recomendacao,
        'pontuacao_total': pontuacao_maxima
    }


def formatar_nome_especialidade(especialidade):
    """Formata o nome da especialidade para exibição"""
    nomes = {
        'cardiologia': 'Cardiologia',
        'ortopedia': 'Ortopedia',
        'neurologia': 'Neurologia',
        'geriatria': 'Geriatria',
        'psiquiatria': 'Psiquiatria',
        'reumatologia': 'Reumatologia',
        'pneumologia': 'Pneumologia',
        'gastroenterologia': 'Gastroenterologia',
        'nutricao': 'Nutrição',
        'oftalmologia': 'Oftalmologia',
        'otorrinolaringologia': 'Otorrinolaringologia',
        'urologia': 'Urologia',
        'assistencia_social': 'Assistência Social',
        'fisioterapia': 'Fisioterapia',
        'dermatologia': 'Dermatologia',
        'angiologia': 'Angiologia',
        'endocrinologia': 'Endocrinologia',
        'farmacia_clinica': 'Farmácia Clínica'
    }
    return nomes.get(especialidade, especialidade.capitalize())