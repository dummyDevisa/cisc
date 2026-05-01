import os
import re

# Lista de todos os arquivos HTML que precisam do menu atualizado
files = ['index.html', 'etl_arquitetura.html', 'devs_etl_detalhado.html', 'visa_etl_detalhado.html', 
         'hitl_devs_arquitetura.html', 'cisc_ia_modelagem.html', 'sala_situacao.html', 'matriz_alertas.html', 'schema_linkage.html', 'dashboards_mockups.html']

base_dir = r'c:\Users\Daniel\Desktop\GITHUB\cisc'

def get_nav_html(active_page):
    return f'''
    <header class="site-header">
        <a href="index.html" class="logo" style="text-decoration: none;">
            <i class="fas fa-microchip"></i>
            <span>CISC BELÉM</span>
        </a>
        <nav class="nav-links">
            <div class="nav-group">
                <span class="group-title">
                    <i class="fas fa-layer-group"></i> Estrutura
                    <i class="fas fa-chevron-down"></i>
                </span>
                <div class="group-content">
                    <a href="index.html" class="{"active" if active_page == "index.html" else ""}"><i class="fas fa-home"></i> Início / Visão Geral</a>
                    <a href="etl_arquitetura.html" class="{"active" if active_page == "etl_arquitetura.html" else ""}"><i class="fas fa-project-diagram"></i> Arquitetura Core</a>
                    <a href="schema_linkage.html" class="{"active" if active_page == "schema_linkage.html" else ""}"><i class="fas fa-database"></i> Schema PostGIS</a>
                </div>
            </div>
            <div class="nav-group">
                <span class="group-title">
                    <i class="fas fa-microchip"></i> Inteligência
                    <i class="fas fa-chevron-down"></i>
                </span>
                <div class="group-content">
                    <a href="devs_etl_detalhado.html" class="{"active" if active_page == "devs_etl_detalhado.html" else ""}"><i class="fas fa-file-medical"></i> Pipeline DEVS</a>
                    <a href="visa_etl_detalhado.html" class="{"active" if active_page == "visa_etl_detalhado.html" else ""}"><i class="fas fa-shield-virus"></i> Pipeline VISA</a>
                    <a href="cisc_ia_modelagem.html" class="{"active" if active_page == "cisc_ia_modelagem.html" else ""}"><i class="fas fa-robot"></i> Modelagem IA/HTR</a>
                    <a href="hitl_devs_arquitetura.html" class="{"active" if active_page == "hitl_devs_arquitetura.html" else ""}"><i class="fas fa-users-cog"></i> Validação HITL</a>
                </div>
            </div>
            <div class="nav-group">
                <span class="group-title">
                    <i class="fas fa-eye"></i> Decisão
                    <i class="fas fa-chevron-down"></i>
                </span>
                <div class="group-content">
                    <a href="sala_situacao.html" class="{"active" if active_page == "sala_situacao.html" else ""}"><i class="fas fa-desktop"></i> Sala de Situação</a>
                    <a href="matriz_alertas.html" class="{"active" if active_page == "matriz_alertas.html" else ""}"><i class="fas fa-exclamation-triangle"></i> Matriz de Alertas</a>
                    <a href="dashboards_mockups.html" class="{"active" if active_page == "dashboards_mockups.html" else ""}"><i class="fas fa-chart-line"></i> Mockups de Dashboards</a>
                </div>
            </div>
            <a href="https://github.com/dummyDevisa/cisc" target="_blank" style="color: var(--text-dim); text-decoration: none; font-size: 0.9rem; font-weight: 600; display: flex; align-items: center; gap: 8px; margin-left: 10px;">
                <i class="fab fa-github"></i> GitHub
            </a>
        </nav>
    </header>
'''

header_pattern = re.compile(r'<header[^>]*>.*?</header>', re.DOTALL)

for filename in files:
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path): continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_nav = get_nav_html(filename)
    
    # Substituir apenas a primeira ocorrência (que deve ser o menu global)
    content = header_pattern.sub(new_nav.strip(), content, count=1)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated nav in {filename}")
