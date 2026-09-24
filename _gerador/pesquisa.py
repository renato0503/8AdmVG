"""Conteúdo dos Pesquisa-Dados.md.

Os METADADOS dos artigos (autores, título, periódico, DOI, citações) NÃO estão aqui: vêm de
_pesquisa/selecionados/G<n>.json, que só contém registros existentes nos brutos da API OpenAlex
(_pesquisa/saidas). Aqui ficam só a leitura/uso de cada artigo, indexada pelo DOI, e os dados
brasileiros (cada um com fonte e link, conferidos na web em 23/09/2026).
"""

TIC = ("Pessoas que usaram a internet (TIC Domicílios 2025)", "88% da população (163 milhões); 65% dos usuários acessam **só pelo celular**", "2025",
       "Cetic.br / CGI.br", "https://www.mobiletime.com.br/noticias/09/12/2025/tic-domicilios-2025/")

P = {
# =========================================================================== G1
1: dict(
 resumo=(
  "O Brasil tem **9,9 milhões de matrículas** na graduação (Censo da Educação Superior 2023), quase 80% em instituições "
  "privadas — e todos esses alunos precisam cumprir **atividades complementares** e, desde a Resolução CNE/CES nº 7/2018, "
  "**atividades de extensão** (no mínimo 10% da carga horária) para se formar. O controle dessas horas ainda é, na maioria "
  "das instituições, feito com **papel, e-mail e planilha**: o aluno junta certificados, entrega na secretaria e espera. "
  "Dois estudos brasileiros recentes encontrados na busca descrevem exatamente essa dor — fluxos \"manuais, descentralizados "
  "e altamente burocráticos\" e \"constante extravio de comprovantes físicos\" (Camargo et al., 2026) — e o interesse dos "
  "estudantes em um **aplicativo** para gerenciar as atividades (Aguiar Filho et al., 2024).\n\n"
  "A literatura internacional mostra por que vale a pena resolver isso: atividades extracurriculares aumentam a "
  "autoeficácia, o senso de pertencimento e a empregabilidade (Griffiths et al., 2021; De Sisto et al., 2021; Ribeiro et "
  "al., 2023; Kanar & Bouckenooghe, 2021), mas a **falta de tempo** é a principal barreira (Le, 2024). E painéis de "
  "acompanhamento (*learning analytics dashboards*) e gamificação aumentam o engajamento quando o aluno **enxerga o próprio "
  "progresso** (Ramaswami et al., 2023; Alam et al., 2023; Chans & Castro, 2021). O HoraCerta junta as duas coisas: "
  "visibilidade do saldo em tempo real + comprovantes organizados + oportunidades próximas."),
 dados=[
  ("Matrículas na graduação no Brasil", "9,9 milhões (+5,6% sobre 2022)", "2023", "INEP, Censo da Educação Superior 2023", "https://www.gov.br/inep/pt-br/centrais-de-conteudo/noticias/censo-da-educacao-superior/mec-e-inep-divulgam-resultado-do-censo-superior-2023"),
  ("Matrículas em instituições privadas", "79,3% (7,9 milhões)", "2023", "INEP, Censo da Educação Superior 2023", "https://download.inep.gov.br/educacao_superior/censo_superior/documentos/2023/apresentacao_censo_da_educacao_superior_2023.pdf"),
  ("Instituições de educação superior", "2.580 (87,8% privadas)", "2023", "INEP, Censo da Educação Superior 2023", "https://www.gov.br/mec/pt-br/assuntos/noticias/2024/outubro/mec-e-inep-divulgam-resultado-do-censo-superior-2023"),
  ("Extensão obrigatória na graduação", "mínimo de 10% da carga horária total do curso", "2018", "Resolução CNE/CES nº 7/2018", "https://www.gov.br/mec/pt-br/cne/normas-classificadas-por-assunto/diretrizes-curriculares-cursos-de-graduacao"),
  ("Estágio + atividades complementares (bacharelados)", "não podem passar de 20% da carga horária total", "2007", "Resolução CNE/CES nº 2/2007", "https://portal.mec.gov.br/cne/arquivos/pdf/2007/rces002_07.pdf"),
  ("DCN do curso de Administração", "atividades complementares devem contribuir para o desenvolvimento de competências", "2021", "Resolução CNE/CES nº 5/2021", "https://abmes.org.br/legislacoes/detalhe/3743/resolucao-cne-ces-n-5"),
  ("Taxa de evasão anual do sistema de ensino superior", "17,5% (maior desde 2010); EAD 24,1% × presencial 9,5% `[verificar no relatório do INEP]`", "2023–2024", "INEP, Censo da Educação Superior 2024 (via imprensa)", "https://download.inep.gov.br/educacao_superior/censo_superior/documentos/2024/apresentacao_censo_da_educacao_superior_2024.pdf"),
  TIC,
 ],
 leitura=[
  "**Escala enorme, processo artesanal.** São quase 10 milhões de alunos com exigência de horas — e a validação ainda depende de papel e de triagem humana na secretaria (Camargo et al., 2026).",
  "**Extensão aumentou a carga.** A curricularização da extensão (10% da carga horária) somou-se às atividades complementares: mais horas para controlar, mais categorias, mais comprovantes.",
  "**Privadas concentram o público.** Com 79% das matrículas em IES privadas (como a Unifacc), o HoraCerta tem um cliente institucional claro: coordenações que querem reduzir retrabalho e reclamação.",
  "**O aluno trabalha e estuda.** Falta de tempo é a barreira nº 1 para participar de atividades (Le, 2024) — por isso o app precisa mostrar *oportunidades próximas e rápidas*, não só contar horas.",
  "**Evasão alta pede engajamento.** Em um sistema com evasão anual de cerca de 17% `[verificar]`, ferramentas que aumentam pertencimento e engajamento (De Sisto et al., 2021) têm valor para a instituição.",
  "**Celular é o canal.** 65% dos usuários de internet acessam *só* pelo celular (TIC 2025): a foto do certificado tem que virar comprovante na hora.",
 ],
 blocos=[
  ("Bloco A. O problema no Brasil: controle manual das atividades complementares", ["10.66104/zh5a8c55", "10.5747/cs.2024.v8.s178", "10.22421/1517-7130/es.2025v26.e1090"]),
  ("Bloco B. Por que as atividades importam (autoeficácia, pertencimento, empregabilidade)", ["10.1080/0309877x.2021.1951687", "10.1080/21568235.2023.2202874", "10.1108/cdi-02-2020-0036", "10.1080/07294360.2021.1902951"]),
  ("Bloco C. Motivação e barreiras para participar", ["10.1080/13639080.2023.2167955", "10.1016/j.heliyon.2024.e27332"]),
  ("Bloco D. Ver o próprio progresso: painéis, gamificação e apps", ["10.18608/jla.2023.7935", "10.14786/flr.v11i2.1277", "10.1111/jcal.12853", "10.3390/computers10100132", "10.1007/s11423-026-10586-2"]),
 ],
 notas={
  "10.66104/zh5a8c55": ("Descreve, na UEPA (campus Redenção), o processo de Atividades Curriculares Complementares como manual, descentralizado e burocrático, com triagem humana na secretaria para aplicar tetos de carga horária e extravio de comprovantes físicos; propõe e valida um sistema web com validação automatizada.",
                        "É o retrato exato da dor do HoraCerta, em uma universidade brasileira. Use para mostrar que o problema é real e que automatizar a validação é viável."),
  "10.5747/cs.2024.v8.s178": ("Estudo de caso na Universidade Fumec (BH), com entrevistas estruturadas com alunos de graduação em 2023, sobre perfis e preferências em relação às atividades complementares; os resultados indicaram interesse dos estudantes em usar um aplicativo móvel.",
                              "Evidência brasileira de demanda: alunos querem um app para as horas. Reforça a hipótese de adoção do HoraCerta."),
  "10.22421/1517-7130/es.2025v26.e1090": ("Estudo transversal com 338 estudantes de Medicina: 75,6% julgaram as atividades complementares \"muito relevantes\" para a formação, com repercussões acadêmicas e psicossociais.",
                                          "Mostra que o aluno valoriza as atividades — o problema não é desinteresse, é gestão. Útil para o bloco 3 do formulário."),
  "10.1080/0309877x.2021.1951687": ("Com 294 estudantes de uma universidade do norte da Inglaterra, explora a relação entre participação em atividades extracurriculares e autoeficácia acadêmica e social.",
                                    "Argumento de valor: as horas não são só burocracia, desenvolvem autoconfiança. O app pode reforçar isso mostrando o que o aluno já conquistou."),
  "10.1080/21568235.2023.2202874": ("Síntese narrativa de 39 artigos (Scopus e Web of Science, 2010–2021): a grande maioria das atividades extracurriculares tem impacto positivo no sucesso acadêmico e na empregabilidade; impactos negativos são residuais.",
                                    "Principal argumento de impacto: atividades bem escolhidas melhoram desempenho e empregabilidade. O HoraCerta ajuda o aluno a escolher melhor, não só a cumprir."),
  "10.1108/cdi-02-2020-0036": ("Estudo longitudinal com estudantes em busca de emprego: a amplitude da participação em atividades extracurriculares se relaciona à autoeficácia para o emprego, mediada pela estratégia de busca de informação.",
                               "Conecta horas complementares à carreira — interessante para o público de Administração e para o bloco 3 (valor para a carreira)."),
  "10.1080/07294360.2021.1902951": ("Com base no modelo de integração de Tinto, mostra que uma atividade extracurricular bem desenhada melhora o senso de pertencimento de alunos do 2º ano.",
                                    "Pertencimento reduz evasão: argumento para a instituição adotar o HoraCerta como ferramenta de engajamento."),
  "10.1080/13639080.2023.2167955": ("46 entrevistas em uma universidade britânica de ampliação de acesso: quatro motivações (extrínseca, intrínseca, social e pró-social) explicam a participação, e variam entre alunos iniciantes e concluintes.",
                                    "Base para a pergunta \"só pelas horas × interesse real\" (Q12). Também sugere que o app mostre oportunidades de acordo com a motivação."),
  "10.1016/j.heliyon.2024.e27332": ("Identifica as principais barreiras à participação de universitários em atividades extracurriculares: falta de tempo e obstáculos pessoais (como baixa autoconfiança).",
                                    "Sustenta a pergunta sobre falta de tempo (Q13) e a funcionalidade de oportunidades rápidas/online no app."),
  "10.18608/jla.2023.7935": ("Avalia um painel de learning analytics com componentes preditivos e prescritivos (feedback de como ajustar o comportamento) e seu efeito no engajamento de estudantes.",
                             "Mostra que ver o próprio progresso, com orientação do que fazer a seguir, aumenta engajamento — é o coração do \"saldo em tempo real\"."),
  "10.14786/flr.v11i2.1277": ("140 estudantes avaliaram dois painéis para planejar e monitorar o percurso acadêmico; o estudo analisa apoios e desafios percebidos no planejamento dos estudos.",
                              "Referência direta para o painel do HoraCerta: planejar e monitorar a trajetória até a formatura."),
  "10.1111/jcal.12853": ("Compara duas turmas (223 alunos) de uma disciplina de STEM, uma com acesso a um painel gamificado; analisa experiência dos alunos e desempenho acadêmico.",
                         "Apoia elementos de gamificação no app (metas, níveis, conquistas por categoria de horas)."),
  "10.3390/computers10100132": ("Propõe e avalia gamificação para aumentar motivação e engajamento de estudantes de Química no ensino superior durante o ensino remoto.",
                                "Artigo mais citado do conjunto (173 citações): base para usar gamificação com cuidado e com apoio do professor/coordenação."),
  "10.1007/s11423-026-10586-2": ("Identifica perfis de engajamento de estudantes com um app móvel de estudo e sua ligação com autorregulação da aprendizagem e desempenho.",
                                 "Mostra que apps de celular funcionam no ensino superior, mas exigem autorregulação — o HoraCerta deve lembrar e orientar, não só registrar."),
 },
 argumentos=[
  "\"São **9,9 milhões** de alunos de graduação no Brasil (INEP, 2023), e todos precisam fechar horas complementares e de extensão para se formar.\"",
  "\"Uma universidade brasileira descreveu o processo como **manual, descentralizado e burocrático**, com **extravio de comprovantes** (Camargo et al., 2026) — é a nossa dor.\"",
  "\"Os alunos **querem um app** para isso (Aguiar Filho et al., 2024) e **valorizam** as atividades (Santos et al., 2025): o problema é a gestão, não o interesse.\"",
  "\"Atividades bem escolhidas melhoram **desempenho e empregabilidade** (Ribeiro et al., 2023, revisão de 39 estudos).\"",
  "\"A barreira nº 1 é **falta de tempo** (Le, 2024) — o HoraCerta mostra oportunidades próximas e o que falta, para o aluno não perder tempo.\"",
  "\"**Ver o próprio progresso** aumenta engajamento (Ramaswami et al., 2023; Alam et al., 2023).\"",
  "\"Para a faculdade: menos papel, menos fila na secretaria e mais pertencimento, que ajuda a segurar a evasão (De Sisto et al., 2021).\"",
 ],
 lacunas=[
  "Não há estatística nacional de quantos alunos atrasam a formatura por falta de horas complementares — **a pesquisa de campo é que vai medir essa percepção**.",
  "A taxa de evasão de 17,5% veio de reportagem sobre o Censo 2024; confirmar no relatório do INEP antes de citar `[verificar]`.",
  "Os dois estudos brasileiros sobre sistemas de atividades complementares são recentes e com poucas citações — usar como evidência de caso, não de efeito geral.",
  "Regras de horas mudam por curso e por instituição: o app precisa ser **configurável** pelo regulamento de cada curso.",
  "Amostra de 15–20 entrevistas é **exploratória**: serve para descobrir dores, não para generalizar.",
 ],
),
# =========================================================================== G2
2: dict(
 resumo=(
  "O turismo vive um momento recorde no Brasil: **9,29 milhões de turistas internacionais em 2025** (+37% sobre 2024), que "
  "deixaram **US$ 7,9 bilhões** na economia (Embratur). Mato Grosso acompanha: cerca de **1,2 milhão de turistas em 2025** "
  "(+18%) e o Parque Nacional da Chapada dos Guimarães saltou de **92 mil visitas (2022) para 183 mil (2025)** (Sedec-MT). "
  "Várzea Grande é a porta de entrada — o Aeroporto Marechal Rondon recebeu 22,6 mil estrangeiros só de janeiro a outubro de 2025.\n\n"
  "A literatura mostra que as **tecnologias de turismo inteligente** (apps, localização, informação contextual) melhoram a "
  "experiência, a satisfação e a intenção de voltar (Zhang et al., 2022; Torabi et al., 2022; Pai et al., 2021), que apps "
  "baseados em localização aumentam a lealdade ao destino quando o conteúdo combina com a experiência real (Xiong & Zhang, "
  "2024) e que recomendação personalizada de rotas é uma área madura (Mou et al., 2022). Ao mesmo tempo, **privacidade da "
  "localização** é a principal barreira (Afolabi et al., 2021; Gao et al., 2023). No Brasil, turismo doméstico reduz "
  "desigualdade regional (Ribeiro et al., 2022) e políticas de regionalização elevam o PIB dos municípios turísticos (Silva et al., 2022)."),
 dados=[
  ("Turistas internacionais no Brasil", "9,29 milhões (+37,1% sobre 2024; recorde)", "2025", "Embratur", "https://embratur.com.br/2026/01/06/brasil-bate-recorde-historico-e-fecha-o-ano-com-92-milhoes-de-turistas-internacionais/"),
  ("Gasto de turistas estrangeiros no Brasil", "US$ 7,9 bilhões (maior da história)", "2025", "Embratur", "https://embratur.com.br/2026/01/26/turistas-estrangeiros-deixam-us-78-bilhoes-na-economia-do-brasil-em-2025-o-maior-valor-da-historia/"),
  ("Turistas em Mato Grosso", "cerca de 1,2 milhão (+18%); ~32 mil estrangeiros", "2025", "Sedec-MT / DataHub MT", "https://www.sedec.mt.gov.br/en/w/turismo-internacional-avan%C3%A7a-e-fortalece-mato-grosso-no-cen%C3%A1rio-global"),
  ("Estrangeiros desembarcados no Aeroporto Marechal Rondon (Várzea Grande)", "22.595 (jan–out)", "2025", "Sedec-MT / DataHub MT", "https://www.midiajur.com.br/geral/mato-grosso-atrai-mais-de-22-mil-turistas-internacionais-em-2025/77610"),
  ("Visitas ao Parque Nacional da Chapada dos Guimarães", "92 mil (2022) → 183 mil (2025)", "2022–2025", "Sedec-MT", "https://www.sedec.mt.gov.br/en/w/turismo-internacional-avan%C3%A7a-e-fortalece-mato-grosso-no-cen%C3%A1rio-global"),
  TIC,
 ],
 leitura=[
  "**Demanda em alta.** Recordes nacionais e estaduais indicam mais visitantes procurando o que fazer — e muitos chegando pela primeira vez.",
  "**VG é a porta de entrada.** O aeroporto internacional fica em Várzea Grande; o visitante passa pela cidade, mas raramente a *conhece*: oportunidade para o guia de bolso.",
  "**Natureza puxa o fluxo.** A Chapada dobrou visitas em três anos; um app que monte rotas combinando natureza, história e gastronomia distribui o fluxo para atrativos menos conhecidos.",
  "**Celular é o guia.** 65% dos usuários de internet acessam só pelo celular (TIC 2025) — mas em áreas naturais o sinal falha: o app precisa de **modo offline**.",
  "**Turismo gera renda local.** Evidência brasileira mostra impacto no PIB municipal e na redução de desigualdade regional — o RotaViva pode destacar comércio e guias locais.",
 ],
 blocos=[
  ("Bloco A. Turismo e desenvolvimento no Brasil", ["10.1080/13683500.2022.2126965", "10.1080/13683500.2022.2048804", "10.31637/epsir-2026-1979"]),
  ("Bloco B. Tecnologias de turismo inteligente e experiência", ["10.3390/su14053048", "10.3390/su14052721", "10.3390/su13021007"]),
  ("Bloco C. Apps guia, localização e lealdade", ["10.21325/jotags.2024.1388", "10.3390/digital4010014", "10.1371/journal.pone.0294244", "10.1080/02508281.2025.2598874"]),
  ("Bloco D. Rotas personalizadas", ["10.1080/17538947.2022.2130456", "10.1016/j.iswa.2023.200263"]),
  ("Bloco E. Privacidade e confiança", ["10.1080/1331677x.2020.1867215", "10.1177/13567667231152938"]),
 ],
 notas={
  "10.1080/13683500.2022.2126965": ("Com modelo insumo-produto inter-regional para as cinco macrorregiões, mede o impacto do gasto do turismo doméstico: o Nordeste tem o maior impacto e o turismo doméstico ajudou a reduzir a desigualdade regional.",
                                    "Argumento de impacto social: turismo interno distribui renda. Um guia que leva o visitante a atrativos locais amplia esse efeito."),
  "10.1080/13683500.2022.2048804": ("Usa desenho de regressão descontínua no Programa de Regionalização do Turismo: municípios turísticos beneficiados tiveram aumento do valor adicionado dos serviços e do PIB per capita, com efeito também na indústria.",
                                    "Mostra que política de turismo tem efeito econômico mensurável — útil para buscar parceria com prefeitura/secretaria de turismo."),
  "10.31637/epsir-2026-1979": ("Analisa empreendedorismo e inovação social em empresas de turismo brasileiras e o papel das tecnologias digitais em criar e promover essa inovação.",
                               "Posiciona o RotaViva como tecnologia que conecta turista a pequenos negócios locais (inovação social)."),
  "10.3390/su14053048": ("Com 486 visitantes de um museu na China, mostra que acessibilidade e interatividade das tecnologias inteligentes influenciam a experiência, a satisfação e as intenções pós-visita.",
                         "Artigo muito citado (165): a experiência melhora quando a tecnologia é acessível e interativa — requisito de design do app."),
  "10.3390/su14052721": ("Modelo integrado que liga o uso exploratório e aproveitador de tecnologias de turismo inteligente a experiências memoráveis, satisfação e intenção de revisita.",
                         "Sustenta que o app não só informa: cria experiência memorável e faz o turista voltar."),
  "10.3390/su13021007": ("Com 312 turistas em Macau (equações estruturais), mostra que a experiência percebida com tecnologia de turismo inteligente afeta significativamente a experiência de viagem e a intenção de revisita.",
                         "Mais uma evidência do vínculo tecnologia → revisita; útil no slide de referencial."),
  "10.21325/jotags.2024.1388": ("Discute como apps de guia turístico (mapas com GPS, descrições escritas e em áudio de museus e áreas protegidas) permitem viajar sem guia e o efeito disso na profissão de guia.",
                                "Base direta do conceito \"guia de bolso\" com áudio; também alerta para incluir guias locais como parceiros, não concorrentes."),
  "10.3390/digital4010014": ("Apresenta um app de realidade aumentada baseado em localização para turistas na Macedônia Ocidental (Grécia), que guia a pontos de interesse e entretém/educa.",
                             "Exemplo real de app regional guiado por localização — referência de funcionalidades para o MVP."),
  "10.1371/journal.pone.0294244": ("Integra o modelo TAM para explicar como letramento digital, facilidade de uso, autonomia percebida, coerência entre conteúdo virtual e experiência real e engajamento levam à lealdade ao destino em apps baseados em localização.",
                                   "Principal referência de adoção: o app precisa ser fácil, dar autonomia e o conteúdo tem que bater com o que o turista vê no local."),
  "10.1080/02508281.2025.2598874": ("Revisão sistemática sobre apps de destinos turísticos (2009–2023): literatura predominantemente quantitativa e baseada no TAM; propõe agenda de pesquisa.",
                                    "Mostra o estado da arte e justifica uma pesquisa qualitativa + quantitativa (formulário + áudio) como a nossa."),
  "10.1080/17538947.2022.2130456": ("Propõe uma rede neural recorrente personalizada que aprende com trajetórias anteriores para recomendar rotas turísticas.",
                                    "Mostra que rota personalizada é tecnicamente viável; no MVP, uma regra simples (tempo + interesse + distância) já demonstra a ideia."),
  "10.1016/j.iswa.2023.200263": ("Propõe um sistema de guia inteligente com posicionamento de atrativos e recomendação (RankSVM e K-means) e planejamento dinâmico de trajeto dentro de pontos turísticos.",
                                 "Referência técnica para a evolução do app (v2): recomendação e trajeto dinâmico."),
  "10.1080/1331677x.2020.1867215": ("Com 384 visitantes de destino inteligente, estuda preocupação com privacidade, risco percebido, controle da informação e confiança no provedor, e seus efeitos nas intenções de comportamento.",
                                    "Base da pergunta Q19 (conforto em compartilhar localização) e da regra de LGPD: localização só com consentimento e processada no aparelho."),
  "10.1177/13567667231152938": ("Com usuários da geração Y na China, mostra que experiência com o app prediz intenção de uso, e que preocupações de privacidade podem desmotivar a continuidade.",
                                "Reforça: privacidade é fator crítico de adoção de apps de viagem."),
 },
 argumentos=[
  "\"O Brasil recebeu **9,3 milhões** de turistas estrangeiros em 2025, recorde histórico (Embratur).\"",
  "\"Mato Grosso recebeu **1,2 milhão** de turistas e a Chapada **dobrou** as visitas desde 2022 (Sedec-MT) — e a porta de entrada é Várzea Grande.\"",
  "\"Tecnologias de turismo inteligente melhoram **experiência, satisfação e revisita** (Zhang et al., 2022; Torabi et al., 2022; Pai et al., 2021).\"",
  "\"Apps de localização geram **lealdade** quando o conteúdo combina com o que o turista vê (Xiong & Zhang, 2024).\"",
  "\"Rotas personalizadas já são tecnicamente maduras (Mou et al., 2022) — o desafio é conteúdo local de qualidade.\"",
  "\"A principal barreira é **privacidade da localização** (Afolabi et al., 2021): no RotaViva a localização fica no celular e só é usada com permissão.\"",
  "\"Turismo doméstico **reduz desigualdade regional** (Ribeiro et al., 2022): o app leva o visitante ao comércio local.\"",
 ],
 lacunas=[
  "Os dados de Mato Grosso vêm de notas da Sedec-MT (DataHub MT); conferir a metodologia de contagem antes de usar em trabalho acadêmico.",
  "Não achamos, na busca, estudo peer-reviewed sobre apps de turismo específicos de Mato Grosso — **lacuna que a pesquisa de campo começa a preencher**.",
  "Parte dos estudos de apps turísticos é da Ásia/Europa; a cultura de uso pode ser diferente em MT.",
  "Conteúdo histórico/cultural precisa de **fonte confiável** (museus, IPHAN, secretarias) — o app não pode inventar história.",
  "Amostra de 15–20 entrevistas é exploratória.",
 ],
),
# =========================================================================== G3
3: dict(
 resumo=(
  "O Censo 2022 do IBGE contou **14,4 milhões de pessoas com deficiência** (7,3% da população de 2 anos ou mais), e a "
  "dificuldade funcional mais comum é **enxergar**: **7,9 milhões** de pessoas têm dificuldade de enxergar mesmo com óculos. "
  "A Lei Brasileira de Inclusão (Lei nº 13.146/2015) garante o direito à acessibilidade, e as normas NBR 9050 e NBR 16537 "
  "definem calçadas acessíveis e piso tátil — mas estudos brasileiros mostram calçadas que **ainda impedem a circulação** "
  "de pessoas com deficiência, sobretudo em cidades pequenas e médias (Caetano et al., 2021).\n\n"
  "A literatura sobre navegação assistiva mostra a migração de bengalas e dispositivos caros para **soluções no smartphone** "
  "(Abidi et al., 2024; Kuriakose et al., 2022; See et al., 2022), com portabilidade e facilidade de uso como requisitos "
  "centrais — e treino como condição de adoção (Theodorou et al., 2022). Do lado da cidade, o principal gargalo é a **falta de "
  "dados confiáveis sobre acessibilidade das calçadas** (Labbé et al., 2023), que ferramentas colaborativas com foto do "
  "celular começam a resolver (Morra et al., 2024). O VozGuia une as duas pontas: **autonomia** para quem não enxerga e "
  "**dados + alertas** para o poder público agir."),
 dados=[
  ("Pessoas com deficiência no Brasil", "14,4 milhões (7,3% da população de 2 anos ou mais)", "2022", "IBGE, Censo Demográfico 2022", "https://agenciabrasil.ebc.com.br/direitos-humanos/noticia/2025-05/brasil-tem-144-milhoes-de-pessoas-com-deficiencia"),
  ("Pessoas com dificuldade de enxergar (mesmo com óculos/lentes)", "7,9 milhões — a dificuldade funcional mais frequente", "2022", "IBGE, Censo Demográfico 2022", "https://www.metropoles.com/brasil/para-144-mi-de-pcds-no-brasil-enxergar-e-maior-dificuldade-funcional"),
  ("Direito à acessibilidade", "Lei Brasileira de Inclusão da Pessoa com Deficiência", "2015", "Lei nº 13.146/2015", "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm"),
  ("Normas técnicas de acessibilidade", "NBR 9050 (edificações e espaço urbano) e NBR 16537 (sinalização tátil no piso)", "—", "ABNT", "https://www.abnt.org.br"),
  ("Apps de zeladoria urbana já usados por prefeituras", "Colab (desde 2013) — foto + local + resposta da prefeitura", "2013–", "Comunitas / Colab", "https://comunitas.org.br/aplicativo-como-canal-de-comunicacao-entre-a-prefeitura-e-cidadao/"),
  TIC,
 ],
 leitura=[
  "**Público grande e invisível.** 7,9 milhões de brasileiros têm dificuldade de enxergar — mais do que a população de muitos estados.",
  "**A lei existe; a calçada não.** A LBI e as normas da ABNT definem o padrão, mas a execução é municipal e fragmentada; falta dado para priorizar obras.",
  "**O celular já está no bolso.** Leitores de tela (TalkBack/VoiceOver) vêm de fábrica; o VozGuia não exige comprar aparelho novo.",
  "**Zeladoria digital já funciona.** Apps como o Colab mostram que prefeituras aceitam receber demandas por app; falta o recorte de **acessibilidade para cegos**.",
  "**Dado agregado vira política pública.** Um mapa colaborativo de obstáculos transforma reclamação individual em priorização de obra.",
 ],
 blocos=[
  ("Bloco A. Navegação assistiva no smartphone", ["10.1016/j.heliyon.2024.e31825", "10.1016/j.eswa.2022.118720", "10.3390/app12062802", "10.1109/access.2021.3111544"]),
  ("Bloco B. Interfaces sonoras, treino e navegação colaborativa", ["10.3389/fresc.2024.1368983", "10.3390/s23010367", "10.3390/app12010523"]),
  ("Bloco C. A cidade vista por quem não enxerga", ["10.1177/23998083241256402", "10.3389/fmed.2024.1361631", "10.3389/fpsyg.2021.731693"]),
  ("Bloco D. Dados de acessibilidade, participação e poder público", ["10.3390/disabilities3040040", "10.1098/rsta.2024.0106", "10.3895/rts.v17n47.11549", "10.9771/cp.v15i1.43946"]),
 ],
 notas={
  "10.1016/j.heliyon.2024.e31825": ("Revisão abrangente da evolução das ferramentas de navegação para pessoas com deficiência visual — da bengala a sistemas eletrônicos com sensores, IA e feedback —, destacando a influência crescente das soluções baseadas em smartphone.",
                                    "Estado da arte: justifica fazer o VozGuia no celular (e não em hardware próprio)."),
  "10.1016/j.eswa.2022.118720": ("Apresenta o DeepNAVI, assistente de navegação em smartphone com deep learning; argumenta que portabilidade e conveniência (uso sem muito treino) são requisitos essenciais pouco atendidos, assim como informar o tipo de obstáculo.",
                                 "Requisitos de produto: portátil, simples e que diga *qual* é o obstáculo — orienta o MVP."),
  "10.3390/app12062802": ("Assistente de mobilidade no celular com câmera de profundidade para desviar de obstáculos e reconhecer objetos, controlado por voz e gestos simples.",
                          "Mostra que controle por voz/gesto é viável — base da interface do VozGuia."),
  "10.1109/access.2021.3111544": ("Sistema de assistência ao uso de transporte público por pessoas cegas usando Bluetooth Low Energy para localizar pontos e veículos, contornando limitações do GPS.",
                                  "Sustenta a pergunta sobre transporte público (Q5) e uma evolução do app com beacons nos pontos de ônibus."),
  "10.3389/fresc.2024.1368983": ("Desenvolve, com design centrado no usuário, interfaces sonar-voz para pessoas cegas localizarem elementos em leitores táteis 2D.",
                                 "Referência de design sonoro centrado no usuário: testar a interface com pessoas cegas desde o início."),
  "10.3390/s23010367": ("App de treino que simula a navegação de pedestre cego ao ar livre; avalia usabilidade, experiência do usuário e sentimento; mostra que treino melhora a aceitação de tecnologias assistivas.",
                        "Tecnologia assistiva tem baixa adoção sem treino: o VozGuia precisa de um modo de aprendizagem guiado."),
  "10.3390/app12010523": ("Propõe navegação guiada em ambientes internos com rotas gravadas por voluntários videntes em uma rede online (crowdsourcing), porque o GPS falha em ambientes fechados.",
                          "Inspira o lado colaborativo: voluntários e familiares podem mapear rotas e obstáculos."),
  "10.1177/23998083241256402": ("Cria índices de acessibilidade urbana para pedestres com deficiência visual a partir de dados geoespaciais abertos e compara bairros de Londres.",
                                "Mostra que é possível medir acessibilidade por bairro — ideia para o painel público do VozGuia."),
  "10.3389/fmed.2024.1361631": ("Questionário com 100 pacientes com deficiência visual em Turim sobre qualidade de vida e problemas do cotidiano em áreas urbanas e extraurbanas.",
                                "Base para o bloco 1 (percepção da cidade) e para ouvir diretamente pessoas cegas na pesquisa."),
  "10.3389/fpsyg.2021.731693": ("26 voluntários com deficiência visual avaliaram 24 ambientes sonoros urbanos quanto a clareza, conforto, segurança e vitalidade.",
                                "O som é informação para quem não enxerga: justifica o \"assistente sonoro\" e cuidado com excesso de áudio."),
  "10.3390/disabilities3040040": ("Workshops com múltiplos atores mostram que a falta de dados confiáveis sobre acessibilidade das calçadas é um grande desafio para as cidades, e analisam como cada ator usa esses dados.",
                                  "Argumento central do lado \"poder público\": os alertas do VozGuia geram o dado que falta às prefeituras."),
  "10.1098/rsta.2024.0106": ("Apresenta o Sidewalk AI Scanner, app web para mapeamento participativo e barato de calçadas com fotos de celular e IA que identifica largura, obstáculos e pavimento.",
                             "Prova de conceito de mapeamento colaborativo por foto — base do botão de alerta com foto."),
  "10.3895/rts.v17n47.11549": ("Propõe método de auditoria virtual para prefeituras de cidades pequenas definirem rotas acessíveis nas calçadas; estudo em Quitandinha (região metropolitana de Curitiba).",
                               "Evidência brasileira de que calçadas ainda impedem a circulação e de que prefeituras precisam de método/dados."),
  "10.9771/cp.v15i1.43946": ("Prospecção tecnológica (patentes no INPI) de produtos de acessibilidade para pessoas com deficiência visual.",
                             "Mostra o que já existe no Brasil e ajuda a posicionar o diferencial do VozGuia (voz + alerta ao poder público)."),
 },
 argumentos=[
  "\"**7,9 milhões** de brasileiros têm dificuldade de enxergar mesmo com óculos (IBGE, Censo 2022).\"",
  "\"A lei garante acessibilidade (LBI, 2015), mas as calçadas **ainda impedem a circulação** (Caetano et al., 2021).\"",
  "\"Navegação assistiva está migrando para o **smartphone** (Abidi et al., 2024) — portátil e sem custo extra.\"",
  "\"O app precisa dizer **qual** é o obstáculo e ser simples de usar (Kuriakose et al., 2022).\"",
  "\"Sem treino, tecnologia assistiva é abandonada (Theodorou et al., 2022): o VozGuia terá modo de aprendizagem.\"",
  "\"As prefeituras **não têm dados** confiáveis de acessibilidade das calçadas (Labbé et al., 2023) — os alertas do VozGuia produzem esse dado.\"",
  "\"Mapeamento por **foto do celular** já foi validado (Morra et al., 2024).\"",
 ],
 lacunas=[
  "O MVP roda no navegador: **não faz visão computacional real** (não detecta obstáculo pela câmera). Ele usa um mapa de obstáculos cadastrados e voz do navegador — deixar isso claro na defesa.",
  "O número de 7,9 milhões inclui baixa visão (\"alguma dificuldade\"), não só cegueira total — citar com precisão.",
  "Não achamos estudo brasileiro sobre canal de alertas de acessibilidade integrado à prefeitura — **lacuna**.",
  "Pesquisar com pessoas cegas exige cuidado ético: consentimento lido em voz alta, sem pressa, e nunca conduzir a pessoa sem perguntar.",
  "Amostra de 15–20 entrevistas é exploratória; a maioria dos entrevistados no shopping será vidente — a triagem separa os perfis.",
 ],
),
# =========================================================================== G4
4: dict(
 resumo=(
  "Comprar a casa é a maior decisão financeira da vida da maioria das famílias — e o mercado está aquecido: só no 1º "
  "semestre de 2025 o financiamento habitacional somou **R$ 134,6 bilhões** em concessões (+25%), sendo **R$ 78,7 bilhões** "
  "com recursos da poupança/SBPE (Abecip). O Minha Casa, Minha Vida ganhou em 2025 uma **Faixa 4** (renda familiar de até "
  "R$ 12 mil, imóveis de até R$ 500 mil, juros de 10,5% ao ano e até 420 parcelas), trazendo a classe média para o programa. "
  "Ao mesmo tempo, o déficit habitacional é de **6,2 milhões de domicílios**, e mais da metade dele (52,2%) é **ônus excessivo "
  "com aluguel** (FJP, 2022): muita gente paga aluguel caro e não consegue juntar a entrada.\n\n"
  "A literatura mostra três coisas úteis para o CasaPiloto: (1) **letramento financeiro** muda a escolha e o conforto com a "
  "hipoteca — quem entende a parcela como fluxo mensal escolhe melhor (Thorp et al., 2023; Ilan & Mugerman, 2025); "
  "(2) **autocontrole** pesa: quem tem dificuldade de poupar tende a não virar proprietário (Schlafmann, 2021); e (3) "
  "**visitas virtuais/VR** a imóveis aceleram a venda e afetam a intenção de compra (Yan et al., 2024; Azmi et al., 2021; "
  "Xiong et al., 2022). O CasaPiloto transforma a \"casa dos sonhos\" do decorado em um **plano mensal** — guardar, investir "
  "ou financiar — antes da conversa com o corretor."),
 dados=[
  ("Financiamento habitacional (todas as fontes)", "R$ 134,6 bilhões no 1º semestre (+25%)", "2025", "Abecip (via IRIB)", "https://www.irib.org.br/noticias/detalhes/abecip-divulga-balanco-do-financiamento-imobiliario-do-1o-semestre"),
  ("Financiamento com recursos da poupança (SBPE)", "R$ 78,7 bilhões no 1º semestre (+22%)", "2025", "Abecip (via IRIB)", "https://www.irib.org.br/noticias/detalhes/abecip-divulga-balanco-do-financiamento-imobiliario-do-1o-semestre"),
  ("MCMV — Faixa 4 (nova)", "renda até R$ 12 mil; imóvel até R$ 500 mil; 10,5% a.a.; até 420 parcelas", "2025", "Agência Brasil / Ministério das Cidades", "https://agenciabrasil.ebc.com.br/economia/noticia/2025-04/entenda-ampliacao-do-programa-minha-casa-minha-vida"),
  ("Déficit habitacional", "6,2 milhões de domicílios", "2022", "Fundação João Pinheiro (FJP)", "https://fjp.mg.gov.br/deficit-habitacional-no-brasil/"),
  ("Ônus excessivo com aluguel (renda até 3 s.m. gastando >30% com aluguel)", "52,2% do déficit — o maior componente", "2022", "FJP / Observatório da Construção (Fiesp)", "https://www.fiesp.com.br/observatoriodaconstrucao/noticias/fundacao-joao-pinheiro-divulga-dados-atualizados-do-deficit-habitacional/"),
  TIC,
 ],
 leitura=[
  "**Mercado aquecido, cliente despreparado.** Há crédito e programa (Faixa 4), mas o comprador chega ao plantão sem saber quanto pode pagar.",
  "**O aluguel trava a entrada.** Metade do déficit é gente pagando aluguel caro demais — sobra pouco para guardar; o simulador precisa mostrar metas realistas e prazos.",
  "**Juros altos mudam a conta.** Com juros de dois dígitos, comparar *guardar e investir* × *financiar* faz diferença de dezenas de milhares de reais — é a conta que o cliente não faz sozinho.",
  "**Construtora ganha lead qualificado.** Quem usa o simulador chega ao corretor sabendo o tipo de casa e o caminho — menos visita perdida, venda mais rápida.",
  "**Decorado virtual.** Evidência internacional mostra que VR reduz o tempo de venda sem alterar o preço (Yan et al., 2024) — argumento comercial para a construtora.",
 ],
 blocos=[
  ("Bloco A. Como se decide comprar a casa", ["10.6007/ijarbss/v11-i7/10295", "10.1108/ijhma-07-2022-0095", "10.1108/el-09-2024-0261"]),
  ("Bloco B. Letramento financeiro, hipoteca e autocontrole", ["10.1017/flw.2023.3", "10.1016/j.jbef.2025.101077", "10.1016/j.jbankfin.2024.107170", "10.1093/rfs/hhaa096", "10.1016/j.jfineco.2026.104239"]),
  ("Bloco C. Decorado virtual: VR e apps no mercado imobiliário", ["10.1108/sasbe-03-2021-0056", "10.1287/isre.2021.9138", "10.1080/02673037.2022.2074971", "10.1016/j.dss.2023.114131", "10.1016/j.chb.2023.107996", "10.3390/electronics12030707"]),
 ],
 notas={
  "10.6007/ijarbss/v11-i7/10295": ("Revisa os fatores que influenciam a decisão de compra do imóvel (preço, localização, características, fatores financeiros) e aponta que unidades encalhadas refletem preço inconsistente e pouca atratividade.",
                                   "Base do bloco 1: a decisão depende de vários fatores — o simulador organiza isso por tipo de casa."),
  "10.1108/ijhma-07-2022-0095": ("Com 300 domicílios em Bishkek (Quirguistão), examina o comportamento de compra de imóveis numa cultura de alto contexto e suas implicações de marketing.",
                                 "Mostra a importância de família, confiança e relação pessoal na compra — por isso o app não substitui o corretor, prepara a conversa."),
  "10.1108/el-09-2024-0261": ("Métodos mistos sobre a busca de informação de compradores (primeira compra e recompra) em plataformas imobiliárias digitais em Taiwan; marca, busca e resultados influenciam o comportamento.",
                              "O comprador já pesquisa online; a construtora precisa estar nesse momento com uma ferramenta útil, não só anúncio."),
  "10.1017/flw.2023.3": ("Pesquisa online testa o conforto e a compreensão da dívida hipotecária: analisa letramento financeiro, conselho de corretor e o efeito de apresentar o empréstimo como valor total × fluxo de parcelas.",
                         "Principal argumento de design: mostrar a dívida em **parcelas mensais** e comparar cenários ajuda a escolher melhor."),
  "10.1016/j.jbef.2025.101077": ("Com dados domiciliares, mostra que tomadores de baixo nível socioeconômico usam a inflação atual (e não a esperada) ao escolher hipotecas indexadas, enquanto os com mais letramento financeiro decidem melhor.",
                                 "Quem tem menos informação erra mais e paga mais: o simulador precisa explicar indexadores e juros em linguagem simples."),
  "10.1016/j.jbankfin.2024.107170": ("Artigo sobre letramento financeiro e estresse com a hipoteca (resumo não disponível na API; ler o texto antes de citar detalhes).",
                                     "Usar apenas a ideia do título: letramento financeiro se relaciona ao estresse com a hipoteca — sustenta a pergunta Q10 (medo da parcela)."),
  "10.1093/rfs/hhaa096": ("Modelo quantitativo mostra que pessoas com mais problemas de autocontrole têm menor probabilidade de virar proprietárias, embora a casa funcione como compromisso de poupança; analisa efeitos de regras de entrada e refinanciamento.",
                          "Justifica a função de **metas de poupança com lembretes**: ajudar o autocontrole é parte da solução."),
  "10.1016/j.jfineco.2026.104239": ("Artigo sobre acessibilidade à moradia e apoio de renda dos pais via co-assinatura do financiamento (resumo não disponível na API; ler o texto antes de citar detalhes).",
                                    "Usar só a ideia do título: apoio familiar é caminho real de acesso — o simulador pode prever composição de renda familiar."),
  "10.1108/sasbe-03-2021-0056": ("Experimento com 60 potenciais compradores: a atmosfera em VR gera prazer e excitação, que influenciam a intenção de compra da casa.",
                                 "Base do \"decorado virtual\": a experiência emocional importa na venda — mas o app equilibra emoção com números."),
  "10.1287/isre.2021.9138": ("Com grande base de uma plataforma imobiliária, mostra que VR reduz o tempo de venda em 28%–49% sem influenciar o preço, funcionando como fonte de informação rica e crível.",
                             "Argumento comercial forte para a construtora: tour virtual acelera venda."),
  "10.1080/02673037.2022.2074971": ("Com dados de transações em Wuhan (China), modela como a VR afeta o envolvimento do comprador no processo de compra de imóveis familiares.",
                                    "Reforça que visitas virtuais alteram o comportamento do comprador real, não só em laboratório."),
  "10.1016/j.dss.2023.114131": ("Artigo sobre o impacto de VR de baixa imersão (tours no navegador/celular) nas vendas do setor imobiliário (resumo não disponível na API; ler o texto antes de citar detalhes).",
                                "Usar só a ideia do título: mesmo VR simples, sem óculos, pode afetar vendas — viável num app de celular."),
  "10.1016/j.chb.2023.107996": ("Artigo que compara experiências imobiliárias imersivas e não imersivas e seus efeitos nas intenções de comportamento (resumo não disponível na API; ler o texto antes de citar detalhes).",
                                "Usar só a ideia do título; útil para discutir qual nível de imersão vale a pena no MVP."),
  "10.3390/electronics12030707": ("Investiga o desenvolvimento de um app imobiliário com IA e VR, com vantagens e desvantagens dessas tecnologias para o mercado.",
                                  "Referência de arquitetura de produto para as versões v1/v2 do CasaPiloto."),
 },
 argumentos=[
  "\"O financiamento habitacional movimentou **R$ 134,6 bilhões** só no 1º semestre de 2025 (Abecip) — mercado aquecido.\"",
  "\"A nova **Faixa 4** do MCMV (até R$ 12 mil de renda) trouxe a classe média para o programa — mais gente precisando simular.\"",
  "\"Mais da metade do déficit habitacional é **aluguel pesado demais** (FJP, 2022): sobra pouco para a entrada.\"",
  "\"Mostrar a dívida como **parcela mensal** ajuda a escolher melhor (Thorp et al., 2023); quem entende menos paga mais (Ilan & Mugerman, 2025).\"",
  "\"Dificuldade de poupar afasta a casa própria (Schlafmann, 2021) — por isso o CasaPiloto tem metas com lembretes.\"",
  "\"Tour virtual reduz o tempo de venda em **28%–49%** sem baixar o preço (Yan et al., 2024) — argumento para a construtora.\"",
 ],
 lacunas=[
  "Quatro artigos do Bloco B/C não têm resumo na API: citar só pelo título até ler o texto completo.",
  "Não achamos estudo brasileiro peer-reviewed sobre simuladores oferecidos por construtoras — **lacuna** e oportunidade.",
  "Taxas e regras do MCMV mudam; o simulador deve mostrar a **data de referência** e que é estimativa, não proposta de crédito.",
  "O app **não pode pedir renda exata** no MVP: usar faixas e deixar o cálculo no aparelho (LGPD).",
  "Amostra de 15–20 entrevistas é exploratória.",
 ],
),
# =========================================================================== G5
5: dict(
 resumo=(
  "O Brasil tinha **6,2 milhões de domicílios em déficit habitacional em 2022** (Fundação João Pinheiro), e o principal "
  "componente é o **ônus excessivo com aluguel** — famílias com renda de até 3 salários mínimos que gastam mais de 30% da "
  "renda com aluguel (52,2% do déficit). Nova estimativa da FJP apresentada em 2025 aponta **5,9 milhões**. Para enfrentar "
  "isso, o Minha Casa, Minha Vida foi retomado (Lei nº 14.620/2023) e já contratou **mais de 1,9 milhão de unidades desde 2023**, "
  "com meta ampliada para 3 milhões após a criação da Faixa 4 — mas o acesso depende de informação, CadÚnico atualizado, "
  "documentos e muitas idas a órgãos públicos.\n\n"
  "A literatura sobre **ônus administrativo** (*administrative burden*) explica por que famílias com direito ficam de fora: "
  "custos de aprendizagem (descobrir o programa), de conformidade (documentos, filas) e psicológicos (estigma, desgaste) "
  "(Bækgaard & Tankink, 2021). A digitalização pode reduzir esses custos — ou transferi-los ao cidadão, que vira um "
  "\"assistente social acidental\" de si mesmo (Madsen et al., 2021; Peeters, 2022). Em programas de aluguel emergencial nos "
  "EUA, o desenho do processo definiu quem conseguiu o benefício (Aiken et al., 2023). No Brasil, estudos do MCMV mostram "
  "efeitos econômicos positivos nos municípios (Marca et al., 2026), mas também insatisfação, segregação e desconfiança "
  "(Stefani, 2021; Villa et al., 2022). O CasaHumanizada propõe **reduzir o ônus administrativo** com informação "
  "centralizada, linguagem simples e atendimento humano.\n\n"
  "O caso local deixa isso concreto: o programa municipal **Casa Cuiabana** recebeu **83.991 inscrições** entre julho e "
  "setembro de 2025 (Prefeitura de Cuiabá). A jornada — cadastro e triagem, entrega de documentação física, análise e "
  "seleção, acompanhamento contínuo dos prazos — tem etapas fragmentadas que geram ansiedade e ruído de informação: "
  "exatamente o que a plataforma quer organizar."),
 dados=[
  ("Inscrições no programa municipal Casa Cuiabana (renda até R$ 2.850, sem imóvel)", "83.991 cadastros entre 15/07 e 19/09", "2025", "Prefeitura de Cuiabá", "https://www.cuiaba.mt.gov.br/noticias/casa-cuiabana-encerra-inscricoes-com-quase-84-mil-cadastros-realizados"),
  ("1º sorteio do Casa Cuiabana", "1.000 selecionados (500 titulares + 500 em cadastro reserva)", "dez/2025", "Prefeitura de Cuiabá", "https://www.cuiaba.mt.gov.br/noticias/programa-casa-cuiabana-avanca-para-etapa-final-e-se-aproxima-da-assinatura-de-contratos"),
  ("Déficit habitacional", "6,2 milhões de domicílios", "2022", "Fundação João Pinheiro (FJP)", "https://fjp.mg.gov.br/deficit-habitacional-no-brasil/"),
  ("Ônus excessivo com aluguel urbano (componente do déficit)", "52,2% do déficit — o maior componente", "2022", "FJP / Observatório da Construção (Fiesp)", "https://www.fiesp.com.br/observatoriodaconstrucao/noticias/fundacao-joao-pinheiro-divulga-dados-atualizados-do-deficit-habitacional/"),
  ("Déficit habitacional (nova estimativa)", "5,9 milhões de unidades (−4,8% sobre 2022)", "divulgado em 2025", "FJP, apresentado na Câmara dos Deputados", "https://www.camara.leg.br/noticias/1164400-pesquisa-aponta-que-o-deficit-habitacional-brasileiro-esta-em-59-milhoes-de-unidades/"),
  ("Retomada do Minha Casa, Minha Vida", "Lei nº 14.620/2023", "2023", "Planalto", "https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14620.htm"),
  ("Unidades do MCMV contratadas desde 2023", "mais de 1,9 milhão; meta ampliada para 3 milhões com a Faixa 4 `[verificar número atualizado]`", "2025", "Ministério das Cidades (via imprensa)", "https://www.gov.br/cidades/pt-br/assuntos/noticias-1/noticia-mcid-n-1864"),
  ("Faixas 1 e 2 (renda até R$ 4.700)", "mais de 661 mil unidades contratadas/financiadas até dez/2025", "2025", "Ministério das Cidades", "https://www.gov.br/cidades/pt-br/assuntos/noticias-1/noticia-mcid-n-1864"),
  TIC,
 ],
 leitura=[
  "**A fila é enorme aqui do lado.** Só o Casa Cuiabana recebeu **83.991 inscrições** em dois meses de 2025, e o 1º sorteio selecionou 1.000 famílias (500 titulares + 500 reserva). A maioria vai esperar — e precisa saber, com clareza, em que etapa está e quais prazos não pode perder.",
  "**O problema é aluguel caro.** Mais da metade do déficit não é falta de teto, é aluguel que consome a renda — o público do CasaHumanizada paga aluguel e não sabe se tem direito a algo.",
  "**Há programa, falta caminho.** O MCMV cresceu muito desde 2023, mas o acesso passa por CadÚnico, faixas de renda, documentos e prefeitura — cada etapa é um custo para a família.",
  "**Informação fragmentada abre espaço para golpe.** Programas federais, estaduais e municipais em sites diferentes geram confusão; um canal único e confiável protege o cidadão.",
  "**Digital sem humano exclui.** 65% dos usuários acessam a internet só pelo celular (TIC 2025), muitos com pouco letramento digital — o app precisa de linguagem simples e opção de atendimento humano.",
  "**Acompanhar reduz ansiedade e retorno ao balcão.** Saber em que etapa está o processo evita idas repetidas ao órgão público.",
 ],
 blocos=[
  ("Bloco A. O déficit e o Minha Casa, Minha Vida", ["10.1590/2236-9996.2026-6571161-en", "10.1590/1678-98732230e020", "10.1016/j.landusepol.2026.108081", "10.1590/0034-761220190341"]),
  ("Bloco B. A experiência de quem é atendido", ["10.21527/2237-6453.2021.55.10215", "10.1590/1678-6971/eramg210115", "10.5334/bc.180", "10.1111/blar.13261"]),
  ("Bloco C. Ônus administrativo: por que quem tem direito fica de fora", ["10.1093/ppmgov/gvab027", "10.1016/j.giq.2021.101653", "10.1093/ppmgov/gvac024", "10.7758/rsf.2023.9.5.05"]),
  ("Bloco D. Serviço público digital, inclusivo e centrado no cidadão", ["10.3390/su17072908", "10.1111/padm.70059"]),
 ],
 notas={
  "10.1590/2236-9996.2026-6571161-en": ("Discute o método de cálculo do déficit habitacional com microdados do Censo, baseado na metodologia da Fundação João Pinheiro, com ganhos de transparência e detalhamento territorial.",
                                        "Ajuda a explicar de onde vem o número do déficit e por que ele pode ser calculado por município — base para priorizar ações locais."),
  "10.1590/1678-98732230e020": ("Analisa o processo da política pública do MCMV (criação em 2009, consolidação e extinção em 2021), com fases, modalidades e faixas de renda ao longo de quatro mandatos.",
                                "Contexto histórico: o programa muda de nome, regra e faixa com frequência — por isso o cidadão se perde e precisa de um canal atualizado."),
  "10.1016/j.landusepol.2026.108081": ("Com diferenças-em-diferenças e econometria espacial (2005–2019), estima que municípios com o PMCMV tiveram PIB per capita ~7,7% maior e salários formais ~5,6% maiores, com efeito anticíclico na recessão de 2014–2016.",
                                       "Argumento de impacto: habitação social gera desenvolvimento local — ampliar o acesso tem retorno econômico."),
  "10.1590/0034-761220190341": ("Avalia a eficiência relativa dos municípios brasileiros na execução do MCMV (2012–2016) e os fatores que afetam essa eficiência.",
                                "Mostra que a capacidade municipal varia muito — o CasaHumanizada pode apoiar prefeituras com menos estrutura."),
  "10.21527/2237-6453.2021.55.10215": ("Com 144 questionários com famílias beneficiárias em Santa Maria/RS e entrevista com o agente operacional, mede a satisfação com o MCMV para orientar a gestão pública.",
                                       "Modelo de pesquisa próximo da nossa (questionário com beneficiários) — boa referência de método."),
  "10.1590/1678-6971/eramg210115": ("Mede o bem-estar financeiro de beneficiários do MCMV com a escala do CFPB e testa o letramento financeiro como antecedente do bem-estar.",
                                    "A casa não resolve tudo: orientação financeira depois da conquista também é parte de um atendimento humanizado."),
  "10.5334/bc.180": ("Com 162 moradores e dois estudos de caso, mostra que a habitação social padronizada ignora as necessidades que mudam ao longo do tempo e gera custos para os moradores.",
                     "Humanizar é ouvir a família: justifica o app coletar preferências e necessidades (sem dados sensíveis)."),
  "10.1111/blar.13261": ("Investiga como o MCMV, somado a conjunturas locais, piorou condições de vida de muitos moradores e aumentou a segregação socioespacial no Rio de Janeiro, gerando desconfiança política.",
                         "Alerta: confiança é frágil. O CasaHumanizada precisa de transparência total e não pode prometer casa."),
  "10.1093/ppmgov/gvab027": ("Organiza o conceito de ônus administrativo, separando o que o Estado faz (regras, exigências) do que o cidadão experimenta (custos de aprendizagem, conformidade e psicológicos).",
                             "Referencial teórico central do grupo: o app ataca os três custos (informação, documentos, desgaste)."),
  "10.1016/j.giq.2021.101653": ("Estuda a autoatendimento digital obrigatório em serviços sociais complexos: o cidadão vira um \"assistente social acidental\", assumindo tarefas antes feitas pelo servidor.",
                                "Alerta de design: digitalizar sem apoio humano transfere o trabalho para quem tem menos recursos. Daí o \"humanizada\"."),
  "10.1093/ppmgov/gvac024": ("Propõe agenda de pesquisa sobre ônus administrativo digital: decisões automatizadas, interações digitais e uso de dados podem criar novos custos ao cidadão.",
                             "Mais um cuidado: o app não deve criar novas barreiras (senhas, uploads difíceis, linguagem técnica)."),
  "10.7758/rsf.2023.9.5.05": ("Com pesquisas nacionais com mais de 200 programas de auxílio-aluguel emergencial nos EUA, analisa os ônus administrativos e os desafios particulares da habitação (engajar inquilinos e proprietários).",
                              "Evidência de que o **desenho do processo** define quem acessa o benefício habitacional."),
  "10.3390/su17072908": ("Estudo qualitativo com casos de vários países: letramento digital limitado, falta de infraestrutura e barreiras institucionais dificultam a inclusão digital de comunidades marginalizadas no governo eletrônico.",
                         "Sustenta a opção de atendimento humano/presencial e linguagem simples."),
  "10.1111/padm.70059": ("Combinando pesquisa com cidadãos e oficinas de cocriação numa cidade italiana, mostra que ciclos iterativos e participativos (design centrado no cidadão) reduzem a distância entre demanda e satisfação.",
                         "Justifica cocriar o CasaHumanizada com famílias e servidores — a pesquisa de campo é o primeiro ciclo."),
 },
 argumentos=[
  "\"Só em Cuiabá, **83.991 famílias** se inscreveram no Casa Cuiabana em 2025 (Prefeitura de Cuiabá) — a demanda está aqui do lado.\"",
  "\"O déficit habitacional é de **6,2 milhões** de domicílios, e **52,2%** dele é aluguel pesado demais (FJP, 2022).\"",
  "\"O MCMV já contratou **mais de 1,9 milhão** de unidades desde 2023 — programa existe; o gargalo é o acesso.\"",
  "\"Quem tem direito fica de fora por **ônus administrativo**: aprender, comprovar, esperar (Bækgaard & Tankink, 2021).\"",
  "\"Digital sem apoio transforma o cidadão em **assistente social de si mesmo** (Madsen et al., 2021) — por isso o CasaHumanizada é digital **e** humano.\"",
  "\"O desenho do processo define quem consegue o benefício habitacional (Aiken et al., 2023).\"",
  "\"Habitação social gera **desenvolvimento local**: +7,7% de PIB per capita nos municípios do MCMV (Marca et al., 2026).\"",
 ],
 lacunas=[
  "O número de unidades contratadas do MCMV muda mês a mês; conferir no Ministério das Cidades na véspera da defesa `[verificar]`.",
  "O app **não substitui** o cadastro oficial (CadÚnico, Caixa, prefeitura): ele informa, organiza e encaminha — deixar claro para não parecer golpe.",
  "Não achamos estudo brasileiro sobre ônus administrativo específico do MCMV — **lacuna** que a pesquisa de campo explora.",
  "Dados de renda e benefícios são sensíveis (LGPD): o teste \"tenho direito?\" deve rodar no aparelho, sem enviar dados.",
  "Amostra de 15–20 entrevistas é exploratória.",
 ],
),
}
