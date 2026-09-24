# Pesquisa e Dados — Grupo 3 · VozGuia

> Apoio à defesa da ideia: dados reais (Brasil/MT) + 14 artigos peer-reviewed (2021–2026). Os metadados dos artigos (autores, título, periódico, DOI, citações) foram copiados **automaticamente** dos resultados da API OpenAlex salvos em `_pesquisa/saidas/` — o script `_pesquisa/selecao.py` falha se algum DOI não existir nesses brutos. Números brasileiros têm fonte com link (conferidos em 23/09/2026). O que não foi confirmado está marcado `[verificar]`.

**Grupo:** 3 · VozGuia · **Professor(a):** Profa. Sandra · **Integrantes:** Karla Moema, Victor Hugo, Nicolas, Fabio, Yasmin · **Código:** G3-<nnn> · **Meta:** 15–20

**Hipótese de campo:** A falta de autonomia da pessoa cega na rua vem mais da **falta de informação sobre o caminho** (onde estão os obstáculos e os pontos de referência) do que da falta de tecnologia — e os problemas de acessibilidade persistem porque **não chegam ao poder público de forma organizada**.

---

## 1. Resumo executivo

O Censo 2022 do IBGE contou **14,4 milhões de pessoas com deficiência** (7,3% da população de 2 anos ou mais), e a dificuldade funcional mais comum é **enxergar**: **7,9 milhões** de pessoas têm dificuldade de enxergar mesmo com óculos. A Lei Brasileira de Inclusão (Lei nº 13.146/2015) garante o direito à acessibilidade, e as normas NBR 9050 e NBR 16537 definem calçadas acessíveis e piso tátil — mas estudos brasileiros mostram calçadas que **ainda impedem a circulação** de pessoas com deficiência, sobretudo em cidades pequenas e médias (Caetano et al., 2021).

A literatura sobre navegação assistiva mostra a migração de bengalas e dispositivos caros para **soluções no smartphone** (Abidi et al., 2024; Kuriakose et al., 2022; See et al., 2022), com portabilidade e facilidade de uso como requisitos centrais — e treino como condição de adoção (Theodorou et al., 2022). Do lado da cidade, o principal gargalo é a **falta de dados confiáveis sobre acessibilidade das calçadas** (Labbé et al., 2023), que ferramentas colaborativas com foto do celular começam a resolver (Morra et al., 2024). O VozGuia une as duas pontas: **autonomia** para quem não enxerga e **dados + alertas** para o poder público agir.

---

## 2. Dados e notícias reais

### 2.1 Tabela de dados

