#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CONECTA 60+ - TREINAMENTO DO MODELO ML
Arquivo standalone - não depende de outros módulos
"""

print("=" * 60)
print("🤖 CONECTA 60+ - TREINAMENTO ML")
print("=" * 60)

# =============================================================================
# IMPORTS
# =============================================================================
print("\n📦 Carregando bibliotecas...")

try:
    import sys
    import os
    import numpy as np
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split, cross_val_score
    import joblib
    import json
    print("✅ Todas as bibliotecas carregadas!")
except ImportError as e:
    print(f"❌ ERRO: Falta instalar biblioteca: {e}")
    print("\n💡 Execute: pip install scikit-learn joblib numpy")
    sys.exit(1)

# =============================================================================
# CONFIGURAÇÕES
# =============================================================================
SEED = 42
N_AMOSTRAS = 1000
TEST_SIZE = 0.2

ESPECIALIDADES = {
    0: "geriatria",
    1: "cardiologia",
    2: "neurologia",
    3: "ortopedia",
    4: "psiquiatria",
    5: "nutricao",
    6: "urologia",
    7: "oftalmologia",
    8: "otorrinolaringologia"
}

# =============================================================================
# GERAÇÃO DE DADOS SINTÉTICOS
# =============================================================================
def gerar_dados_sinteticos():
    """
    Gera dados sintéticos de pacientes idosos
    
    Simula 6 perfis clínicos:
    1. Cognitivo (Neurologia)
    2. Cardíaco (Cardiologia)
    3. Mobilidade (Ortopedia)
    4. Emocional (Psiquiatria)
    5. Nutricional (Nutrição)
    6. Saudável (Geriatria)
    """
    print(f"\n📊 Gerando {N_AMOSTRAS} amostras sintéticas...")
    
    np.random.seed(SEED)
    X = []
    y = []
    
    for i in range(N_AMOSTRAS):
        # Valor aleatório para decidir perfil
        rand = np.random.random()
        
        # Features base (respostas das 100 perguntas)
        # Valores 0-3 (índice da resposta escolhida)
        features = np.random.choice([1, 2], size=100)
        
        # PERFIL 1: Problemas cognitivos → Neurologia (15%)
        if rand < 0.15:
            # Perguntas 21-35 são sobre cognição
            # Respostas ruins (índice 2-3)
            features[21:36] = np.random.choice([2, 3], size=15)
            y.append(2)  # neurologia
        
        # PERFIL 2: Problemas cardíacos → Cardiologia (15%)
        elif rand < 0.30:
            # Perguntas 36-50 são sobre coração
            features[36:51] = np.random.choice([2, 3], size=15)
            y.append(1)  # cardiologia
        
        # PERFIL 3: Problemas de mobilidade → Ortopedia (15%)
        elif rand < 0.45:
            # Perguntas 1-20 são sobre mobilidade
            features[0:20] = np.random.choice([2, 3], size=20)
            y.append(3)  # ortopedia
        
        # PERFIL 4: Problemas emocionais → Psiquiatria (15%)
        elif rand < 0.60:
            # Perguntas 61-70 são sobre emoção
            features[61:71] = np.random.choice([2, 3], size=10)
            y.append(4)  # psiquiatria
        
        # PERFIL 5: Problemas nutricionais → Nutrição (15%)
        elif rand < 0.75:
            # Perguntas 51-60 são sobre nutrição
            features[51:61] = np.random.choice([2, 3], size=10)
            y.append(5)  # nutricao
        
        # PERFIL 6: Saudável → Geriatria (25%)
        else:
            # Respostas boas (índice 0-1)
            features = np.random.choice([0, 1], size=100)
            y.append(0)  # geriatria
        
        X.append(features)
        
        # Progress
        if (i + 1) % 200 == 0:
            print(f"   Progresso: {i+1}/{N_AMOSTRAS} amostras")
    
    X = np.array(X, dtype=np.float32)
    y = np.array(y, dtype=np.int32)
    
    print(f"✅ Dados gerados com sucesso!")
    print(f"   X shape: {X.shape}")
    print(f"   y shape: {y.shape}")
    print(f"   Classes únicas: {sorted(set(y))}")
    
    return X, y

# =============================================================================
# TREINAMENTO
# =============================================================================
def treinar():
    """Pipeline completo de treinamento"""
    
    # ETAPA 1: Gerar dados
    X, y = gerar_dados_sinteticos()
    
    # ETAPA 2: Split treino/teste
    print(f"\n🔀 Dividindo dados (treino {int((1-TEST_SIZE)*100)}% / teste {int(TEST_SIZE*100)}%)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, 
        test_size=TEST_SIZE, 
        random_state=SEED, 
        stratify=y
    )
    print(f"   Treino: {len(X_train)} amostras")
    print(f"   Teste: {len(X_test)} amostras")
    
    # ETAPA 3: Normalização
    print("\n🔄 Normalizando features (StandardScaler)...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    print("   ✅ Features normalizadas (média=0, std=1)")
    
    # ETAPA 4: Treinamento do Random Forest
    print("\n🌲 Treinando Random Forest Classifier...")
    print("   Hiperparâmetros:")
    print("   - n_estimators: 100 árvores")
    print("   - max_depth: 10 níveis")
    print("   - min_samples_split: 5")
    print("   - min_samples_leaf: 2")
    print("   - random_state: 42")
    
    modelo = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=SEED,
        n_jobs=-1,
        verbose=0
    )
    
    modelo.fit(X_train_scaled, y_train)
    print("   ✅ Modelo treinado!")
    
    # ETAPA 5: Avaliação
    print("\n📈 Avaliando modelo...")
    train_acc = modelo.score(X_train_scaled, y_train)
    test_acc = modelo.score(X_test_scaled, y_test)
    
    print(f"   📊 Acurácia Treino: {train_acc:.4f} ({train_acc*100:.2f}%)")
    print(f"   📊 Acurácia Teste:  {test_acc:.4f} ({test_acc*100:.2f}%)")
    
    # ETAPA 6: Cross-validation
    print("\n🔄 Validação cruzada (5-fold)...")
    try:
        cv_scores = cross_val_score(
            modelo, X_train_scaled, y_train, 
            cv=5, 
            scoring='accuracy',
            n_jobs=-1
        )
        print(f"   📊 Scores por fold: {[f'{s:.3f}' for s in cv_scores]}")
        print(f"   📊 CV Média: {cv_scores.mean():.4f} ({cv_scores.mean()*100:.2f}%)")
        print(f"   📊 CV Desvio: ±{cv_scores.std():.4f} ({cv_scores.std()*100:.2f}%)")
        cv_mean = float(cv_scores.mean())
        cv_std = float(cv_scores.std())
    except Exception as e:
        print(f"   ⚠️ CV não executado: {e}")
        cv_mean = 0.0
        cv_std = 0.0
    
    # ETAPA 7: Feature Importance
    print("\n🔝 Top 10 features mais importantes:")
    importances = modelo.feature_importances_
    indices = np.argsort(importances)[-10:][::-1]
    for i, idx in enumerate(indices, 1):
        print(f"   {i}. Pergunta {idx+1}: {importances[idx]:.4f}")
    
    # ETAPA 8: Salvar modelo
    print("\n💾 Salvando modelo e artefatos...")
    os.makedirs("models", exist_ok=True)
    
    # Salvar modelo
    joblib.dump(modelo, "models/classificador.pkl")
    print("   ✅ models/classificador.pkl")
    
    # Salvar scaler
    joblib.dump(scaler, "models/scaler.pkl")
    print("   ✅ models/scaler.pkl")
    
    # Salvar metadados
    metadata = {
        "versao": "1.0",
        "data_treinamento": "2025-01-XX",
        "modelo": "RandomForestClassifier",
        "hiperparametros": {
            "n_estimators": 100,
            "max_depth": 10,
            "min_samples_split": 5,
            "min_samples_leaf": 2,
            "random_state": SEED
        },
        "metricas": {
            "train_accuracy": float(train_acc),
            "test_accuracy": float(test_acc),
            "cv_mean": cv_mean,
            "cv_std": cv_std
        },
        "dados": {
            "n_samples_total": int(len(X)),
            "n_samples_train": int(len(X_train)),
            "n_samples_test": int(len(X_test)),
            "n_features": int(X.shape[1])
        },
        "classes": ESPECIALIDADES
    }
    
    with open("models/metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    print("   ✅ models/metadata.json")
    
    # Resumo final
    print("\n" + "=" * 60)
    print("✅ TREINAMENTO CONCLUÍDO COM SUCESSO!")
    print("=" * 60)
    print(f"\n📁 Arquivos criados em: models/")
    print(f"   - classificador.pkl ({os.path.getsize('models/classificador.pkl')/1024:.1f} KB)")
    print(f"   - scaler.pkl ({os.path.getsize('models/scaler.pkl')/1024:.1f} KB)")
    print(f"   - metadata.json")
    
    print(f"\n🎯 Métricas finais:")
    print(f"   - Acurácia Teste: {test_acc*100:.2f}%")
    print(f"   - CV Média: {cv_mean*100:.2f}% (±{cv_std*100:.2f}%)")
    
    print(f"\n📊 Próximo passo:")
    print(f"   python src/evaluate.py  (gerar 5 gráficos)")
    print(f"   streamlit run src/main.py  (testar aplicação)")
    
    return True

# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    print(f"\n🐍 Python {sys.version}")
    print(f"📂 Diretório: {os.getcwd()}")
    
    try:
        sucesso = treinar()
        if sucesso:
            sys.exit(0)
        else:
            sys.exit(1)
    
    except KeyboardInterrupt:
        print("\n\n⚠️ Treinamento interrompido pelo usuário")
        sys.exit(1)
    
    except Exception as e:
        print(f"\n❌ ERRO DURANTE TREINAMENTO:")
        print(f"   Tipo: {type(e).__name__}")
        print(f"   Mensagem: {e}")
        print("\n📋 Traceback completo:")
        import traceback
        traceback.print_exc()
        sys.exit(1)