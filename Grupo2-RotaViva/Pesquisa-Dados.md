# Pesquisa e Dados — Grupo 2 · RotaViva

> Apoio à defesa da ideia: dados reais (Brasil/MT) + 14 artigos peer-reviewed (2021–2026). Os metadados dos artigos (autores, título, periódico, DOI, citações) foram copiados **automaticamente** dos resultados da API OpenAlex salvos em `_pesquisa/saidas/` — o script `_pesquisa/selecao.py` falha se algum DOI não existir nesses brutos. Números brasileiros têm fonte com link (conferidos em 23/09/2026). O que não foi confirmado está marcado `[verificar]`.

**Grupo:** 2 · RotaViva · **Professor(a):** Prof. Renato · **Integrantes:** Cinthia, Danielly, Leandro, Guilherme, Esther · **Código:** G2-<nnn> · **Meta:** 15–20

**Hipótese de campo:** As pessoas deixam de conhecer atrativos que estão perto porque **não sabem que eles existem** e **não têm tempo de montar um roteiro** — a informação existe, mas está espalhada e não é contextualizada pela localização.

---

## 1. Resumo executivo

O turismo vive um momento recorde no Brasil: **9,29 milhões de turistas internacionais em 2025** (+37% sobre 2024), que deixaram **US$ 7,9 bilhões** na economia (Embratur). Mato Grosso acompanha: cerca de **1,2 milhão de turistas em 2025** (+18%) e o Parque Nacional da Chapada dos Guimarães saltou de **92 mil visitas (2022) para 183 mil (2025)** (Sedec-MT). Várzea Grande é a porta de entrada — o Aeroporto Marechal Rondon recebeu 22,6 mil estrangeiros só de janeiro a outubro de 2025.

A literatura mostra que as **tecnologias de turismo inteligente** (apps, localização, informação contextual) melhoram a experiência, a satisfação e a intenção de voltar (Zhang et al., 2022; Torabi et al., 2022; Pai et al., 2021), que apps baseados em localização aumentam a lealdade ao destino quando o conteúdo combina com a experiência real (Xiong & Zhang, 2024) e que recomendação personalizada de rotas é uma área madura (Mou et al., 2022). Ao mesmo tempo, **privacidade da localização** é a principal barreira (Afolabi et al., 2021; Gao et al., 2023). No Brasil, turismo doméstico reduz desigualdade regional (Ribeiro et al., 2022) e políticas de regionalização elevam o PIB dos municípios turísticos (Silva et al., 2022).

---

## 2. Dados e notícias reais

### 2.1 Tabela de dados