| Dado | Número | Ano | Fonte |
|---|---|---|---|
| Pessoas com deficiência no Brasil | 14,4 milhões (7,3% da população de 2 anos ou mais) | 2022 | IBGE, Censo Demográfico 2022 ([agenciabrasil.ebc.com.br](https://agenciabrasil.ebc.com.br/direitos-humanos/noticia/2025-05/brasil-tem-144-milhoes-de-pessoas-com-deficiencia)) |
| Pessoas com dificuldade de enxergar (mesmo com óculos/lentes) | 7,9 milhões — a dificuldade funcional mais frequente | 2022 | IBGE, Censo Demográfico 2022 ([metropoles.com](https://www.metropoles.com/brasil/para-144-mi-de-pcds-no-brasil-enxergar-e-maior-dificuldade-funcional)) |
| Direito à acessibilidade | Lei Brasileira de Inclusão da Pessoa com Deficiência | 2015 | Lei nº 13.146/2015 ([planalto.gov.br](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm)) |
| Normas técnicas de acessibilidade | NBR 9050 (edificações e espaço urbano) e NBR 16537 (sinalização tátil no piso) | — | ABNT ([abnt.org.br](https://www.abnt.org.br)) |
| Apps de zeladoria urbana já usados por prefeituras | Colab (desde 2013) — foto + local + resposta da prefeitura | 2013– | Comunitas / Colab ([comunitas.org.br](https://comunitas.org.br/aplicativo-como-canal-de-comunicacao-entre-a-prefeitura-e-cidadao/)) |
| Pessoas que usaram a internet (TIC Domicílios 2025) | 88% da população (163 milhões); 65% dos usuários acessam **só pelo celular** | 2025 | Cetic.br / CGI.br ([mobiletime.com.br](https://www.mobiletime.com.br/noticias/09/12/2025/tic-domicilios-2025/)) |

### 2.2 Leitura dos dados

1. **Público grande e invisível.** 7,9 milhões de brasileiros têm dificuldade de enxergar — mais do que a população de muitos estados.
2. **A lei existe; a calçada não.** A LBI e as normas da ABNT definem o padrão, mas a execução é municipal e fragmentada; falta dado para priorizar obras.
3. **O celular já está no bolso.** Leitores de tela (TalkBack/VoiceOver) vêm de fábrica; o VozGuia não exige comprar aparelho novo.
4. **Zeladoria digital já funciona.** Apps como o Colab mostram que prefeituras aceitam receber demandas por app; falta o recorte de **acessibilidade para cegos**.
5. **Dado agregado vira política pública.** Um mapa colaborativo de obstáculos transforma reclamação individual em priorização de obra.

---

## 3. Referencial científico (14 artigos, 2021–2026)

### Bloco A. Navegação assistiva no smartphone

**1. Mustufa Haider Abidi; Arshad Noor Siddiquee; Hisham Alkhalefah; Vishwaraj Srivastava (2024).** A comprehensive review of navigation systems for visually impaired individuals. *Heliyon*. DOI: [10.1016/j.heliyon.2024.e31825](https://doi.org/10.1016/j.heliyon.2024.e31825). Citações (OpenAlex): 79. Acesso: aberto.
- **O que sustenta:** Revisão abrangente da evolução das ferramentas de navegação para pessoas com deficiência visual — da bengala a sistemas eletrônicos com sensores, IA e feedback —, destacando a influência crescente das soluções baseadas em smartphone.
- **Como usar na defesa:** Estado da arte: justifica fazer o VozGuia no celular (e não em hardware próprio).

**2. Bineeth Kuriakose; Raju Shrestha; Frode Eika Sandnes (2022).** DeepNAVI: A deep learning based smartphone navigation assistant for people with visual impairments. *Expert Systems with Applications*. DOI: [10.1016/j.eswa.2022.118720](https://doi.org/10.1016/j.eswa.2022.118720). Citações (OpenAlex): 110. Acesso: aberto.
- **O que sustenta:** Apresenta o DeepNAVI, assistente de navegação em smartphone com deep learning; argumenta que portabilidade e conveniência (uso sem muito treino) são requisitos essenciais pouco atendidos, assim como informar o tipo de obstáculo.
- **Como usar na defesa:** Requisitos de produto: portátil, simples e que diga *qual* é o obstáculo — orienta o MVP.

**3. Aaron Raymond See; Bien Grenier Sasing; Welsey Daniel Advincula (2022).** A Smartphone-Based Mobility Assistant Using Depth Imaging for Visually Impaired and Blind. *Applied Sciences*. DOI: [10.3390/app12062802](https://doi.org/10.3390/app12062802). Citações (OpenAlex): 44. Acesso: aberto.
- **O que sustenta:** Assistente de mobilidade no celular com câmera de profundidade para desviar de obstáculos e reconhecer objetos, controlado por voz e gestos simples.
- **Como usar na defesa:** Mostra que controle por voz/gesto é viável — base da interface do VozGuia.

**4. Salvador Martínez-Cruz; Luis Alberto Morales-Hernandez; Gerardo Israel Perez-Soto; Juan P. Benítez-Rangel et al. (2021).** An Outdoor Navigation Assistance System for Visually Impaired People in Public Transportation. *IEEE Access*. DOI: [10.1109/access.2021.3111544](https://doi.org/10.1109/access.2021.3111544). Citações (OpenAlex): 47. Acesso: aberto.
- **O que sustenta:** Sistema de assistência ao uso de transporte público por pessoas cegas usando Bluetooth Low Energy para localizar pontos e veículos, contornando limitações do GPS.
- **Como usar na defesa:** Sustenta a pergunta sobre transporte público (Q5) e uma evolução do app com beacons nos pontos de ônibus.

### Bloco B. Interfaces sonoras, treino e navegação colaborativa

**5. Gaspar Ramôa; Vincent Schmidt; Thorsten Schwarz; Rainer Stiefelhagen et al. (2024).** SONOICE! a Sonar–Voice dynamic user interface for assisting individuals with blindness and visual impairment in pinpointing elements in 2D tactile readers. *Frontiers in Rehabilitation Sciences*. DOI: [10.3389/fresc.2024.1368983](https://doi.org/10.3389/fresc.2024.1368983). Citações (OpenAlex): 5. Acesso: aberto.
- **O que sustenta:** Desenvolve, com design centrado no usuário, interfaces sonar-voz para pessoas cegas localizarem elementos em leitores táteis 2D.
- **Como usar na defesa:** Referência de design sonoro centrado no usuário: testar a interface com pessoas cegas desde o início.

**6. Paraskevi Theodorou; Kleomenis Tsiligkos; Apostolos N. Meliones; Costas Filios (2022).** A Training Smartphone Application for the Simulation of Outdoor Blind Pedestrian Navigation: Usability, UX Evaluation, Sentiment Analysis. *Sensors*. DOI: [10.3390/s23010367](https://doi.org/10.3390/s23010367). Citações (OpenAlex): 14. Acesso: aberto.
- **O que sustenta:** App de treino que simula a navegação de pedestre cego ao ar livre; avalia usabilidade, experiência do usuário e sentimento; mostra que treino melhora a aceitação de tecnologias assistivas.
- **Como usar na defesa:** Tecnologia assistiva tem baixa adoção sem treino: o VozGuia precisa de um modo de aprendizagem guiado.

**7. Darius Plikynas; Audrius Indriulionis; Algirdas Laukaitis; Leonidas L. Sakalauskas (2022).** Indoor-Guided Navigation for People Who Are Blind: Crowdsourcing for Route Mapping and Assistance. *Applied Sciences*. DOI: [10.3390/app12010523](https://doi.org/10.3390/app12010523). Citações (OpenAlex): 17. Acesso: aberto.
- **O que sustenta:** Propõe navegação guiada em ambientes internos com rotas gravadas por voluntários videntes em uma rede online (crowdsourcing), porque o GPS falha em ambientes fechados.
- **Como usar na defesa:** Inspira o lado colaborativo: voluntários e familiares podem mapear rotas e obstáculos.

### Bloco C. A cidade vista por quem não enxerga

**8. Achituv Cohen; Sagi Dalyot; Asya Natapov; TRISALYN A. NELSON (2024).** How accessible are cities for visually impaired pedestrians? A case of Greater London. *Environment and Planning B Urban Analytics and City Science*. DOI: [10.1177/23998083241256402](https://doi.org/10.1177/23998083241256402). Citações (OpenAlex): 8. Acesso: aberto.
- **O que sustenta:** Cria índices de acessibilidade urbana para pedestres com deficiência visual a partir de dados geoespaciais abertos e compara bairros de Londres.
- **Como usar na defesa:** Mostra que é possível medir acessibilidade por bairro — ideia para o painel público do VozGuia.

**9. Alessia Nuzzi; Alice Becco; Andrea Boschiroli; Andrea Coletto et al. (2024).** Blindness and visual impairment: quality of life and accessibility in the city of Turin. *Frontiers in Medicine*. DOI: [10.3389/fmed.2024.1361631](https://doi.org/10.3389/fmed.2024.1361631). Citações (OpenAlex): 10. Acesso: aberto.
- **O que sustenta:** Questionário com 100 pacientes com deficiência visual em Turim sobre qualidade de vida e problemas do cotidiano em áreas urbanas e extraurbanas.
- **Como usar na defesa:** Base para o bloco 1 (percepção da cidade) e para ouvir diretamente pessoas cegas na pesquisa.

**10. Sen Zhang; Ke Zhang; Meng Zhang; Xiaoyang Liu (2022).** Evaluation of the Visually Impaired Experience of the Sound Environment in Urban Spaces. *Frontiers in Psychology*. DOI: [10.3389/fpsyg.2021.731693](https://doi.org/10.3389/fpsyg.2021.731693). Citações (OpenAlex): 3. Acesso: aberto.
- **O que sustenta:** 26 voluntários com deficiência visual avaliaram 24 ambientes sonoros urbanos quanto a clareza, conforto, segurança e vitalidade.
- **Como usar na defesa:** O som é informação para quem não enxerga: justifica o "assistente sonoro" e cuidado com excesso de áudio.

### Bloco D. Dados de acessibilidade, participação e poder público

**11. Delphine Labbé; Yochai Eisenberg; Devon Snyder; Judy Shanley et al. (2023).** Multiple-Stakeholder Perspectives on Accessibility Data and the Use of Socio-Technical Tools to Improve Sidewalk Accessibility. *Disabilities*. DOI: [10.3390/disabilities3040040](https://doi.org/10.3390/disabilities3040040). Citações (OpenAlex): 10. Acesso: aberto.
- **O que sustenta:** Workshops com múltiplos atores mostram que a falta de dados confiáveis sobre acessibilidade das calçadas é um grande desafio para as cidades, e analisam como cada ator usa esses dados.
- **Como usar na defesa:** Argumento central do lado "poder público": os alertas do VozGuia geram o dado que falta às prefeituras.

**12. Diego Morra; Xiaosheng Zhu; Chang Liu; K.K. Fu et al. (2024).** Mapping sidewalk accessibility with smartphone imagery and Visual AI: a participatory approach. *Philosophical Transactions of the Royal Society A Mathematical Physical and Engineering Sciences*. DOI: [10.1098/rsta.2024.0106](https://doi.org/10.1098/rsta.2024.0106). Citações (OpenAlex): 7. Acesso: fechado.
- **O que sustenta:** Apresenta o Sidewalk AI Scanner, app web para mapeamento participativo e barato de calçadas com fotos de celular e IA que identifica largura, obstáculos e pavimento.
- **Como usar na defesa:** Prova de conceito de mapeamento colaborativo por foto — base do botão de alerta com foto.

**13. Fernando Domingues Caetano; Jeronimo Paulo da Cunha Pimentel de Meira; Suzi Cristini Rodrigues (2021).** Outlines for accessible routes on sidewalks: a big challenge for small brazilian cities. *Revista Tecnologia e Sociedade*. DOI: [10.3895/rts.v17n47.11549](https://doi.org/10.3895/rts.v17n47.11549). Citações (OpenAlex): 1. Acesso: aberto.
- **O que sustenta:** Propõe método de auditoria virtual para prefeituras de cidades pequenas definirem rotas acessíveis nas calçadas; estudo em Quitandinha (região metropolitana de Curitiba).
- **Como usar na defesa:** Evidência brasileira de que calçadas ainda impedem a circulação e de que prefeituras precisam de método/dados.

**14. Adriana Monteiro Cunha; Sidnei Cerqueira dos Santos (2022).** Tecnologias Assistivas para Pessoas com Deficiência Visual. *Cadernos de Prospecção*. DOI: [10.9771/cp.v15i1.43946](https://doi.org/10.9771/cp.v15i1.43946). Citações (OpenAlex): 3. Acesso: aberto.
- **O que sustenta:** Prospecção tecnológica (patentes no INPI) de produtos de acessibilidade para pessoas com deficiência visual.
- **Como usar na defesa:** Mostra o que já existe no Brasil e ajuda a posicionar o diferencial do VozGuia (voz + alerta ao poder público).

### Quadro-resumo

| # | Referência | Bloco | DOI |
|---|---|---|---|
| 1 | Abidi et al. (2024) | Bloco A | 10.1016/j.heliyon.2024.e31825 |
| 2 | Kuriakose et al. (2022) | Bloco A | 10.1016/j.eswa.2022.118720 |
| 3 | See et al. (2022) | Bloco A | 10.3390/app12062802 |
| 4 | Martínez-Cruz et al. (2021) | Bloco A | 10.1109/access.2021.3111544 |
| 5 | Ramôa et al. (2024) | Bloco B | 10.3389/fresc.2024.1368983 |
| 6 | Theodorou et al. (2022) | Bloco B | 10.3390/s23010367 |
| 7 | Plikynas et al. (2022) | Bloco B | 10.3390/app12010523 |
| 8 | Cohen et al. (2024) | Bloco C | 10.1177/23998083241256402 |
| 9 | Nuzzi et al. (2024) | Bloco C | 10.3389/fmed.2024.1361631 |
| 10 | Zhang et al. (2022) | Bloco C | 10.3389/fpsyg.2021.731693 |
| 11 | Labbé et al. (2023) | Bloco D | 10.3390/disabilities3040040 |
| 12 | Morra et al. (2024) | Bloco D | 10.1098/rsta.2024.0106 |
| 13 | Caetano et al. (2021) | Bloco D | 10.3895/rts.v17n47.11549 |
| 14 | Cunha & Santos (2022) | Bloco D | 10.9771/cp.v15i1.43946 |

---

## 4. Argumentos prontos para a defesa

1. "**7,9 milhões** de brasileiros têm dificuldade de enxergar mesmo com óculos (IBGE, Censo 2022)."
2. "A lei garante acessibilidade (LBI, 2015), mas as calçadas **ainda impedem a circulação** (Caetano et al., 2021)."
3. "Navegação assistiva está migrando para o **smartphone** (Abidi et al., 2024) — portátil e sem custo extra."
4. "O app precisa dizer **qual** é o obstáculo e ser simples de usar (Kuriakose et al., 2022)."
5. "Sem treino, tecnologia assistiva é abandonada (Theodorou et al., 2022): o VozGuia terá modo de aprendizagem."
6. "As prefeituras **não têm dados** confiáveis de acessibilidade das calçadas (Labbé et al., 2023) — os alertas do VozGuia produzem esse dado."
7. "Mapeamento por **foto do celular** já foi validado (Morra et al., 2024)."

---

## 5. Lacunas, limites e cuidados

- O MVP roda no navegador: **não faz visão computacional real** (não detecta obstáculo pela câmera). Ele usa um mapa de obstáculos cadastrados e voz do navegador — deixar isso claro na defesa.
- O número de 7,9 milhões inclui baixa visão ("alguma dificuldade"), não só cegueira total — citar com precisão.
- Não achamos estudo brasileiro sobre canal de alertas de acessibilidade integrado à prefeitura — **lacuna**.
- Pesquisar com pessoas cegas exige cuidado ético: consentimento lido em voz alta, sem pressa, e nunca conduzir a pessoa sem perguntar.
- Amostra de 15–20 entrevistas é exploratória; a maioria dos entrevistados no shopping será vidente — a triagem separa os perfis.

---

## 6. Fontes e proveniência

- **Artigos:** OpenAlex (api.openalex.org), buscas registradas em `_pesquisa/saidas/G3_*.json|.md` (script `_pesquisa/openalex_busca.py`, rodado em 23/09/2026). Seleção final em `_pesquisa/selecionados/G3.json`.
- **Contagem de citações:** valor do OpenAlex no dia da busca (muda com o tempo).
- **Dados brasileiros:** links na tabela 2.1; notícias oficiais (gov.br, Embratur, IBGE, INEP, FJP) têm prioridade sobre imprensa.
- **Regra do projeto:** nenhuma referência pode ser inventada. Se precisar de outro artigo, rode uma nova busca e acrescente o DOI em `_pesquisa/selecao.py`.
