import os
import re

files = ['index.html', 'etl_arquitetura.html', 'devs_etl_detalhado.html', 'visa_etl_detalhado.html', 
         'hitl_devs_arquitetura.html', 'cisc_ia_modelagem.html', 'sala_situacao.html', 'matriz_alertas.html', 'schema_linkage.html']

base_dir = r'c:\Users\Daniel\Desktop\GITHUB\cisc'

for filename in files:
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path): continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Encontrar todos os blocos <header>...</header>
    header_pattern = re.compile(r'<header[^>]*>.*?</header>', re.DOTALL)
    headers = header_pattern.findall(content)
    
    if len(headers) > 1:
        print(f"Found {len(headers)} headers in {filename}. Keeping only the first one.")
        # Mantemos apenas o primeiro header e removemos os outros
        first_header = headers[0]
        
        # Estratégia: Remover todos os headers e depois reinserir o primeiro logo após o <body>
        # Mas para ser mais seguro, vamos apenas remover os duplicados que estão dentro de main/cards
        
        # Primeiro, removemos todos
        content_no_headers = header_pattern.sub('', content)
        
        # Reinserimos o primeiro header logo após a abertura do <body> ou da mesh background
        if '<div class="bg-mesh"></div>' in content_no_headers:
            content = content_no_headers.replace('<div class="bg-mesh"></div>', '<div class="bg-mesh"></div>\n    ' + first_header)
        elif '<body>' in content_no_headers:
            content = content_no_headers.replace('<body>', '<body>\n    ' + first_header)
        else:
            # Fallback
            content = first_header + content_no_headers

        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned up headers in {filename}")
    else:
        print(f"Only 1 header in {filename}, skipping cleanup.")