| Dado | Número | Ano | Fonte |
|---|---|---|---|
| Turistas internacionais no Brasil | 9,29 milhões (+37,1% sobre 2024; recorde) | 2025 | Embratur ([embratur.com.br](https://embratur.com.br/2026/01/06/brasil-bate-recorde-historico-e-fecha-o-ano-com-92-milhoes-de-turistas-internacionais/)) |
| Gasto de turistas estrangeiros no Brasil | US$ 7,9 bilhões (maior da história) | 2025 | Embratur ([embratur.com.br](https://embratur.com.br/2026/01/26/turistas-estrangeiros-deixam-us-78-bilhoes-na-economia-do-brasil-em-2025-o-maior-valor-da-historia/)) |
| Turistas em Mato Grosso | cerca de 1,2 milhão (+18%); ~32 mil estrangeiros | 2025 | Sedec-MT / DataHub MT ([sedec.mt.gov.br](https://www.sedec.mt.gov.br/en/w/turismo-internacional-avan%C3%A7a-e-fortalece-mato-grosso-no-cen%C3%A1rio-global)) |
| Estrangeiros desembarcados no Aeroporto Marechal Rondon (Várzea Grande) | 22.595 (jan–out) | 2025 | Sedec-MT / DataHub MT ([midiajur.com.br](https://www.midiajur.com.br/geral/mato-grosso-atrai-mais-de-22-mil-turistas-internacionais-em-2025/77610)) |
| Visitas ao Parque Nacional da Chapada dos Guimarães | 92 mil (2022) → 183 mil (2025) | 2022–2025 | Sedec-MT ([sedec.mt.gov.br](https://www.sedec.mt.gov.br/en/w/turismo-internacional-avan%C3%A7a-e-fortalece-mato-grosso-no-cen%C3%A1rio-global)) |
| Pessoas que usaram a internet (TIC Domicílios 2025) | 88% da população (163 milhões); 65% dos usuários acessam **só pelo celular** | 2025 | Cetic.br / CGI.br ([mobiletime.com.br](https://www.mobiletime.com.br/noticias/09/12/2025/tic-domicilios-2025/)) |

### 2.2 Leitura dos dados

1. **Demanda em alta.** Recordes nacionais e estaduais indicam mais visitantes procurando o que fazer — e muitos chegando pela primeira vez.
2. **VG é a porta de entrada.** O aeroporto internacional fica em Várzea Grande; o visitante passa pela cidade, mas raramente a *conhece*: oportunidade para o guia de bolso.
3. **Natureza puxa o fluxo.** A Chapada dobrou visitas em três anos; um app que monte rotas combinando natureza, história e gastronomia distribui o fluxo para atrativos menos conhecidos.
4. **Celular é o guia.** 65% dos usuários de internet acessam só pelo celular (TIC 2025) — mas em áreas naturais o sinal falha: o app precisa de **modo offline**.
5. **Turismo gera renda local.** Evidência brasileira mostra impacto no PIB municipal e na redução de desigualdade regional — o RotaViva pode destacar comércio e guias locais.

---

## 3. Referencial científico (14 artigos, 2021–2026)

### Bloco A. Turismo e desenvolvimento no Brasil

**1. Luiz Carlos de Santana Ribeiro; Gervásio Ferreira dos Santos; Milene Takasago (2022).** Does domestic tourism reduce regional inequalities in Brazil?. *Current Issues in Tourism*. DOI: [10.1080/13683500.2022.2126965](https://doi.org/10.1080/13683500.2022.2126965). Citações (OpenAlex): 15. Acesso: aberto.
- **O que sustenta:** Com modelo insumo-produto inter-regional para as cinco macrorregiões, mede o impacto do gasto do turismo doméstico: o Nordeste tem o maior impacto e o turismo doméstico ajudou a reduzir a desigualdade regional.
- **Como usar na defesa:** Argumento de impacto social: turismo interno distribui renda. Um guia que leva o visitante a atrativos locais amplia esse efeito.

**2. Thiago Christiano Silva; Pedro Vicente da Silva Neto; Benjamin Miranda Tabak (2022).** Tourism and the economy: evidence from Brazil. *Current Issues in Tourism*. DOI: [10.1080/13683500.2022.2048804](https://doi.org/10.1080/13683500.2022.2048804). Citações (OpenAlex): 14. Acesso: fechado.
- **O que sustenta:** Usa desenho de regressão descontínua no Programa de Regionalização do Turismo: municípios turísticos beneficiados tiveram aumento do valor adicionado dos serviços e do PIB per capita, com efeito também na indústria.
- **Como usar na defesa:** Mostra que política de turismo tem efeito econômico mensurável — útil para buscar parceria com prefeitura/secretaria de turismo.

**3. Michelle Maiurro; Zélia Maria de Jesus Breda; Filipa Brandão; Carlos Manuel Martins da Costa (2025).** The role of digital technologies in promoting social innovation in tourism Brazilian companies. *European Public & Social Innovation Review*. DOI: [10.31637/epsir-2026-1979](https://doi.org/10.31637/epsir-2026-1979). Citações (OpenAlex): 2. Acesso: aberto.
- **O que sustenta:** Analisa empreendedorismo e inovação social em empresas de turismo brasileiras e o papel das tecnologias digitais em criar e promover essa inovação.
- **Como usar na defesa:** Posiciona o RotaViva como tecnologia que conecta turista a pequenos negócios locais (inovação social).

### Bloco B. Tecnologias de turismo inteligente e experiência

**4. Yuwen Zhang; Marios D. Sotiriadis; Shiwei Shen (2022).** Investigating the Impact of Smart Tourism Technologies on Tourists’ Experiences. *Sustainability*. DOI: [10.3390/su14053048](https://doi.org/10.3390/su14053048). Citações (OpenAlex): 165. Acesso: aberto.
- **O que sustenta:** Com 486 visitantes de um museu na China, mostra que acessibilidade e interatividade das tecnologias inteligentes influenciam a experiência, a satisfação e as intenções pós-visita.
- **Como usar na defesa:** Artigo muito citado (165): a experiência melhora quando a tecnologia é acessível e interativa — requisito de design do app.

**5. Zabih-Allah Torabi; Ali Asghar Shalbafian; Zaheer Allam; Zahed Ghaderi et al. (2022).** Enhancing Memorable Experiences, Tourist Satisfaction, and Revisit Intention through Smart Tourism Technologies. *Sustainability*. DOI: [10.3390/su14052721](https://doi.org/10.3390/su14052721). Citações (OpenAlex): 160. Acesso: aberto.
- **O que sustenta:** Modelo integrado que liga o uso exploratório e aproveitador de tecnologias de turismo inteligente a experiências memoráveis, satisfação e intenção de revisita.
- **Como usar na defesa:** Sustenta que o app não só informa: cria experiência memorável e faz o turista voltar.

**6. Chen-Kuo Pai; Sangguk Kang; Yumeng Liu; Yingchuan Zheng (2021).** An Examination of Revisit Intention Based on Perceived Smart Tourism Technology Experience. *Sustainability*. DOI: [10.3390/su13021007](https://doi.org/10.3390/su13021007). Citações (OpenAlex): 86. Acesso: aberto.
- **O que sustenta:** Com 312 turistas em Macau (equações estruturais), mostra que a experiência percebida com tecnologia de turismo inteligente afeta significativamente a experiência de viagem e a intenção de revisita.
- **Como usar na defesa:** Mais uma evidência do vínculo tecnologia → revisita; útil no slide de referencial.

### Bloco C. Apps guia, localização e lealdade

**7. Remziye Ekici Cilkin; Derya TOKSÖZ (2024).** Reflections of Technological Developments on Tourist Guidance: Mobile Tourist Guide Applications. *Journal of Tourism and Gastronomy Studies*. DOI: [10.21325/jotags.2024.1388](https://doi.org/10.21325/jotags.2024.1388). Citações (OpenAlex): 2. Acesso: aberto.
- **O que sustenta:** Discute como apps de guia turístico (mapas com GPS, descrições escritas e em áudio de museus e áreas protegidas) permitem viajar sem guia e o efeito disso na profissão de guia.
- **Como usar na defesa:** Base direta do conceito "guia de bolso" com áudio; também alerta para incluir guias locais como parceiros, não concorrentes.

**8. Athanasios Evagelou; Alexandros Kleftodimos; Georgios Lappas (2024).** Creating Location-Based Mobile Applications for Tourism: A Virtual AR Guide for Western Macedonia. *Digital*. DOI: [10.3390/digital4010014](https://doi.org/10.3390/digital4010014). Citações (OpenAlex): 15. Acesso: aberto.
- **O que sustenta:** Apresenta um app de realidade aumentada baseado em localização para turistas na Macedônia Ocidental (Grécia), que guia a pontos de interesse e entretém/educa.
- **Como usar na defesa:** Exemplo real de app regional guiado por localização — referência de funcionalidades para o MVP.

**9. Shaowei Xiong; Tong Zhang (2024).** Enhancing tourist loyalty through location-based service apps: Exploring the roles of digital literacy, perceived ease of use, perceived autonomy, virtual-content congruency, and tourist engagement. *PLoS ONE*. DOI: [10.1371/journal.pone.0294244](https://doi.org/10.1371/journal.pone.0294244). Citações (OpenAlex): 28. Acesso: aberto.
- **O que sustenta:** Integra o modelo TAM para explicar como letramento digital, facilidade de uso, autonomia percebida, coerência entre conteúdo virtual e experiência real e engajamento levam à lealdade ao destino em apps baseados em localização.
- **Como usar na defesa:** Principal referência de adoção: o app precisa ser fácil, dar autonomia e o conteúdo tem que bater com o que o turista vê no local.

**10. Arghavan Hadinejad; Naser Pourazad; Lara Stocchi; Violetta Wik (2026).** Tourism destination mobile applications: an AI-human loop analysis and future research programme. *Tourism Recreation Research*. DOI: [10.1080/02508281.2025.2598874](https://doi.org/10.1080/02508281.2025.2598874). Citações (OpenAlex): 3. Acesso: aberto.
- **O que sustenta:** Revisão sistemática sobre apps de destinos turísticos (2009–2023): literatura predominantemente quantitativa e baseada no TAM; propõe agenda de pesquisa.
- **Como usar na defesa:** Mostra o estado da arte e justifica uma pesquisa qualitativa + quantitativa (formulário + áudio) como a nossa.

### Bloco D. Rotas personalizadas

**11. Naixia Mou; Qi Jiang; Lingxian Zhang; Jiqiang Niu et al. (2022).** Personalized tourist route recommendation model with a trajectory understanding via neural networks. *International Journal of Digital Earth*. DOI: [10.1080/17538947.2022.2130456](https://doi.org/10.1080/17538947.2022.2130456). Citações (OpenAlex): 56. Acesso: aberto.
- **O que sustenta:** Propõe uma rede neural recorrente personalizada que aprende com trajetórias anteriores para recomendar rotas turísticas.
- **Como usar na defesa:** Mostra que rota personalizada é tecnicamente viável; no MVP, uma regra simples (tempo + interesse + distância) já demonstra a ideia.

**12. Haiyan Niu (2023).** The effect of intelligent tour guide system based on attraction positioning and recommendation to improve the experience of tourists visiting scenic spots. *Intelligent Systems with Applications*. DOI: [10.1016/j.iswa.2023.200263](https://doi.org/10.1016/j.iswa.2023.200263). Citações (OpenAlex): 14. Acesso: aberto.
- **O que sustenta:** Propõe um sistema de guia inteligente com posicionamento de atrativos e recomendação (RankSVM e K-means) e planejamento dinâmico de trajeto dentro de pontos turísticos.
- **Como usar na defesa:** Referência técnica para a evolução do app (v2): recomendação e trajeto dinâmico.

### Bloco E. Privacidade e confiança

**13. Olayinka Olasumbo Afolabi; Ali Öztüren; Mustafa İlkan (2021).** Effects of privacy concern, risk, and information control in a smart tourism destination. *Economic Research-Ekonomska Istraživanja*. DOI: [10.1080/1331677x.2020.1867215](https://doi.org/10.1080/1331677x.2020.1867215). Citações (OpenAlex): 50. Acesso: aberto.
- **O que sustenta:** Com 384 visitantes de destino inteligente, estuda preocupação com privacidade, risco percebido, controle da informação e confiança no provedor, e seus efeitos nas intenções de comportamento.
- **Como usar na defesa:** Base da pergunta Q19 (conforto em compartilhar localização) e da regra de LGPD: localização só com consentimento e processada no aparelho.

**14. Ziyi Gao; Jun‐Hwa Cheah; Xin‐Jean Lim; Siew Imm Ng et al. (2023).** Can travel apps improve tourists’ intentions? Investigating the drivers of Chinese gen Y users’ experience. *Journal Of Vacation Marketing*. DOI: [10.1177/13567667231152938](https://doi.org/10.1177/13567667231152938). Citações (OpenAlex): 45. Acesso: fechado.
- **O que sustenta:** Com usuários da geração Y na China, mostra que experiência com o app prediz intenção de uso, e que preocupações de privacidade podem desmotivar a continuidade.
- **Como usar na defesa:** Reforça: privacidade é fator crítico de adoção de apps de viagem.

### Quadro-resumo

| # | Referência | Bloco | DOI |
|---|---|---|---|
| 1 | Ribeiro et al. (2022) | Bloco A | 10.1080/13683500.2022.2126965 |
| 2 | Silva et al. (2022) | Bloco A | 10.1080/13683500.2022.2048804 |
| 3 | Maiurro et al. (2025) | Bloco A | 10.31637/epsir-2026-1979 |
| 4 | Zhang et al. (2022) | Bloco B | 10.3390/su14053048 |
| 5 | Torabi et al. (2022) | Bloco B | 10.3390/su14052721 |
| 6 | Pai et al. (2021) | Bloco B | 10.3390/su13021007 |
| 7 | Cilkin & TOKSÖZ (2024) | Bloco C | 10.21325/jotags.2024.1388 |
| 8 | Evagelou et al. (2024) | Bloco C | 10.3390/digital4010014 |
| 9 | Xiong & Zhang (2024) | Bloco C | 10.1371/journal.pone.0294244 |
| 10 | Hadinejad et al. (2026) | Bloco C | 10.1080/02508281.2025.2598874 |
| 11 | Mou et al. (2022) | Bloco D | 10.1080/17538947.2022.2130456 |
| 12 | Niu (2023) | Bloco D | 10.1016/j.iswa.2023.200263 |
| 13 | Afolabi et al. (2021) | Bloco E | 10.1080/1331677x.2020.1867215 |
| 14 | Gao et al. (2023) | Bloco E | 10.1177/13567667231152938 |

---

## 4. Argumentos prontos para a defesa

1. "O Brasil recebeu **9,3 milhões** de turistas estrangeiros em 2025, recorde histórico (Embratur)."
2. "Mato Grosso recebeu **1,2 milhão** de turistas e a Chapada **dobrou** as visitas desde 2022 (Sedec-MT) — e a porta de entrada é Várzea Grande."
3. "Tecnologias de turismo inteligente melhoram **experiência, satisfação e revisita** (Zhang et al., 2022; Torabi et al., 2022; Pai et al., 2021)."
4. "Apps de localização geram **lealdade** quando o conteúdo combina com o que o turista vê (Xiong & Zhang, 2024)."
5. "Rotas personalizadas já são tecnicamente maduras (Mou et al., 2022) — o desafio é conteúdo local de qualidade."
6. "A principal barreira é **privacidade da localização** (Afolabi et al., 2021): no RotaViva a localização fica no celular e só é usada com permissão."
7. "Turismo doméstico **reduz desigualdade regional** (Ribeiro et al., 2022): o app leva o visitante ao comércio local."

---

## 5. Lacunas, limites e cuidados

- Os dados de Mato Grosso vêm de notas da Sedec-MT (DataHub MT); conferir a metodologia de contagem antes de usar em trabalho acadêmico.
- Não achamos, na busca, estudo peer-reviewed sobre apps de turismo específicos de Mato Grosso — **lacuna que a pesquisa de campo começa a preencher**.
- Parte dos estudos de apps turísticos é da Ásia/Europa; a cultura de uso pode ser diferente em MT.
- Conteúdo histórico/cultural precisa de **fonte confiável** (museus, IPHAN, secretarias) — o app não pode inventar história.
- Amostra de 15–20 entrevistas é exploratória.

---

## 6. Fontes e proveniência

- **Artigos:** OpenAlex (api.openalex.org), buscas registradas em `_pesquisa/saidas/G2_*.json|.md` (script `_pesquisa/openalex_busca.py`, rodado em 23/09/2026). Seleção final em `_pesquisa/selecionados/G2.json`.
- **Contagem de citações:** valor do OpenAlex no dia da busca (muda com o tempo).
- **Dados brasileiros:** links na tabela 2.1; notícias oficiais (gov.br, Embratur, IBGE, INEP, FJP) têm prioridade sobre imprensa.
- **Regra do projeto:** nenhuma referência pode ser inventada. Se precisar de outro artigo, rode uma nova busca e acrescente o DOI em `_pesquisa/selecao.py`.
