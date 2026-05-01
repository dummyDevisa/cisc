import os
import re

# Define the new CSS for the navigation
NEW_CSS = """
        /* Nova Navegação Organizada e Alinhada */
        .nav-links {
            display: flex;
            align-items: center;
            gap: 30px;
        }

        .nav-group {
            position: relative;
            display: flex;
            align-items: center;
        }

        .group-title {
            color: var(--text-dim);
            font-size: 0.9rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            padding: 10px 0;
        }

        .group-title i.fa-chevron-down {
            font-size: 0.7rem;
            opacity: 0.5;
            transition: transform 0.3s ease;
        }

        .nav-group:hover .group-title {
            color: var(--primary);
        }

        .nav-group:hover i.fa-chevron-down {
            transform: rotate(180deg);
            color: var(--primary);
        }

        .group-content {
            position: absolute;
            top: 100%;
            right: 0;
            background: var(--glass);
            backdrop-filter: blur(20px);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 10px;
            min-width: 240px;
            opacity: 0;
            visibility: hidden;
            transform: translateY(10px);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 20px 40px rgba(0,0,0,0.5);
            display: flex;
            flex-direction: column;
            gap: 4px;
            z-index: 1000;
        }

        .nav-group:hover .group-content {
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
        }

        .group-content a {
            padding: 12px 16px;
            border-radius: 8px;
            color: var(--text-dim) !important;
            font-size: 0.85rem !important;
            text-decoration: none !important;
            display: flex !important;
            align-items: center;
            gap: 12px;
            transition: all 0.2s ease;
        }

        .group-content a:hover {
            background: rgba(255,255,255,0.05);
            color: var(--primary) !important;
            padding-left: 20px;
        }

        .group-content a i {
            width: 18px;
            text-align: center;
            font-size: 1rem;
        }

        @media (max-width: 1024px) {
            .nav-links { gap: 15px; }
            .group-title { font-size: 0.8rem; }
        }
"""

# Define the new Header HTML
def get_header(active_page=""):
    return f"""
    <header class="site-header">
        <a href="index.html" class="logo" style="text-decoration: none;">
            <i class="fas fa-microchip"></i>
            <span>CISC BELÉM</span>
        </a>
        <nav class="nav-links">
            <!-- Grupo 1: Fundação -->
            <div class="nav-group">
                <span class="group-title">
                    <i class="fas fa-layer-group"></i> Estrutura
                    <i class="fas fa-chevron-down"></i>
                </span>
                <div class="group-content">
                    <a href="index.html" class="{'active' if active_page == 'index.html' else ''}"><i class="fas fa-home"></i> Início / Visão Geral</a>
                    <a href="etl_arquitetura.html" class="{'active' if active_page == 'etl_arquitetura.html' else ''}"><i class="fas fa-project-diagram"></i> Arquitetura Core</a>
                    <a href="schema_linkage.html" class="{'active' if active_page == 'schema_linkage.html' else ''}"><i class="fas fa-database"></i> Schema PostGIS</a>
                </div>
            </div>

            <!-- Grupo 2: Dados & IA -->
            <div class="nav-group">
                <span class="group-title">
                    <i class="fas fa-microchip"></i> Inteligência
                    <i class="fas fa-chevron-down"></i>
                </span>
                <div class="group-content">
                    <a href="devs_etl_detalhado.html" class="{'active' if active_page == 'devs_etl_detalhado.html' else ''}"><i class="fas fa-file-medical"></i> Pipeline DEVS</a>
                    <a href="visa_etl_detalhado.html" class="{'active' if active_page == 'visa_etl_detalhado.html' else ''}"><i class="fas fa-shield-virus"></i> Pipeline VISA</a>
                    <a href="cisc_ia_modelagem.html" class="{'active' if active_page == 'cisc_ia_modelagem.html' else ''}"><i class="fas fa-robot"></i> Modelagem IA/HTR</a>
                    <a href="hitl_devs_arquitetura.html" class="{'active' if active_page == 'hitl_devs_arquitetura.html' else ''}"><i class="fas fa-users-cog"></i> Validação HITL</a>
                </div>
            </div>

            <!-- Grupo 3: Operação -->
            <div class="nav-group">
                <span class="group-title">
                    <i class="fas fa-eye"></i> Decisão
                    <i class="fas fa-chevron-down"></i>
                </span>
                <div class="group-content">
                    <a href="sala_situacao.html" class="{'active' if active_page == 'sala_situacao.html' else ''}"><i class="fas fa-desktop"></i> Sala de Situação</a>
                    <a href="matriz_alertas.html" class="{'active' if active_page == 'matriz_alertas.html' else ''}"><i class="fas fa-exclamation-triangle"></i> Matriz de Alertas</a>
                </div>
            </div>

            <a href="https://github.com/dummyDevisa/cisc" target="_blank" style="color: var(--text-dim); text-decoration: none; font-size: 0.9rem; font-weight: 600; display: flex; align-items: center; gap: 8px; margin-left: 10px; transition: all 0.3s ease;">
                <i class="fab fa-github"></i> GitHub
            </a>
        </nav>
    </header>
"""

files = [
    'index.html',
    'etl_arquitetura.html',
    'devs_etl_detalhado.html',
    'visa_etl_detalhado.html',
    'hitl_devs_arquitetura.html',
    'cisc_ia_modelagem.html',
    'sala_situacao.html',
    'matriz_alertas.html',
    'schema_linkage.html'
]

base_dir = r'c:\Users\Daniel\Desktop\GITHUB\cisc'

for filename in files:
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace CSS (same pattern as before)
    css_pattern = re.compile(r'/\* Nova Navegação Organizada e Alinhada \*/.*?(@media \(max-width: 1024px\) \{.*?\})', re.DOTALL)
    if css_pattern.search(content):
        content = css_pattern.sub(NEW_CSS, content)

    # Replace Header
    header_pattern = re.compile(r'<header[^>]*>.*?</header>', re.DOTALL)
    content = header_pattern.sub(get_header(filename), content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated Logo Link in {filename}")
