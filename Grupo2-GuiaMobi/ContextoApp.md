# Contexto do App — GuiaMobi

**Grupo 2 — GuiaMobi** · Prof. Renato · Integrantes: Cinthia, Danielly, Leandro, Guilherme, Esther.
Código de coleta: `G2-<nnn>` · Formulário: 20 perguntas · Meta: 15–20 respostas · MVP: [`app.html`](app.html)

---

## 1. Pitch em uma frase

O GuiaMobi é um **guia turístico de bolso**: pela latitude e longitude do celular, mostra o que há de interessante por perto, **conta a história do lugar em áudio** e **monta rotas** que cabem no tempo do visitante — valorizando o comércio e os guias locais.

---

## 2. O problema e a oportunidade (por que agora)

- **Invisibilidade do que está perto.** Visitantes (e muitos moradores) não sabem que existem atrativos a poucos quilômetros — história, cultura, natureza e gastronomia ficam de fora do roteiro.
- **Informação espalhada e sem contexto.** Redes sociais, sites e boca a boca não respondem à pergunta "o que dá para fazer **aqui, agora, com o tempo que eu tenho**?".
- **Roteiro dá trabalho.** Montar uma sequência que caiba em meio período exige pesquisa; guia contratado nem sempre cabe no orçamento.
- **Sinal fraco na natureza.** Em áreas como Chapada e Pantanal, a internet falha — o guia precisa funcionar offline.

**Pesquisa que sustenta o problema** (detalhes em `Pesquisa-Dados.md`):
- 9,3 milhões de turistas internacionais no Brasil em 2025, recorde (Embratur).
- ~1,2 milhão de turistas em Mato Grosso em 2025 (+18%); visitas ao PN da Chapada dos Guimarães passaram de 92 mil (2022) para 183 mil (2025) (Sedec-MT).
- O aeroporto internacional de Várzea Grande é a porta de entrada do estado.
- Tecnologias de turismo inteligente melhoram experiência, satisfação e intenção de revisita (Zhang et al., 2022; Torabi et al., 2022; Pai et al., 2021).
- Privacidade da localização é barreira de adoção (Afolabi et al., 2021; Gao et al., 2023).

**Hipótese de campo:** as pessoas deixam de conhecer atrativos próximos por **não saberem que existem** e **não terem tempo de montar roteiro**.

**Por que agora.** Recordes de turismo, crescimento da Chapada, voz sintética de qualidade nos celulares e hábito de usar o celular como mapa.

---

## 3. Público e personas

**Persona 1 — Laura, 29 anos, analista de São Paulo, em viagem de trabalho a Cuiabá.** Tem uma tarde livre. Dor: não sabe o que vale a pena perto do hotel. Quer: uma rota de 4 horas com o que é imperdível.

**Persona 2 — Seu Jorge, 58 anos, morador de Várzea Grande.** Recebe parentes de fora todo ano. Dor: sempre leva ao mesmo lugar. Quer: ideias novas e histórias para contar.

**Persona 3 — Daniel, 24 anos, mochileiro estrangeiro.** Vai para o Pantanal. Dor: idioma, sinal de internet e segurança. Quer: guia offline, com áudio, e indicação de guias locais confiáveis.

---

## 4. Proposta de valor (mini canvas)

| Bloco | Conteúdo |
| --- | --- |
| **Tarefa do usuário** | Aproveitar o tempo livre num lugar conhecendo o que ele tem de melhor. |
| **Dores** | Não saber o que existe perto, perder tempo procurando, roteiro difícil, sinal fraco, insegurança. |
| **Ganhos** | Descoberta, história contada, rota pronta, economia de tempo, experiência memorável. |
| **Solução** | Lista "perto de mim" + narração em áudio + rotas por tempo e interesse + diário de viagem. |
| **Canais** | PWA; QR Codes em hotéis, aeroporto e restaurantes; parceria com secretarias de turismo. |
| **Proposta de valor** | "O que tem de bom aqui — no seu tempo, na sua mão." |
| **Alternativa atual** | Google Maps, Instagram, TripAdvisor, guia contratado, recepção do hotel. |

---

## 5. Jornada do usuário

**Chegar.** Abre o app (sem cadastro), permite a localização ou escolhe onde está.

**Descobrir.** Vê a lista ordenada por distância, filtra por interesse, toca num lugar e **ouve** a história.

**Planejar.** Informa quanto tempo tem e os interesses; o app monta a rota (vizinho mais próximo dentro do tempo) e narra a sequência.

**Lembrar.** Marca visitados e favoritos; sugere um lugar novo para a curadoria.

---

## 6. Funcionalidades — MVP | v1 | v2

