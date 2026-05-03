import re

with open('dashboards_mockups.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the clean status-row block
status_row = """        <div class="status-row">
            <!-- EPI STATUS -->
            <div class="status-card active" id="btn-epi" onclick="filterMapLayers('epi')">
                <div class="card-header-q">
                    <div class="dept-label-q truncate whitespace-nowrap">Vigilância em Saúde</div>
                    <div class="update-tag-q truncate whitespace-nowrap">Tempo Real</div>
                </div>
                <div class="card-body-q">
                    <div class="axis-icon-wrap">
                        <i class="fas fa-heartbeat"></i>
                    </div>
                    <div class="data-content-q">
                        <div class="data-value-q">415 <span class="data-unit-q">casos</span></div>
                    </div>
                    <div class="data-trend-q trend-up">
                        <i class="fas fa-arrow-up"></i> 22%
                    </div>
                </div>
                <div class="alert-badge-q badge-epi-q">
                    <i class="fas fa-exclamation-circle"></i> EMERGÊNCIA
                </div>
            </div>

            <!-- VISA STATUS -->
            <div class="status-card" id="btn-visa" onclick="filterMapLayers('visa')">
                <div class="card-header-q">
                    <div class="dept-label-q truncate whitespace-nowrap">Vigilância Sanitária</div>
                    <div class="update-tag-q truncate whitespace-nowrap">08:00</div>
                </div>
                <div class="card-body-q">
                    <div class="axis-icon-wrap">
                        <i class="fas fa-shield-alt"></i>
                    </div>
                    <div class="data-content-q">
                        <div class="data-value-q">92 <span class="data-unit-q">%</span></div>
                    </div>
                    <div class="data-trend-q trend-down">
                        <i class="fas fa-check"></i> OK
                    </div>
                </div>
                <div class="alert-badge-q badge-visa-q">
                    <i class="fas fa-check-circle"></i> NORMALIDADE
                </div>
            </div>

            <!-- CLIMA STATUS -->
            <div class="status-card" id="btn-clima" onclick="filterMapLayers('clima')">
                <div class="card-header-q">
                    <div class="dept-label-q truncate whitespace-nowrap">Inteligência Meteo.</div>
                    <div class="update-tag-q truncate whitespace-nowrap">Atualizado</div>
                </div>
                <div class="card-body-q">
                    <div class="axis-icon-wrap">
                        <i class="fas fa-sun"></i>
                    </div>
                    <div class="data-content-q">
                        <div class="data-value-q">11+ <span class="data-unit-q">UV</span></div>
                    </div>
                    <div class="data-trend-q">
                        ESTÁVEL
                    </div>
                </div>
                <div class="alert-badge-q badge-clima-q">
                    <i class="fas fa-exclamation-circle"></i> ATENÇÃO
                </div>
            </div>

            <!-- HIDRO STATUS -->
            <div class="status-card" id="btn-hidro" onclick="filterMapLayers('hidro')">
                <div class="card-header-q">
                    <div class="dept-label-q truncate whitespace-nowrap">Monitoramento Hidro.</div>
                    <div class="update-tag-q truncate whitespace-nowrap">Online</div>
                </div>
                <div class="card-body-q">
                    <div class="axis-icon-wrap">
                        <i class="fas fa-water"></i>
                    </div>
                    <div class="data-content-q">
                        <div class="data-value-q">3.45 <span class="data-unit-q">m</span></div>
                    </div>
                    <div class="data-trend-q trend-down">
                        NORMAL
                    </div>
                </div>
                <div class="alert-badge-q badge-hidro-q">
                    <i class="fas fa-info-circle"></i> NORMALIDADE
                </div>
            </div>
        </div>"""

# Remove all status-cards and status-row fragments between network-status-bar and main-grid
network_bar_end = r'</div>\s+</div>\s+</div>\s+</div>\s+</div>\s+</div>\s+</div>\s+</div>\s+</div>' # This is too specific
# Let's find the closing tag of network-status-bar
# <div class="network-status-bar bg-slate-800/50"> ... </div>

# Actually, I'll just find the range to replace.
start_token = '<div class="network-status-bar bg-slate-800/50">'
end_token = '<div class="main-grid">'

# Re-read to find exact positions
network_bar_pos = content.find(start_token)
main_grid_pos = content.find(end_token)

# We want to keep the network bar but remove everything between it and main-grid.
# The network bar ends with a </div> at line 811.
network_bar_content_end = content.find('</div>', content.find('Monitorando: 08 Distritos', network_bar_pos)) + 6

# Remove everything between network_bar_content_end and main_grid_pos
part1 = content[:network_bar_content_end]
part2 = content[main_grid_pos:]

# Now insert status_row inside main-grid's map-section
insertion_point = r'<main class="map-section">'
replacement = f'<main class="map-section">\n{status_row}'

new_content = part1 + "\n\n" + part2.replace(insertion_point, replacement, 1)

# Fix hud-overlay top offset
new_content = new_content.replace('<div class="hud-overlay">', '<div class="hud-overlay" style="top: 125px;">', 1)

with open('dashboards_mockups.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Status-row correctly integrated above map only.")
