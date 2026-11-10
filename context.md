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
| 2 | **GuiaMobi** — guia turístico de bolso por latitude/longitude, rotas e áudio | Prof. Renato | Cinthia, Danielly, Leandro, Guilherme, Esther | `G2-<nnn>` |
| 3 | **VozGuia** — celular vira assistente sonoro para cegos + alertas ao poder público | Profa. Sandra | Karla Moema, Victor Hugo, Nicolas, Fabio, Yasmin | `G3-<nnn>` |
| 4 | **CasaPiloto** — simulador da construtora: guardar × investir × financiar por tipo de casa | Profa. Polyana | Aliny, André, Michelly, Everson | `G4-<nnn>` |
| 5 | **CasaHumanizada** — programas de moradia num lugar só (nome dado pelo grupo) | Prof. Heitor | Bianca, Giovanna, Estefane | `G5-<nnn>` |

- Os nomes **HoraCerta, VozGuia e CasaPiloto foram propostos por nós** (os grupos só enviaram a ideia). O G2 começou como "RotaViva" e foi **renomeado para GuiaMobi** a pedido do professor (23/09/2026); `Grupo2-RotaViva/` ficou só com um redirecionamento para os links antigos não quebrarem. Trocar é fácil: `nome` em `_gerador/dados.py` + renomear a pasta + `py _gerador/gen.py`.
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
| GuiaMobi | Perto de mim (GPS ou posição simulada), 12 pontos de Cuiabá/VG/Chapada/Pantanal (coordenadas aproximadas), narração por voz, rota por tempo e interesse com esquema SVG, diário, sugestões |
| VozGuia | Botões grandes, voz + vibração, caminhada de treino simulada em VG, mapa colaborativo, alertas com foto e protocolo (resposta do órgão simulada), alto contraste, tutorial falado |
| CasaPiloto | 4 casas piloto com planta SVG e tour, simulador guardar × investir × financiar (Price/SAC, FGTS, aluguel, valorização), semáforo 30% da renda, plano com depósitos e checklist, contato com corretor (simulado, com consentimento) |
| CasaHumanizada | Programas (incl. Casa Cuiabana e MCMV faixas 2025), teste "tenho direito?" local (7 perguntas), checklist de documentos, inscrições com etapas, prazos e central de avisos, agendamento e chat (simulados), alerta anti-golpe |

## 7. Pendências

- [ ] Grupos revisarem os nomes propostos e as 20 perguntas (Parte 2)
- [ ] Confirmar datas reais da defesa e da ida ao shopping (materiais dizem "Setembro de 2026")
- [ ] Conferir `[verificar]` nos Pesquisa-Dados (G1 evasão; G5 unidades MCMV)
- [ ] Conteúdo do GuiaMobi (textos e coordenadas) validar com fontes oficiais
- [ ] Ida ao shopping, tabulação e sprints 3–5 (ver `SPRINTS.md`)

---

## 8. Sessão 23/09/2026 (noite) — estado para continuar amanhã