| Capacidade | MVP (neste repositório) | v1 | v2 |
| --- | --- | --- | --- |
| Perto de mim (GPS ou posição simulada) | ✅ | Mapa real | Realidade aumentada |
| Narração em áudio | ✅ voz do navegador | Áudios gravados por guias locais | Vários idiomas |
| Rota por tempo e interesse | ✅ (heurística) | Horários de funcionamento | Recomendação personalizada (IA) |
| Offline | ✅ (dados no app + PWA) | Pacotes por região | Mapas offline |
| Comércio e guias locais | Texto nos pontos | Perfis de parceiros | Reservas e cupons |
| Sugestões da comunidade | ✅ (local) | Curadoria | Avaliações |

---

## 7. Diferenciais e alternativas

| Alternativa | Limitação | Diferencial do GuiaMobi |
| --- | --- | --- |
| Google Maps | Mostra lugares, não conta a história nem monta roteiro por tempo | Rota por tempo + narração |
| Redes sociais | Conteúdo disperso, focado em lugares da moda | Curadoria local e lugares pouco conhecidos |
| Guia contratado | Custo e agenda | Complementa: indica guias locais para passeios que exigem |
| Folhetos/posto de informação | Horário restrito, sem personalização | Disponível 24h, no bolso |

---

## 8. Dados, governo e LGPD

- **Localização processada no aparelho**, usada só para calcular distâncias; nada é enviado no MVP.
- **Consentimento explícito** antes do GPS; alternativa de posição simulada.
- **Conteúdo com fonte:** textos históricos validados com fontes oficiais (Sedec-MT, ICMBio, IPHAN, prefeituras) antes da publicação — no MVP estão marcados como exemplo.
- **Dados agregados** (lugares mais procurados) podem apoiar políticas de turismo, sempre anonimizados.

---

## 9. Impacto e sustentabilidade

**Impacto:** distribuição do fluxo turístico para atrativos menos conhecidos; renda para comércio e guias locais; valorização da história regional.

**Sustentabilidade (hipóteses):** parceria com secretarias de turismo e trade; destaque pago e identificado para negócios locais; pacotes de conteúdo premium (roteiros guiados).

---

## 10. Métricas de sucesso (KPIs)

| KPI | O que mede |
| --- | --- |
| Rotas montadas por usuário | Valor do planejador |
| Narrações ouvidas até o fim | Qualidade do conteúdo |
| Lugares marcados como visitados | Conversão em visita real |
| % de uso com GPS permitido | Confiança/privacidade |
| Sugestões aprovadas | Engajamento da comunidade |
| Cliques para parceiros locais | Impacto econômico |

---

## 11. Riscos e mitigação

| Risco | Impacto | Mitigação |
| --- | --- | --- |
| Informação desatualizada (horários, acesso) | Alto | Curadoria periódica + data da última revisão |
| Segurança em trilhas/natureza | Alto | Avisos e indicação de guia credenciado quando necessário |
| Privacidade da localização | Médio | Processamento local e consentimento |
| Concorrência de grandes plataformas | Médio | Foco em conteúdo local profundo e narração |
| Conteúdo histórico incorreto | Médio | Validação com fontes oficiais |

---

## 12. Roadmap de sprints

| Sprint | Nome | Entregáveis |
| --- | --- | --- |
| 0 | Fundação | App de coleta + perfil |
| 1 | Perguntas | 20 perguntas 1–5 |
| 2 | Código | `G2-<nnn>` + exportação |
| 3 | Campo | Coleta (15–20) + áudios, comparando moradores × visitantes |
| 4 | Análise | Leitura dos blocos e da hipótese |
| 5 | Refino | MVP ajustado + apresentação |

---

## 13. Como o formulário valida a hipótese

| Bloco | Perguntas | O que investiga | Base |
| --- | --- | --- | --- |
| 1 | Q1–Q5 | Hábitos de passeio e conhecimento da região | Ribeiro et al. (2022); Silva et al. (2022) |
| 2 | Q6–Q10 | Informação e orientação no destino | Cilkin & Toksöz (2024); Afolabi et al. (2021) |
| 3 | Q11–Q15 | Rotas e experiência | Mou et al. (2022); Zhang et al. (2022) |
| 4 | Q16–Q20 | O guia de bolso | Xiong & Zhang (2024); Gao et al. (2023) |

**Leitura:** Q4 e Q5 altas + Q6 baixa confirmam a hipótese (não sabem o que existe; perdem tempo). Q19 baixa sinaliza que privacidade da localização é barreira central. A triagem permite comparar **moradores × visitantes**.

---

## 14. Pitch de 30 segundos

"Chegou em Várzea Grande ou Cuiabá e não sabe o que fazer com a tarde livre? O GuiaMobi usa a sua localização para mostrar o que tem de interessante perto de você, conta a história de cada lugar em áudio, como um guia de bolso, e monta uma rota que cabe no seu tempo — da Chapada ao centro histórico, passando pelo comércio local. Menos tempo procurando, mais tempo vivendo o lugar."
