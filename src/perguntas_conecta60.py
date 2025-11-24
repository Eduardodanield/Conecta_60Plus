# src/perguntas_conecta60.py
"""
BANCO COMPLETO - 100 PERGUNTAS REAIS DO PDF CONECTA 60+
Cada pergunta analisada individualmente com opções corretas
"""

import random
from typing import List, Dict

# =============================================================================
# 100 PERGUNTAS REAIS DO PDF - ANALISADAS UMA POR UMA
# =============================================================================

BANCO_100_PERGUNTAS = [
    # CATEGORIA 1: MOBILIDADE E SAÚDE FÍSICA (1-20)
    {
        "id": 1,
        "pergunta": "Você consegue caminhar sem ajuda por pelo menos 100 metros?",
        "opcoes": ["Sim, facilmente", "Sim, com esforço", "Com ajuda", "Não consigo"],
        "categoria": "mobilidade",
        "especialidades": {"ortopedia": 3, "geriatria": 2, "fisioterapia": 1}
    },
    {
        "id": 2,
        "pergunta": "Você utiliza algum auxílio para caminhar? (bengala, andador, cadeira de rodas)",
        "opcoes": ["Não uso", "Uso às vezes", "Uso sempre", "Uso cadeira de rodas"],
        "categoria": "mobilidade",
        "especialidades": {"ortopedia": 3, "fisioterapia": 2, "geriatria": 2}
    },
    {
        "id": 3,
        "pergunta": "Você consegue subir e descer escadas sem ajuda?",
        "opcoes": ["Sim, facilmente", "Sim, mas cansado", "Preciso parar no meio", "Não consigo"],
        "categoria": "mobilidade",
        "especialidades": {"cardiologia": 2, "ortopedia": 2, "geriatria": 2}
    },
    {
        "id": 4,
        "pergunta": "Você consegue se levantar de uma cadeira sem ajuda?",
        "opcoes": ["Sim, facilmente", "Com dificuldade", "Preciso de ajuda", "Não consigo"],
        "categoria": "mobilidade",
        "especialidades": {"ortopedia": 3, "geriatria": 2, "reumatologia": 1}
    },
    {
        "id": 5,
        "pergunta": "Você pratica atividade física regularmente? Com que frequência?",
        "opcoes": ["Sim, diariamente", "Sim, 3-4x semana", "Raramente", "Não pratico"],
        "categoria": "mobilidade",
        "especialidades": {"geriatria": 2, "cardiologia": 1, "fisioterapia": 1}
    },
    {
        "id": 6,
        "pergunta": "Você consegue se vestir sozinho(a)?",
        "opcoes": ["Sim, totalmente", "Com pouca ajuda", "Com muita ajuda", "Não consigo"],
        "categoria": "mobilidade",
        "especialidades": {"geriatria": 3, "fisioterapia": 2}
    },
    {
        "id": 7,
        "pergunta": "Você consegue tomar banho sozinho(a)?",
        "opcoes": ["Sim, totalmente", "Com pouca ajuda", "Com muita ajuda", "Não consigo"],
        "categoria": "mobilidade",
        "especialidades": {"geriatria": 3, "fisioterapia": 2}
    },
    {
        "id": 8,
        "pergunta": "Você consegue usar o banheiro sozinho(a)?",
        "opcoes": ["Sim, totalmente", "Com pouca ajuda", "Com muita ajuda", "Não consigo"],
        "categoria": "mobilidade",
        "especialidades": {"geriatria": 3, "urologia": 1}
    },
    {
        "id": 9,
        "pergunta": "Você sente dores frequentes? Em que região?",
        "opcoes": ["Não sinto", "Dor leve", "Dor moderada", "Dor intensa"],
        "categoria": "mobilidade",
        "especialidades": {"reumatologia": 3, "ortopedia": 2, "geriatria": 2}
    },
    {
        "id": 10,
        "pergunta": "Você tem dificuldade para pegar objetos pequenos?",
        "opcoes": ["Não", "Um pouco", "Bastante", "Muita dificuldade"],
        "categoria": "mobilidade",
        "especialidades": {"reumatologia": 2, "ortopedia": 2, "neurologia": 1}
    },
    {
        "id": 11,
        "pergunta": "Você consegue realizar suas atividades domésticas? (cozinhar, limpar)",
        "opcoes": ["Sim, todas", "Maioria delas", "Algumas apenas", "Não consigo"],
        "categoria": "mobilidade",
        "especialidades": {"geriatria": 3, "fisioterapia": 1}
    },
    {
        "id": 12,
        "pergunta": "Você sente fraqueza muscular frequentemente?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "mobilidade",
        "especialidades": {"geriatria": 2, "neurologia": 2, "endocrinologia": 1}
    },
    {
        "id": 13,
        "pergunta": "Você teve alguma fratura nos últimos 2 anos?",
        "opcoes": ["Não", "Sim, uma", "Sim, duas", "Sim, três ou mais"],
        "categoria": "mobilidade",
        "especialidades": {"ortopedia": 3, "geriatria": 2, "endocrinologia": 1}
    },
    {
        "id": 14,
        "pergunta": "Você consegue caminhar distâncias curtas sem se cansar?",
        "opcoes": ["Sim, facilmente", "Sim, mas canso", "Canso muito", "Não consigo"],
        "categoria": "mobilidade",
        "especialidades": {"cardiologia": 3, "pneumologia": 2, "geriatria": 1}
    },
    {
        "id": 15,
        "pergunta": "Você tem artrite ou artrose diagnosticada?",
        "opcoes": ["Não", "Sim, controlada", "Sim, descontrolada", "Não sei"],
        "categoria": "mobilidade",
        "especialidades": {"reumatologia": 4, "ortopedia": 2, "geriatria": 1}
    },
    {
        "id": 16,
        "pergunta": "Você consegue se agachar e levantar sem dificuldade?",
        "opcoes": ["Sim, facilmente", "Com dificuldade", "Com muita dificuldade", "Não consigo"],
        "categoria": "mobilidade",
        "especialidades": {"ortopedia": 3, "reumatologia": 2, "geriatria": 2}
    },
    {
        "id": 17,
        "pergunta": "Você sente rigidez nas articulações pela manhã?",
        "opcoes": ["Não", "Menos de 30 min", "30 min a 1 hora", "Mais de 1 hora"],
        "categoria": "mobilidade",
        "especialidades": {"reumatologia": 4, "geriatria": 1}
    },
    {
        "id": 18,
        "pergunta": "Você consegue carregar compras de supermercado?",
        "opcoes": ["Sim, sem problema", "Sim, mas pesado", "Com dificuldade", "Não consigo"],
        "categoria": "mobilidade",
        "especialidades": {"ortopedia": 2, "geriatria": 2, "fisioterapia": 1}
    },
    {
        "id": 19,
        "pergunta": "Você faz fisioterapia ou algum acompanhamento físico?",
        "opcoes": ["Sim, regularmente", "Já fiz antes", "Nunca fiz", "Preciso fazer"],
        "categoria": "mobilidade",
        "especialidades": {"fisioterapia": 3, "geriatria": 2}
    },
    {
        "id": 20,
        "pergunta": "Você sente que sua mobilidade piorou no último ano?",
        "opcoes": ["Não", "Um pouco", "Bastante", "Muito"],
        "categoria": "mobilidade",
        "especialidades": {"geriatria": 3, "ortopedia": 2, "neurologia": 1}
    },
    
    # CATEGORIA 2: COGNIÇÃO E MEMÓRIA (21-35)
    {
        "id": 21,
        "pergunta": "Você esquece compromissos ou eventos importantes com frequência?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "cognitivo",
        "especialidades": {"neurologia": 3, "geriatria": 2, "psiquiatria": 1}
    },
    {
        "id": 22,
        "pergunta": "Você tem dificuldade para lembrar nomes de pessoas conhecidas?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "cognitivo",
        "especialidades": {"neurologia": 3, "geriatria": 2}
    },
    {
        "id": 23,
        "pergunta": "Você consegue gerenciar suas finanças sozinho(a)?",
        "opcoes": ["Sim, totalmente", "Com pouca ajuda", "Com muita ajuda", "Não consigo"],
        "categoria": "cognitivo",
        "especialidades": {"neurologia": 3, "geriatria": 2}
    },
    {
        "id": 24,
        "pergunta": "Você tem dificuldade para aprender coisas novas?",
        "opcoes": ["Não", "Um pouco", "Bastante", "Muita dificuldade"],
        "categoria": "cognitivo",
        "especialidades": {"neurologia": 3, "geriatria": 2}
    },
    {
        "id": 25,
        "pergunta": "Você se perde em lugares conhecidos?",
        "opcoes": ["Nunca", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "cognitivo",
        "especialidades": {"neurologia": 4, "geriatria": 2}
    },
    {
        "id": 26,
        "pergunta": "Você tem dificuldade para encontrar palavras durante conversas?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "cognitivo",
        "especialidades": {"neurologia": 3, "geriatria": 2}
    },
    {
        "id": 27,
        "pergunta": "Você consegue lembrar o que comeu no café da manhã hoje?",
        "opcoes": ["Sim, claramente", "Sim, mas com esforço", "Não tenho certeza", "Não lembro"],
        "categoria": "cognitivo",
        "especialidades": {"neurologia": 3, "geriatria": 2}
    },
    {
        "id": 28,
        "pergunta": "Você tem dificuldade para tomar decisões do dia a dia?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "cognitivo",
        "especialidades": {"neurologia": 2, "geriatria": 2, "psiquiatria": 1}
    },
    {
        "id": 29,
        "pergunta": "Você consegue usar o telefone celular sem ajuda?",
        "opcoes": ["Sim, facilmente", "Com pouca ajuda", "Com muita ajuda", "Não consigo"],
        "categoria": "cognitivo",
        "especialidades": {"neurologia": 2, "geriatria": 2}
    },
    {
        "id": 30,
        "pergunta": "Você se sente confuso(a) frequentemente?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "cognitivo",
        "especialidades": {"neurologia": 3, "geriatria": 2}
    },
    {
        "id": 31,
        "pergunta": "Você consegue seguir instruções de receitas ou manuais?",
        "opcoes": ["Sim, facilmente", "Com dificuldade", "Com muita dificuldade", "Não consigo"],
        "categoria": "cognitivo",
        "especialidades": {"neurologia": 2, "geriatria": 2}
    },
    {
        "id": 32,
        "pergunta": "Você tem dificuldade para se concentrar?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "cognitivo",
        "especialidades": {"neurologia": 2, "psiquiatria": 2, "geriatria": 1}
    },
    {
        "id": 33,
        "pergunta": "Alguém já expressou preocupação com sua memória?",
        "opcoes": ["Não", "Uma pessoa", "Algumas pessoas", "Várias pessoas"],
        "categoria": "cognitivo",
        "especialidades": {"neurologia": 3, "geriatria": 2}
    },
    {
        "id": 34,
        "pergunta": "Você consegue lembrar datas importantes (aniversários, consultas)?",
        "opcoes": ["Sim, sempre", "Na maioria das vezes", "Às vezes", "Raramente"],
        "categoria": "cognitivo",
        "especialidades": {"neurologia": 3, "geriatria": 2}
    },
    {
        "id": 35,
        "pergunta": "Você tem dificuldade para reconhecer rostos familiares?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "cognitivo",
        "especialidades": {"neurologia": 4, "geriatria": 2}
    },
    
    # CATEGORIA 3: SAÚDE CARDIOVASCULAR (36-50)
    {
        "id": 36,
        "pergunta": "Você tem pressão alta (hipertensão)?",
        "opcoes": ["Não", "Sim, controlada", "Sim, descontrolada", "Não sei"],
        "categoria": "cardiovascular",
        "especialidades": {"cardiologia": 4, "geriatria": 1}
    },
    {
        "id": 37,
        "pergunta": "Você faz uso de medicamentos para o coração?",
        "opcoes": ["Não", "Sim, regularmente", "Sim, às vezes", "Não sei"],
        "categoria": "cardiovascular",
        "especialidades": {"cardiologia": 4, "geriatria": 2}
    },
    {
        "id": 38,
        "pergunta": "Você sente dor ou desconforto no peito?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "cardiovascular",
        "especialidades": {"cardiologia": 4, "geriatria": 1}
    },
    {
        "id": 39,
        "pergunta": "Você tem falta de ar ao fazer atividades leves?",
        "opcoes": ["Não", "Em atividades pesadas", "Em atividades moderadas", "Em atividades leves"],
        "categoria": "cardiovascular",
        "especialidades": {"cardiologia": 4, "pneumologia": 2, "geriatria": 1}
    },
    {
        "id": 40,
        "pergunta": "Você tem diabetes?",
        "opcoes": ["Não", "Sim, controlada", "Sim, descontrolada", "Não sei"],
        "categoria": "cardiovascular",
        "especialidades": {"endocrinologia": 3, "cardiologia": 2, "geriatria": 2}
    },
    {
        "id": 41,
        "pergunta": "Você monitora sua pressão arterial regularmente?",
        "opcoes": ["Sim, diariamente", "Sim, semanalmente", "Raramente", "Nunca"],
        "categoria": "cardiovascular",
        "especialidades": {"cardiologia": 2, "geriatria": 2}
    },
    {
        "id": 42,
        "pergunta": "Você já teve infarto ou AVC (derrame)?",
        "opcoes": ["Não", "Sim, infarto", "Sim, AVC", "Sim, ambos"],
        "categoria": "cardiovascular",
        "especialidades": {"cardiologia": 4, "neurologia": 3, "geriatria": 2}
    },
    {
        "id": 43,
        "pergunta": "Você tem colesterol alto?",
        "opcoes": ["Não", "Sim, controlado", "Sim, descontrolado", "Não sei"],
        "categoria": "cardiovascular",
        "especialidades": {"cardiologia": 3, "endocrinologia": 2, "geriatria": 1}
    },
    {
        "id": 44,
        "pergunta": "Você sente palpitações ou batimentos cardíacos irregulares?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "cardiovascular",
        "especialidades": {"cardiologia": 4, "geriatria": 1}
    },
    {
        "id": 45,
        "pergunta": "Você fuma ou já fumou?",
        "opcoes": ["Nunca fumei", "Já fumei, parei", "Fumo ocasionalmente", "Fumo regularmente"],
        "categoria": "cardiovascular",
        "especialidades": {"pneumologia": 3, "cardiologia": 2, "geriatria": 1}
    },
    {
        "id": 46,
        "pergunta": "Você sente inchaço nas pernas ou pés?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "cardiovascular",
        "especialidades": {"cardiologia": 3, "angiologia": 2, "geriatria": 1}
    },
    {
        "id": 47,
        "pergunta": "Você acorda à noite com falta de ar?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "cardiovascular",
        "especialidades": {"cardiologia": 4, "pneumologia": 2, "geriatria": 1}
    },
    {
        "id": 48,
        "pergunta": "Você tem histórico familiar de problemas cardíacos?",
        "opcoes": ["Não", "Sim, pais", "Sim, irmãos", "Sim, vários familiares"],
        "categoria": "cardiovascular",
        "especialidades": {"cardiologia": 2, "geriatria": 1}
    },
    {
        "id": 49,
        "pergunta": "Você consulta um cardiologista regularmente?",
        "opcoes": ["Sim, regularmente", "Sim, às vezes", "Raramente", "Nunca"],
        "categoria": "cardiovascular",
        "especialidades": {"cardiologia": 2, "geriatria": 2}
    },
    {
        "id": 50,
        "pergunta": "Você teve alguma cirurgia cardíaca?",
        "opcoes": ["Não", "Sim, há menos de 1 ano", "Sim, há 1-5 anos", "Sim, há mais de 5 anos"],
        "categoria": "cardiovascular",
        "especialidades": {"cardiologia": 4, "geriatria": 1}
    },
    
    # CATEGORIA 4: NUTRIÇÃO E ALIMENTAÇÃO (51-60)
    {
        "id": 51,
        "pergunta": "Você faz quantas refeições por dia?",
        "opcoes": ["1 ou menos", "2 refeições", "3 refeições", "4 ou mais"],
        "categoria": "nutricional",
        "especialidades": {"nutricao": 3, "geriatria": 2}
    },
    {
        "id": 52,
        "pergunta": "Você perdeu peso sem querer nos últimos 6 meses?",
        "opcoes": ["Não", "Menos de 3 kg", "De 3 a 5 kg", "Mais de 5 kg"],
        "categoria": "nutricional",
        "especialidades": {"nutricao": 3, "geriatria": 2, "gastroenterologia": 1}
    },
    {
        "id": 53,
        "pergunta": "Você tem dificuldade para mastigar ou engolir?",
        "opcoes": ["Não", "Pouca", "Moderada", "Muita dificuldade"],
        "categoria": "nutricional",
        "especialidades": {"geriatria": 2, "gastroenterologia": 2, "odontologia": 2}
    },
    {
        "id": 54,
        "pergunta": "Você tem bom apetite?",
        "opcoes": ["Sim, muito bom", "Bom", "Regular", "Ruim"],
        "categoria": "nutricional",
        "especialidades": {"nutricao": 2, "geriatria": 2}
    },
    {
        "id": 55,
        "pergunta": "Você consome frutas e verduras diariamente?",
        "opcoes": ["Sim, sempre", "Na maioria dos dias", "Às vezes", "Raramente"],
        "categoria": "nutricional",
        "especialidades": {"nutricao": 3, "geriatria": 1}
    },
    {
        "id": 56,
        "pergunta": "Você bebe água suficiente durante o dia? (pelo menos 1,5L)",
        "opcoes": ["Sim, mais de 2L", "Sim, 1,5-2L", "Menos de 1,5L", "Muito pouco"],
        "categoria": "nutricional",
        "especialidades": {"nutricao": 2, "geriatria": 2}
    },
    {
        "id": 57,
        "pergunta": "Você tem restrições alimentares ou alergias?",
        "opcoes": ["Não", "Sim, uma", "Sim, algumas", "Sim, várias"],
        "categoria": "nutricional",
        "especialidades": {"nutricao": 2, "geriatria": 1}
    },
    {
        "id": 58,
        "pergunta": "Você consegue preparar suas próprias refeições?",
        "opcoes": ["Sim, todas", "Maioria delas", "Algumas", "Não consigo"],
        "categoria": "nutricional",
        "especialidades": {"geriatria": 3, "nutricao": 1}
    },
    {
        "id": 59,
        "pergunta": "Você usa prótese dentária? Ela está bem ajustada?",
        "opcoes": ["Não uso", "Sim, bem ajustada", "Sim, mas desconfortável", "Sim, muito ruim"],
        "categoria": "nutricional",
        "especialidades": {"odontologia": 3, "geriatria": 1}
    },
    {
        "id": 60,
        "pergunta": "Você teve alteração no paladar recentemente?",
        "opcoes": ["Não", "Um pouco", "Bastante", "Muito"],
        "categoria": "nutricional",
        "especialidades": {"geriatria": 2, "neurologia": 1, "otorrinolaringologia": 1}
    },
    
    # CATEGORIA 5: SAÚDE EMOCIONAL (61-70)
    {
        "id": 61,
        "pergunta": "Você se sente triste ou desanimado(a) frequentemente?",
        "opcoes": ["Nunca", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "emocional",
        "especialidades": {"psiquiatria": 3, "geriatria": 2}
    },
    {
        "id": 62,
        "pergunta": "Você perdeu interesse em atividades que antes gostava?",
        "opcoes": ["Não", "Um pouco", "Bastante", "Completamente"],
        "categoria": "emocional",
        "especialidades": {"psiquiatria": 3, "geriatria": 2}
    },
    {
        "id": 63,
        "pergunta": "Você se sente ansioso(a) ou preocupado(a) excessivamente?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "emocional",
        "especialidades": {"psiquiatria": 3, "geriatria": 1}
    },
    {
        "id": 64,
        "pergunta": "Você tem dificuldade para dormir devido a preocupações?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "emocional",
        "especialidades": {"psiquiatria": 2, "neurologia": 1, "geriatria": 2}
    },
    {
        "id": 65,
        "pergunta": "Você se sente sozinho(a) ou isolado(a)?",
        "opcoes": ["Não", "Às vezes", "Frequentemente", "Sempre"],
        "categoria": "emocional",
        "especialidades": {"psiquiatria": 2, "geriatria": 2, "assistencia_social": 2}
    },
    {
        "id": 66,
        "pergunta": "Você já pensou que a vida não vale a pena?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "emocional",
        "especialidades": {"psiquiatria": 4, "geriatria": 2}
    },
    {
        "id": 67,
        "pergunta": "Você se sente irritado(a) com facilidade?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "emocional",
        "especialidades": {"psiquiatria": 2, "geriatria": 1}
    },
    {
        "id": 68,
        "pergunta": "Você tem medo de sair de casa?",
        "opcoes": ["Não", "Um pouco", "Bastante", "Muito medo"],
        "categoria": "emocional",
        "especialidades": {"psiquiatria": 3, "geriatria": 1}
    },
    {
        "id": 69,
        "pergunta": "Você faz acompanhamento com psicólogo ou psiquiatra?",
        "opcoes": ["Sim, regularmente", "Sim, às vezes", "Já fiz antes", "Nunca fiz"],
        "categoria": "emocional",
        "especialidades": {"psiquiatria": 2, "geriatria": 1}
    },
    {
        "id": 70,
        "pergunta": "Você se sente satisfeito(a) com sua vida?",
        "opcoes": ["Muito satisfeito", "Satisfeito", "Pouco satisfeito", "Insatisfeito"],
        "categoria": "emocional",
        "especialidades": {"psiquiatria": 2, "geriatria": 2}
    },
    
    # CATEGORIA 6: SONO E REPOUSO (71-75)
    {
        "id": 71,
        "pergunta": "Quantas horas você dorme por noite em média?",
        "opcoes": ["Mais de 7 horas", "5 a 7 horas", "3 a 5 horas", "Menos de 3 horas"],
        "categoria": "sono",
        "especialidades": {"neurologia": 2, "psiquiatria": 2, "geriatria": 2}
    },
    {
        "id": 72,
        "pergunta": "Você tem dificuldade para adormecer?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "sono",
        "especialidades": {"psiquiatria": 2, "neurologia": 2, "geriatria": 1}
    },
    {
        "id": 73,
        "pergunta": "Você acorda várias vezes durante a noite?",
        "opcoes": ["Não", "1-2 vezes", "3-4 vezes", "Mais de 4 vezes"],
        "categoria": "sono",
        "especialidades": {"neurologia": 2, "urologia": 1, "geriatria": 2}
    },
    {
        "id": 74,
        "pergunta": "Você acorda se sentindo cansado(a)?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "sono",
        "especialidades": {"neurologia": 2, "psiquiatria": 1, "geriatria": 2}
    },
    {
        "id": 75,
        "pergunta": "Você ronca ou tem apneia do sono?",
        "opcoes": ["Não", "Ronco leve", "Ronco forte", "Tenho apneia"],
        "categoria": "sono",
        "especialidades": {"otorrinolaringologia": 3, "pneumologia": 2, "geriatria": 1}
    },
    
    # CATEGORIA 7: VISÃO E AUDIÇÃO (76-80)
    {
        "id": 76,
        "pergunta": "Você tem dificuldade para enxergar? Usa óculos?",
        "opcoes": ["Não tenho dificuldade", "Uso óculos, enxergo bem", "Uso óculos, ainda tenho dificuldade", "Muita dificuldade"],
        "categoria": "visao",
        "especialidades": {"oftalmologia": 3, "geriatria": 1}
    },
    {
        "id": 77,
        "pergunta": "Você tem dificuldade para ouvir conversas?",
        "opcoes": ["Não", "Pouca", "Moderada", "Muita dificuldade"],
        "categoria": "audicao",
        "especialidades": {"otorrinolaringologia": 3, "geriatria": 1}
    },
    {
        "id": 78,
        "pergunta": "Você usa aparelho auditivo?",
        "opcoes": ["Não preciso", "Preciso mas não uso", "Sim, às vezes", "Sim, sempre"],
        "categoria": "audicao",
        "especialidades": {"otorrinolaringologia": 3, "geriatria": 1}
    },
    {
        "id": 79,
        "pergunta": "Você faz exames de vista regularmente?",
        "opcoes": ["Sim, anualmente", "A cada 2 anos", "Raramente", "Nunca"],
        "categoria": "visao",
        "especialidades": {"oftalmologia": 2, "geriatria": 1}
    },
    {
        "id": 80,
        "pergunta": "Você tem zumbido nos ouvidos?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "audicao",
        "especialidades": {"otorrinolaringologia": 3, "neurologia": 1, "geriatria": 1}
    },
    
    # CATEGORIA 8: QUEDAS E EQUILÍBRIO (81-85)
    {
        "id": 81,
        "pergunta": "Você caiu alguma vez nos últimos 6 meses?",
        "opcoes": ["Não", "Uma vez", "Duas vezes", "Três ou mais"],
        "categoria": "quedas",
        "especialidades": {"ortopedia": 2, "neurologia": 2, "geriatria": 3}
    },
    {
        "id": 82,
        "pergunta": "Você tem medo de cair?",
        "opcoes": ["Não", "Um pouco", "Bastante", "Muito medo"],
        "categoria": "quedas",
        "especialidades": {"geriatria": 3, "fisioterapia": 2}
    },
    {
        "id": 83,
        "pergunta": "Você sente tonturas ou vertigens?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "equilibrio",
        "especialidades": {"otorrinolaringologia": 3, "neurologia": 2, "geriatria": 1}
    },
    {
        "id": 84,
        "pergunta": "Você tem dificuldade para manter o equilíbrio?",
        "opcoes": ["Não", "Pouca", "Moderada", "Muita dificuldade"],
        "categoria": "equilibrio",
        "especialidades": {"neurologia": 2, "otorrinolaringologia": 2, "geriatria": 2}
    },
    {
        "id": 85,
        "pergunta": "Sua casa está adaptada para evitar quedas? (tapetes seguros, iluminação adequada)",
        "opcoes": ["Sim, totalmente", "Parcialmente", "Pouco adaptada", "Não está adaptada"],
        "categoria": "quedas",
        "especialidades": {"geriatria": 2, "fisioterapia": 1}
    },
    
    # CATEGORIA 9: MEDICAMENTOS (86-90)
    {
        "id": 86,
        "pergunta": "Quantos medicamentos você toma por dia?",
        "opcoes": ["Nenhum", "1 a 3", "4 a 6", "Mais de 6"],
        "categoria": "medicamentos",
        "especialidades": {"geriatria": 3, "farmacia_clinica": 2}
    },
    {
        "id": 87,
        "pergunta": "Você toma seus medicamentos nos horários corretos?",
        "opcoes": ["Sim, sempre", "Na maioria das vezes", "Às vezes", "Raramente"],
        "categoria": "medicamentos",
        "especialidades": {"geriatria": 2, "farmacia_clinica": 2}
    },
    {
        "id": 88,
        "pergunta": "Você tem dificuldade para lembrar de tomar os medicamentos?",
        "opcoes": ["Não", "Raramente", "Às vezes", "Frequentemente"],
        "categoria": "medicamentos",
        "especialidades": {"geriatria": 2, "neurologia": 1}
    },
    {
        "id": 89,
        "pergunta": "Você já teve efeitos colaterais de medicamentos?",
        "opcoes": ["Não", "Sim, leves", "Sim, moderados", "Sim, graves"],
        "categoria": "medicamentos",
        "especialidades": {"geriatria": 3, "farmacia_clinica": 2}
    },
    {
        "id": 90,
        "pergunta": "Você usa algum sistema de organização de medicamentos?",
        "opcoes": ["Sim, sempre", "Às vezes", "Raramente", "Não uso"],
        "categoria": "medicamentos",
        "especialidades": {"geriatria": 2, "farmacia_clinica": 1}
    },
    
    # CATEGORIA 10: SOCIAL E FAMILIAR (91-100)
    {
        "id": 91,
        "pergunta": "Você mora sozinho(a) ou com alguém?",
        "opcoes": ["Sozinho", "Com cônjuge", "Com família", "Casa de repouso"],
        "categoria": "social",
        "especialidades": {"geriatria": 2, "assistencia_social": 2}
    },
    {
        "id": 92,
        "pergunta": "Você tem filhos? Quantos?",
        "opcoes": ["Não tenho", "1 ou 2", "3 ou 4", "5 ou mais"],
        "categoria": "social",
        "especialidades": {"geriatria": 1}
    },
    {
        "id": 93,
        "pergunta": "Com que frequência você recebe visitas de familiares ou amigos?",
        "opcoes": ["Diariamente", "Semanalmente", "Mensalmente", "Raramente"],
        "categoria": "social",
        "especialidades": {"geriatria": 2, "assistencia_social": 1}
    },
    {
        "id": 94,
        "pergunta": "Você participa de atividades sociais ou grupos? (igreja, clube, etc)",
        "opcoes": ["Sim, regularmente", "Sim, às vezes", "Raramente", "Não participo"],
        "categoria": "social",
        "especialidades": {"geriatria": 2, "psiquiatria": 1}
    },
    {
        "id": 95,
        "pergunta": "Você se sente apoiado(a) pela sua família?",
        "opcoes": ["Sim, muito", "Sim, razoavelmente", "Pouco", "Não me sinto apoiado"],
        "categoria": "social",
        "especialidades": {"geriatria": 2, "psiquiatria": 1, "assistencia_social": 1}
    },
    {
        "id": 96,
        "pergunta": "Você tem alguém para ajudá-lo(a) em caso de emergência?",
        "opcoes": ["Sim, sempre disponível", "Sim, geralmente", "Às vezes", "Não tenho"],
        "categoria": "social",
        "especialidades": {"geriatria": 2, "assistencia_social": 2}
    },
    {
        "id": 97,
        "pergunta": "Você consegue sair de casa sozinho(a)?",
        "opcoes": ["Sim, facilmente", "Sim, com esforço", "Com ajuda", "Não consigo"],
        "categoria": "social",
        "especialidades": {"geriatria": 3, "ortopedia": 1}
    },
    {
        "id": 98,
        "pergunta": "Você usa transporte público ou precisa de ajuda para se locomover?",
        "opcoes": ["Uso transporte público", "Alguém me leva", "Táxi/aplicativo", "Não saio"],
        "categoria": "social",
        "especialidades": {"geriatria": 2, "assistencia_social": 1}
    },
    {
        "id": 99,
        "pergunta": "Você se sente útil e valorizado(a)?",
        "opcoes": ["Sim, muito", "Sim, razoavelmente", "Pouco", "Não me sinto"],
        "categoria": "social",
        "especialidades": {"psiquiatria": 2, "geriatria": 2}
    },
    {
        "id": 100,
        "pergunta": "Você gostaria de participar de mais atividades sociais?",
        "opcoes": ["Sim, muito", "Sim, um pouco", "Talvez", "Não"],
        "categoria": "social",
        "especialidades": {"geriatria": 1, "assistencia_social": 1}
    }
]


def get_perguntas_gratuitas(num_perguntas: int = 10, idade: int = 65, sexo: str = "ambos") -> List[Dict]:
    """
    Seleciona perguntas do banco de 100 perguntas reais do PDF
    
    Args:
        num_perguntas: Quantidade desejada (padrão 10)
        idade: Idade do paciente (não usado aqui, mas mantido para compatibilidade)
        sexo: Sexo do paciente (não usado aqui, mas mantido para compatibilidade)
    """
    print(f"\n🔍 Selecionando {num_perguntas} perguntas do banco de 100...")
    print(f"👤 Perfil: {idade} anos, sexo {sexo}\n")
    
    # Embaralhar perguntas para variedade
    perguntas_disponiveis = BANCO_100_PERGUNTAS.copy()
    random.shuffle(perguntas_disponiveis)
    
    # Garantir variedade de categorias
    perguntas_selecionadas = []
    categorias_usadas = set()
    
    # Primeira passada: 1 pergunta por categoria diferente
    for pergunta in perguntas_disponiveis:
        if len(perguntas_selecionadas) >= num_perguntas:
            break
        
        if pergunta["categoria"] not in categorias_usadas:
            perguntas_selecionadas.append(pergunta.copy())
            categorias_usadas.add(pergunta["categoria"])
            print(f"⏳ [{len(perguntas_selecionadas)}/{num_perguntas}] {pergunta['categoria']}")
            print(f"   ✅ {pergunta['pergunta'][:60]}...")
    
    # Segunda passada: completar se necessário
    if len(perguntas_selecionadas) < num_perguntas:
        for pergunta in perguntas_disponiveis:
            if len(perguntas_selecionadas) >= num_perguntas:
                break
            
            if pergunta not in perguntas_selecionadas:
                perguntas_selecionadas.append(pergunta.copy())
                print(f"⏳ [{len(perguntas_selecionadas)}/{num_perguntas}] {pergunta['categoria']}")
                print(f"   ✅ {pergunta['pergunta'][:60]}...")
    
    print(f"\n✨ {len(perguntas_selecionadas)} perguntas prontas!\n")
    
    return perguntas_selecionadas[:num_perguntas]