### 8.1 Feito hoje
- Pacote completo publicado em https://renato0503.github.io/8AdmVG/ (5 grupos, pesquisa verificada, slides + PDFs, coleta, MVPs, hub). Commits `084ce91`, `2d4f11e` (.nojekyll — sem ele o Pages esconde `_pesquisa/` e `_gerador/`), `0a717ef`, `51823a4`.
- **G2 renomeado de RotaViva para GuiaMobi** (pedido do professor). `Grupo2-RotaViva/` ficou só com redirecionamento para os links antigos.
- **G5 Casa Humanizada** recebeu o contexto da apresentação do grupo (Casa Cuiabana 83.991 cadastros, jornada em 4 etapas, 6 funcionalidades, antes × depois); app ganhou Casa Cuiabana, prazos por etapa e central de avisos.
- **Kit CONFACC 2026** montado em `D:\Dev\UnifaccApps\Confacc2026\` (17 resumos das 3 turmas; ver `LEIA-ME.md` de lá).
- **Curso confirmado pela chamada:** Administração (FACC-MT), disciplina Laboratório de Criação e Inovação, turma 2120231N.

### 8.2 Nomes completos (chamada de 23/09/2026)
| Grupo | Integrantes |
|---|---|
| G1 HoraCerta | José Arlindo da Cunha Filho, Taynara Luana de Oliveira, Luana da Silva Araújo, Leticia Leydiane de Oliveira, Samara de Campos Henrique |
| G2 GuiaMobi | Cinthia Ferreira da Silva Oliveira, Danielly Gomes de Souza Pinto, Leandro Teodoro de Santana, Guilherme Henrique Xavier Sampaio, Esther Rodrigues da Conceição |
| G3 VozGuia | Karla Moema Henning Pitaluga, Victor Hugo Gomes de Almeida dos Passos, Nicolas Alexandre Freitas Moraes, Fabio Teyllor Tatehira do Couto, Yasmim Quéren Rodrigues Feitosa |
| G4 CasaPiloto | Aliny Suquerê Guimarães, André Henrique Magalhães Duarte, Michelly de Jesus Pereira Silva, Everson Alencar de Souza |
| G5 Casa Humanizada | Bianca Veronez Dias, Geovanna Shara Soares da Silveira, Estefane Souza da Costa |

- Valéria Cristina dos Santos está na chamada, mas **não entra em nenhum trabalho** (decisão do professor, 25/09/2026).
- **Orientador de todos os trabalhos do CONFACC:** Renato de Oliveira Rosa (25/09/2026).
- `grupos.md` e o site ainda usam os primeiros nomes (decidir se trocar pelos completos; se sim, editar `grupos.md` e rodar `py _gerador/gen.py`, e ajustar os `ContextoApp.md` à mão).

### 8.3 Próximos passos (amanhã)
1. Reabrir o prazo de submissão do CONFACC na plataforma e orientar os grupos a enviar (kit pronto).
2. Seguir as pendências da seção 7 (validação das 20 perguntas com os grupos, datas, `[verificar]`, ida ao shopping).

---

## 9. Sessão 25/09/2026 — MVPs reconstruídos e figuras do CONFACC

### 9.1 MVPs reconstruídos (design e arquitetura próprios)
Os 5 apps (`Grupo<N>/app.html`) foram refeitos com identidade e arquitetura próprias e cada grupo ganhou **landing** (`Grupo<N>/index.html`) no estilo do próprio app, com o app ao vivo num mockup de celular:

| Grupo | App | Arquitetura / destaque |
|---|---|---|
| G1 | HoraCerta | Web Components + IndexedDB (caderneta acadêmica) |
| G2 | GuiaMobi | mapa SVG com pan/zoom, painel deslizante e rotas por URL (o RotaViva virou redirecionamento) |
| G3 | VozGuia | máquina de estados por gestos, voz e vibração (alto contraste) |
| G4 | CasaPiloto | reatividade por Proxy + gráficos em canvas (prancha técnica) |
| G5 | Casa Humanizada | motor de conversa por árvore de diálogo + linha do tempo e prazos |

- `sw.js` **rede-primeiro** nos 5; hub atualizado; publicado no repo `8AdmVG` (Pages ativo).

### 9.2 CONFACC — Figura 1
- As 5 figuras `Gx-Nome-figura1-mvp.png` foram regeradas pelo `build.py` do kit (`D:\Dev\UnifaccApps\Confacc2026\`), que agora também captura apps por **`window.__rotas`** e protege o `preparo` com `try/except`.
- `py build.py` → OK (17 trabalhos).

### 9.3 Continua pendente
- Itens das seções 7 e 8 (validação das 20 perguntas com os grupos, datas, `[verificar]`, ida ao shopping).
- **CONFACC:** preencher e-mails, subir as imagens (quadro1 + figura1) e revisar os textos antes de enviar.

---

## 10. Sessão 06/10/2026 — Termo de Consentimento (TCLE)

- **Termo_Consentimento_8AdmVG.pdf** criado na raiz da pasta, no mesmo padrão visual do TCLE do AdmCBA (Termo_Consentimento_AdmCBA.pdf), gerado via 
eportlab.
- 2 páginas, A4, com: cabeçalho UNIFACC + Curso/Turma, bloco de metadados (Professor, Disciplina, Curso/Turma, Local, Período), 4 blocos laterais (O que é / Como funciona · Riscos e Benefícios / Seus Direitos), contato, Declaração de Ciência e área de assinatura.
- Cita explicitamente os 5 apps do projeto (HoraCerta, GuiaMobi, VozGuia, CasaPiloto, Casa Humanizada) e a disciplina "Laboratório de Criação e Inovação".
- LGPD (Lei 13.709/2018) e e-mail 
enato.rosa@unifacc.edu.br mencionados no documento.
- Script: C:\Users\Renato\AppData\Local\Temp\opencode\gerar_tcle.py (reaproveitável — gera também o do 3SemVG).
- Pendente: gerar variantes _imprimir.pdf e _leve.pdf (caso o professor queira, igual ao AdmCBA tem).


### 10.1 Ajustes finais no TCLE (06/10/2026)
- Removida a seção "Declaração de ciência" e a área de assinatura (o termo é só informativo, **somente entregue**, sem coleta de assinatura no shopping).
- Local corrigido: **Região do Aeroporto de Cuiabá - MT** (sem "shopping center").
- Período corrigido: **8º Semestre de Administração**.
- Script: C:\Users\Renato\AppData\Local\Temp\opencode\gerar_tcle.py.
- Refeito para caber em **1 página A4** com margens/entrelinhas maiores (versão "somente entregue").
- Texto sem adjetivações, sem travessão e com conectivos após o ponto final (Assim, Dessa forma, Por isso, Além disso, Ainda, Por fim).


### 10.2 App de coleta replicado do AdmCBA (06/10/2026)
- `App/index.html` (e cópia idêntica em `coleta/index.html`) refeito a partir do `AdmCBA/App/index.html`, que é o modelo aprovado. O AdmCBA não foi alterado.
- Fluxo: grupo → **Quem está coletando? (aluno)** → perfil por observação → 20 perguntas (escala 1–5 com rótulos intermediários e **confirmação em cada resposta**) → e-mail opcional → código `G<n>-<nnn>`.
- Mantidos da turma: as 20 perguntas, triagem e nota de campo de cada grupo. Acrescentados: `alunos[]` (nomes completos) e cores por grupo; `_gerador/gen.py` passou a mesclar `_gerador/coleta_extra.json` (alunos e cores), então regenerar não apaga a tela do aluno.
- Lista de grupos da home agora vem de `GRUPOS` (antes era fixa de 1 a 6 no modelo, o que quebrava com 5 grupos).
- Sincronização: usa a **mesma planilha Google do AdmCBA** (`DEFAULT_SHEET_URL`, mesma estrutura de colunas). Atenção: os códigos `G<n>-<nnn>` se repetem entre turmas; separar pela coluna `grupoNome`.
- Chaves de `localStorage` próprias: `cd8admvg_*`. READMEs de `App/` e `coleta/` atualizados.
- Teste automatizado (Playwright): fluxo completo em todos os 5 grupos, sem erro.
- Publicado em **repositório próprio da turma** (`renato0503/8AdmVG`, commit `3532404`): https://renato0503.github.io/8AdmVG/coleta/ (no ar e conferido).

## 11. Sessão 20/10/2026 — Resultados da coleta, análise por grupo e publicação

### 11.1 Fonte dos dados e regras de tratamento
- **Planilha de respostas (banco único das 3 turmas):** `1hdR-swgduz5jqhra3OqUNp109xQbrMP42CC_evDXupM`, aba **Respostas** (gid 2144392800), compartilhada como "qualquer pessoa com o link". Colunas: `recebidoEm, codigo, aluno, grupo, grupoNome, criadoEm, faixaEtaria, sexo, classe, raca, orgao, Q1..Q20, email_contato`.
- **Não há coluna de turma.** A turma se deduz por `grupoNome` (nomes únicos entre turmas; na planilha o G5 do 8AdmVG aparece como "CasaHumanizada"). Os códigos `G<n>-<nnn>` **se repetem** (contador local em cada celular), então a chave de unicidade usada é (grupoNome, codigo, criadoEm); 3 duplicatas exatas foram removidas.
- **A triagem de cada grupo (ex.: situação acadêmica, quem cuida das contas, convivência no EDA) NÃO chega à planilha**: o Apps Script só tem a coluna `orgao` (usada pelo Fila Cidadã). Está nos celulares/CSV exportado. Correção pendente: coluna genérica de triagem (e coluna `turma`) no Apps Script.
- **Respostas de arquivo (celular que não sincronizou), somadas ao HTML e fora da planilha:** `coleta-3semvg.json` (8 respostas, G4 SuaCasaSuaVida, atribuídas a Julimary da Silva Amorim) e `cassia_coleta-3semvg.json` (4 respostas de 20 e 21/10, G5 EDA, Cássia Virgínia Aparecida da Silva Nobrega). A G5-001 desse arquivo, de 07/10 (antes da coleta), foi **ignorada** por parecer teste; incluir se for válida (lista `ARQUIVOS` em `_ferramentas/resultados-coleta/build_html.py`). Se o celular sincronizar depois, a deduplicação remove a cópia.
- **Metas por grupo (linhas no gráfico):** 15 (meta inicial), **30 (mínimo total)** e **35 (margem de segurança)**.

### 11.2 Painel de resultados (HTML) e publicação
- **Link da turma (GitHub Pages, repositório próprio):** https://renato0503.github.io/8AdmVG/resultados/
- Arquivos: `resultados/index.html` (só esta turma) e, na raiz de `D:\Dev\UnifaccApps`, `Resultados-Coleta.html` (3 turmas) e `Sintese-Resultados.md` (texto completo das análises).
- Conteúdo: síntese da turma, respostas por grupo, perfil observado, 20 perguntas em barras divergentes (polo A à esquerda, polo B à direita, 3 ao centro), análise estatística, interpretação e **hipótese × resultado × literatura** por grupo.
- **Botão "Atualizar agora":** lê a planilha ao vivo e recalcula tudo no navegador. Em `https://` usa `fetch`; aberto como arquivo local (`file://`) usa JSONP do Google (`gviz`). Alternativa: `python atualizar-resultados.py` (raiz) regrava a cópia embutida nos 4 HTMLs.
- **Privacidade:** o HTML não traz e-mails (coluna `email_contato` removida antes de embutir); traz o nome dos alunos coletores por grupo.
- **Gerador e fontes:** `_ferramentas/resultados-coleta/` (README com o fluxo para regerar).

