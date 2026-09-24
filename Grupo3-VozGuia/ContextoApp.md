# Contexto do App — VozGuia

**Grupo 3 — VozGuia** · Profa. Sandra · Integrantes: Karla Moema, Victor Hugo, Nicolas, Fabio, Yasmin.
Código de coleta: `G3-<nnn>` · Formulário: 20 perguntas · Meta: 15–20 respostas · MVP: [`app.html`](app.html)

---

## 1. Pitch em uma frase

O VozGuia transforma o celular da pessoa cega ou com baixa visão em um **assistente sonoro** que avisa o que está no caminho — e, com um toque, envia **alertas de acessibilidade ao poder público**, formando um mapa colaborativo que ajuda a cidade a priorizar consertos.

---

## 2. O problema e a oportunidade (por que agora)

- **Autonomia limitada.** Buracos, carros na calçada, piso tátil interrompido e semáforos sonoros quebrados tornam o deslocamento perigoso e dependente de outra pessoa.
- **Tecnologia assistiva cara.** Dispositivos dedicados custam caro e exigem treino; o celular, que a pessoa já tem, é subaproveitado.
- **Problemas que não chegam ao poder público.** Quem enfrenta a barreira raramente consegue registrá-la de forma organizada — e a prefeitura não tem dados para priorizar obras.

**Pesquisa que sustenta o problema** (detalhes em `Pesquisa-Dados.md`):
- 14,4 milhões de pessoas com deficiência no Brasil; **7,9 milhões** com dificuldade de enxergar mesmo com óculos (IBGE, Censo 2022).
- A Lei Brasileira de Inclusão (Lei nº 13.146/2015) garante acessibilidade; normas NBR 9050 e NBR 16537 definem calçadas e piso tátil.
- Soluções de navegação assistiva migram para o smartphone (Abidi et al., 2024); portabilidade e simplicidade são requisitos (Kuriakose et al., 2022).
- Cidades não têm dados confiáveis de acessibilidade das calçadas (Labbé et al., 2023); mapeamento participativo por foto é viável (Morra et al., 2024).

**Hipótese de campo:** a falta de autonomia vem mais da **falta de informação sobre o caminho** do que da falta de tecnologia — e os problemas persistem porque **não chegam ao poder público de forma organizada**.

**Por que agora.** Leitores de tela vêm de fábrica nos celulares; voz sintética em português é de boa qualidade; prefeituras já usam apps de zeladoria (ex.: Colab).

---

## 3. Público e personas

**Persona 1 — Rita, 42 anos, cega desde os 20, atendente de telemarketing.** Vai de ônibus ao trabalho. Dor: o ponto mudou de lugar e ninguém avisou; tropeçou num buraco novo. Quer: saber o que tem no caminho **antes** de chegar lá.

**Persona 2 — Pedro, 67 anos, baixa visão por glaucoma.** Anda pouco sozinho por medo. Dor: perdeu confiança depois de uma queda. Quer: um app simples, com letras grandes e voz lenta, para voltar a caminhar no bairro.

**Persona 3 — Ana, 35 anos, filha de Pedro.** Quer ajudar a mapear o trajeto do pai e cobrar a prefeitura. Quer: registrar obstáculos com foto e acompanhar o protocolo.

**Persona 4 — Secretaria municipal.** Quer dados organizados (onde, o quê, quantas confirmações) para priorizar obras de acessibilidade.

---

## 4. Proposta de valor (mini canvas)

| Bloco | Conteúdo |
| --- | --- |
| **Tarefa do usuário** | Deslocar-se com segurança e autonomia; ver a cidade corrigir barreiras. |
| **Dores** | Obstáculos inesperados, dependência, tecnologia cara, reclamação que não dá em nada. |
| **Ganhos** | Aviso antecipado por voz e vibração, confiança, protocolo acompanhável, cidade mais acessível. |
| **Solução** | Assistente sonoro + mapa colaborativo + alertas com foto e protocolo ao órgão responsável. |
| **Canais** | PWA acessível; associações de pessoas com deficiência visual; prefeitura. |
| **Proposta de valor** | "O caminho falado para você; o problema mostrado para a cidade." |
| **Alternativa atual** | Bengala, cão-guia, ajuda de terceiros, Google Maps com leitor de tela, ouvidoria por telefone. |

---

## 5. Jornada do usuário

**Aprender.** Modo aprendizagem falado explica os botões grandes e as abas.

**Caminhar.** O app avisa por voz e vibração os pontos cadastrados à frente (buraco à direita a 20 m; ponto de ônibus; faixa).

**Registrar.** Encontrou um obstáculo novo? Um toque abre o alerta (tipo, lado, foto opcional); o app gera protocolo e adiciona o ponto ao mapa.

**Acompanhar.** O usuário ouve a situação do alerta (enviado, em análise, resolvido); outros usuários confirmam "ainda está lá" ou "já foi resolvido".

---

## 6. Funcionalidades — MVP | v1 | v2

