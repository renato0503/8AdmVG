# Contexto do App — HoraCerta

**Grupo 1 — HoraCerta** · Prof. Renato · Integrantes: José Arlindo, Taynara, Luana, Leticia, Samara.
Código de coleta: `G1-<nnn>` · Formulário: 20 perguntas · Meta: 15–20 respostas · MVP: [`app.html`](app.html)

---

## 1. Pitch em uma frase

O HoraCerta é o app único do aluno de graduação para **acompanhar em tempo real** as horas complementares e de extensão — saldo por categoria, comprovantes guardados no celular e eventos que valem horas — e, para a faculdade, **validação organizada e sem papel**.

---

## 2. O problema e a oportunidade (por que agora)

Todo aluno de graduação precisa cumprir **atividades complementares** previstas no projeto pedagógico do curso e, desde a Resolução CNE/CES nº 7/2018, **atividades de extensão** (mínimo de 10% da carga horária). O controle ainda é artesanal:

- **O aluno não enxerga o saldo.** Ele não sabe quantas horas já foram validadas, quantas estão em análise e quantas faltam por categoria — e descobre o problema no último semestre.
- **Comprovantes se perdem.** Certificados em papel, e-mails antigos, prints: a prova da atividade some justamente quando precisa ser entregue.
- **A validação é lenta e manual.** A secretaria confere certificado por certificado, aplica tetos por categoria e devolve (ou recusa) semanas depois.
- **O aluno que trabalha não fica sabendo** de palestras, cursos e projetos que valeriam horas.

**Pesquisa que sustenta o problema** (detalhes em `Pesquisa-Dados.md`):
- 9,9 milhões de matrículas na graduação, 79,3% em instituições privadas (INEP, Censo 2023).
- Na UEPA, o processo de ACC foi descrito como "manual, descentralizado e altamente burocrático", com extravio de comprovantes físicos (Camargo et al., 2026).
- Alunos da Universidade Fumec demonstraram interesse em um aplicativo para gerir as atividades complementares (Aguiar Filho et al., 2024).
- Falta de tempo é a principal barreira para participar de atividades extracurriculares (Le, 2024).
- Painéis de acompanhamento aumentam o engajamento quando o aluno vê o próprio progresso (Ramaswami et al., 2023).

**Hipótese de campo:** a maior dor não é a falta de atividades, mas a **falta de controle** — o aluno não sabe o saldo, perde comprovantes e deixa tudo para o fim.

**Por que agora.** (1) A curricularização da extensão aumentou a quantidade de horas a controlar; (2) 65% dos internautas brasileiros acessam a internet só pelo celular (TIC 2025) — a câmera do celular já é o "scanner" do aluno; (3) as instituições privadas buscam reduzir evasão e retrabalho administrativo.

---

## 3. Público e personas

**Persona 1 — Taís, 21 anos, estudante de Administração que trabalha no comércio.** Estuda à noite e trabalha de dia. Sabe que "precisa de horas", mas não sabe quantas faltam. Dor: perdeu dois certificados de cursos online e não tem tempo para garimpar eventos. Quer: ver o saldo na hora e receber aviso de atividades rápidas.

**Persona 2 — Marcos, 34 anos, aluno EAD no último ano.** Voltou a estudar depois de anos. Dor: descobriu no 7º semestre que suas horas estavam concentradas numa só categoria e várias não contavam por causa do teto. Quer: saber o que falta **por categoria** e um ritmo mensal para fechar a tempo.

**Persona 3 — Profa. Cláudia, coordenadora de curso.** Recebe pilhas de certificados no fim do semestre. Dor: retrabalho, certificados ilegíveis, reclamação de aluno. Quer: uma fila organizada, com comprovante anexado, categoria e horas já informadas, e validação em um toque.

---

## 4. Proposta de valor (mini canvas)

| Bloco | Conteúdo |
| --- | --- |
| **Tarefa do usuário** | Cumprir as horas exigidas sem susto na formatura. |
| **Dores** | Não saber o saldo, perder comprovantes, validação lenta, não ficar sabendo de eventos, falta de tempo. |
| **Ganhos esperados** | Saldo em tempo real, comprovantes seguros, ritmo mensal claro, oportunidades próximas, validação rápida. |
| **Solução** | Painel por categoria + registro de atividade com foto do certificado + agenda de eventos + fila de validação para a coordenação. |
| **Canais** | App/PWA do aluno; painel web da coordenação; parceria com a IES. |
| **Proposta de valor** | "Suas horas, certas, na palma da mão." |
| **Alternativa atual** | Pasta de certificados, e-mail para a secretaria, planilha pessoal, sistema acadêmico genérico. |

---

## 5. Jornada do usuário

**Configurar.** O aluno escolhe o curso; o app carrega o regulamento (total e categorias, com tetos) e a previsão de formatura.

**Registrar.** Participou de algo? Cria a atividade, escolhe a categoria, informa as horas e tira foto do certificado. Fica como rascunho até enviar.

**Enviar e acompanhar.** Envia para validação; o status muda para "em análise". A coordenação valida ou recusa com motivo — e o aluno vê na hora.

**Planejar.** O painel mostra o ritmo necessário (horas/mês até a formatura), a categoria mais atrasada e o próximo evento que resolve essa categoria.

---

## 6. Funcionalidades — MVP | v1 | v2