### 11.3 Método estatístico
- Escala 1–5 entre dois polos (1 = polo A, 5 = polo B); **o sentido de cada pergunta varia**, e média baixa pode significar pouco problema (erro corrigido no EDA, ver 3SemVG).
- Por pergunta: média, DP, %1–2, %4–5, **IC95% por bootstrap** e **teste de permutação (inversão de sinais) contra o ponto neutro 3**, com **correção de Holm** nas 20 perguntas do grupo. "Interesse/utilidade médio" = média por respondente dos itens que começam com Utilidade ou Interesse.
- Amostra de conveniência com 10 a 33 respostas por grupo: leitura exploratória, sem generalização. Efeito de teto e concordância automática reduzem o valor dos itens de utilidade; pesam mais os itens de comportamento e de dor.

### 11.4 Literatura: verificação dos DOIs
- Todos os DOIs dos `Pesquisa-Dados.md` (213 únicos) foram conferidos na API da Crossref (existência e título); só os verificados são citados nas análises.
- **AdmCBA e 8AdmVG:** todas as referências existem e os títulos batem.
- **3SemVG:** 24 referências **não se confirmam** (DOIs inexistentes, de outros artigos ou com autores genéricos como "Doe; Lee", "Smith; Jones", "fake"): Dinheiro na Mão 2 (Chong et al.; Fonseca e Matray; e Kaiser et al. com autoria errada, DOI real), LifePath 2, Quita.AI 2, SuaCasaSuaVida 2, EDA 2 (um DOI aponta para "Issue Information"), **Vida no Controle 14 (todas)**. Para o Vida no Controle e para a parte de carreira do LifePath usei artigos achados por busca na Crossref. **Pendente: avisar os grupos para corrigir os arquivos `Pesquisa-Dados.md`.**
- As notas de paralelo só afirmam o que título e resumo sustentam; resumos vêm dos arquivos dos grupos. Gelper et al. (2026) está só como leitura sugerida (sem resumo na API).