| Capacidade | MVP (neste repositório) | v1 | v2 |
| --- | --- | --- | --- |
| Avisos por voz e vibração | ✅ pontos cadastrados, trajeto de treino | GPS em tempo real | Detecção de obstáculo pela câmera (IA) |
| Mapa colaborativo | ✅ local, com confirmações | Nuvem compartilhada | Índice de acessibilidade por bairro |
| Alertas ao poder público | ✅ protocolo e etapas **simulados** | Integração com ouvidoria/zeladoria | Painel público de indicadores |
| Acessibilidade (voz, fonte, contraste) | ✅ | Testes com usuários cegos | Comandos de voz |
| Treino | ✅ tutorial falado | Trilhas de treino por trajeto | Parceria com instrutores de O&M |

---

## 7. Diferenciais e alternativas

| Alternativa | Limitação | Diferencial do VozGuia |
| --- | --- | --- |
| Apps de mapa + leitor de tela | Não sabem do buraco na calçada | Mapa de obstáculos da própria comunidade |
| Dispositivos assistivos dedicados | Caros e com treino longo | Usa o celular que a pessoa já tem |
| Ouvidoria por telefone | Sem foto, sem localização precisa, sem acompanhamento | Alerta com local, foto e protocolo |
| Apps de zeladoria gerais | Não pensados para cegos | Interface acessível e recorte de acessibilidade |

---

## 8. Dados, governo e LGPD

- **Dados sensíveis:** deficiência é dado pessoal sensível (LGPD, art. 5º, II) — o app **não pergunta** a condição do usuário.
- **Localização** processada no aparelho; alertas enviam só o local do problema, não o trajeto da pessoa.
- **Fotos:** orientação para não fotografar rostos e placas; na v1, desfoque automático.
- **Dados abertos:** o mapa de obstáculos agregado pode ser publicado para a sociedade e o poder público.

---

## 9. Impacto e sustentabilidade

**Impacto:** mais autonomia e segurança para pessoas cegas e com baixa visão; dados para priorizar obras; cumprimento da LBI.

**Sustentabilidade (hipóteses):** gratuito para o usuário; financiado por prefeituras (licença do painel de gestão), editais de tecnologia assistiva e parcerias com associações.

---

## 10. Métricas de sucesso (KPIs)

| KPI | O que mede |
| --- | --- |
| Deslocamentos com o app | Uso real do assistente |
| Pontos mapeados e confirmados | Qualidade do mapa colaborativo |
| Alertas enviados × resolvidos | Resposta do poder público |
| Tempo médio de resolução | Eficiência da prefeitura |
| Usuários que concluem o tutorial | Adoção da tecnologia assistiva |
| Avaliação de confiança (usuários cegos) | Segurança percebida |

---

## 11. Riscos e mitigação

| Risco | Impacto | Mitigação |
| --- | --- | --- |
| Confiança excessiva no app | Alto | Aviso claro: não substitui bengala, cão-guia ou O&M |
| Mapa desatualizado | Alto | Confirmações da comunidade e expiração de pontos antigos |
| Precisão do GPS (5–10 m) | Médio | Avisar com margem e lado; v2 com beacons |
| Prefeitura não responder | Médio | Painel público de alertas pendentes |
| Interface inacessível | Alto | Testes com usuários cegos desde o MVP |

---

## 12. Roadmap de sprints

| Sprint | Nome | Entregáveis |
| --- | --- | --- |
| 0 | Fundação | App de coleta + perfil |
| 1 | Perguntas | 20 perguntas 1–5 |
| 2 | Código | `G3-<nnn>` + exportação |
| 3 | Campo | Coleta (15–20) + áudios, com protocolo de acessibilidade para entrevistados cegos |
| 4 | Análise | Blocos + hipótese |
| 5 | Refino | MVP ajustado + apresentação |

---

## 13. Como o formulário valida a hipótese

| Bloco | Perguntas | O que investiga | Base |
| --- | --- | --- | --- |
| 1 | Q1–Q5 | Percepção da acessibilidade na cidade | Cohen et al. (2024); Caetano et al. (2021) |
| 2 | Q6–Q10 | Autonomia e tecnologia | Abidi et al. (2024); Kuriakose et al. (2022) |
| 3 | Q11–Q15 | Alertas ao poder público | Labbé et al. (2023); Morra et al. (2024) |
| 4 | Q16–Q20 | O assistente sonoro | See et al. (2022); Martínez-Cruz et al. (2021) |

**Leitura:** Q1–Q4 baixas e Q16/Q17 altas confirmam que o problema é **informação sobre o caminho**. Q12–Q13 baixas e Q14–Q15 altas confirmam o gargalo do **canal com o poder público**. A triagem separa quem **tem ou convive** com deficiência visual — as respostas desse grupo têm peso especial na análise.

---

## 14. Pitch de 30 segundos

"Imagine atravessar a cidade sem enxergar a calçada. O VozGuia transforma o celular em um assistente sonoro: avisa por voz onde está o ponto de ônibus, a faixa e o buraco que alguém já registrou. E, quando encontra um obstáculo novo, com um toque o alerta vai para a prefeitura com local, foto e protocolo. Mais autonomia para quem não enxerga, mais informação para quem precisa consertar a cidade."
