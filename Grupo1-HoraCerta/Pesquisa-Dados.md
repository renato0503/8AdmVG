# Pesquisa e Dados — Grupo 1 · HoraCerta

> Apoio à defesa da ideia: dados reais (Brasil/MT) + 14 artigos peer-reviewed (2021–2026). Os metadados dos artigos (autores, título, periódico, DOI, citações) foram copiados **automaticamente** dos resultados da API OpenAlex salvos em `_pesquisa/saidas/` — o script `_pesquisa/selecao.py` falha se algum DOI não existir nesses brutos. Números brasileiros têm fonte com link (conferidos em 23/09/2026). O que não foi confirmado está marcado `[verificar]`.

**Grupo:** 1 · HoraCerta · **Professor(a):** Prof. Renato · **Integrantes:** José Arlindo, Taynara, Luana, Leticia, Samara · **Código:** G1-<nnn> · **Meta:** 15–20

**Hipótese de campo:** A maior dor não é a falta de atividades, mas a **falta de controle**: o aluno não sabe quantas horas já tem validadas, perde comprovantes e deixa tudo para o fim do curso — e isso vira risco de atrasar a colação de grau.

---

## 1. Resumo executivo

O Brasil tem **9,9 milhões de matrículas** na graduação (Censo da Educação Superior 2023), quase 80% em instituições privadas — e todos esses alunos precisam cumprir **atividades complementares** e, desde a Resolução CNE/CES nº 7/2018, **atividades de extensão** (no mínimo 10% da carga horária) para se formar. O controle dessas horas ainda é, na maioria das instituições, feito com **papel, e-mail e planilha**: o aluno junta certificados, entrega na secretaria e espera. Dois estudos brasileiros recentes encontrados na busca descrevem exatamente essa dor — fluxos "manuais, descentralizados e altamente burocráticos" e "constante extravio de comprovantes físicos" (Camargo et al., 2026) — e o interesse dos estudantes em um **aplicativo** para gerenciar as atividades (Aguiar Filho et al., 2024).

A literatura internacional mostra por que vale a pena resolver isso: atividades extracurriculares aumentam a autoeficácia, o senso de pertencimento e a empregabilidade (Griffiths et al., 2021; De Sisto et al., 2021; Ribeiro et al., 2023; Kanar & Bouckenooghe, 2021), mas a **falta de tempo** é a principal barreira (Le, 2024). E painéis de acompanhamento (*learning analytics dashboards*) e gamificação aumentam o engajamento quando o aluno **enxerga o próprio progresso** (Ramaswami et al., 2023; Alam et al., 2023; Chans & Castro, 2021). O HoraCerta junta as duas coisas: visibilidade do saldo em tempo real + comprovantes organizados + oportunidades próximas.

---

## 2. Dados e notícias reais

### 2.1 Tabela de dados