### 11.5 Situação dos grupos (leitura de 20/10/2026, 80 respostas válidas)
| Grupo | Projeto | n | Veredito (hipótese de campo) |
|---|---|---|---|
| G1 | HoraCerta | 15 | Parcialmente sustentada |
| G2 | GuiaMobi | 15 | Parcialmente sustentada |
| G3 | VozGuia | 17 | Sustentada (resultado mais robusto da coleta) |
| G4 | CasaPiloto | 19 | Sustentada |
| G5 | CasaHumanizada | 14 | Parcialmente sustentada; demanda pela solução é alta |

### 11.6 Pendências
- Os textos (`interp.json`, `analise_grupos.json`, `sintese.json`) citam números de uma data; **reler e atualizar quando o n mudar** (a página avisa).
- Recrutar mais respostas nos grupos abaixo de 30 (mínimo total) e de 35 (margem de segurança).
- Corrigir o Apps Script: coluna genérica de triagem e coluna `turma`; reimplantar.
- Commit/push pendentes (não foram feitos de propósito): `context.md`, `Termo_Consentimento_*.pdf` e a pasta local `Resultados/` (Resultados-*.md e estatisticas-por-pergunta.csv, versão descritiva inicial).
- **Sprint R1 (painel 100% mobile): ✅ concluída em 20/10/2026** (tabelas em cartões, toque no lugar de tooltip, seções recolhíveis; zero rolagem horizontal em 320–430 px). Pendente só o teste em aparelho real (Chrome Android e Safari iOS). Detalhes em `SPRINTS.md` (Track R).

