# Pesquisa e Dados — Grupo 4 · CasaPiloto

> Apoio à defesa da ideia: dados reais (Brasil/MT) + 14 artigos peer-reviewed (2021–2026). Os metadados dos artigos (autores, título, periódico, DOI, citações) foram copiados **automaticamente** dos resultados da API OpenAlex salvos em `_pesquisa/saidas/` — o script `_pesquisa/selecao.py` falha se algum DOI não existir nesses brutos. Números brasileiros têm fonte com link (conferidos em 23/09/2026). O que não foi confirmado está marcado `[verificar]`.

**Grupo:** 4 · CasaPiloto · **Professor(a):** Profa. Polyana · **Integrantes:** Aliny, André, Michelly, Everson · **Código:** G4-<nnn> · **Meta:** 15–20

**Hipótese de campo:** As pessoas não compram (ou compram mal) porque **não conseguem traduzir o sonho da casa em números mensais** — não sabem quanto guardar, onde investir nem se a parcela cabe — e desconfiam da simulação feita só pelo corretor no plantão de vendas.

---

## 1. Resumo executivo

Comprar a casa é a maior decisão financeira da vida da maioria das famílias — e o mercado está aquecido: só no 1º semestre de 2025 o financiamento habitacional somou **R$ 134,6 bilhões** em concessões (+25%), sendo **R$ 78,7 bilhões** com recursos da poupança/SBPE (Abecip). O Minha Casa, Minha Vida ganhou em 2025 uma **Faixa 4** (renda familiar de até R$ 12 mil, imóveis de até R$ 500 mil, juros de 10,5% ao ano e até 420 parcelas), trazendo a classe média para o programa. Ao mesmo tempo, o déficit habitacional é de **6,2 milhões de domicílios**, e mais da metade dele (52,2%) é **ônus excessivo com aluguel** (FJP, 2022): muita gente paga aluguel caro e não consegue juntar a entrada.

A literatura mostra três coisas úteis para o CasaPiloto: (1) **letramento financeiro** muda a escolha e o conforto com a hipoteca — quem entende a parcela como fluxo mensal escolhe melhor (Thorp et al., 2023; Ilan & Mugerman, 2025); (2) **autocontrole** pesa: quem tem dificuldade de poupar tende a não virar proprietário (Schlafmann, 2021); e (3) **visitas virtuais/VR** a imóveis aceleram a venda e afetam a intenção de compra (Yan et al., 2024; Azmi et al., 2021; Xiong et al., 2022). O CasaPiloto transforma a "casa dos sonhos" do decorado em um **plano mensal** — guardar, investir ou financiar — antes da conversa com o corretor.

---

## 2. Dados e notícias reais

### 2.1 Tabela de dados

