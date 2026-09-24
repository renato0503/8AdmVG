# Contexto do App — CasaHumanizada

**Grupo 5 — CasaHumanizada** · Prof. Heitor · Integrantes: Bianca, Giovanna, Estefane.
Código de coleta: `G5-<nnn>` · Formulário: 20 perguntas · Meta: 15–20 respostas · MVP: [`app.html`](app.html)

> **Enquadramento do grupo:** *Projeto de Gestão da Mudança — Inovação e Gestão Pública.* "Tecnologia para tornar o acesso à moradia simples e humano: centralizando etapas, desmistificando burocracias e preparando pessoas para a inovação pública." (apresentação de Geovanna Shara e Bianca Veronez)

---

## 1. Pitch em uma frase

O CasaHumanizada **centraliza os programas e oportunidades habitacionais** num só lugar, diz em linguagem simples **se a família tem direito**, guia o **checklist de documentos**, mostra o **status do cadastro com etapas e prazos**, envia **notificações** e oferece **atendimento humano** — para que o caminho até a moradia seja simples e digno.

**Pergunta que originou o projeto:** *"Como tornar a jornada de quem busca uma oportunidade de moradia mais simples, clara e humanizada?"*

---

## 2. O problema e a oportunidade (por que agora)

**A dor, perto de casa.** O programa municipal **Casa Cuiabana** (renda familiar bruta de até R$ 2.850, sem imóvel próprio) recebeu **83.991 cadastros** entre 15/07 e 19/09/2025, e o 1º sorteio, em dezembro de 2025, selecionou **1.000 famílias** (500 titulares + 500 em cadastro reserva) ([Prefeitura de Cuiabá](https://www.cuiaba.mt.gov.br/noticias/casa-cuiabana-encerra-inscricoes-com-quase-84-mil-cadastros-realizados)). Ou seja: dezenas de milhares de famílias ficam esperando — e precisam saber em que etapa estão e quais prazos não podem perder.

**A jornada atual do cidadão** tem múltiplas etapas fragmentadas, que geram ansiedade e ruído de informação:

1. Cadastro inicial e triagem
2. Entrega de documentação física
3. Análise rigorosa e seleção
4. Acompanhamento contínuo dos prazos

- **Informação espalhada.** Programas federais, estaduais e municipais em sites diferentes, com regras que mudam — a família não sabe por onde começar.
- **"Será que eu tenho direito?"** Faixas de renda, CadÚnico, prioridades: o critério é confuso e muitos nem tentam.
- **Burocracia e idas repetidas.** Documentos faltando, fila, volta outro dia — muitas famílias desistem no meio.
- **Atendimento pouco humanizado** e **golpes** que exploram a desinformação ("pague para se inscrever").

**Pesquisa que sustenta o problema** (detalhes em `Pesquisa-Dados.md`):
- 83.991 cadastros no Casa Cuiabana em 2025; 1.000 selecionados no 1º sorteio (Prefeitura de Cuiabá).
- Déficit de 6,2 milhões de domicílios em 2022, 52,2% por ônus excessivo com aluguel (FJP); nova estimativa de 5,9 milhões apresentada em 2025.
- MCMV retomado (Lei nº 14.620/2023), com mais de 1,9 milhão de unidades contratadas desde 2023.
- **Ônus administrativo** (custos de aprender, cumprir exigências e desgaste psicológico) exclui quem tem direito (Bækgaard & Tankink, 2021).
- Autoatendimento digital sem apoio transforma o cidadão em "assistente social acidental" (Madsen et al., 2021).
- O desenho do processo define quem consegue benefício habitacional (Aiken et al., 2023).

**Hipótese de campo:** muitas famílias com direito **não se inscrevem ou desistem** por **falta de informação clara, burocracia e atendimento pouco humanizado**.

**Por que agora.** Retomada e ampliação do MCMV (inclusive Faixa 4), celular como principal acesso à internet (65% só pelo celular — TIC 2025) e agenda de governo digital centrado no cidadão.

---

## 3. Público e personas

**Persona 1 — Josiane, 38 anos, diarista, mãe solo de 3 filhos.** Paga R$ 900 de aluguel com renda de cerca de R$ 2.200. Dor: já ouviu falar do MCMV mas não sabe onde se inscrever e tem medo de golpe. Quer: saber se tem direito e o que levar, sem perder dia de trabalho.

**Persona 2 — Seu Antônio, 66 anos, aposentado, mora de favor com a filha.** Pouca familiaridade com celular. Dor: não entende sites do governo. Quer: falar com uma pessoa.

**Persona 3 — Carla, 27 anos, técnica de enfermagem, renda familiar de R$ 5.500.** Dor: acha que "programa do governo é só para quem ganha muito pouco". Quer: saber se a faixa dela tem financiamento facilitado.

**Persona 4 — Servidor(a) da habitação/assistência.** Dor: atende muitas dúvidas repetidas e famílias sem documentos. Quer: famílias que chegam informadas e com a documentação certa.

---

## 4. Proposta de valor (mini canvas)

| Bloco | Conteúdo |
| --- | --- |
| **Tarefa do usuário** | Encontrar e conseguir uma solução de moradia a que tem direito. |
| **Dores** | Não saber se tem direito, informação espalhada, documentos, filas, golpes, atendimento frio. |
| **Ganhos** | Clareza, economia de viagens, segurança contra golpes, acompanhamento, acolhimento. |
| **Solução** | Catálogo de programas com fonte oficial + teste "tenho direito?" local + checklist de documentos + acompanhamento de etapas + agendamento e chat. |
| **Canais** | Site/app responsivo; CRAS e plantões presenciais; parceria com prefeitura. |
| **Proposta de valor** | "Moradia é direito; o caminho até ela tem que ser simples." |
| **Alternativa atual** | Ir ao CRAS/prefeitura sem saber o que levar, redes sociais, "conhecidos", atravessadores. |

---

## 5. Jornada do usuário

**Descobrir.** Vê os programas por esfera (federal, estadual, municipal), com quem pode participar e onde se inscrever — e o alerta contra golpes.

**Testar.** Responde 6 perguntas (renda da família em faixa, imóvel, CadÚnico, situação de moradia, prioridades, entidade); recebe "parece compatível / talvez / não parece", com o motivo.

**Preparar.** O checklist de documentos se ajusta aos programas escolhidos.

**Acompanhar.** Registra o protocolo e marca as etapas (inscrição → documentos → análise → seleção → contrato → chaves).

**Ser atendido.** Agenda atendimento presencial ou tira dúvidas no chat.

---

## 6. Funcionalidades — MVP | v1 | v2

As seis funcionalidades propostas pelo grupo — **Consulta de oportunidades**, **Requisitos claros**, **Notificações ativas**, **Checklist de documentos**, **Status do cadastro** e **Etapas e prazos** — estão todas representadas no MVP:

| Capacidade | MVP (neste repositório) | v1 | v2 |
| --- | --- | --- | --- |
| Consulta de oportunidades | ✅ programas municipais (incl. Casa Cuiabana), estaduais e federais, com link oficial | Atualização por equipe/curadoria | Integração com dados abertos |
| Requisitos claros | ✅ resumo sem jargão + teste "tenho direito?" no aparelho | Regras por município | Pré-cadastro com consentimento |
| Checklist de documentos | ✅ ajustado aos programas acompanhados | Foto dos documentos guardada com segurança | Envio direto ao órgão |
| Status do cadastro | ✅ linha do tempo por etapa (marcada pelo usuário) | Status automático via órgão | Integração com o sistema da prefeitura |
| Etapas e prazos | ✅ prazo por etapa, com contagem de dias | Prazos oficiais por edital | Calendário integrado |
| Notificações ativas | ✅ central de avisos no app (simulada) | Notificação push/WhatsApp | Alertas personalizados |
| Atendimento humano | ✅ agendamento e chat **simulados** | Plantão real com servidores/voluntários | Chat com atendente + IA supervisionada |

### Antes × depois (gestão da mudança)

| Cenário anterior | Com o CasaHumanizada |
| --- | --- |
| Informações difíceis de localizar | Informações totalmente centralizadas |
| Dúvidas frequentes sobre documentos | Checklist guiado e interativo |
| Dificuldade em acompanhar etapas | Acompanhamento do status em tempo real |
| Risco constante de perder prazos | Notificações e lembretes automáticos |
| Linguagem complexa e burocrática | Linguagem simples, clara e inclusiva |

A mudança não é só tecnológica: exige preparar **servidores** (publicar prazos e status de forma aberta, atender com linguagem simples) e **cidadãos** (confiar no canal digital, com apoio presencial para quem precisa).

---

## 7. Diferenciais e alternativas

| Alternativa | Limitação | Diferencial do CasaHumanizada |
| --- | --- | --- |
| Site gov.br de cada programa | Um site por programa; linguagem técnica | Tudo num lugar, em linguagem simples |
| Ir direto ao CRAS/prefeitura | Idas repetidas, falta de documento | Chega preparado, com checklist |
| Redes sociais e "conhecidos" | Informação errada, golpes | Fonte oficial e alerta contra golpe |
| Atravessadores | Cobram por algo gratuito | Gratuito e transparente |

**Diferencial central:** digital **e** humano — reduz o ônus administrativo sem transferi-lo para quem tem menos recursos.

---

## 8. Dados, governo e LGPD

- **Renda e situação de moradia são dados sensíveis na prática:** o teste roda **só no aparelho**, sem envio.
- **Nunca** pedir senha gov.br, dados bancários ou pagamento.
- **Não substitui o cadastro oficial**: o app informa, organiza e encaminha; a decisão é do órgão.
- **Direitos do titular:** exportar e apagar tudo (já no MVP).

---

## 9. Impacto e sustentabilidade

**Impacto:** mais famílias elegíveis chegando aos programas; menos desistências e golpes; atendimento público mais eficiente; efeitos econômicos locais da habitação social (Marca et al., 2026).

**Sustentabilidade (hipóteses):** parceria com prefeituras e governo estadual; extensão universitária; editais de inovação social; gratuito para o cidadão.

---

## 10. Métricas de sucesso (KPIs)

| KPI | O que mede |
| --- | --- |
| Testes "tenho direito?" concluídos | Alcance e clareza |
| Checklists completos antes do atendimento | Preparo das famílias |
| Idas ao órgão por inscrição concluída | Redução do ônus administrativo |
| Inscrições acompanhadas até a entrega | Persistência no processo |
| Satisfação com o atendimento | Humanização |
| Relatos de golpe evitado | Proteção ao cidadão |

---

## 11. Riscos e mitigação

| Risco | Impacto | Mitigação |
| --- | --- | --- |
| Regras desatualizadas | Alto | Data de referência + link oficial + revisão periódica |
| App confundido com canal oficial / golpe | Alto | Identidade clara, sem cobrança, sem pedir senha |
| Falsa expectativa ("o app me deu a casa") | Alto | Linguagem de orientação, não de aprovação |
| Exclusão digital | Médio | Atendimento presencial e linguagem simples |
| Dados sensíveis | Alto | Processamento local e minimização |

---

## 12. Roadmap de sprints

| Sprint | Nome | Entregáveis |
| --- | --- | --- |
| 0 | Fundação | App de coleta + perfil |
| 1 | Perguntas | 20 perguntas 1–5 |
| 2 | Código | `G5-<nnn>` + exportação |
| 3 | Campo | Coleta (15–20) + áudios, com cuidado de tema sensível |
| 4 | Análise | Blocos + hipótese |
| 5 | Refino | MVP ajustado + apresentação |

---

## 13. Como o formulário valida a hipótese

| Bloco | Perguntas | O que investiga | Base |
| --- | --- | --- | --- |
| 1 | Q1–Q5 | Moradia e necessidade | Forcel et al. (2026); Villa et al. (2022) |
| 2 | Q6–Q10 | Informação sobre os programas | Euclydes et al. (2022); Vieira et al. (2021) |
| 3 | Q11–Q15 | Cadastro, atendimento e acompanhamento | Bækgaard & Tankink (2021); Madsen et al. (2021) |
| 4 | Q16–Q20 | O app CasaHumanizada | Djatmika et al. (2025); Aiken et al. (2023) |

**Leitura:** Q1/Q3 altas (necessidade) com Q6/Q7 baixas (não conhece, não sabe se tem direito) confirmam o **gargalo de informação**. Q11/Q12 baixas e Q13 alta confirmam o **ônus administrativo**; Q14 mede a **humanização**. Q19 (confiança em enviar documentos) indica se o app deve priorizar o digital ou o atendimento presencial.

---

## 14. Pitch de 30 segundos

"Você paga um aluguel que pesa no bolso e já ouviu falar de programa de moradia, mas não sabe se tem direito, que documentos levar nem onde se inscrever? O CasaHumanizada reúne todos os programas num lugar só, faz um teste rápido pra você saber se se encaixa, organiza os documentos e mostra em que etapa está o seu processo — com gente de verdade pra ajudar quando precisar. Moradia é direito; o caminho até ela tem que ser simples."