## 12. Sessão 21/10/2026 — análise regerada com a base atual

- **Snapshot:** 419 respostas válidas nas 3 turmas (3 duplicatas exatas removidas; 12 respostas de arquivo). **8AdmVG: 151** — HoraCerta 28, GuiaMobi 32, VozGuia 31, CasaPiloto 32, CasaHumanizada 28. A planilha segue recebendo respostas.
- **Regerados:** `Resultados-Coleta.html`, `8AdmVG/resultados/index.html`, `3SemVG/resultados/index.html`, `AdmCBA/resultados/index.html` e `Sintese-Resultados.md` (leitura de 21/10/2026).
- **Textos reescritos** em `_ferramentas/resultados-coleta/`: `interp.json` e `analise_grupos.json` dos 5 grupos do 8AdmVG e dos dois grupos do 3SemVG cujo n mudou (Dinheiro na Mão 29, Vida no Controle 32); `ninterp.json` e `atual.json` sincronizados; `sintese.json` com n = 419, data 21/10/2026 e sínteses geral/das turmas atualizadas.
- **Vereditos 8AdmVG:** VozGuia sustentada (17/20 itens após Holm); CasaPiloto sustentada; HoraCerta, GuiaMobi e CasaHumanizada parcialmente sustentadas (CasaHumanizada com demanda alta: interesse 4,25).
- **Verificação:** as 4 páginas abrem sem erro de JS e sem aviso de "dados mudaram"; o n exibido é igual ao n dos textos nos 17 grupos. `build_html.py` passou a carimbar a data do snapshot dinamicamente.
- **Pendente:** nova leitura quando a base estabilizar (nenhum grupo chegou a 35; HoraCerta e CasaHumanizada estão em 28) e commit/push do `8AdmVG` — `resultados/index.html` mudou.

