# Contexto do App — CasaPiloto

**Grupo 4 — CasaPiloto** · Profa. Polyana · Integrantes: Aliny, André, Michelly, Everson.
Código de coleta: `G4-<nnn>` · Formulário: 20 perguntas · Meta: 15–20 respostas · MVP: [`app.html`](app.html)

---

## 1. Pitch em uma frase

O CasaPiloto é um simulador oferecido por **construtoras**: o cliente escolhe o **tipo de casa** (a casa piloto) e vê, lado a lado, quanto precisa **guardar**, quanto renderia **investindo** e quanto custa **financiar** — e sai com um plano mensal até a chave.

---

## 2. O problema e a oportunidade (por que agora)

- **O sonho não vira número.** O cliente se encanta no decorado, mas não sabe quanto guardar por mês, em quanto tempo junta a entrada ou se a parcela cabe na renda.
- **Três caminhos, nenhuma comparação.** Guardar e comprar à vista, investir, ou dar entrada e financiar — ninguém mostra os três juntos, com aluguel e valorização no meio.
- **Desconfiança do plantão.** A simulação feita só pelo corretor, na hora da venda, gera sensação de pressão.
- **Para a construtora:** visitas que não viram venda e clientes reprovados na análise de crédito.

**Pesquisa que sustenta o problema** (detalhes em `Pesquisa-Dados.md`):
- R$ 134,6 bilhões em financiamento habitacional no 1º semestre de 2025 (+25%) (Abecip).
- Nova Faixa 4 do MCMV (renda até R$ 12 mil, imóvel até R$ 500 mil, 10,5% a.a.) em 2025.
- Déficit de 6,2 milhões de domicílios, 52,2% por ônus excessivo com aluguel (FJP, 2022).
- Apresentar a dívida como parcela mensal melhora a compreensão da hipoteca (Thorp et al., 2023); menor letramento financeiro leva a escolhas piores (Ilan & Mugerman, 2025).
- Autocontrole na poupança pesa na chance de virar proprietário (Schlafmann, 2021).
- Tour em realidade virtual reduz o tempo de venda em 28%–49% sem mudar o preço (Yan et al., 2024).

**Hipótese de campo:** as pessoas não compram (ou compram mal) porque **não traduzem o sonho da casa em números mensais** e desconfiam da simulação feita só no plantão.

---

## 3. Público e personas

**Persona 1 — Aline e Rafael, 31 e 33 anos, pagam R$ 1.300 de aluguel.** Querem a casa de 3 quartos antes do segundo filho. Dor: não sabem se juntam mais ou financiam já. Quer: comparar os caminhos com o aluguel entrando na conta.

**Persona 2 — Everaldo, 45 anos, autônomo.** Renda variável, medo de parcela longa. Dor: nunca sabe quanto consegue guardar. Quer: meta mensal realista e lembretes.

**Persona 3 — Gerente comercial da construtora.** Dor: muita visita, pouca venda qualificada. Quer: leads que chegam sabendo o modelo, a faixa de renda e o caminho escolhido.

---

## 4. Proposta de valor (mini canvas)

| Bloco | Conteúdo |
| --- | --- |
| **Tarefa do usuário** | Comprar a casa certa, no momento certo, sem se afogar em parcela. |
| **Dores** | Não saber quanto guardar, medo da parcela, juros incompreensíveis, pressão de venda. |
| **Ganhos** | Plano mensal, comparação clara, confiança, chegar ao corretor preparado. |
| **Solução** | Catálogo de casas piloto + simulador guardar × investir × financiar (Price/SAC, FGTS, valorização, aluguel) + plano com depósitos e lembretes. |
| **Canais** | PWA com a marca da construtora; QR Code no decorado; site e anúncios. |
| **Proposta de valor (cliente)** | "Escolha a casa e veja o caminho." |
| **Proposta de valor (construtora)** | Lead qualificado e venda mais rápida. |
| **Alternativa atual** | Simulador do banco (sem a casa), planilha, corretor no plantão. |

---

## 5. Jornada do usuário

**Escolher.** Navega pelos modelos, vê a planta e o tour virtual.

**Simular.** Informa faixa de renda, quanto consegue guardar, aluguel atual e FGTS; ajusta premissas (entrada, prazo, juros, rendimento, valorização).

**Comparar.** Vê o tempo até a casa em cada caminho, a parcela Price e SAC, o total pago ao banco e o semáforo da parcela na renda.

**Planejar e agir.** Cria o plano: meta da entrada, depósitos, lembrete mensal e checklist de documentos. Quando estiver pronto, envia a simulação ao corretor (com consentimento).

---

## 6. Funcionalidades — MVP | v1 | v2

