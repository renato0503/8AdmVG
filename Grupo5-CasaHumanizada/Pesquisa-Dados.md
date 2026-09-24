# Pesquisa e Dados — Grupo 5 · CasaHumanizada

> Apoio à defesa da ideia: dados reais (Brasil/MT) + 14 artigos peer-reviewed (2021–2026). Os metadados dos artigos (autores, título, periódico, DOI, citações) foram copiados **automaticamente** dos resultados da API OpenAlex salvos em `_pesquisa/saidas/` — o script `_pesquisa/selecao.py` falha se algum DOI não existir nesses brutos. Números brasileiros têm fonte com link (conferidos em 23/09/2026). O que não foi confirmado está marcado `[verificar]`.

**Grupo:** 5 · CasaHumanizada · **Professor(a):** Prof. Heitor · **Integrantes:** Bianca, Giovanna, Estefane · **Código:** G5-<nnn> · **Meta:** 15–20

**Hipótese de campo:** Muitas famílias que teriam direito a um programa habitacional **não chegam a se inscrever, perdem prazos ou desistem no meio** — não por falta de programas, mas por **falta de informação clara, excesso de burocracia e atendimento pouco humanizado** (o chamado ônus administrativo).

---

## 1. Resumo executivo

O Brasil tinha **6,2 milhões de domicílios em déficit habitacional em 2022** (Fundação João Pinheiro), e o principal componente é o **ônus excessivo com aluguel** — famílias com renda de até 3 salários mínimos que gastam mais de 30% da renda com aluguel (52,2% do déficit). Nova estimativa da FJP apresentada em 2025 aponta **5,9 milhões**. Para enfrentar isso, o Minha Casa, Minha Vida foi retomado (Lei nº 14.620/2023) e já contratou **mais de 1,9 milhão de unidades desde 2023**, com meta ampliada para 3 milhões após a criação da Faixa 4 — mas o acesso depende de informação, CadÚnico atualizado, documentos e muitas idas a órgãos públicos.

A literatura sobre **ônus administrativo** (*administrative burden*) explica por que famílias com direito ficam de fora: custos de aprendizagem (descobrir o programa), de conformidade (documentos, filas) e psicológicos (estigma, desgaste) (Bækgaard & Tankink, 2021). A digitalização pode reduzir esses custos — ou transferi-los ao cidadão, que vira um "assistente social acidental" de si mesmo (Madsen et al., 2021; Peeters, 2022). Em programas de aluguel emergencial nos EUA, o desenho do processo definiu quem conseguiu o benefício (Aiken et al., 2023). No Brasil, estudos do MCMV mostram efeitos econômicos positivos nos municípios (Marca et al., 2026), mas também insatisfação, segregação e desconfiança (Stefani, 2021; Villa et al., 2022). O CasaHumanizada propõe **reduzir o ônus administrativo** com informação centralizada, linguagem simples e atendimento humano.

O caso local deixa isso concreto: o programa municipal **Casa Cuiabana** recebeu **83.991 inscrições** entre julho e setembro de 2025 (Prefeitura de Cuiabá). A jornada — cadastro e triagem, entrega de documentação física, análise e seleção, acompanhamento contínuo dos prazos — tem etapas fragmentadas que geram ansiedade e ruído de informação: exatamente o que a plataforma quer organizar.

---

## 2. Dados e notícias reais

### 2.1 Tabela de dados