---

## 13. Sessão 09/11/2026 — Relato Autoetnográfico (formulário e geração de PDFs)

- **Participam:** G1 HoraCerta e G2 GuiaMobi (10 alunos; o professor responsável é Renato, os demais grupos ficam de fora).
- **Nos relatos sai:** Faculdade Católica de Mato Grosso, 8º Semestre, Bacharelado em Administração, FACC-MT.
- **O que é:** cada aluno orientado pelo Prof. Renato responde a um formulário, e as respostas preenchem o modelo oficial do relato autoetnográfico. Um DOCX e um PDF são gerados por aluno.
- **Formulário:** https://renato0503.github.io/relato-autoetnografico/ (repositório `renato0503/relato-autoetnografico`; só a pasta `formulario/` é publicada).
- **Respostas:** planilha privada `1GbpdlfNvbRuIYr051hxfl4SceSFN_l4mEo-LwIV_Kws`, abas `Respostas` (1 linha por aluno; reenvio atualiza) e `Historico` (todos os envios).
- **Geração:** `python gerar.py` em `D:\Dev\UnifaccApps\RelatoAutoetnografico\`; os arquivos saem em `saida/` e o terminal lista quem não respondeu. Fluxo completo no `README.md` de lá.
- **Testado em 09/11/2026:** envio real pela página publicada, reenvio sem duplicar, leitura pelo gerador e geração de DOCX e PDF pelo Word com dados de teste.
- **Pendente:** preencher a área do mestrado em `TITULACAO` no `gerar.py` (sem isso não gera) e apagar a linha `TESTE - APAGAR ESTA LINHA` da planilha, se ainda estiver lá (o gerador a ignora).

---

## 14. Sessão 09/11/2026 — Banners e fichas da III Mostra Synergeia (G1, G3 e G4)

- **Pedido:** banners de apresentação de **Michelly** (CasaPiloto/G4), **Samara** (HoraCerta/G1) e **Karla** (VozGuia/G3), no modelo `Modelo-banner III MOSTRA SYNERGEIA 2026.pptx`, mais as fichas de inscrição.
- **Entregue em** `D:\Dev\UnifaccApps\Mostra-Synergeia-2026\` (com `README.md` próprio):
  - `G1-HoraCerta\`, `G3-VozGuia\`, `G4-CasaPiloto\` → `Banner-*.pptx`, `Banner-*.pdf`, `Ficha-Inscricao-*.docx`, `Ficha-Inscricao-*.pdf`.
- **Banner:** 80 × 120 cm, cabeçalho e rodapé do modelo preservados; título; autores completos + orientador (Renato de Oliveira Rosa); Introdução/Referencial teórico (esquerda) e Procedimentos metodológicos/Considerações finais (direita); Referências na faixa inferior.
- **Texto:** encurtado, justificado, em linguagem direta (problema → solução → dado → próximo passo). Fontes: `Confacc2026/8AdmVG/G<N>-*.md`, `ContextoApp.md`, `Pesquisa-Dados.md` e `Resultados/Resultados-8AdmVG.md` (HoraCerta n = 32; VozGuia n = 34; CasaPiloto n = 34). Só DOIs já verificados.
- **Faixa visual:** logo do app, **print das 3 telas do MVP** (figura do kit CONFACC), **gráfico** das principais respostas (% de respostas 4–5) com destaque numérico e **QR code** do app.
- **QR codes (todos HTTP 200 em 09/11/2026):**
  - HoraCerta: https://renato0503.github.io/8AdmVG/Grupo1-HoraCerta/app.html
  - VozGuia: https://renato0503.github.io/8AdmVG/Grupo3-VozGuia/app.html
  - CasaPiloto: https://renato0503.github.io/8AdmVG/Grupo4-CasaPiloto/app.html
- **Ficha:** Campus **Aeroporto**; modalidade **Apresentação de banner**; todos os autores (campos I–III + linhas extras IV/V quando necessário); orientador; curso **Administração**; disciplina **Laboratório de Criação e Inovação**; **8º Semestre**; figura do MVP na área “COLOQUE A SUA APRESENTAÇÃO A SEGUIR”; espaçamento ajustado para **1 página A4**.
- **Testes:** `validate.py` do kit PPTX → **All validations PASSED** nos banners; fichas em 1 página (PDF); QR apontando para os apps publicados.
- **Scripts preservados:** `Mostra-Synergeia-2026\_scripts\` (gerar_graficos.py, gerar_qr.py, gerar_banners_v2.py, layout_banners.ps1, gerar_fichas.py, exportar_fichas.ps1). Gráficos e QR em `_graficos\`.
- **Pendente:** revisão do conteúdo pelos grupos (nomes, curso, semestre) e commit/push. Nada foi commitado nesta sessão.

---

## 15. Sessão 09/11/2026 — Apresentação do HoraCerta (deck) e conferência da visão de negócio

- **Pedido:** montar a apresentação do HoraCerta com o mesmo motor dos decks do AdmCBA (origem `D:\Dev\cerradofinancas\marketing\Palestras`) e garantir no app o bloco das “outras disciplinas”, como no CasaPiloto.
- **Deck entregue:** `Grupo1-HoraCerta\Apresentacao-HoraCerta.html` + `.pdf` (14 slides, palco 1920×1080). Motor em `assets/deck/` (`deck.css`, `deck.js` e fontes), o mesmo das apresentações do AdmCBA.
- **Tema:** indigo/âmbar do HoraCerta, definido em `body[data-tema="h1"]` no próprio HTML.
- **Roteiro (14 slides):** capa; provocação; problema com dados (INEP, CNE/CES, n=32); personas; proposta antes × depois; como funciona com 3 telas do app; pesquisa de campo (75% comprovantes, 69% app único, 47% sem clareza, 59% falta de tempo); missão/visão/valores; SWOT; inovação; roadmap; impacto/KPIs; riscos; fechamento com QR.
- **Assets do deck:** `assets/deck/shots/h1-painel.png`, `h1-atividades.png`, `h1-negocio.png` (capturados do app a 430×900 via Playwright) e `assets/deck/qr/g1.png` (abre o app).
- **Recursos:** notas do apresentador em todos os slides, navegação por teclado/toque, barra de progresso e exportação em PDF pelo `@media print`. PDF gerado com 14 páginas.
- **Landing:** `Grupo1-HoraCerta/index.html` ganhou os links **“Apresentação completa”** (HTML) e **“Apresentação em PDF”**.
- **App:** a aba **Negócio** (plano de negócios, mentoria e ecossistema) **já existia** desde o commit `3a6f2ed`, no mesmo padrão do CasaPiloto; por isso não houve alteração de código no app. Conferido com `_ferramentas/smoke.py`: 8 rotas, 0 erro de JS, 0 px de overflow e estado mantido.
- **Testes:** 14 slides, 0 erro de JS, 0 imagem quebrada; o deck abre por `file://` e por HTTP.
- **Pendente:** revisão do texto pelo grupo e commit/push (nada foi commitado nesta sessão).
