#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CONECTA 60+ - GERAÇÃO DE GRÁFICOS E MÉTRICAS
Arquivo standalone - gera os 5 gráficos obrigatórios para o TCC
"""

print("=" * 60)
print("📊 CONECTA 60+ - AVALIAÇÃO E GRÁFICOS")
print("=" * 60)

# =============================================================================
# IMPORTS
# =============================================================================
print("\n📦 Carregando bibliotecas...")

try:
    import os
    import sys
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
    from sklearn.preprocessing import label_binarize
    from sklearn.model_selection import learning_curve, train_test_split
    import joblib
    print("✅ Bibliotecas carregadas!")
except ImportError as e:
    print(f"❌ ERRO: Falta instalar biblioteca: {e}")
    print("\n💡 Execute: pip install matplotlib seaborn scikit-learn pandas numpy joblib")
    sys.exit(1)

# =============================================================================
# CONFIGURAÇÕES
# =============================================================================
SEED = 42
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

# Estilo dos gráficos
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# =============================================================================
# GERAÇÃO DE DADOS (mesmo do train.py)
# =============================================================================
def gerar_dados_sinteticos(n_amostras=1000):
    """Gera dados sintéticos para avaliação"""
    print(f"\n📊 Gerando {n_amostras} amostras para avaliação...")
    
    np.random.seed(SEED)
    X = []
    y = []
    
    for _ in range(n_amostras):
        rand = np.random.random()
        features = np.random.choice([1, 2], size=100)
        
        if rand < 0.15:
            features[21:36] = np.random.choice([2, 3], size=15)
            y.append(2)
        elif rand < 0.30:
            features[36:51] = np.random.choice([2, 3], size=15)
            y.append(1)
        elif rand < 0.45:
            features[0:20] = np.random.choice([2, 3], size=20)
            y.append(3)
        elif rand < 0.60:
            features[61:71] = np.random.choice([2, 3], size=10)
            y.append(4)
        elif rand < 0.75:
            features[51:61] = np.random.choice([2, 3], size=10)
            y.append(5)
        else:
            features = np.random.choice([0, 1], size=100)
            y.append(0)
        
        X.append(features)
    
    return np.array(X, dtype=np.float32), np.array(y, dtype=np.int32)

# =============================================================================
# GRÁFICO 1: MATRIZ DE CONFUSÃO
# =============================================================================
def gerar_confusion_matrix(y_test, y_pred, classes):
    """Gera matriz de confusão"""
    print("\n📊 [1/5] Gerando Matriz de Confusão...")
    
    plt.figure(figsize=(12, 10))
    cm = confusion_matrix(y_test, y_pred)
    
    # Normalizar para percentuais
    cm_percent = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100
    
    # Criar heatmap
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=classes, yticklabels=classes,
                cbar_kws={'label': 'Quantidade'})
    
    plt.title('Matriz de Confusão\n(Predição do Modelo Random Forest)', 
              fontsize=16, fontweight='bold', pad=20)
    plt.ylabel('Classe Real', fontsize=12, fontweight='bold')
    plt.xlabel('Classe Predita', fontsize=12, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    
    os.makedirs("reports/figures", exist_ok=True)
    plt.savefig('reports/figures/confusion_matrix.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("   ✅ confusion_matrix.png salvo")

# =============================================================================
# GRÁFICO 2: IMPORTÂNCIA DE FEATURES
# =============================================================================
def gerar_feature_importance(modelo):
    """Gera gráfico de importância das features"""
    print("\n📊 [2/5] Gerando Importância de Features...")
    
    plt.figure(figsize=(12, 8))
    
    importances = modelo.feature_importances_
    indices = np.argsort(importances)[-20:]  # Top 20
    
    # Criar labels das perguntas
    labels = [f'Pergunta {i+1}' for i in indices]
    
    # Gráfico de barras horizontal
    colors = plt.cm.viridis(np.linspace(0.3, 0.9, len(indices)))
    plt.barh(range(len(indices)), importances[indices], color=colors, edgecolor='black')
    plt.yticks(range(len(indices)), labels)
    plt.xlabel('Importância', fontsize=12, fontweight='bold')
    plt.title('Top 20 Perguntas Mais Importantes\n(Feature Importance - Random Forest)', 
              fontsize=16, fontweight='bold', pad=20)
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    
    plt.savefig('reports/figures/feature_importance.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("   ✅ feature_importance.png salvo")

# =============================================================================
# GRÁFICO 3: CURVAS ROC
# =============================================================================
def gerar_roc_curves(y_test, y_proba, classes):
    """Gera curvas ROC para cada classe"""
    print("\n📊 [3/5] Gerando Curvas ROC...")
    
    plt.figure(figsize=(12, 8))
    
    # Binarizar classes para ROC multiclasse
    y_test_bin = label_binarize(y_test, classes=list(range(len(classes))))
    
    # Calcular ROC para cada classe
    for i in range(min(6, len(classes))):  # Top 6 classes
        fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_proba[:, i])
        roc_auc = auc(fpr, tpr)
        
        plt.plot(fpr, tpr, lw=2, 
                label=f'{classes[i]} (AUC = {roc_auc:.2f})')
    
    # Linha diagonal (classificador aleatório)
    plt.plot([0, 1], [0, 1], 'k--', lw=2, label='Classificador Aleatório (AUC = 0.50)')
    
    plt.xlabel('Taxa de Falsos Positivos', fontsize=12, fontweight='bold')
    plt.ylabel('Taxa de Verdadeiros Positivos', fontsize=12, fontweight='bold')
    plt.title('Curvas ROC por Especialidade\n(Receiver Operating Characteristic)', 
              fontsize=16, fontweight='bold', pad=20)
    plt.legend(loc='lower right', fontsize=10)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    
    plt.savefig('reports/figures/roc_curves.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("   ✅ roc_curves.png salvo")

# =============================================================================
# GRÁFICO 4: CURVA DE APRENDIZADO
# =============================================================================
def gerar_learning_curve(modelo, X, y):
    """Gera curva de aprendizado"""
    print("\n📊 [4/5] Gerando Curva de Aprendizado...")
    print("   (Pode demorar alguns segundos...)")
    
    plt.figure(figsize=(12, 8))
    
    # Calcular curva de aprendizado
    train_sizes = np.linspace(0.1, 1.0, 10)
    train_sizes_abs, train_scores, val_scores = learning_curve(
        modelo, X, y, 
        cv=5, 
        n_jobs=-1,
        train_sizes=train_sizes,
        random_state=SEED,
        scoring='accuracy'
    )
    
    # Calcular médias e desvios
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    val_mean = np.mean(val_scores, axis=1)
    val_std = np.std(val_scores, axis=1)
    
    # Plot
    plt.plot(train_sizes_abs, train_mean, 'o-', color='#2E86AB', 
            label='Acurácia Treino', linewidth=2, markersize=8)
    plt.fill_between(train_sizes_abs, 
                     train_mean - train_std, 
                     train_mean + train_std, 
                     alpha=0.15, color='#2E86AB')
    
    plt.plot(train_sizes_abs, val_mean, 's-', color='#A23B72',
            label='Acurácia Validação', linewidth=2, markersize=8)
    plt.fill_between(train_sizes_abs,
                     val_mean - val_std,
                     val_mean + val_std,
                     alpha=0.15, color='#A23B72')
    
    plt.xlabel('Número de Amostras de Treino', fontsize=12, fontweight='bold')
    plt.ylabel('Acurácia', fontsize=12, fontweight='bold')
    plt.title('Curva de Aprendizado\n(Convergência do Modelo)', 
              fontsize=16, fontweight='bold', pad=20)
    plt.legend(loc='lower right', fontsize=12)
    plt.grid(alpha=0.3)
    plt.ylim([0.7, 1.01])
    plt.tight_layout()
    
    plt.savefig('reports/figures/learning_curve.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("   ✅ learning_curve.png salvo")

# =============================================================================
# GRÁFICO 5: DISTRIBUIÇÃO DE CLASSES
# =============================================================================
def gerar_class_distribution(y, classes):
    """Gera gráfico de distribuição de classes"""
    print("\n📊 [5/5] Gerando Distribuição de Classes...")
    
    plt.figure(figsize=(12, 8))
    
    unique, counts = np.unique(y, return_counts=True)
    percentages = counts / len(y) * 100
    
    # Criar gráfico de barras
    colors = plt.cm.Set3(np.linspace(0, 1, len(unique)))
    bars = plt.bar([classes[i] for i in unique], counts, 
                   color=colors, edgecolor='black', linewidth=1.5)
    
    # Adicionar valores nas barras
    for i, (bar, count, pct) in enumerate(zip(bars, counts, percentages)):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{count}\n({pct:.1f}%)',
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    plt.xlabel('Especialidade', fontsize=12, fontweight='bold')
    plt.ylabel('Quantidade de Amostras', fontsize=12, fontweight='bold')
    plt.title('Distribuição de Classes no Dataset\n(Balanceamento dos Dados)', 
              fontsize=16, fontweight='bold', pad=20)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    
    plt.savefig('reports/figures/class_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("   ✅ class_distribution.png salvo")

# =============================================================================
# TABELA DE MÉTRICAS
# =============================================================================
def gerar_tabela_metricas(y_test, y_pred, classes):
    """Gera tabela CSV com métricas detalhadas"""
    print("\n📊 Gerando tabela de métricas...")
    
    # Classification report
    report = classification_report(y_test, y_pred, 
                                   target_names=classes,
                                   output_dict=True)
    
    # Converter para DataFrame
    df = pd.DataFrame(report).transpose()
    
    # Salvar
    os.makedirs("reports/tables", exist_ok=True)
    df.to_csv('reports/tables/classification_report.csv')
    
    print("   ✅ classification_report.csv salvo")
    
    # Mostrar resumo
    print("\n📋 Resumo das Métricas:")
    print(f"   Acurácia: {report['accuracy']:.4f} ({report['accuracy']*100:.2f}%)")
    print(f"   F1-Score (macro): {report['macro avg']['f1-score']:.4f}")
    print(f"   Precisão (macro): {report['macro avg']['precision']:.4f}")
    print(f"   Recall (macro): {report['macro avg']['recall']:.4f}")

# =============================================================================
# MAIN - PIPELINE COMPLETO
# =============================================================================
def gerar_todos_graficos():
    """Pipeline completo de geração de gráficos"""
    
    # 1. Verificar se modelo existe
    if not os.path.exists("models/classificador.pkl"):
        print("\n❌ ERRO: Modelo não encontrado!")
        print("   Execute primeiro: python src/train.py")
        return False
    
    # 2. Carregar modelo
    print("\n📂 Carregando modelo treinado...")
    modelo = joblib.load("models/classificador.pkl")
    scaler = joblib.load("models/scaler.pkl")
    print("   ✅ Modelo carregado")
    
    # 3. Gerar dados
    X, y = gerar_dados_sinteticos(1000)
    
    # 4. Split e predição
    print("\n🔀 Preparando dados de teste...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=SEED, stratify=y
    )
    
    X_test_scaled = scaler.transform(X_test)
    y_pred = modelo.predict(X_test_scaled)
    y_proba = modelo.predict_proba(X_test_scaled)
    
    X_scaled = scaler.transform(X)
    
    # 5. Nomes das classes
    classes_usadas = sorted(set(y))
    nomes_classes = [ESPECIALIDADES[i] for i in classes_usadas]
    
    print(f"   Classes encontradas: {len(classes_usadas)}")
    print("   ✅ Dados preparados")
    
    # 6. Gerar os 5 gráficos
    print("\n" + "=" * 60)
    print("🎨 GERANDO OS 5 GRÁFICOS OBRIGATÓRIOS")
    print("=" * 60)
    
    gerar_confusion_matrix(y_test, y_pred, nomes_classes)
    gerar_feature_importance(modelo)
    gerar_roc_curves(y_test, y_proba, nomes_classes)
    gerar_learning_curve(modelo, X_scaled, y)
    gerar_class_distribution(y, nomes_classes)
    
    # 7. Gerar tabela de métricas
    gerar_tabela_metricas(y_test, y_pred, nomes_classes)
    
    # Resumo final
    print("\n" + "=" * 60)
    print("✅ TODOS OS GRÁFICOS GERADOS COM SUCESSO!")
    print("=" * 60)
    print("\n📁 Arquivos criados:")
    print("   reports/figures/")
    print("   ├── confusion_matrix.png")
    print("   ├── feature_importance.png")
    print("   ├── roc_curves.png")
    print("   ├── learning_curve.png")
    print("   └── class_distribution.png")
    print("\n   reports/tables/")
    print("   └── classification_report.csv")
    
    print("\n🎯 Próximo passo:")
    print("   streamlit run src/main.py")
    
    return True

# =============================================================================
# EXECUÇÃO
# =============================================================================
if __name__ == "__main__":
    try:
        sucesso = gerar_todos_graficos()
        sys.exit(0 if sucesso else 1)
    
    except KeyboardInterrupt:
        print("\n\n⚠️ Geração interrompida pelo usuário")
        sys.exit(1)
    
    except Exception as e:
        print(f"\n❌ ERRO DURANTE GERAÇÃO:")
        print(f"   Tipo: {type(e).__name__}")
        print(f"   Mensagem: {e}")
        print("\n📋 Traceback completo:")
        import traceback
        traceback.print_exc()
        sys.exit(1)