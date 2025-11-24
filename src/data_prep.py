# src/data_prep.py
"""
MÓDULO DE PREPARAÇÃO DE DADOS
Responsável: [Nome do Engenheiro de Dados]
"""

import numpy as np
import pandas as pd
from typing import Tuple

def gerar_dados_sinteticos(n_amostras: int = 1000, seed: int = 42) -> Tuple[np.ndarray, np.ndarray]:
    """
    Gera dados sintéticos de pacientes idosos
    
    Returns:
        X: Features (n_amostras, 100)
        y: Labels (n_amostras,)
    """
    np.random.seed(seed)
    
    X = []
    y = []
    
    # Perfis clínicos
    perfis = [
        (0.15, [21, 36], 2, "Cognitivo → Neurologia"),
        (0.30, [36, 51], 1, "Cardíaco → Cardiologia"),
        (0.45, [0, 20], 3, "Mobilidade → Ortopedia"),
        (0.60, [61, 71], 4, "Emocional → Psiquiatria"),
        (0.75, [51, 61], 5, "Nutricional → Nutrição"),
        (1.00, None, 0, "Saudável → Geriatria")
    ]
    
    for _ in range(n_amostras):
        rand = np.random.random()
        features = np.random.choice([1, 2], size=100)
        
        for prob, intervalo, label, desc in perfis:
            if rand < prob:
                if intervalo:
                    features[intervalo[0]:intervalo[1]] = np.random.choice([2, 3], size=intervalo[1]-intervalo[0])
                else:
                    features = np.random.choice([0, 1], size=100)
                y.append(label)
                break
        
        X.append(features)
    
    return np.array(X, dtype=np.float32), np.array(y, dtype=np.int32)

def preprocessar_respostas(respostas: dict) -> np.ndarray:
    """Converte respostas do questionário para vetor de features"""
    features = np.zeros(100, dtype=np.float32)
    
    for id_pergunta, indice_resposta in respostas.items():
        if 1 <= id_pergunta <= 100:
            features[id_pergunta - 1] = indice_resposta
    
    return features.reshape(1, -1)