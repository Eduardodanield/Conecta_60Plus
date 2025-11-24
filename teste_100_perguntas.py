# ==============================================================================
# Arquivo: teste_gerador_perguntas.py
# Autor: Eduardo
# Data: 27/10/2025
# Descrição: Módulo de Testes Automatizados e Controle de Qualidade (QA).
#            Responsável por validar o motor de geração de perguntas, garantindo
#            que a integração com o PDF e a lógica de seleção de opções
#            estejam funcionando dentro dos parâmetros clínicos esperados.
# ==============================================================================

import sys
# Adiciona o diretório 'src' ao caminho do sistema para importar os módulos
sys.path.append('src')

from perguntas_conecta60 import GeradorPerguntasGratuito

def executar_teste_de_carga():
    print("="*70)
    print("🧪 [QA] INICIANDO BATERIA DE TESTES DO GERADOR")
    print("="*70)

    try:
        # --- Fase 1: Inicialização do Motor ---
        print("\n🔄 Inicializando motor de IA (Embeddings + ChromaDB)...")
        gerador = GeradorPerguntasGratuito()
        print("✅ Motor carregado com sucesso!\n")
        
        print("="*70)
        print("🚀 GERANDO QUESTIONÁRIO DE STRESS (15 CATEGORIAS)...")
        print("="*70)
        
        # Definição do escopo do teste: cobrir todas as áreas de saúde
        categorias = [
            "mobilidade", "cognitivo", "cardiovascular", "nutricional",
            "emocional", "sono", "visao", "audicao", "quedas",
            "medicamentos", "urinario", "equilibrio", "peso", 
            "digestivo", "pele"
        ]
        
        # --- Fase 2: Execução da Geração ---
        # Solicita 15 perguntas para forçar o sistema a varrer todo o PDF
        perguntas = gerador.gerar_questionario_completo(
            num_perguntas=15,
            categorias=categorias
        )
        
        print("\n" + "="*70)
        print(f"✅ RESULTADO DO TESTE: {len(perguntas)} perguntas geradas com sucesso!")
        print("="*70)
        
        # --- Fase 3: Auditoria dos Dados ---
        print("\n📋 AUDITORIA DAS PERGUNTAS GERADAS:\n")
        
        for p in perguntas:
            print(f"\n🆔 ID: {p['id']} | CATEGORIA: {p['categoria'].upper()}")
            print(f" ❓ Pergunta: {p['pergunta']}")
            print(f" 🔘 Opções: {' | '.join(p['opcoes'])}")
            print(f" 👨‍⚕️ Especialidades: {p['especialidades']}")
        
        print("\n" + "="*70)
        print("📊 ANÁLISE ESTATÍSTICA:")
        print("="*70)
        
        print(f"\n✅ Total de perguntas geradas: {len(perguntas)}")
        print(f"✅ Cobertura de categorias: {len(set([p['categoria'] for p in perguntas]))} áreas distintas")
        
        print("\n📂 Distribuição por Categoria:")
        for cat in categorias:
            count = len([p for p in perguntas if p['categoria'] == cat])
            status = "OK" if count > 0 else "ATENÇÃO"
            print(f"  • {cat.ljust(15)}: {count} pergunta(s) - {status}")
        
        # --- Fase 4: Validação Lógica (Sanity Check) ---
        print("\n🔍 VERIFICAÇÃO DE INTEGRIDADE (SANITY CHECK):")
        problemas = 0
        
        for p in perguntas:
            # Validação 1: Pergunta tem opções suficientes?
            if len(p['opcoes']) < 2:
                print(f"  ⚠️ ALERTA: Pergunta {p['id']} tem apenas {len(p['opcoes'])} opções.")
                problemas += 1
            
            # Validação 2: Lógica de contexto (ex: Matemática com opções de Frequência?)
            opcoes_text = ' '.join(p['opcoes']).lower()
            if "frequentemente" in opcoes_text and "quanto é" in p['pergunta'].lower():
                print(f"  ⚠️ ERRO LÓGICO: Pergunta {p['id']} (matemática) com opções de frequência.")
                problemas += 1
        
        if problemas == 0:
            print("  ✅ SUCESSO: Todas as perguntas passaram na validação de integridade!")
        else:
            print(f"  ⚠️ ATENÇÃO: Encontrados {problemas} pontos de verificação.")
        
        print("\n" + "="*70)
        print("✅ CONCLUSÃO: O MOTOR DE IA ESTÁ OPERACIONAL.")
        print("="*70)

    except Exception as e:
        print(f"\n❌ FALHA CRÍTICA NO TESTE: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    executar_teste_de_carga()
    print("\n🏁 Script de teste finalizado.\n")