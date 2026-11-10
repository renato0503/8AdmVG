# Log de Sprints — App de Formulário (Customer Discovery · 8AdmVG)

Registro do desenvolvimento do app de formulário usado na **Parte 3** (ida ao shopping), desde a fundação até o app ficar **pronto**.

> Regra: **se não está escrito, não aconteceu.** Toda sprint fecha com data, entrega, verificação e bloqueios.

---

## Roadmap

| Sprint | Objetivo | Entrega | Verificação | Status |
|---|---|---|---|---|
| **0** | Fundação | Estrutura do app + Bloco de perfil | Perfil aparece em nova resposta | ✅ concluída |
| **1** | Perguntas do grupo | Blocos de perguntas no app | Perguntas na ordem e tipos corretos | ✅ concluída |
| **2** | Código + planilha | Código por resposta + respostas na planilha | Salvar gera linha e incrementa o código | ✅ concluída |
| **3** | Campo + correlação | Coleta no shopping + áudios ligados por código | Todo áudio começa por código válido | ⏳ a fazer |
| **4** | Análise | Tabulação quanti + leitura quali | Achados com % e frases por código | ⏳ a fazer |
| **5** | Refino final | App pronto + relatório de achados | DoD cumprido e relatório entregue | ⏳ a fazer |

**Legenda de status:** ⏳ a fazer · 🔄 em andamento · ✅ concluída · ⛔ bloqueada

---

## Definição de pronto (DoD)

- [ ] Testado no celular com respostas reais de teste
- [ ] Bloco de perfil gravando corretamente
- [ ] Perguntas na ordem final, sem erro de tipo
- [ ] Código aparecendo e incrementando a cada resposta
- [ ] Respostas caindo automaticamente na planilha
- [ ] Áudios correlacionáveis (todo áudio tem código)
- [ ] Sem erro bloqueante em uso contínuo

---

## Modelo de registro

```
SPRINT ___   Data: __/__   Responsável: ____________

Objetivo:    ______________________________________
Entregue:    ______________________________________
Verificação: ______________________________________
Bloqueios:   ______________________________________
Próxima:     ______________________________________
Status:      ⏳ / 🔄 / ✅ / ⛔
```

---

## Registro

### Sprint 0 — Fundação
- **Data:** 23/09/2026 · **Responsável:** Renato
- **Entregue:** `App/index.html` (base do 3SemVG, com as correções já feitas lá: bug do `forEach` no Bloco 0, botão voltar no e-mail/TCLE, sync opcional com Google Sheets, compartilhar/mesclar JSON) + triagem e nota de campo por grupo.
- **Status:** ✅ concluída

### Sprint 1 — Perguntas do grupo
- **Data:** 23/09/2026 · **Responsável:** Renato
- **Entregue:** 5 × 20 = **100 perguntas** injetadas por `_gerador/gen.py` a partir de `_gerador/dados.py` (fonte única também dos `formulario-app.md`). `coleta/` é cópia idêntica publicada.
- **Verificação:** 100 perguntas no app; gerador falha se algum grupo não tiver exatamente 20.
- **Próxima:** validação das perguntas com os grupos (Parte 2).
- **Status:** ✅ concluída (sujeita à validação em aula)

### Sprint 2 — Código + planilha
- **Status:** ✅ herdada do 3SemVG (código `G<n>-<nnn>`, export CSV/JSON, sync opcional) — testar com a planilha real da turma.

### Sprints 3–5
- **Status:** ⏳ a fazer (campo, análise, refino)

## Registro — Painel de resultados (Track R)

### Sprint R1 — Painel de resultados 100% mobile ✅
- **Data do registro:** 20/10/2026 (pedido do professor; ainda não iniciada)
- **Objetivo:** o painel de resultados (`resultados/index.html`, link do GitHub Pages compartilhado com os alunos) deve **caber na tela do celular**, sem rolagem horizontal e com leitura confortável, em qualquer largura de 320 a 430 px (e paisagem).
- **Escopo previsto:**
  - Garantir zero rolagem horizontal em 320, 360, 390 e 430 px: tabelas (análise estatística, "Ver como tabela", literatura) viram **cartões empilhados** ou ganham versão compacta, sem estourar a largura.
  - Reorganizar o topo para telas estreitas: título, botão **Atualizar agora**, tema, abas de turma e seletor de grupo (chips) em linhas que quebram bem, com alvos de toque de pelo menos 44 px.
  - Substituir o **tooltip de passar o mouse** por toque (abrir/fechar um detalhe da pergunta ao tocar na barra).
  - Gráfico das 20 perguntas: pergunta acima da barra em largura total, média em destaque, polos A e B legíveis; testar a escala de fonte (16 px mínimo no corpo, sem zoom automático).
  - Cartões de indicadores (KPIs) e gráfico "Respostas por grupo" (linhas 15, 30 e 35) legíveis em coluna única; rótulos das metas sem sobreposição.
  - Textos longos (síntese, interpretação, hipótese × resultado × literatura): parágrafos curtos, seções recolhíveis (abrir/fechar) para reduzir a rolagem.
  - Modo escuro e claro mantidos; botão de atualizar fixo ou de fácil acesso no celular.
- **Critérios de aceite:** (1) sem rolagem horizontal nas larguras acima; (2) todos os controles tocáveis com o polegar; (3) nenhum texto cortado; (4) carrega em rede móvel em poucos segundos; (5) testado em Chrome Android e Safari iOS (ou emulação) e com teste automatizado de largura (Playwright) em 320/360/390/430 px.
- **Onde mexer:** `_ferramentas/resultados-coleta/template2.html` (CSS responsivo e JS de renderização); regerar com `build_html.py` e atualizar os dados com `atualizar-resultados.py`; republicar os 3 `resultados/index.html` e `Resultados-Coleta.html`.
- **Estado atual (ponto de partida):** já há regras responsivas básicas (grade em coluna única abaixo de 700 px, sem rolagem horizontal na página em 390 px), mas as tabelas largas, o tooltip por mouse e os textos longos não foram otimizados para celular.
- **Entregue em 20/10/2026:**
  - **Tabelas viram cartões** em telas de até 700 px (análise estatística e "Ver como tabela"): pergunta, polos, contagens 1–5 e média empilhados; sem rolagem horizontal.
  - **Toque no lugar do tooltip:** tocar numa pergunta abre o detalhe (contagem de cada nota, média, n); teclado (Enter/espaço) também funciona. O tooltip por mouse continua no desktop.
  - **Seções recolhíveis** (síntese geral, análise estatística, hipótese × resultado × literatura): abertas no desktop; no celular a síntese geral e a literatura começam fechadas. O estado aberto/fechado é mantido ao trocar de grupo.
  - Topo reorganizado (botão Atualizar agora em largura total), abas/chips/botões com **mínimo de 44 px**, texto base de 16 px, cartões de indicadores em 2 colunas, links DOI com quebra de linha e área de toque.
- **Verificação (Playwright, toque emulado, 320/360/390/430 px; 360 px em modo escuro):** excesso horizontal de **174 px para 0 px**; alvos de toque menores que 44 px de **17–18 para 0**; sem erro no console; desktop sem regressão. Teste reutilizável: `_ferramentas/resultados-coleta/audit_mobile.py <url>`.
- **Status:** ✅ concluída (20/10/2026). Pendente apenas teste em aparelho real (Chrome Android e Safari iOS).
