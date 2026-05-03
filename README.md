# CISC Belém — Centro de Informação em Saúde e Clima

> **SESMA · Departamento de Vigilância em Saúde (DEVS) · Departamento de Vigilância Sanitária (DEVISA) · Ministério da Saúde**  
> Inauguração prevista: Junho/2026 · Operação plena: Agosto/2026

## O que é o CISC

O **Centro de Informação em Saúde e Clima (CISC)** é uma unidade técnica municipal
criada pela parceria entre o **Ministério da Saúde** (via CGClima/SVSA) e a
**Secretaria Municipal de Saúde de Belém** (SMS), com a missão de **antecipar e
mitigar os impactos de eventos climáticos extremos sobre a saúde da população**.

O CISC não é apenas um sistema de TI, mas a aplicação prática do conceito de **Saúde Única (One Health)**, reconhecendo que a saúde humana está indissociavelmente ligada à saúde do ambiente. O cruzamento de dados de vigilância em saúde (epidemiológica, sanitária e ambiental) com gatilhos climáticos é uma das estratégias mais avançadas e modernas na inteligência em saúde pública hoje.

Trata-se de um **organismo de inteligência** que integra cinco eixos profissionais para transformar dados brutos de saúde, clima e território em **alertas precoces, protocolos de resposta e decisões em tempo real** para a gestão pública municipal.

## Os 5 Eixos Profissionais do CISC

O Centro opera com uma equipe mínima de **5 profissionais especializados**,
cada um responsável por um eixo de inteligência:

### 🏥 Eixo 1 — Epidemiologista
Traduz o risco climático em impacto clínico. Monitora doenças sensíveis ao clima
(DDA, arboviroses, leptospirose, SRAG), elabora boletins epidemiológicos semanais
e constrói a **matriz de decisão** que correlaciona alertas climáticos com sobrecarga
na APS e urgências. Domina os sistemas legados do SUS (SINAN, SIM, SIH, e-SUS APS)
e modelos em R para detecção de anomalias.

### 🗺️ Eixo 2 — Geógrafo / Análise Espacial
Espacializa e territorializa os dados. Cruza informações de saúde, censo (IBGE) e
índices de vulnerabilidade social (IVS) com manchas climáticas (ilhas de calor,
alagamentos) para **identificar microclimas e priorizar ações intraurbanas**.
Produz cartografia para Defesa Civil, Assistência Social e localização de populações
vulneráveis (ribeirinhos, indígenas, idosos, situação de rua).

### 🌦️ Eixo 3 — Meteorologista / Climatologista
Os "olhos preditivos" do Centro. Monitora continuamente temperatura, umidade,
precipitação, qualidade do ar e **dados hidrológicos** (nível de rios e tábuas de
maré — particularidade crítica de Belém). Interpreta previsões do INMET, CEMADEN,
Censipam, ANA e Marinha, e **sinaliza gatilhos com 72h de antecedência** para
elevar os níveis de alerta municipal.

### 📊 Eixo 4 — Cientista de Dados
Focado na automação analítica e modelos preditivos. Calcula linhas de base
históricas, aplica regressões quantílicas e DLM para encontrar relações
clima↔saúde, e desenvolve algoritmos de **detecção estatística de anomalias**
(CUSUM, SaTScan, ML) que disparam alertas autônomos quando o excesso de
atendimentos ultrapassa o esperado.