| Capacidade | MVP (neste repositório) | v1 | v2 |
| --- | --- | --- | --- |
| Catálogo de casas piloto | ✅ 4 modelos de exemplo + planta SVG | Modelos reais da construtora | Personalização de acabamento com preço |
| Simulador de 3 caminhos | ✅ Price, SAC, FGTS, aluguel, valorização | Taxas atualizadas automaticamente | Pré-análise de crédito com parceiro |
| Tour virtual | ✅ cômodo a cômodo (ilustrativo) | Fotos 360° | VR/AR |
| Plano de poupança | ✅ depósitos, lembrete, checklist | Notificações reais | Integração com conta/investimento |
| Contato com corretor | ✅ simulado, com consentimento | CRM da construtora | Agendamento de visita |

---

## 7. Diferenciais e alternativas

| Alternativa | Limitação | Diferencial do CasaPiloto |
| --- | --- | --- |
| Simulador do banco | Só financiamento; não conhece a casa | Parte do modelo de casa e compara 3 caminhos |
| Corretor no plantão | Pressão de venda | O cliente simula sozinho, no tempo dele |
| Planilha | Difícil e sem juros compostos/valorização | Cálculo pronto e visual |
| Portais imobiliários | Anúncio, não planejamento | Plano mensal até a chave |

---

## 8. Dados, governo e LGPD

- **Sem renda exata:** só faixa de renda; cálculo feito no aparelho.
- **Consentimento explícito** para compartilhar a simulação com a construtora.
- **Transparência:** simulações são estimativas, não proposta de crédito; premissas visíveis e editáveis.
- **Finalidade limitada:** dados usados só para o atendimento solicitado.

---

## 9. Impacto e sustentabilidade

**Impacto:** famílias mais preparadas, menos inadimplência, menos compras por impulso; construtora com funil de vendas mais eficiente.

**Sustentabilidade (hipóteses):** licença SaaS para construtoras (white label) por empreendimento; comissão por lead qualificado; gratuito para o comprador.

---

## 10. Métricas de sucesso (KPIs)

| KPI | O que mede |
| --- | --- |
| Simulações concluídas | Uso do simulador |
| Planos criados e depósitos registrados | Engajamento de longo prazo |
| Leads enviados ao corretor | Conversão para a construtora |
| Taxa de aprovação de crédito dos leads | Qualidade do preparo |
| Tempo entre visita e venda | Eficiência comercial |

---

## 11. Riscos e mitigação

| Risco | Impacto | Mitigação |
| --- | --- | --- |
| Taxas/regras desatualizadas | Alto | Premissas editáveis, data de referência, revisão mensal |
| Cliente tomar a simulação como promessa | Alto | Aviso claro de estimativa |
| Viés da construtora (empurrar venda) | Médio | Mostrar também "guardar" e "investir" |
| Dados pessoais no contato | Médio | Consentimento e minimização |
| Baixa adoção por construtoras | Médio | Piloto com uma construtora de VG/Cuiabá |

---

## 12. Roadmap de sprints

| Sprint | Nome | Entregáveis |
| --- | --- | --- |
| 0 | Fundação | App de coleta + perfil |
| 1 | Perguntas | 20 perguntas 1–5 |
| 2 | Código | `G4-<nnn>` + exportação |
| 3 | Campo | Coleta (15–20) + áudios |
| 4 | Análise | Blocos + hipótese |
| 5 | Refino | MVP ajustado + apresentação |

---

## 13. Como o formulário valida a hipótese

| Bloco | Perguntas | O que investiga | Base |
| --- | --- | --- | --- |
| 1 | Q1–Q5 | Desejo e momento da compra | Hassan et al. (2021); Kaynak et al. (2022) |
| 2 | Q6–Q10 | Guardar, investir e financiar | Thorp et al. (2023); Schlafmann (2021) |
| 3 | Q11–Q15 | Relação com a construtora | Lee & Liu (2025); Hu et al. (2024) |
| 4 | Q16–Q20 | O simulador CasaPiloto | Azmi et al. (2021); Yan et al. (2024) |

**Leitura:** Q1 alta com Q6/Q9 baixas e Q10 alta confirmam a hipótese (desejo forte, números nebulosos, medo da parcela). Q4 baixa e Q12 alta confirmam a **desconfiança do plantão**. Q15 mostra se o cliente aceita compartilhar faixa de renda — decisivo para o modelo de negócio.

---

## 14. Pitch de 30 segundos

"Você visitou o decorado, se apaixonou pela casa, mas saiu sem saber se consegue comprar. No CasaPiloto você escolhe o tipo de casa e vê, lado a lado, quanto precisa guardar por mês, quanto renderia investindo e quanto custa financiar. Tudo no seu celular, no seu tempo, antes de falar com o corretor. A casa dos sonhos vira um plano com data para acontecer."
