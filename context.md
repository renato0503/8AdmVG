# Context — Projeto Customer Discovery (8AdmVG / Unifacc)

Registro do que foi pedido e feito, para continuar depois.
**Pasta raiz:** `D:\Dev\UnifaccApps\8AdmVG` · **Repo:** https://github.com/renato0503/8AdmVG · **Site (Pages):** https://renato0503.github.io/8AdmVG/
**Turma:** Administração · 8º Semestre (VG) — FACC/Unifacc · coordenação Prof. Renato Rosa (Cerrado Tech)

> Este projeto replica, para outra turma e outras ideias, o pacote do `D:\Dev\UnifaccApps\3SemVG` (que por sua vez veio do `AdmCBA`).
> Partes 1–3 são geradas a partir dos modelos do 3SemVG por `_gerador/gen_partes.py`.

---

## 1. Os 5 grupos

| Grupo | Projeto | Responsável | Integrantes | Código |
|---|---|---|---|---|
| 1 | **HoraCerta** — app único de horas complementares em tempo real | Prof. Renato | José Arlindo, Taynara, Luana, Leticia, Samara | `G1-<nnn>` |
| 2 | **RotaViva** — guia turístico de bolso por latitude/longitude, rotas e áudio | Prof. Renato | Cinthia, Danielly, Leandro, Guilherme, Esther | `G2-<nnn>` |
| 3 | **VozGuia** — celular vira assistente sonoro para cegos + alertas ao poder público | Profa. Sandra | Karla Moema, Victor Hugo, Nicolas, Fabio, Yasmin | `G3-<nnn>` |
| 4 | **CasaPiloto** — simulador da construtora: guardar × investir × financiar por tipo de casa | Profa. Polyana | Aliny, André, Michelly, Everson | `G4-<nnn>` |
| 5 | **CasaHumanizada** — programas de moradia num lugar só (nome dado pelo grupo) | Prof. Heitor | Bianca, Giovanna, Estefane | `G5-<nnn>` |

- Os nomes **HoraCerta, RotaViva, VozGuia e CasaPiloto foram propostos por nós** (os grupos só enviaram a ideia). Trocar é fácil: `nome` em `_gerador/dados.py` + renomear a pasta + `py _gerador/gen.py`.
- 23/09/2026: **Samara saiu do Grupo 5 e foi para o Grupo 1** (já refletido em `grupos.md`).
- G5 enviou contexto extra (apresentação "Projeto de Gestão da Mudança — Inovação e Gestão Pública", de Geovanna Shara e Bianca Veronez): caso **Casa Cuiabana** (83.991 cadastros em 2025, confirmado no site da Prefeitura de Cuiabá), jornada em 4 etapas, 6 funcionalidades (consulta de oportunidades, requisitos claros, notificações, checklist, status, etapas e prazos) e quadro antes × depois. Incorporado em dados, pesquisa, slides, ContextoApp e app. Obs.: a lista de integrantes diz "Giovanna"; a apresentação assina "Geovanna Shara" — confirmar a grafia.

## 2. Regras do app de coleta (iguais ao 3SemVG)

Bloco 0 (perfil) por observação + 1 triagem por grupo · **20 perguntas em escala 1–5** com polos rotulados · sem resposta aberta · falas no **áudio do WhatsApp** que começa com o código `G<n>-<nnn>` · dupla em campo (formulário + áudio) · meta 15–20 por grupo.

## 3. Estrutura

```
8AdmVG/
├── index.html · manifest.json · sw.js       ← hub (GERADO)
├── grupos.md                                ← FONTE dos integrantes/professores
├── App/ · coleta/                           ← app de coleta (perguntas injetadas pelo gerador; coleta/ = cópia publicada)
├── Parte 1/ · Parte 2/ · Parte 3/           ← slides + cadernos + PDFs (GERADOS de 3SemVG)
├── GrupoN-Nome/
│   ├── README.md · formulario-app.md · Pesquisa-Dados.md · Slides-*.html · index.html · manifest.json · sw.js  (GERADOS)
│   ├── ContextoApp.md                       ← escrito à mão
│   ├── app.html                             ← MVP escrito à mão
│   └── Slides-*.pdf
├── assets/  identidade/temas.css (GERADO) · logos/ · mvp/ (mvp.css, mvp.js) · landing.css · reveal/ · caderno.css · md-viewer.html
├── _pesquisa/  openalex_busca.py · saidas/ (brutos da API) · selecao.py · selecionados/ · INDICE-PESQUISA.md (GERADO)
└── _gerador/   dados.py · pesquisa.py · extra.py · gen.py · gen_partes.py · hub.py · pdf.py · testar_apps.py · prints.py
```