### 💻 Eixo 5 — Analista de TI / Engenheiro de Dados
O arquiteto digital. Projeta e sustenta a integração técnica do CISC: o banco
central (PostgreSQL/PostGIS), os pipelines de ETL (Airflow + Python), as APIs de
ingestão, a automação OCR/HITL para dados manuscritos e a configuração da
**Sala de Situação** (Grafana + Superset no Videowall 80").

> **Este repositório é a base de trabalho do Eixo 5**, documentando a
> arquitetura técnica que sustenta todos os outros eixos.

## O Servidor como Coração do CISC

O servidor não é um sistema do DEVS. Ele é o **coração operacional do Centro** —
o órgão que recebe, processa e distribui inteligência para toda a Sala de Situação.

A arquitetura foi concebida como um **núcleo de ingestão universal**: qualquer fonte
relevante pode ser conectada, independentemente de origem, formato ou protocolo.

O **DEVS** e o **DEVISA** são as duas primeiras e mais críticas fontes institucionais
do CISC — ambas integrantes da comissão gestora do Centro:

- **DEVS** (DVE, DCE, CIEVS, DANT): dados epidemiológicos, notificações de surtos,
  fichas de campo, exportações SINAN/e-SUS
- **DEVISA** (DVSA, DVSE/VISAMB): dados de qualidade da água e do ar (VIGIAGUA/VIGIAR),
  surtos de Doenças Transmitidas por Alimentos (DTA), monitoramento de açaí/LACEN,
  laudos de inspeção sanitária ambiental

À medida que o CISC amadurece, novos parceiros serão conectados: agências
meteorológicas, institutos de pesquisa, Defesa Civil, universidades e redes de
sensores urbanos.

### Particularidades de Belém: Integração Hidrológica

Belém exige uma camada nativa de **dados hidrológicos e de maré**:
*   Níveis de rios (ANA)
*   Tábuas de maré (Marinha do Brasil)
*   Precipitação acumulada cruzada com cotas de alagamento

Esse cruzamento com manchas de vulnerabilidade urbana permite **direcionar equipes
de saúde antes da emergência se instalar**.

## Stack Tecnológica

| Camada | Tecnologia | Função |
|---|---|---|
| **Orquestração** | Apache Airflow | Workflows, DAGs, tratamento de falhas |
| **Processamento** | Python (Pandas/Polars) | ETL, limpeza, normalização geográfica |
| **Modelos Epi** | R / Shiny | Baselines, regressões, vigilância sindrômica |
| **Datalake** | MinIO (S3) | PDFs, CSVs, imagens originais |
| **DW** | PostgreSQL + PostGIS | Fonte de verdade geoespacial |
| **BI Enterprise** | Apache Superset | Mapas de calor e análises cartográficas |
| **BI Self-Service** | Metabase | Painéis acessíveis para gestores |
| **Real-time** | Grafana | Alertas visuais/sonoros no Videowall |
| **OCR/HTR** | Florence-2 / PaliGemma 2 | Leitura de manuscritos com HITL |
| **Segurança** | WireGuard / Tailscale | VPN servidor local ↔ nuvem |
| **Infra** | Docker / Compose | Portabilidade total |

## Parceria MS × SMS

| Responsável | Contribuição |
|---|---|
| **MS (CGClima/SVSA)** | 5 Workstations, servidor, TV 4K 80", videoconferência, mobiliário, custeio da equipe por 2 anos, acesso a plataformas nacionais |
| **SMS Belém** | Espaço físico, adaptação, organograma, POPs, articulação de dados locais |
| **Conjunto** | Seleção da equipe, alertas precoces, análises exploratórias integradas |

## Diagramas e Protótipos

| Artefato | Descrição |
|---|---|
| [**Arquitetura Agnóstica**](etl_arquitetura.html) | Fluxograma macro do servidor centralizador (DEVS, DEVISA, INMET, CEMADEN, etc.). |
| [**Pipeline DEVS**](devs_etl_detalhado.html) | Do papel ao dado estruturado via OCR, HITL e Python. |
| [**Pipeline VISA**](visa_etl_detalhado.html) | Dados de DTA, VIGIAGUA, qualidade do ar e monitoramento de açaí. |
| [**Arquitetura HITL**](hitl_devs_arquitetura.html) | Motor de decisão IA + humanos (Learning Loop). |
| [**Estratégia de IA/HTR**](cisc_ia_modelagem.html) | Modelos, hardware e fine-tuning local. |
| [**Framework Estatístico**](cisc_framework_estatistico.html) | Regressão Quantílica e Modelagem Preditiva (Padrão Rio). |
| [**Sala de Situação**](sala_situacao.html) | Videowall, painéis real-time e protocolo de alertas. |
| [**Matriz de Alertas**](matriz_alertas.html) | Gatilhos climáticos × thresholds epidemiológicos × sanitários. |

## Documentação de Referência

* [**Acervo Documental CISC (NotebookLM)**](https://notebooklm.google.com/notebook/ab930b41-9c51-4b42-9f63-a687c30f49ed)

## Governança

O CISC será incluído no **organograma da SMS**, com:
*   Missão, visão e valores próprios
*   **POPs** (Procedimentos Operacionais Padrão)
*   Fluxos interno, intra e intersetorial
*   Articulação com **Defesa Civil**, **Meio Ambiente** e **Assistência Social**
*   Integração com app **"Guardiões da Saúde"** (até Dez/2026)

## Roadmap

### ✅ Concluído (Abr/2026)
- [x] Definição do espaço físico do CISC
- [x] Definição do responsável e demandas (pela Secretária)

### 📌 Curto Prazo (Mai — Jul/2026)
- [ ] Selecionar e contratar equipe técnica (5 profissionais)
- [ ] Elaborar planta do CISC e diagnóstico de risco
- [ ] Definir lotação no organograma, missão, visão e valores
- [ ] Receber equipamentos (workstations, servidor, videowall)
- [ ] 🚀 **Inauguração do CISC (MVP)** — Jun/2026
- [ ] Articular dados de saúde locais
- [ ] Ambientação e capacitação dos profissionais

### 📐 Médio Prazo (Jul — Dez/2026)
- [ ] Criar modelo de arquitetura de dados saúde + clima
- [ ] Criar POPs e fluxos de trabalho intersetorial
- [ ] Articular dados climáticos, ambientais e de saneamento
- [ ] Análises exploratórias integradas
- [ ] Internalizar protocolos de eventos extremos hidrológicos
- [ ] Integrar app "Guardiões da Saúde" ao CISC

### 🔭 Longo Prazo (Ago/2026 — Jun/2027)
- [ ] Sistemas de alerta precoce para extremo de temperatura
- [ ] Protocolo operacional da cidade para extremo de temperatura

*Cronograma baseado no Plano de Ação do Ministério da Saúde (CGClima/SVSA, 2026).*