| Capacidade | MVP (neste repositório) | v1 | v2 |
| --- | --- | --- | --- |
| Saldo por categoria com tetos | ✅ | Regulamento importado do PPC | Vários cursos/dupla formação |
| Registro com comprovante (foto/PDF) | ✅ (no aparelho) | Nuvem segura | Leitura automática do certificado (OCR) |
| Fluxo de validação | ✅ (coordenação simulada) | Painel web real da coordenação | Integração com o sistema acadêmico |
| Agenda de eventos | ✅ (exemplo) | Publicação pela IES e parceiros | Recomendação pelo perfil e tempo livre |
| Ritmo até a formatura | ✅ | Alertas mensais | Previsão de risco de atraso |
| Exportar (CSV/JSON) | ✅ | Relatório PDF para a secretaria | API |

---

## 7. Diferenciais e alternativas

| Alternativa | Limitação | Diferencial do HoraCerta |
| --- | --- | --- |
| Pasta/e-mail de certificados | Perde, não soma, não avisa | Soma por categoria com teto, em tempo real |
| Sistema acadêmico da IES | Mostra só o que já foi validado, muitas vezes tarde | Mostra também o que está em análise e o que falta |
| Planilha pessoal | Trabalhosa e sem comprovante | Foto do certificado vira registro |
| Grupos de WhatsApp de eventos | Informação solta | Agenda filtrada pelo que falta ao aluno |

**Diferencial central:** une **visibilidade para o aluno** e **fluxo de validação para a instituição** num só lugar.

---

## 8. Dados, governo e LGPD

- **Minimização:** só dados acadêmicos necessários (atividade, horas, categoria, comprovante).
- **Finalidade:** comprovação de atividades para integralização curricular.
- **Transparência:** o aluno vê o status e o motivo de cada recusa.
- **Segurança:** no MVP, tudo fica no aparelho (localStorage); na v1, armazenamento com controle de acesso da IES.
- **Direitos do titular:** exportar e apagar os próprios dados (já no MVP).

---

## 9. Impacto e sustentabilidade

**Impacto:** menos alunos com colação atrasada por falta de horas; mais participação em atividades de qualidade; menos retrabalho na secretaria.

**Sustentabilidade (hipóteses a validar):** licença institucional por aluno para IES privadas; versão gratuita para o aluno; parcerias com organizadores de eventos e cursos.

---

## 10. Métricas de sucesso (KPIs)

| KPI | O que mede |
| --- | --- |
| % de alunos com saldo configurado | Adoção inicial |
| Atividades registradas com comprovante | Uso real do "comprovante no bolso" |
| Tempo médio de validação | Eficiência para a coordenação |
| % de recusas | Qualidade das submissões |
| Alunos no último ano com horas completas | Impacto na formatura |
| Inscrições em eventos pelo app | Valor da agenda |

---

## 11. Riscos e mitigação

| Risco | Impacto | Mitigação |
| --- | --- | --- |
| Regulamentos diferentes por curso/IES | Alto | Regulamento configurável (já no MVP) |
| Certificados falsos | Médio | Validação humana + evolução para QR/assinatura digital |
| Baixa adesão da coordenação | Alto | Começar por um curso-piloto na Unifacc |
| Armazenamento de arquivos | Médio | Compressão de fotos (já no MVP); nuvem na v1 |
| Dependência do sistema acadêmico | Médio | Exportação CSV antes de integração |

---

## 12. Roadmap de sprints

| Sprint | Nome | Entregáveis |
| --- | --- | --- |
| 0 | Fundação | App de coleta + perfil por observação |
| 1 | Perguntas | 20 perguntas em escala 1–5 |
| 2 | Código + planilha | Código `G1-<nnn>` + exportação |
| 3 | Campo | Coleta no shopping (15–20) + áudios |
| 4 | Análise | Cruzamento dos blocos e leitura da hipótese |
| 5 | Refino | Ajustes no MVP conforme achados + apresentação |

---

## 13. Como o formulário valida a hipótese

| Bloco | Perguntas | O que investiga | Base |
| --- | --- | --- | --- |
| 1 | Q1–Q5 | Conhecimento das regras e situação das horas | Ribeiro et al. (2023); Santos et al. (2025) |
| 2 | Q6–Q10 | Comprovantes e processo de validação | Camargo et al. (2026); Aguiar Filho et al. (2024) |
| 3 | Q11–Q15 | Oportunidades, tempo e motivação | Chapman et al. (2023); Le (2024) |
| 4 | Q16–Q20 | App e acompanhamento em tempo real | Ramaswami et al. (2023); Alam et al. (2023) |

**Leitura:** se Q4 (clareza do saldo) for baixa e Q5/Q15 (preocupação, deixar para o fim) forem altas, a hipótese de **falta de controle** se confirma. Se Q11 (achar atividades) for o ponto mais crítico, o foco do produto muda para a **agenda de oportunidades**. O bloco 2 mostra se a dor está no **processo da instituição**. O áudio `G1-<nnn>` traz as histórias (o certificado perdido, a correria do último semestre).

---

## 14. Pitch de 30 segundos

"Você está no fim do curso e não sabe quantas horas complementares ainda faltam? Perdeu aquele certificado? O HoraCerta mostra em tempo real quantas horas você já tem validadas, quantas faltam em cada categoria e quais eventos perto de você valem horas. Tirou foto do certificado, está enviado para a coordenação. Sem papel, sem fila, sem susto na formatura. Suas horas, certas, na palma da mão."