| Dado | Número | Ano | Fonte |
|---|---|---|---|
| Matrículas na graduação no Brasil | 9,9 milhões (+5,6% sobre 2022) | 2023 | INEP, Censo da Educação Superior 2023 ([gov.br](https://www.gov.br/inep/pt-br/centrais-de-conteudo/noticias/censo-da-educacao-superior/mec-e-inep-divulgam-resultado-do-censo-superior-2023)) |
| Matrículas em instituições privadas | 79,3% (7,9 milhões) | 2023 | INEP, Censo da Educação Superior 2023 ([download.inep.gov.br](https://download.inep.gov.br/educacao_superior/censo_superior/documentos/2023/apresentacao_censo_da_educacao_superior_2023.pdf)) |
| Instituições de educação superior | 2.580 (87,8% privadas) | 2023 | INEP, Censo da Educação Superior 2023 ([gov.br](https://www.gov.br/mec/pt-br/assuntos/noticias/2024/outubro/mec-e-inep-divulgam-resultado-do-censo-superior-2023)) |
| Extensão obrigatória na graduação | mínimo de 10% da carga horária total do curso | 2018 | Resolução CNE/CES nº 7/2018 ([gov.br](https://www.gov.br/mec/pt-br/cne/normas-classificadas-por-assunto/diretrizes-curriculares-cursos-de-graduacao)) |
| Estágio + atividades complementares (bacharelados) | não podem passar de 20% da carga horária total | 2007 | Resolução CNE/CES nº 2/2007 ([portal.mec.gov.br](https://portal.mec.gov.br/cne/arquivos/pdf/2007/rces002_07.pdf)) |
| DCN do curso de Administração | atividades complementares devem contribuir para o desenvolvimento de competências | 2021 | Resolução CNE/CES nº 5/2021 ([abmes.org.br](https://abmes.org.br/legislacoes/detalhe/3743/resolucao-cne-ces-n-5)) |
| Taxa de evasão anual do sistema de ensino superior | 17,5% (maior desde 2010); EAD 24,1% × presencial 9,5% `[verificar no relatório do INEP]` | 2023–2024 | INEP, Censo da Educação Superior 2024 (via imprensa) ([download.inep.gov.br](https://download.inep.gov.br/educacao_superior/censo_superior/documentos/2024/apresentacao_censo_da_educacao_superior_2024.pdf)) |
| Pessoas que usaram a internet (TIC Domicílios 2025) | 88% da população (163 milhões); 65% dos usuários acessam **só pelo celular** | 2025 | Cetic.br / CGI.br ([mobiletime.com.br](https://www.mobiletime.com.br/noticias/09/12/2025/tic-domicilios-2025/)) |

### 2.2 Leitura dos dados

1. **Escala enorme, processo artesanal.** São quase 10 milhões de alunos com exigência de horas — e a validação ainda depende de papel e de triagem humana na secretaria (Camargo et al., 2026).
2. **Extensão aumentou a carga.** A curricularização da extensão (10% da carga horária) somou-se às atividades complementares: mais horas para controlar, mais categorias, mais comprovantes.
3. **Privadas concentram o público.** Com 79% das matrículas em IES privadas (como a Unifacc), o HoraCerta tem um cliente institucional claro: coordenações que querem reduzir retrabalho e reclamação.
4. **O aluno trabalha e estuda.** Falta de tempo é a barreira nº 1 para participar de atividades (Le, 2024) — por isso o app precisa mostrar *oportunidades próximas e rápidas*, não só contar horas.
5. **Evasão alta pede engajamento.** Em um sistema com evasão anual de cerca de 17% `[verificar]`, ferramentas que aumentam pertencimento e engajamento (De Sisto et al., 2021) têm valor para a instituição.
6. **Celular é o canal.** 65% dos usuários de internet acessam *só* pelo celular (TIC 2025): a foto do certificado tem que virar comprovante na hora.

---

## 3. Referencial científico (14 artigos, 2021–2026)

### Bloco A. O problema no Brasil: controle manual das atividades complementares

**1. Franco Feitosa Corrêa de Camargo; Daniel Barros Bastos; Natyelle Santana Milhomem; Simone Pio Parreira et al. (2026).** ACC DIGITAL: DESENVOLVIMENTO DE UM SISTEMA WEB INTEGRADO PARA CONTROLE E VALIDAÇÃO AUTOMATIZADA DE ATIVIDADES COMPLEMENTARES ACADÊMICAS. *Revista Multidisciplinar do Nordeste Mineiro*. DOI: [10.66104/zh5a8c55](https://doi.org/10.66104/zh5a8c55). Citações (OpenAlex): 0. Acesso: aberto.
- **O que sustenta:** Descreve, na UEPA (campus Redenção), o processo de Atividades Curriculares Complementares como manual, descentralizado e burocrático, com triagem humana na secretaria para aplicar tetos de carga horária e extravio de comprovantes físicos; propõe e valida um sistema web com validação automatizada.
- **Como usar na defesa:** É o retrato exato da dor do HoraCerta, em uma universidade brasileira. Use para mostrar que o problema é real e que automatizar a validação é viável.

**2. Armando Sérgio de Aguiar Filho; Frederico Giffoni de Carvalho Dutra; José Maurício Costa (2024).** APLICATIVO UNIVERSITÁRIO DO BEM: DESENVOLVIMENTO DE TECNOLOGIA PARA GESTÃO DE ATIVIDADES COMPLEMENTARES EM INSTITUIÇÕES DE ENSINO SUPERIOR. *COLLOQUIUM SOCIALIS*. DOI: [10.5747/cs.2024.v8.s178](https://doi.org/10.5747/cs.2024.v8.s178). Citações (OpenAlex): 1. Acesso: aberto.
- **O que sustenta:** Estudo de caso na Universidade Fumec (BH), com entrevistas estruturadas com alunos de graduação em 2023, sobre perfis e preferências em relação às atividades complementares; os resultados indicaram interesse dos estudantes em usar um aplicativo móvel.
- **Como usar na defesa:** Evidência brasileira de demanda: alunos querem um app para as horas. Reforça a hipótese de adoção do HoraCerta.

**3. Jaqueline Perschin Santos; Bianca Vitória Schuta Bodanese; Mariana Demétrio de Sousa Pontes (2025).** Participação de estudantes de medicina em atividades complementares e suas repercussões acadêmicas e psicossociais. *Espaço para a Saúde - Revista de Saúde Pública do Paraná*. DOI: [10.22421/1517-7130/es.2025v26.e1090](https://doi.org/10.22421/1517-7130/es.2025v26.e1090). Citações (OpenAlex): 0. Acesso: aberto.
- **O que sustenta:** Estudo transversal com 338 estudantes de Medicina: 75,6% julgaram as atividades complementares "muito relevantes" para a formação, com repercussões acadêmicas e psicossociais.
- **Como usar na defesa:** Mostra que o aluno valoriza as atividades — o problema não é desinteresse, é gestão. Útil para o bloco 3 do formulário.

### Bloco B. Por que as atividades importam (autoeficácia, pertencimento, empregabilidade)

**4. Teri-Lisa Griffiths; Jill Dickinson; Catherine J. Day (2021).** Exploring the relationship between extracurricular activities and student self-efficacy within university. *Journal of Further and Higher Education*. DOI: [10.1080/0309877x.2021.1951687](https://doi.org/10.1080/0309877x.2021.1951687). Citações (OpenAlex): 55. Acesso: aberto.
- **O que sustenta:** Com 294 estudantes de uma universidade do norte da Inglaterra, explora a relação entre participação em atividades extracurriculares e autoeficácia acadêmica e social.
- **Como usar na defesa:** Argumento de valor: as horas não são só burocracia, desenvolvem autoconfiança. O app pode reforçar isso mostrando o que o aluno já conquistou.

**5. Norberto Ribeiro; Carla Malafaia; Tiago Neves; Isabel Menezes (2023).** The impact of extracurricular activities on university students’ academic success and employability. *European Journal of Higher Education*. DOI: [10.1080/21568235.2023.2202874](https://doi.org/10.1080/21568235.2023.2202874). Citações (OpenAlex): 41. Acesso: fechado.
- **O que sustenta:** Síntese narrativa de 39 artigos (Scopus e Web of Science, 2010–2021): a grande maioria das atividades extracurriculares tem impacto positivo no sucesso acadêmico e na empregabilidade; impactos negativos são residuais.
- **Como usar na defesa:** Principal argumento de impacto: atividades bem escolhidas melhoram desempenho e empregabilidade. O HoraCerta ajuda o aluno a escolher melhor, não só a cumprir.

**6. Adam Michael Kanar; Dave Bouckenooghe (2021).** The role of extracurricular activities in shaping university students' employment self-efficacy perceptions. *Career Development International*. DOI: [10.1108/cdi-02-2020-0036](https://doi.org/10.1108/cdi-02-2020-0036). Citações (OpenAlex): 34. Acesso: fechado.
- **O que sustenta:** Estudo longitudinal com estudantes em busca de emprego: a amplitude da participação em atividades extracurriculares se relaciona à autoeficácia para o emprego, mediada pela estratégia de busca de informação.
- **Como usar na defesa:** Conecta horas complementares à carreira — interessante para o público de Administração e para o bloco 3 (valor para a carreira).

**7. Marco De Sisto; Afreen Huq; Genevieve Dickinson (2021).** Sense of belonging in second-year undergraduate students: the value of extracurricular activities. *Higher Education Research & Development*. DOI: [10.1080/07294360.2021.1902951](https://doi.org/10.1080/07294360.2021.1902951). Citações (OpenAlex): 39. Acesso: aberto.
- **O que sustenta:** Com base no modelo de integração de Tinto, mostra que uma atividade extracurricular bem desenhada melhora o senso de pertencimento de alunos do 2º ano.
- **Como usar na defesa:** Pertencimento reduz evasão: argumento para a instituição adotar o HoraCerta como ferramenta de engajamento.

### Bloco C. Motivação e barreiras para participar

**8. Gary Chapman; Washad Emambocus; Demola Obembe (2023).** Higher education student motivations for extracurricular activities: evidence from UK universities. *Journal of Education and Work*. DOI: [10.1080/13639080.2023.2167955](https://doi.org/10.1080/13639080.2023.2167955). Citações (OpenAlex): 37. Acesso: aberto.
- **O que sustenta:** 46 entrevistas em uma universidade britânica de ampliação de acesso: quatro motivações (extrínseca, intrínseca, social e pró-social) explicam a participação, e variam entre alunos iniciantes e concluintes.
- **Como usar na defesa:** Base para a pergunta "só pelas horas × interesse real" (Q12). Também sugere que o app mostre oportunidades de acordo com a motivação.

**9. Ha Van Le (2024).** Factors impeding university students' participation in English extracurricular activities: Time constraints and personal obstacles. *Heliyon*. DOI: [10.1016/j.heliyon.2024.e27332](https://doi.org/10.1016/j.heliyon.2024.e27332). Citações (OpenAlex): 7. Acesso: aberto.
- **O que sustenta:** Identifica as principais barreiras à participação de universitários em atividades extracurriculares: falta de tempo e obstáculos pessoais (como baixa autoconfiança).
- **Como usar na defesa:** Sustenta a pergunta sobre falta de tempo (Q13) e a funcionalidade de oportunidades rápidas/online no app.

### Bloco D. Ver o próprio progresso: painéis, gamificação e apps

**10. Gomathy Ramaswami; Teo Sušnjak; Anuradha Mathrani (2023).** Effectiveness of a Learning Analytics Dashboard for Increasing Student Engagement Levels. *Journal of Learning Analytics*. DOI: [10.18608/jla.2023.7935](https://doi.org/10.18608/jla.2023.7935). Citações (OpenAlex): 50. Acesso: aberto.
- **O que sustenta:** Avalia um painel de learning analytics com componentes preditivos e prescritivos (feedback de como ajustar o comportamento) e seu efeito no engajamento de estudantes.
- **Como usar na defesa:** Mostra que ver o próprio progresso, com orientação do que fazer a seguir, aumenta engajamento — é o coração do "saldo em tempo real".

**11. Anni Silvola; Amanda M. Sjoblom; Piia Näykki; Egle Gedrimiene et al. (2023).** Learning analytics for academic paths: student evaluations of two dashboards for study planning and monitoring. *Frontline Learning Research*. DOI: [10.14786/flr.v11i2.1277](https://doi.org/10.14786/flr.v11i2.1277). Citações (OpenAlex): 9. Acesso: aberto.
- **O que sustenta:** 140 estudantes avaliaram dois painéis para planejar e monitorar o percurso acadêmico; o estudo analisa apoios e desafios percebidos no planejamento dos estudos.
- **Como usar na defesa:** Referência direta para o painel do HoraCerta: planejar e monitorar a trajetória até a formatura.

**12. Md Imtiajul Alam; Lauren Malone; Larysa Nadolny; Michael Geoffrey Brown et al. (2023).** Investigating the impact of a gamified learning analytics dashboard: Student experiences and academic achievement. *Journal of Computer Assisted Learning*. DOI: [10.1111/jcal.12853](https://doi.org/10.1111/jcal.12853). Citações (OpenAlex): 33. Acesso: aberto.
- **O que sustenta:** Compara duas turmas (223 alunos) de uma disciplina de STEM, uma com acesso a um painel gamificado; analisa experiência dos alunos e desempenho acadêmico.
- **Como usar na defesa:** Apoia elementos de gamificação no app (metas, níveis, conquistas por categoria de horas).

**13. Guillermo Manuel Chans; May Portuguez Castro (2021).** Gamification as a Strategy to Increase Motivation and Engagement in Higher Education Chemistry Students. *Computers*. DOI: [10.3390/computers10100132](https://doi.org/10.3390/computers10100132). Citações (OpenAlex): 173. Acesso: aberto.
- **O que sustenta:** Propõe e avalia gamificação para aumentar motivação e engajamento de estudantes de Química no ensino superior durante o ensino remoto.
- **Como usar na defesa:** Artigo mais citado do conjunto (173 citações): base para usar gamificação com cuidado e com apoio do professor/coordenação.

**14. Jacqueline Wong; Mohammad Khalil; Vsevolod Suschevskiy; Martine Baars et al. (2026).** Student engagement profiles in a mobile app: Links to self-regulated learning and performance. *Educational Technology Research and Development*. DOI: [10.1007/s11423-026-10586-2](https://doi.org/10.1007/s11423-026-10586-2). Citações (OpenAlex): 3. Acesso: aberto.
- **O que sustenta:** Identifica perfis de engajamento de estudantes com um app móvel de estudo e sua ligação com autorregulação da aprendizagem e desempenho.
- **Como usar na defesa:** Mostra que apps de celular funcionam no ensino superior, mas exigem autorregulação — o HoraCerta deve lembrar e orientar, não só registrar.

### Quadro-resumo

| # | Referência | Bloco | DOI |
|---|---|---|---|
| 1 | Camargo et al. (2026) | Bloco A | 10.66104/zh5a8c55 |
| 2 | Filho et al. (2024) | Bloco A | 10.5747/cs.2024.v8.s178 |
| 3 | Santos et al. (2025) | Bloco A | 10.22421/1517-7130/es.2025v26.e1090 |
| 4 | Griffiths et al. (2021) | Bloco B | 10.1080/0309877x.2021.1951687 |
| 5 | Ribeiro et al. (2023) | Bloco B | 10.1080/21568235.2023.2202874 |
| 6 | Kanar & Bouckenooghe (2021) | Bloco B | 10.1108/cdi-02-2020-0036 |
| 7 | Sisto et al. (2021) | Bloco B | 10.1080/07294360.2021.1902951 |
| 8 | Chapman et al. (2023) | Bloco C | 10.1080/13639080.2023.2167955 |
| 9 | Le (2024) | Bloco C | 10.1016/j.heliyon.2024.e27332 |
| 10 | Ramaswami et al. (2023) | Bloco D | 10.18608/jla.2023.7935 |
| 11 | Silvola et al. (2023) | Bloco D | 10.14786/flr.v11i2.1277 |
| 12 | Alam et al. (2023) | Bloco D | 10.1111/jcal.12853 |
| 13 | Chans & Castro (2021) | Bloco D | 10.3390/computers10100132 |
| 14 | Wong et al. (2026) | Bloco D | 10.1007/s11423-026-10586-2 |

---

## 4. Argumentos prontos para a defesa

1. "São **9,9 milhões** de alunos de graduação no Brasil (INEP, 2023), e todos precisam fechar horas complementares e de extensão para se formar."
2. "Uma universidade brasileira descreveu o processo como **manual, descentralizado e burocrático**, com **extravio de comprovantes** (Camargo et al., 2026) — é a nossa dor."
3. "Os alunos **querem um app** para isso (Aguiar Filho et al., 2024) e **valorizam** as atividades (Santos et al., 2025): o problema é a gestão, não o interesse."
4. "Atividades bem escolhidas melhoram **desempenho e empregabilidade** (Ribeiro et al., 2023, revisão de 39 estudos)."
5. "A barreira nº 1 é **falta de tempo** (Le, 2024) — o HoraCerta mostra oportunidades próximas e o que falta, para o aluno não perder tempo."
6. "**Ver o próprio progresso** aumenta engajamento (Ramaswami et al., 2023; Alam et al., 2023)."
7. "Para a faculdade: menos papel, menos fila na secretaria e mais pertencimento, que ajuda a segurar a evasão (De Sisto et al., 2021)."

---

## 5. Lacunas, limites e cuidados

- Não há estatística nacional de quantos alunos atrasam a formatura por falta de horas complementares — **a pesquisa de campo é que vai medir essa percepção**.
- A taxa de evasão de 17,5% veio de reportagem sobre o Censo 2024; confirmar no relatório do INEP antes de citar `[verificar]`.
- Os dois estudos brasileiros sobre sistemas de atividades complementares são recentes e com poucas citações — usar como evidência de caso, não de efeito geral.
- Regras de horas mudam por curso e por instituição: o app precisa ser **configurável** pelo regulamento de cada curso.
- Amostra de 15–20 entrevistas é **exploratória**: serve para descobrir dores, não para generalizar.

---

## 6. Fontes e proveniência

- **Artigos:** OpenAlex (api.openalex.org), buscas registradas em `_pesquisa/saidas/G1_*.json|.md` (script `_pesquisa/openalex_busca.py`, rodado em 23/09/2026). Seleção final em `_pesquisa/selecionados/G1.json`.
- **Contagem de citações:** valor do OpenAlex no dia da busca (muda com o tempo).
- **Dados brasileiros:** links na tabela 2.1; notícias oficiais (gov.br, Embratur, IBGE, INEP, FJP) têm prioridade sobre imprensa.
- **Regra do projeto:** nenhuma referência pode ser inventada. Se precisar de outro artigo, rode uma nova busca e acrescente o DOI em `_pesquisa/selecao.py`.
