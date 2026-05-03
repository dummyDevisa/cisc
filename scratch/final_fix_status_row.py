import re

with open('dashboards_mockups.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the clean map-section block
clean_map_section = """        <main class="map-section">
            <div class="status-row">
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
            </div>
            
            <div class="hud-overlay" style="top: 125px;">
                <div class="hud-tag active" id="hud-epi" style="color: #ef4444;" onclick="filterMapLayers('epi')">
                    <span class="status-indicator"></span>
                    <i class="fas fa-heartbeat"></i>
                    EPIDEMIOLOGIA
                </div>
                <div class="hud-tag" id="hud-visa" style="color: #10b981;" onclick="filterMapLayers('visa')">
                    <span class="status-indicator"></span>
                    <i class="fas fa-shield-alt"></i>
                    SANITÁRIA
                </div>
                <div class="hud-tag" id="hud-clima" style="color: #f97316;" onclick="filterMapLayers('clima')">
                    <span class="status-indicator"></span>
                    <i class="fas fa-sun"></i>
                    CLIMA
                </div>
                <div class="hud-tag" id="hud-hidro" style="color: #3b82f6;" onclick="filterMapLayers('hidro')">
                    <span class="status-indicator"></span>
                    <i class="fas fa-water"></i>
                    HIDRO
                </div>
            </div>
            <div id="map"></div>"""

# Define the start and end of the mess
# Everything from <main class="map-section"> to <div id="map"></div>
pattern = re.compile(r'<main class="map-section">.*?(<div id="map">)', re.DOTALL)
new_content = pattern.sub(clean_map_section + r'\1', content)

with open('dashboards_mockups.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Final cleanup completed.")
