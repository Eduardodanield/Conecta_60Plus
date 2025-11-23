# src/gerar_pdf.py
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas
from datetime import datetime
import io


def gerar_pdf_relatorio(dados_pessoais, analise, perguntas, respostas):
    """
    Gera PDF do relatório com LETRAS GRANDES para idosos.
    """
    # Buffer em memória
    buffer = io.BytesIO()
    
    # Criar documento
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    # Container para elementos
    elementos = []
    
    # Estilos personalizados com LETRAS GRANDES
    styles = getSampleStyleSheet()
    
    # Título GRANDE
    style_titulo = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=colors.HexColor('#1f77b4'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Subtítulo
    style_subtitulo = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=20,
        textColor=colors.HexColor('#ff7f0e'),
        spaceAfter=15,
        fontName='Helvetica-Bold'
    )
    
    # Texto normal GRANDE
    style_normal = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=16,
        leading=24,
        textColor=colors.black,
        spaceAfter=10,
        fontName='Helvetica'
    )
    
    # Texto em negrito
    style_bold = ParagraphStyle(
        'CustomBold',
        parent=styles['Normal'],
        fontSize=18,
        leading=26,
        textColor=colors.black,
        spaceAfter=10,
        fontName='Helvetica-Bold'
    )
    
    # ===== TÍTULO =====
    elementos.append(Paragraph("🏥 CONECTA 60+", style_titulo))
    elementos.append(Paragraph("Relatório de Avaliação Geriátrica", style_subtitulo))
    elementos.append(Spacer(1, 0.5*cm))
    
    # ===== DADOS PESSOAIS =====
    elementos.append(Paragraph("📋 Dados Pessoais", style_subtitulo))
    
    dados_table = [
        ["Nome:", dados_pessoais.get('nome', '')],
        ["Idade:", f"{dados_pessoais.get('idade', '')} anos"],
        ["Sexo:", dados_pessoais.get('sexo', '')],
        ["Cidade:", dados_pessoais.get('cidade', '')],
        ["Data:", datetime.now().strftime("%d/%m/%Y às %H:%M")]
    ]
    
    table_dados = Table(dados_table, colWidths=[5*cm, 10*cm])
    table_dados.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 16),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#1f77b4')),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.lightgrey),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#E8F4F8')),
    ]))
    
    elementos.append(table_dados)
    elementos.append(Spacer(1, 1*cm))
    
    # ===== RESULTADO =====
    elementos.append(Paragraph("📊 Resultado da Avaliação", style_subtitulo))
    elementos.append(Spacer(1, 0.3*cm))
    
    # Mapear nomes de especialidades
    nomes_especialidades = {
        'cardiologia': 'Cardiologia',
        'ortopedia': 'Ortopedia',
        'neurologia': 'Neurologia',
        'geriatria': 'Geriatria',
        'psiquiatria': 'Psiquiatria',
        'nutricao': 'Nutrição',
        'oftalmologia': 'Oftalmologia',
        'otorrinolaringologia': 'Otorrinolaringologia',
        'urologia': 'Urologia',
        'dermatologia': 'Dermatologia',
        'gastroenterologia': 'Gastroenterologia',
        'endocrinologia': 'Endocrinologia'
    }
    
    especialidade_formatada = nomes_especialidades.get(
        analise['especialidade'], 
        analise['especialidade'].capitalize()
    )
    
    # Cor da urgência
    cor_urgencia = {
        'alta': colors.red,
        'média': colors.orange,
        'baixa': colors.green
    }
    
    resultado_data = [
        ["Especialidade Recomendada:", especialidade_formatada],
        ["Nível de Urgência:", analise['urgencia'].upper()],
        ["Pontuação Total:", str(analise['pontuacao_total'])]
    ]
    
    table_resultado = Table(resultado_data, colWidths=[8*cm, 7*cm])
    table_resultado.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 18),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 1), (1, 1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#1f77b4')),
        ('TEXTCOLOR', (1, 1), (1, 1), cor_urgencia.get(analise['urgencia'], colors.black)),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 15),
        ('TOPPADDING', (0, 0), (-1, -1), 15),
        ('GRID', (0, 0), (-1, -1), 2, colors.grey),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FFE5B4')),
        ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#FFE4E1')),
        ('BACKGROUND', (0, 2), (-1, 2), colors.HexColor('#E0FFE0')),
    ]))
    
    elementos.append(table_resultado)
    elementos.append(Spacer(1, 0.8*cm))
    
    # ===== RECOMENDAÇÃO =====
    elementos.append(Paragraph("💡 Recomendação", style_subtitulo))
    elementos.append(Paragraph(analise['recomendacao'], style_bold))
    elementos.append(Spacer(1, 0.5*cm))
    
    # ===== ÁREAS DE ATENÇÃO =====
    if analise['categorias_problema']:
        elementos.append(Paragraph("⚠️ Áreas que Requerem Atenção", style_subtitulo))
        categorias_texto = ", ".join(analise['categorias_problema'])
        elementos.append(Paragraph(categorias_texto.capitalize(), style_normal))
        elementos.append(Spacer(1, 0.5*cm))
    
    # ===== PRÓXIMOS PASSOS =====
    elementos.append(Paragraph("🏥 Próximos Passos", style_subtitulo))
    
    proximos_passos = [
        f"1. Agende uma consulta com {especialidade_formatada}",
        "2. Leve este relatório impresso na consulta",
        "3. Mencione as áreas de atenção identificadas",
        "4. Siga as orientações médicas recebidas"
    ]
    
    for passo in proximos_passos:
        elementos.append(Paragraph(passo, style_normal))
    
    elementos.append(Spacer(1, 1*cm))
    
    # ===== RODAPÉ =====
    style_rodape = ParagraphStyle(
        'Rodape',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.grey,
        alignment=TA_CENTER
    )
    
    elementos.append(Spacer(1, 2*cm))
    elementos.append(Paragraph("─" * 60, style_rodape))
    elementos.append(Paragraph(
        "Este relatório foi gerado pelo sistema Conecta 60+<br/>"
        "Para dúvidas, consulte um profissional de saúde", 
        style_rodape
    ))
    
    # Construir PDF
    doc.build(elementos)
    
    # Retornar buffer
    buffer.seek(0)
    return buffer