## 4. Comandos

```powershell
py _gerador/gen.py            # regenera grupos, hub, temas, logos SVG, coleta e índice de pesquisa
py _gerador/gen_partes.py     # regenera Partes 1–3 a partir do 3SemVG (e acusa restos do 3SemVG)
py _gerador/pdf.py [filtro]   # PDFs via Playwright (estável; substitui o Regenerar-PDFs.ps1 do 3SemVG)
py _gerador/testar_apps.py    # teste de fumaça dos 5 MVPs em 375x667 (cliques, erros JS, overflow, persistência)
py _pesquisa/selecao.py       # confere se todo DOI usado existe nos brutos da API (falha se não existir)
```

PDF: 12 páginas por deck de grupo; Parte 1 = 9, Parte 2 = 12, Parte 3 = 9; cadernos 19 / 8 / 7.

## 5. Pesquisa (lição aprendida do 3SemVG)

No 3SemVG apareceram **citações fabricadas** (G6 com 14/14 inventadas). Aqui o fluxo impede isso: buscas reais → `saidas/*.json` → `selecao.py` copia os metadados **dos brutos** para `selecionados/G<n>.json` → o gerador monta as referências a partir desse JSON. Só a leitura/uso de cada artigo é texto nosso (`_gerador/pesquisa.py`). 14 artigos por grupo, 70 no total. Artigos sem resumo na API (4 do G4) estão marcados "citar só pelo título".

Dados brasileiros conferidos na web em 23/09/2026 (INEP, IBGE Censo 2022, Embratur, Sedec-MT, FJP, Abecip, Ministério das Cidades, Cetic.br, Prefeitura de Cuiabá). Pendentes `[verificar]`: evasão 17,5% (G1, veio de imprensa) e total de unidades do MCMV (G5, muda todo mês).

## 6. MVPs (app.html)

Todos: PWA, dados só no aparelho (localStorage), exportar/importar JSON, apagar tudo, conteúdo de exemplo rotulado, testados em 375px sem erro de JS.

| Grupo | O que faz |
|---|---|
| HoraCerta | Saldo por categoria com teto, ritmo até a formatura, atividades com foto/PDF do certificado, fluxo de validação (coordenação simulada), eventos, CSV |
| RotaViva | Perto de mim (GPS ou posição simulada), 12 pontos de Cuiabá/VG/Chapada/Pantanal (coordenadas aproximadas), narração por voz, rota por tempo e interesse com esquema SVG, diário, sugestões |
| VozGuia | Botões grandes, voz + vibração, caminhada de treino simulada em VG, mapa colaborativo, alertas com foto e protocolo (resposta do órgão simulada), alto contraste, tutorial falado |
| CasaPiloto | 4 casas piloto com planta SVG e tour, simulador guardar × investir × financiar (Price/SAC, FGTS, aluguel, valorização), semáforo 30% da renda, plano com depósitos e checklist, contato com corretor (simulado, com consentimento) |
| CasaHumanizada | Programas (incl. Casa Cuiabana e MCMV faixas 2025), teste "tenho direito?" local (7 perguntas), checklist de documentos, inscrições com etapas, prazos e central de avisos, agendamento e chat (simulados), alerta anti-golpe |

## 7. Pendências

- [ ] Grupos revisarem os nomes propostos e as 20 perguntas (Parte 2)
- [ ] Confirmar datas reais da defesa e da ida ao shopping (materiais dizem "Setembro de 2026")
- [ ] Conferir `[verificar]` nos Pesquisa-Dados (G1 evasão; G5 unidades MCMV)
- [ ] Conteúdo do RotaViva (textos e coordenadas) validar com fontes oficiais
- [ ] Ida ao shopping, tabulação e sprints 3–5 (ver `SPRINTS.md`)