| Dado | Número | Ano | Fonte |
|---|---|---|---|
| Inscrições no programa municipal Casa Cuiabana (renda até R$ 2.850, sem imóvel) | 83.991 cadastros entre 15/07 e 19/09 | 2025 | Prefeitura de Cuiabá ([cuiaba.mt.gov.br](https://www.cuiaba.mt.gov.br/noticias/casa-cuiabana-encerra-inscricoes-com-quase-84-mil-cadastros-realizados)) |
| 1º sorteio do Casa Cuiabana | 1.000 selecionados (500 titulares + 500 em cadastro reserva) | dez/2025 | Prefeitura de Cuiabá ([cuiaba.mt.gov.br](https://www.cuiaba.mt.gov.br/noticias/programa-casa-cuiabana-avanca-para-etapa-final-e-se-aproxima-da-assinatura-de-contratos)) |
| Déficit habitacional | 6,2 milhões de domicílios | 2022 | Fundação João Pinheiro (FJP) ([fjp.mg.gov.br](https://fjp.mg.gov.br/deficit-habitacional-no-brasil/)) |
| Ônus excessivo com aluguel urbano (componente do déficit) | 52,2% do déficit — o maior componente | 2022 | FJP / Observatório da Construção (Fiesp) ([fiesp.com.br](https://www.fiesp.com.br/observatoriodaconstrucao/noticias/fundacao-joao-pinheiro-divulga-dados-atualizados-do-deficit-habitacional/)) |
| Déficit habitacional (nova estimativa) | 5,9 milhões de unidades (−4,8% sobre 2022) | divulgado em 2025 | FJP, apresentado na Câmara dos Deputados ([camara.leg.br](https://www.camara.leg.br/noticias/1164400-pesquisa-aponta-que-o-deficit-habitacional-brasileiro-esta-em-59-milhoes-de-unidades/)) |
| Retomada do Minha Casa, Minha Vida | Lei nº 14.620/2023 | 2023 | Planalto ([planalto.gov.br](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14620.htm)) |
| Unidades do MCMV contratadas desde 2023 | mais de 1,9 milhão; meta ampliada para 3 milhões com a Faixa 4 `[verificar número atualizado]` | 2025 | Ministério das Cidades (via imprensa) ([gov.br](https://www.gov.br/cidades/pt-br/assuntos/noticias-1/noticia-mcid-n-1864)) |
| Faixas 1 e 2 (renda até R$ 4.700) | mais de 661 mil unidades contratadas/financiadas até dez/2025 | 2025 | Ministério das Cidades ([gov.br](https://www.gov.br/cidades/pt-br/assuntos/noticias-1/noticia-mcid-n-1864)) |
| Pessoas que usaram a internet (TIC Domicílios 2025) | 88% da população (163 milhões); 65% dos usuários acessam **só pelo celular** | 2025 | Cetic.br / CGI.br ([mobiletime.com.br](https://www.mobiletime.com.br/noticias/09/12/2025/tic-domicilios-2025/)) |

### 2.2 Leitura dos dados

1. **A fila é enorme aqui do lado.** Só o Casa Cuiabana recebeu **83.991 inscrições** em dois meses de 2025, e o 1º sorteio selecionou 1.000 famílias (500 titulares + 500 reserva). A maioria vai esperar — e precisa saber, com clareza, em que etapa está e quais prazos não pode perder.
2. **O problema é aluguel caro.** Mais da metade do déficit não é falta de teto, é aluguel que consome a renda — o público do CasaHumanizada paga aluguel e não sabe se tem direito a algo.
3. **Há programa, falta caminho.** O MCMV cresceu muito desde 2023, mas o acesso passa por CadÚnico, faixas de renda, documentos e prefeitura — cada etapa é um custo para a família.
4. **Informação fragmentada abre espaço para golpe.** Programas federais, estaduais e municipais em sites diferentes geram confusão; um canal único e confiável protege o cidadão.
5. **Digital sem humano exclui.** 65% dos usuários acessam a internet só pelo celular (TIC 2025), muitos com pouco letramento digital — o app precisa de linguagem simples e opção de atendimento humano.
6. **Acompanhar reduz ansiedade e retorno ao balcão.** Saber em que etapa está o processo evita idas repetidas ao órgão público.

---

## 3. Referencial científico (14 artigos, 2021–2026)

### Bloco A. O déficit e o Minha Casa, Minha Vida

**1. Priscila Kauana Barelli Forcel; Elza Luli Miyasaka; Tiago Augusto da Cunha (2026).** Housing deficit and census microdata: methodological framework, challenges, and perspectives. *Cadernos Metrópole*. DOI: [10.1590/2236-9996.2026-6571161-en](https://doi.org/10.1590/2236-9996.2026-6571161-en). Citações (OpenAlex): 1. Acesso: aberto.
- **O que sustenta:** Discute o método de cálculo do déficit habitacional com microdados do Censo, baseado na metodologia da Fundação João Pinheiro, com ganhos de transparência e detalhamento territorial.
- **Como usar na defesa:** Ajuda a explicar de onde vem o número do déficit e por que ele pode ser calculado por município — base para priorizar ações locais.

**2. Fillipe Maciel Euclydes; Vinícius de Souza Moreira; Andréia de Fátima Hoelzle Martins; Suely de Fátima Ramos Silveira (2022).** O processo de política pública do “Minha Casa, Minha Vida”: criação, desenvolvimento e extinção. *Revista de Sociologia e Política*. DOI: [10.1590/1678-98732230e020](https://doi.org/10.1590/1678-98732230e020). Citações (OpenAlex): 3. Acesso: aberto.
- **O que sustenta:** Analisa o processo da política pública do MCMV (criação em 2009, consolidação e extinção em 2021), com fases, modalidades e faixas de renda ao longo de quatro mandatos.
- **Como usar na defesa:** Contexto histórico: o programa muda de nome, regra e faixa com frequência — por isso o cidadão se perde e precisa de um canal atualizado.

**3. Luan Marca; Luis Fernando Tavares Vieira Braga; Adelar Fochezatto; Augusto Mussi Alvim (2026).** Economic, environmental, and spatial impacts of Brazil's Minha Casa Minha Vida program. *Land Use Policy*. DOI: [10.1016/j.landusepol.2026.108081](https://doi.org/10.1016/j.landusepol.2026.108081). Citações (OpenAlex): 1. Acesso: aberto.
- **O que sustenta:** Com diferenças-em-diferenças e econometria espacial (2005–2019), estima que municípios com o PMCMV tiveram PIB per capita ~7,7% maior e salários formais ~5,6% maiores, com efeito anticíclico na recessão de 2014–2016.
- **Como usar na defesa:** Argumento de impacto: habitação social gera desenvolvimento local — ampliar o acesso tem retorno econômico.

**4. Ludmila Ferreira Bandeira; Edgar Reyes (2021).** Programa Minha Casa Minha Vida (2012-2016): análise da eficiência relativa dos municípios brasileiros na execução de programas federais. *Revista de Administração Pública*. DOI: [10.1590/0034-761220190341](https://doi.org/10.1590/0034-761220190341). Citações (OpenAlex): 2. Acesso: aberto.
- **O que sustenta:** Avalia a eficiência relativa dos municípios brasileiros na execução do MCMV (2012–2016) e os fatores que afetam essa eficiência.
- **Como usar na defesa:** Mostra que a capacidade municipal varia muito — o CasaHumanizada pode apoiar prefeituras com menos estrutura.

### Bloco B. A experiência de quem é atendido

**5. Mariane Beatriz Wittmann; David Lorenzi Júnior; Sirlei Glasenapp; Fernando Batista Bandeira da Fontoura (2021).** O Programa Minha Casa Minha Vida sob a Perspectiva dos Beneficiários e Agente Operacional. *Desenvolvimento em Questão*. DOI: [10.21527/2237-6453.2021.55.10215](https://doi.org/10.21527/2237-6453.2021.55.10215). Citações (OpenAlex): 2. Acesso: aberto.
- **O que sustenta:** Com 144 questionários com famílias beneficiárias em Santa Maria/RS e entrevista com o agente operacional, mede a satisfação com o MCMV para orientar a gestão pública.
- **Como usar na defesa:** Modelo de pesquisa próximo da nossa (questionário com beneficiários) — boa referência de método.

**6. Kelmara Mendes Vieira; Aureliano Angel Bressan; Luana dos Santos Fraga (2021).** FINANCIAL WELL-BEING OF THE BENEFICIARIES OF THE MINHA CASA MINHA VIDA PROGRAM: PERCEPTION AND ANTECEDENTS. *RAM. Revista de Administração Mackenzie*. DOI: [10.1590/1678-6971/eramg210115](https://doi.org/10.1590/1678-6971/eramg210115). Citações (OpenAlex): 18. Acesso: aberto.
- **O que sustenta:** Mede o bem-estar financeiro de beneficiários do MCMV com a escala do CFPB e testa o letramento financeiro como antecedente do bem-estar.
- **Como usar na defesa:** A casa não resolve tudo: orientação financeira depois da conquista também é parte de um atendimento humanizado.

**7. Simone Barbosa Villa; Paula Barcelos Vasconcellos; Karen Carrer Ruman de Bortoli; Lúcio Borges de Araújo (2022).** Lack of adaptability in Brazilian social housing: impacts on residents. *Buildings and Cities*. DOI: [10.5334/bc.180](https://doi.org/10.5334/bc.180). Citações (OpenAlex): 33. Acesso: aberto.
- **O que sustenta:** Com 162 moradores e dois estudos de caso, mostra que a habitação social padronizada ignora as necessidades que mudam ao longo do tempo e gera custos para os moradores.
- **Como usar na defesa:** Humanizar é ouvir a família: justifica o app coletar preferências e necessidades (sem dados sensíveis).

**8. Silvia Stefani (2021).** Building Mistrust: ‘Minha Casa Minha Vida’ and its Political Effects in Rio de Janeiro. *Bulletin of Latin American Research*. DOI: [10.1111/blar.13261](https://doi.org/10.1111/blar.13261). Citações (OpenAlex): 20. Acesso: aberto.
- **O que sustenta:** Investiga como o MCMV, somado a conjunturas locais, piorou condições de vida de muitos moradores e aumentou a segregação socioespacial no Rio de Janeiro, gerando desconfiança política.
- **Como usar na defesa:** Alerta: confiança é frágil. O CasaHumanizada precisa de transparência total e não pode prometer casa.

### Bloco C. Ônus administrativo: por que quem tem direito fica de fora

**9. Martin Bækgaard; Tara Tankink (2021).** Administrative Burden: Untangling a Bowl of Conceptual Spaghetti. *Perspectives on Public Management and Governance*. DOI: [10.1093/ppmgov/gvab027](https://doi.org/10.1093/ppmgov/gvab027). Citações (OpenAlex): 139. Acesso: aberto.
- **O que sustenta:** Organiza o conceito de ônus administrativo, separando o que o Estado faz (regras, exigências) do que o cidadão experimenta (custos de aprendizagem, conformidade e psicológicos).
- **Como usar na defesa:** Referencial teórico central do grupo: o app ataca os três custos (informação, documentos, desgaste).

**10. Christian Østergaard Madsen; Ida Lindgren; Ulf Melin (2021).** The accidental caseworker – How digital self-service influences citizens' administrative burden. *Government Information Quarterly*. DOI: [10.1016/j.giq.2021.101653](https://doi.org/10.1016/j.giq.2021.101653). Citações (OpenAlex): 135. Acesso: aberto.
- **O que sustenta:** Estuda a autoatendimento digital obrigatório em serviços sociais complexos: o cidadão vira um "assistente social acidental", assumindo tarefas antes feitas pelo servidor.
- **Como usar na defesa:** Alerta de design: digitalizar sem apoio humano transfere o trabalho para quem tem menos recursos. Daí o "humanizada".

**11. Rik Peeters (2022).** Digital Administrative Burdens: An Agenda for Analyzing the Citizen Experience of Digital Bureaucratic Encounters. *Perspectives on Public Management and Governance*. DOI: [10.1093/ppmgov/gvac024](https://doi.org/10.1093/ppmgov/gvac024). Citações (OpenAlex): 68. Acesso: fechado.
- **O que sustenta:** Propõe agenda de pesquisa sobre ônus administrativo digital: decisões automatizadas, interações digitais e uso de dados podem criar novos custos ao cidadão.
- **Como usar na defesa:** Mais um cuidado: o app não deve criar novas barreiras (senhas, uploads difíceis, linguagem técnica).

**12. Claudia Aiken; Ingrid Gould Ellen; Vincent J. Reina (2023).** Administrative Burdens in Emergency Rental Assistance Programs. *RSF The Russell Sage Foundation Journal of the Social Sciences*. DOI: [10.7758/rsf.2023.9.5.05](https://doi.org/10.7758/rsf.2023.9.5.05). Citações (OpenAlex): 36. Acesso: aberto.
- **O que sustenta:** Com pesquisas nacionais com mais de 200 programas de auxílio-aluguel emergencial nos EUA, analisa os ônus administrativos e os desafios particulares da habitação (engajar inquilinos e proprietários).
- **Como usar na defesa:** Evidência de que o **desenho do processo** define quem acessa o benefício habitacional.

### Bloco D. Serviço público digital, inclusivo e centrado no cidadão

**13. Gatot Hery Djatmika; Obsatar Sinaga; Suharno Pawirosumarto (2025).** Digital Transformation and Social Inclusion in Public Services: A Qualitative Analysis of E-Government Adoption for Marginalized Communities in Sustainable Governance. *Sustainability*. DOI: [10.3390/su17072908](https://doi.org/10.3390/su17072908). Citações (OpenAlex): 146. Acesso: aberto.
- **O que sustenta:** Estudo qualitativo com casos de vários países: letramento digital limitado, falta de infraestrutura e barreiras institucionais dificultam a inclusão digital de comunidades marginalizadas no governo eletrônico.
- **Como usar na defesa:** Sustenta a opção de atendimento humano/presencial e linguagem simples.

**14. Hemin Choi; Maria Cucciniello (2026).** Citizen‐Centered Public Service Design in Agile Digital Transformation: Insights From Public Mobility Services. *Public Administration*. DOI: [10.1111/padm.70059](https://doi.org/10.1111/padm.70059). Citações (OpenAlex): 3. Acesso: aberto.
- **O que sustenta:** Combinando pesquisa com cidadãos e oficinas de cocriação numa cidade italiana, mostra que ciclos iterativos e participativos (design centrado no cidadão) reduzem a distância entre demanda e satisfação.
- **Como usar na defesa:** Justifica cocriar o CasaHumanizada com famílias e servidores — a pesquisa de campo é o primeiro ciclo.

### Quadro-resumo

| # | Referência | Bloco | DOI |
|---|---|---|---|
| 1 | Forcel et al. (2026) | Bloco A | 10.1590/2236-9996.2026-6571161-en |
| 2 | Euclydes et al. (2022) | Bloco A | 10.1590/1678-98732230e020 |
| 3 | Marca et al. (2026) | Bloco A | 10.1016/j.landusepol.2026.108081 |
| 4 | Bandeira & Reyes (2021) | Bloco A | 10.1590/0034-761220190341 |
| 5 | Wittmann et al. (2021) | Bloco B | 10.21527/2237-6453.2021.55.10215 |
| 6 | Vieira et al. (2021) | Bloco B | 10.1590/1678-6971/eramg210115 |
| 7 | Villa et al. (2022) | Bloco B | 10.5334/bc.180 |
| 8 | Stefani (2021) | Bloco B | 10.1111/blar.13261 |
| 9 | Bækgaard & Tankink (2021) | Bloco C | 10.1093/ppmgov/gvab027 |
| 10 | Madsen et al. (2021) | Bloco C | 10.1016/j.giq.2021.101653 |
| 11 | Peeters (2022) | Bloco C | 10.1093/ppmgov/gvac024 |
| 12 | Aiken et al. (2023) | Bloco C | 10.7758/rsf.2023.9.5.05 |
| 13 | Djatmika et al. (2025) | Bloco D | 10.3390/su17072908 |
| 14 | Choi & Cucciniello (2026) | Bloco D | 10.1111/padm.70059 |

---

## 4. Argumentos prontos para a defesa

1. "Só em Cuiabá, **83.991 famílias** se inscreveram no Casa Cuiabana em 2025 (Prefeitura de Cuiabá) — a demanda está aqui do lado."
2. "O déficit habitacional é de **6,2 milhões** de domicílios, e **52,2%** dele é aluguel pesado demais (FJP, 2022)."
3. "O MCMV já contratou **mais de 1,9 milhão** de unidades desde 2023 — programa existe; o gargalo é o acesso."
4. "Quem tem direito fica de fora por **ônus administrativo**: aprender, comprovar, esperar (Bækgaard & Tankink, 2021)."
5. "Digital sem apoio transforma o cidadão em **assistente social de si mesmo** (Madsen et al., 2021) — por isso o CasaHumanizada é digital **e** humano."
6. "O desenho do processo define quem consegue o benefício habitacional (Aiken et al., 2023)."
7. "Habitação social gera **desenvolvimento local**: +7,7% de PIB per capita nos municípios do MCMV (Marca et al., 2026)."

---

## 5. Lacunas, limites e cuidados

- O número de unidades contratadas do MCMV muda mês a mês; conferir no Ministério das Cidades na véspera da defesa `[verificar]`.
- O app **não substitui** o cadastro oficial (CadÚnico, Caixa, prefeitura): ele informa, organiza e encaminha — deixar claro para não parecer golpe.
- Não achamos estudo brasileiro sobre ônus administrativo específico do MCMV — **lacuna** que a pesquisa de campo explora.
- Dados de renda e benefícios são sensíveis (LGPD): o teste "tenho direito?" deve rodar no aparelho, sem enviar dados.
- Amostra de 15–20 entrevistas é exploratória.

---

## 6. Fontes e proveniência

- **Artigos:** OpenAlex (api.openalex.org), buscas registradas em `_pesquisa/saidas/G5_*.json|.md` (script `_pesquisa/openalex_busca.py`, rodado em 23/09/2026). Seleção final em `_pesquisa/selecionados/G5.json`.
- **Contagem de citações:** valor do OpenAlex no dia da busca (muda com o tempo).
- **Dados brasileiros:** links na tabela 2.1; notícias oficiais (gov.br, Embratur, IBGE, INEP, FJP) têm prioridade sobre imprensa.
- **Regra do projeto:** nenhuma referência pode ser inventada. Se precisar de outro artigo, rode uma nova busca e acrescente o DOI em `_pesquisa/selecao.py`.