| Dado | Número | Ano | Fonte |
|---|---|---|---|
| Financiamento habitacional (todas as fontes) | R$ 134,6 bilhões no 1º semestre (+25%) | 2025 | Abecip (via IRIB) ([irib.org.br](https://www.irib.org.br/noticias/detalhes/abecip-divulga-balanco-do-financiamento-imobiliario-do-1o-semestre)) |
| Financiamento com recursos da poupança (SBPE) | R$ 78,7 bilhões no 1º semestre (+22%) | 2025 | Abecip (via IRIB) ([irib.org.br](https://www.irib.org.br/noticias/detalhes/abecip-divulga-balanco-do-financiamento-imobiliario-do-1o-semestre)) |
| MCMV — Faixa 4 (nova) | renda até R$ 12 mil; imóvel até R$ 500 mil; 10,5% a.a.; até 420 parcelas | 2025 | Agência Brasil / Ministério das Cidades ([agenciabrasil.ebc.com.br](https://agenciabrasil.ebc.com.br/economia/noticia/2025-04/entenda-ampliacao-do-programa-minha-casa-minha-vida)) |
| Déficit habitacional | 6,2 milhões de domicílios | 2022 | Fundação João Pinheiro (FJP) ([fjp.mg.gov.br](https://fjp.mg.gov.br/deficit-habitacional-no-brasil/)) |
| Ônus excessivo com aluguel (renda até 3 s.m. gastando >30% com aluguel) | 52,2% do déficit — o maior componente | 2022 | FJP / Observatório da Construção (Fiesp) ([fiesp.com.br](https://www.fiesp.com.br/observatoriodaconstrucao/noticias/fundacao-joao-pinheiro-divulga-dados-atualizados-do-deficit-habitacional/)) |
| Pessoas que usaram a internet (TIC Domicílios 2025) | 88% da população (163 milhões); 65% dos usuários acessam **só pelo celular** | 2025 | Cetic.br / CGI.br ([mobiletime.com.br](https://www.mobiletime.com.br/noticias/09/12/2025/tic-domicilios-2025/)) |

### 2.2 Leitura dos dados

1. **Mercado aquecido, cliente despreparado.** Há crédito e programa (Faixa 4), mas o comprador chega ao plantão sem saber quanto pode pagar.
2. **O aluguel trava a entrada.** Metade do déficit é gente pagando aluguel caro demais — sobra pouco para guardar; o simulador precisa mostrar metas realistas e prazos.
3. **Juros altos mudam a conta.** Com juros de dois dígitos, comparar *guardar e investir* × *financiar* faz diferença de dezenas de milhares de reais — é a conta que o cliente não faz sozinho.
4. **Construtora ganha lead qualificado.** Quem usa o simulador chega ao corretor sabendo o tipo de casa e o caminho — menos visita perdida, venda mais rápida.
5. **Decorado virtual.** Evidência internacional mostra que VR reduz o tempo de venda sem alterar o preço (Yan et al., 2024) — argumento comercial para a construtora.

---

## 3. Referencial científico (14 artigos, 2021–2026)

### Bloco A. Como se decide comprar a casa

**1. Mohammad Mujaheed Hassan; Nobaya Binti Ahmad; Ahmad Hariza Hashim (2021).** Factors Influencing Housing Purchase Decision. *International Journal of Academic Research in Business and Social Sciences*. DOI: [10.6007/ijarbss/v11-i7/10295](https://doi.org/10.6007/ijarbss/v11-i7/10295). Citações (OpenAlex): 25. Acesso: aberto.
- **O que sustenta:** Revisa os fatores que influenciam a decisão de compra do imóvel (preço, localização, características, fatores financeiros) e aponta que unidades encalhadas refletem preço inconsistente e pouca atratividade.
- **Como usar na defesa:** Base do bloco 1: a decisão depende de vários fatores — o simulador organiza isso por tipo de casa.

**2. Erdener Kaynak; Ali Kara; Azamat Maksüdünov (2022).** An empirical investigation of home buying behavior in a high-context culture: a strategic marketing-oriented approach. *International Journal of Housing Markets and Analysis*. DOI: [10.1108/ijhma-07-2022-0095](https://doi.org/10.1108/ijhma-07-2022-0095). Citações (OpenAlex): 19. Acesso: aberto.
- **O que sustenta:** Com 300 domicílios em Bishkek (Quirguistão), examina o comportamento de compra de imóveis numa cultura de alto contexto e suas implicações de marketing.
- **Como usar na defesa:** Mostra a importância de família, confiança e relação pessoal na compra — por isso o app não substitui o corretor, prepara a conversa.

**3. Pei-Chun Lee; P. L. F. Liu (2025).** Digital information-seeking of homebuyers on real estate platforms in Taiwan. *The Electronic Library*. DOI: [10.1108/el-09-2024-0261](https://doi.org/10.1108/el-09-2024-0261). Citações (OpenAlex): 2. Acesso: fechado.
- **O que sustenta:** Métodos mistos sobre a busca de informação de compradores (primeira compra e recompra) em plataformas imobiliárias digitais em Taiwan; marca, busca e resultados influenciam o comportamento.
- **Como usar na defesa:** O comprador já pesquisa online; a construtora precisa estar nesse momento com uma ferramenta útil, não só anúncio.

### Bloco B. Letramento financeiro, hipoteca e autocontrole

**4. Susan Thorp; Liu Junhao; Julie Richardson Agnew; Hazel Bateman et al. (2023).** Feeling comfortable with a mortgage: The impact of framing, financial literacy and advice. *Journal of Financial Literacy and Wellbeing*. DOI: [10.1017/flw.2023.3](https://doi.org/10.1017/flw.2023.3). Citações (OpenAlex): 15. Acesso: aberto.
- **O que sustenta:** Pesquisa online testa o conforto e a compreensão da dívida hipotecária: analisa letramento financeiro, conselho de corretor e o efeito de apresentar o empréstimo como valor total × fluxo de parcelas.
- **Como usar na defesa:** Principal argumento de design: mostrar a dívida em **parcelas mensais** e comparar cenários ajuda a escolher melhor.

**5. Mordechai Ilan; Yevgeny Mugerman (2025).** Misguided mortgage choices: Financial literacy, inflation expectations, and borrowing decisions. *Journal of Behavioral and Experimental Finance*. DOI: [10.1016/j.jbef.2025.101077](https://doi.org/10.1016/j.jbef.2025.101077). Citações (OpenAlex): 10. Acesso: aberto.
- **O que sustenta:** Com dados domiciliares, mostra que tomadores de baixo nível socioeconômico usam a inflação atual (e não a esperada) ao escolher hipotecas indexadas, enquanto os com mais letramento financeiro decidem melhor.
- **Como usar na defesa:** Quem tem menos informação erra mais e paga mais: o simulador precisa explicar indexadores e juros em linguagem simples.

**6. Mingzhi Hu; Mingzhi Hu; Liu Yingchun; Liu Yingchun et al. (2024).** Financial literacy and mortgage stress. *Journal of Banking & Finance*. DOI: [10.1016/j.jbankfin.2024.107170](https://doi.org/10.1016/j.jbankfin.2024.107170). Citações (OpenAlex): 7. Acesso: fechado.
- **O que sustenta:** Artigo sobre letramento financeiro e estresse com a hipoteca (resumo não disponível na API; ler o texto antes de citar detalhes).
- **Como usar na defesa:** Usar apenas a ideia do título: letramento financeiro se relaciona ao estresse com a hipoteca — sustenta a pergunta Q10 (medo da parcela).

**7. Kathrin Schlafmann (2021).** Housing, Mortgages, and Self-control. *CBS Research Portal (Copenhagen Business School)*. DOI: [10.1093/rfs/hhaa096](https://doi.org/10.1093/rfs/hhaa096). Citações (OpenAlex): 47. Acesso: aberto.
- **O que sustenta:** Modelo quantitativo mostra que pessoas com mais problemas de autocontrole têm menor probabilidade de virar proprietárias, embora a casa funcione como compromisso de poupança; analisa efeitos de regras de entrada e refinanciamento.
- **Como usar na defesa:** Justifica a função de **metas de poupança com lembretes**: ajudar o autocontrole é parte da solução.

**8. Jason Allen; Kyra Carmichael; Robert Clark; Shaoteng Li et al. (2026).** Housing affordability and parental income support: The role of mortgage co-signing. *Journal of Financial Economics*. DOI: [10.1016/j.jfineco.2026.104239](https://doi.org/10.1016/j.jfineco.2026.104239). Citações (OpenAlex): 1. Acesso: fechado.
- **O que sustenta:** Artigo sobre acessibilidade à moradia e apoio de renda dos pais via co-assinatura do financiamento (resumo não disponível na API; ler o texto antes de citar detalhes).
- **Como usar na defesa:** Usar só a ideia do título: apoio familiar é caminho real de acesso — o simulador pode prever composição de renda familiar.

### Bloco C. Decorado virtual: VR e apps no mercado imobiliário

**9. Athira Azmi; Rahinah Ibrahim; Maszura Abdul Ghafar; Ali Rashidi (2021).** Smarter real estate marketing using virtual reality to influence potential homebuyers' emotions and purchase intention. *Smart and Sustainable Built Environment*. DOI: [10.1108/sasbe-03-2021-0056](https://doi.org/10.1108/sasbe-03-2021-0056). Citações (OpenAlex): 71. Acesso: fechado.
- **O que sustenta:** Experimento com 60 potenciais compradores: a atmosfera em VR gera prazer e excitação, que influenciam a intenção de compra da casa.
- **Como usar na defesa:** Base do "decorado virtual": a experiência emocional importa na venda — mas o app equilibra emoção com números.

**10. Zhenbin Yan; Zixuan Meng; Yong Tan (2024).** Does Virtual Reality Help Property Sales? Empirical Evidence from a Real Estate Platform. *Information Systems Research*. DOI: [10.1287/isre.2021.9138](https://doi.org/10.1287/isre.2021.9138). Citações (OpenAlex): 16. Acesso: fechado.
- **O que sustenta:** Com grande base de uma plataforma imobiliária, mostra que VR reduz o tempo de venda em 28%–49% sem influenciar o preço, funcionando como fonte de informação rica e crível.
- **Como usar na defesa:** Argumento comercial forte para a construtora: tour virtual acelera venda.

**11. Chuyi Xiong; Ka Shing Cheung; Deborah Susan Levy; Michael J. Allen (2022).** The effect of virtual reality on the marketing of residential property. *Housing Studies*. DOI: [10.1080/02673037.2022.2074971](https://doi.org/10.1080/02673037.2022.2074971). Citações (OpenAlex): 47. Acesso: fechado.
- **O que sustenta:** Com dados de transações em Wuhan (China), modela como a VR afeta o envolvimento do comprador no processo de compra de imóveis familiares.
- **Como usar na defesa:** Reforça que visitas virtuais alteram o comportamento do comprador real, não só em laboratório.

**12. Shih‐Hui Hsiao; Yen-Yao Wang; Tony L.J. Lin (2023).** The impact of low-immersion virtual reality on product sales: Insights from the real estate industry. *Decision Support Systems*. DOI: [10.1016/j.dss.2023.114131](https://doi.org/10.1016/j.dss.2023.114131). Citações (OpenAlex): 35. Acesso: fechado.
- **O que sustenta:** Artigo sobre o impacto de VR de baixa imersão (tours no navegador/celular) nas vendas do setor imobiliário (resumo não disponível na API; ler o texto antes de citar detalhes).
- **Como usar na defesa:** Usar só a ideia do título: mesmo VR simples, sem óculos, pode afetar vendas — viável num app de celular.

**13. Maurizio Mauri; Gaia Rancati; Giuseppe Riva; Andrea Gaggioli (2023).** Comparing the effects of immersive and non-immersive real estate experience on behavioral intentions. *Computers in Human Behavior*. DOI: [10.1016/j.chb.2023.107996](https://doi.org/10.1016/j.chb.2023.107996). Citações (OpenAlex): 42. Acesso: fechado.
- **O que sustenta:** Artigo que compara experiências imobiliárias imersivas e não imersivas e seus efeitos nas intenções de comportamento (resumo não disponível na API; ler o texto antes de citar detalhes).
- **Como usar na defesa:** Usar só a ideia do título; útil para discutir qual nível de imersão vale a pena no MVP.

**14. Ivana Miljković; Olena Shlyakhetko; Соломія Федушко (2023).** Real Estate App Development Based on AI/VR Technologies. *Electronics*. DOI: [10.3390/electronics12030707](https://doi.org/10.3390/electronics12030707). Citações (OpenAlex): 40. Acesso: aberto.
- **O que sustenta:** Investiga o desenvolvimento de um app imobiliário com IA e VR, com vantagens e desvantagens dessas tecnologias para o mercado.
- **Como usar na defesa:** Referência de arquitetura de produto para as versões v1/v2 do CasaPiloto.

### Quadro-resumo

| # | Referência | Bloco | DOI |
|---|---|---|---|
| 1 | Hassan et al. (2021) | Bloco A | 10.6007/ijarbss/v11-i7/10295 |
| 2 | Kaynak et al. (2022) | Bloco A | 10.1108/ijhma-07-2022-0095 |
| 3 | Lee & Liu (2025) | Bloco A | 10.1108/el-09-2024-0261 |
| 4 | Thorp et al. (2023) | Bloco B | 10.1017/flw.2023.3 |
| 5 | Ilan & Mugerman (2025) | Bloco B | 10.1016/j.jbef.2025.101077 |
| 6 | Hu et al. (2024) | Bloco B | 10.1016/j.jbankfin.2024.107170 |
| 7 | Schlafmann (2021) | Bloco B | 10.1093/rfs/hhaa096 |
| 8 | Allen et al. (2026) | Bloco B | 10.1016/j.jfineco.2026.104239 |
| 9 | Azmi et al. (2021) | Bloco C | 10.1108/sasbe-03-2021-0056 |
| 10 | Yan et al. (2024) | Bloco C | 10.1287/isre.2021.9138 |
| 11 | Xiong et al. (2022) | Bloco C | 10.1080/02673037.2022.2074971 |
| 12 | Hsiao et al. (2023) | Bloco C | 10.1016/j.dss.2023.114131 |
| 13 | Mauri et al. (2023) | Bloco C | 10.1016/j.chb.2023.107996 |
| 14 | Miljković et al. (2023) | Bloco C | 10.3390/electronics12030707 |

---

## 4. Argumentos prontos para a defesa

1. "O financiamento habitacional movimentou **R$ 134,6 bilhões** só no 1º semestre de 2025 (Abecip) — mercado aquecido."
2. "A nova **Faixa 4** do MCMV (até R$ 12 mil de renda) trouxe a classe média para o programa — mais gente precisando simular."
3. "Mais da metade do déficit habitacional é **aluguel pesado demais** (FJP, 2022): sobra pouco para a entrada."
4. "Mostrar a dívida como **parcela mensal** ajuda a escolher melhor (Thorp et al., 2023); quem entende menos paga mais (Ilan & Mugerman, 2025)."
5. "Dificuldade de poupar afasta a casa própria (Schlafmann, 2021) — por isso o CasaPiloto tem metas com lembretes."
6. "Tour virtual reduz o tempo de venda em **28%–49%** sem baixar o preço (Yan et al., 2024) — argumento para a construtora."

---

## 5. Lacunas, limites e cuidados

- Quatro artigos do Bloco B/C não têm resumo na API: citar só pelo título até ler o texto completo.
- Não achamos estudo brasileiro peer-reviewed sobre simuladores oferecidos por construtoras — **lacuna** e oportunidade.
- Taxas e regras do MCMV mudam; o simulador deve mostrar a **data de referência** e que é estimativa, não proposta de crédito.
- O app **não pode pedir renda exata** no MVP: usar faixas e deixar o cálculo no aparelho (LGPD).
- Amostra de 15–20 entrevistas é exploratória.

---

## 6. Fontes e proveniência

- **Artigos:** OpenAlex (api.openalex.org), buscas registradas em `_pesquisa/saidas/G4_*.json|.md` (script `_pesquisa/openalex_busca.py`, rodado em 23/09/2026). Seleção final em `_pesquisa/selecionados/G4.json`.
- **Contagem de citações:** valor do OpenAlex no dia da busca (muda com o tempo).
- **Dados brasileiros:** links na tabela 2.1; notícias oficiais (gov.br, Embratur, IBGE, INEP, FJP) têm prioridade sobre imprensa.
- **Regra do projeto:** nenhuma referência pode ser inventada. Se precisar de outro artigo, rode uma nova busca e acrescente o DOI em `_pesquisa/selecao.py`.
