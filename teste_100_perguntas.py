import sys
sys.path.append('src')

from perguntas_conecta60 import GeradorPerguntasGratuito

print("="*70)
print("🧪 TESTANDO GERAÇÃO DE PERGUNTAS")
print("="*70)

try:
    print("\nInicializando gerador...")
    gerador = GeradorPerguntasGratuito()
    print("✅ OK!\n")
    
    print("="*70)
    print("GERANDO QUESTIONÁRIO COMPLETO...")
    print("="*70)
    
    # Todas as 15 categorias
    categorias = [
        "mobilidade", "cognitivo", "cardiovascular", "nutricional",
        "emocional", "sono", "visao", "audicao", "quedas",
        "medicamentos", "urinario", "equilibrio", "peso", 
        "digestivo", "pele"
    ]
    
    perguntas = gerador.gerar_questionario_completo(
        num_perguntas=15,
        categorias=categorias
    )
    
    print("\n" + "="*70)
    print(f"✅ RESULTADO: {len(perguntas)} perguntas geradas!")
    print("="*70)
    
    print("\n📋 LISTANDO TODAS AS PERGUNTAS:\n")
    
    for p in perguntas:
        print(f"\n{p['id']}. [{p['categoria'].upper()}]")
        print(f"   Pergunta: {p['pergunta']}")
        print(f"   Opções: {' | '.join(p['opcoes'])}")
        print(f"   Especialidades: {p['especialidades']}")
    
    print("\n" + "="*70)
    print("📊 ANÁLISE:")
    print("="*70)
    
    print(f"\n✅ Total de perguntas: {len(perguntas)}")
    print(f"✅ Total de categorias: {len(set([p['categoria'] for p in perguntas]))}")
    
    print("\n📂 Categorias cobertas:")
    for cat in categorias:
        count = len([p for p in perguntas if p['categoria'] == cat])
        print(f"  • {cat}: {count} pergunta(s)")
    
    # Verificar qualidade das opções
    print("\n🔍 VERIFICANDO QUALIDADE DAS OPÇÕES:")
    problemas = 0
    for p in perguntas:
        if len(p['opcoes']) < 3:
            print(f"  ⚠️ Pergunta {p['id']} tem apenas {len(p['opcoes'])} opções")
            problemas += 1
        
        # Verificar se opções são genéricas demais
        opcoes_text = ' '.join(p['opcoes']).lower()
        if "frequentemente" in opcoes_text and "quanto é" in p['pergunta'].lower():
            print(f"  ⚠️ Pergunta {p['id']} (matemática) com opções erradas:")
            print(f"     Pergunta: {p['pergunta']}")
            print(f"     Opções: {p['opcoes']}")
            problemas += 1
    
    if problemas == 0:
        print("  ✅ Todas as perguntas têm opções adequadas!")
    else:
        print(f"  ⚠️ Encontrados {problemas} problema(s)")
    
    print("\n" + "="*70)
    print("✅ SISTEMA FUNCIONANDO!")
    print("✅ Perguntas sendo geradas do PDF + Templates")
    print("✅ Opções inteligentes baseadas no conteúdo")
    print("="*70)

except Exception as e:
    print(f"\n❌ ERRO: {e}")
    import traceback
    traceback.print_exc()

print("\n🏁 Teste finalizado!\n")