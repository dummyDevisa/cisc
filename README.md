# CISC Belém — Hub de Arquitetura e Implementação

> **SESMA · Departamento de Vigilância em Saúde (DEVS) · Ministério da Saúde**  
> Cronograma ativo: Jan/2026 → Ago/2026

## O que é este repositório
Espaço de **arquitetura técnica, prototipagem e documentação de decisões** para a
implantação do **CISC (Centro de Informação em Saúde e Clima)** em Belém.

O produto central deste repositório é a definição e prototipagem do
**servidor de dados do CISC**: um núcleo agnóstico e escalável que centraliza,
transforma e disponibiliza informações de saúde, clima e território para a
Sala de Situação municipal.

## O Servidor como Coração do CISC
O servidor não é um sistema do DEVS. Ele é o **coração operacional do Centro** —
o órgão que recebe, processa e distribui inteligência para toda a Sala de Situação.

Sem dados limpos e integrados, o CISC não tem pulso. Por isso, a arquitetura deste
servidor foi concebida como um **núcleo de ingestão universal**: qualquer fonte de
dados relevante para a saúde, o clima ou o território de Belém pode ser conectada a
ele, independentemente de origem, formato ou protocolo.

O **DEVS** é a primeira e mais crítica fonte a ser integrada. Ele concentra a
inteligência epidemiológica local, mas ainda opera de forma majoritariamente manual
(fichas em papel, planilhas descentralizadas, sistemas legados federais). Modernizar
esse fluxo é o passo zero — sem ele, o centro não tem o dado de saúde que justifica
sua existência.

À medida que o CISC amadurece, novos parceiros poderão ser conectados ao mesmo
núcleo: agências meteorológicas, institutos de pesquisa, defesa civil, vigilância
ambiental, universidades, redes de sensores urbanos ou qualquer outro ator que
produza dado útil à inteligência em saúde pública. A plataforma está projetada para
crescer sem reestruturação.

## Stack Tecnológica e Interoperabilidade
Para garantir que o CISC Belém fale a mesma língua que os principais centros de saúde do Brasil (como a **Fiocruz**), as seguintes tecnologias foram selecionadas como padrão:

*   **Orquestração:** Apache Airflow (Gestão de workflows e falhas).
*   **Processamento:** Python (Pandas/Polars) + Suporte a R/Shiny (Modelos Epidemiológicos).
*   **Armazenamento:** MinIO (Datalake Bruto) e PostgreSQL com PostGIS (Banco Estruturado).
*   **Inteligência (BI):** Apache Superset (Enterprise/Deep Analysis) e Metabase (Self-Service para gestores).
*   **Segurança:** Modelo Híbrido com Túnel VPN (WireGuard/Tailscale) para comunicação segura entre o servidor físico local e a nuvem (Vitrine).

## Diagramas e Protótipos

| Artefato | Descrição |
|---|---|
| [**Arquitetura Agnóstica (Coração do CISC)**](etl_arquitetura.html) | Fluxograma macro do servidor centralizador integrando múltiplas fontes (DEVS, INMET, CEMADEN, etc.). |
| [**Pipeline Detalhado DEVS**](devs_etl_detalhado.html) | Aprofundamento do fluxo interno do DEVS: do papel ao dado estruturado via OCR, HITL e Python. |
| [**Arquitetura Lógica HITL**](hitl_devs_arquitetura.html) | Ideação do motor de decisão que orquestra a colaboração entre IA e humanos (Learning Loop). |
| [**Estratégia de IA e HTR**](cisc_ia_modelagem.html) | Modelagem técnica de reconhecimento de manuscritos, seleção de modelos e requisitos de hardware. |

## Documentação de Referência

* [**Acervo Documental CISC (NotebookLM)**](https://notebooklm.google.com/notebook/ab930b41-9c51-4b42-9f63-a687c30f49ed) — Base documental completa do projeto para consulta interativa e atualização.

## Roadmap de Implementação

- [ ] **Mai/2026** — Contratação/designação da equipe técnica mínima
- [ ] **Jun/2026** — Capacitação e alinhamento metodológico
- [ ] **Jul/2026** — Articulação com áreas técnicas da SMS e órgãos externos
- [ ] **Ago/2026** — Primeiras análises, painéis e operação progressiva do CISC

*Cronograma baseado no Plano Estratégico do Ministério da Saúde (2026).*
