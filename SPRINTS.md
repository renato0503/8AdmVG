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
