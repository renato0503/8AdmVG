"""Fonte única de dados dos 5 grupos do 8AdmVG.

Integrantes e professor(a) responsável vêm de ../grupos.md (lido em gen.py), para que
trocas de integrantes sejam feitas só lá. Aqui ficam: nome do projeto, ideia expandida,
hipótese, roteiro de campo, as 20 perguntas (escala 1–5) e a identidade visual.
"""

TURMA = "8AdmVG"
CURSO = "Administração · 8º Semestre (VG)"
INSTITUICAO = "FACC/Unifacc · Várzea Grande–MT"
COORD = "Prof. Renato Rosa"

PERFIL = [
    ("faixa", "Faixa etária", ["18–24", "25–34", "35–44", "45–59", "60+"]),
    ("sexo", "Sexo", ["Feminino", "Masculino", "Não identificado"]),
    ("classe", "Classe social (estimada)", ["A/B", "C", "D/E", "Não sei estimar"]),
    ("raca", "Raça/cor (estimada)", ["Branca", "Preta", "Parda", "Amarela", "Indígena", "Não sei estimar"]),
]

GRUPOS = {
# ------------------------------------------------------------------ G1
1: dict(
    nome="HoraCerta",
    pasta="Grupo1-HoraCerta",
    slug="horacerta",
    tagline="Suas horas complementares em tempo real, num app só",
    foco="gestão de horas complementares (atividades complementares e extensão) na graduação",
    ideia_expandida=(
        "O **HoraCerta** é um app único para o aluno de graduação acompanhar **em tempo real** tudo o que "
        "se refere às horas complementares: quantas horas o curso exige por categoria, quantas já foram "
        "**validadas**, quantas estão **em análise**, onde estão os **comprovantes** (foto/PDF guardados no "
        "celular) e quais **eventos próximos** valem horas. Do lado da instituição, a coordenação recebe os "
        "comprovantes organizados e valida sem papel."
    ),
    publico="alunos de graduação (presencial e EAD), coordenações de curso e secretarias acadêmicas",
    hipotese=(
        "A maior dor não é a falta de atividades, mas a **falta de controle**: o aluno não sabe quantas horas "
        "já tem validadas, perde comprovantes e deixa tudo para o fim do curso — e isso vira risco de atrasar "
        "a colação de grau."
    ),
    objetivo=(
        "Descobrir como os alunos controlam hoje as horas complementares e validar se a **falta de visibilidade "
        "do saldo**, a **perda de comprovantes** e a **burocracia da validação** são as principais dores."
    ),
    onde="Praça de alimentação, entrada principal e áreas de estudo/lazer",
    quem="Jovens e adultos que estudam ou estudaram em faculdade (18–35 anos, principalmente)",
    como="\"Você faz faculdade? 2 minutinhos de pesquisa sobre horas complementares.\"",
    pitch15="Você faz ou já fez faculdade? Podemos te fazer umas perguntas rápidas sobre horas complementares?",
    triagem=("situacao", "Situação acadêmica (triagem)", ["Estudante de graduação", "Já formado(a)", "Não fez faculdade", "Não sei informar"]),
    nota_campo="Se a pessoa **não fez faculdade**, marque a triagem e agradeça — as 20 perguntas são para quem estuda ou estudou.",
    blocos=[
        ("Conhecimento e situação das horas", "Ribeiro et al. (2023); Santos et al. (2025)", [
            ("O quanto você conhece as regras de horas complementares do seu curso (total exigido, o que vale)", "Não conhece nada", "Conhece muito bem"),
            ("Como está a sua situação de horas em relação ao que falta para se formar", "Muito atrasada", "Em dia ou completa"),
            ("Com que frequência você perdeu uma atividade que valeria horas por não saber dela a tempo", "Nunca", "Sempre"),
            ("Clareza sobre quantas horas você já tem validadas hoje", "Nenhuma clareza", "Clareza total"),
            ("Preocupação de não fechar as horas a tempo da formatura", "Nenhuma", "Muita"),
        ]),
        ("Comprovantes e processo de validação", "Camargo et al. (2026); Aguiar Filho et al. (2024)", [
            ("Com que frequência você já perdeu um certificado ou comprovante", "Nunca", "Sempre"),
            ("Facilidade do processo de entregar e validar horas na sua instituição", "Muito difícil", "Muito fácil"),
            ("Tempo de espera para saber se as horas foram aceitas", "Muito rápido", "Muito demorado"),
            ("Com que frequência teve horas recusadas ou lançadas na categoria errada", "Nunca", "Sempre"),
            ("O quanto o processo depende de papel ou de ir presencialmente à secretaria", "Nada", "Totalmente"),
        ]),
        ("Oportunidades, tempo e motivação", "Chapman et al. (2023); Le (2024); Griffiths et al. (2021)", [
            ("Facilidade de encontrar atividades que valem horas (palestras, cursos, voluntariado)", "Muito difícil", "Muito fácil"),
            ("O que mais pesa na escolha de uma atividade", "Só as horas", "O interesse real"),
            ("O quanto a falta de tempo (trabalho, família) atrapalha cumprir as horas", "Nada", "Muito"),
            ("Valor que você vê nas atividades complementares para a sua carreira", "Nenhum valor", "Muito valor"),
            ("Com que frequência você deixa as horas para a reta final do curso", "Nunca", "Sempre"),
        ]),
        ("App e acompanhamento em tempo real", "Ramaswami et al. (2023); Alam et al. (2023); Wong et al. (2026)", [
            ("Utilidade de ver em tempo real o saldo de horas por categoria", "Nada útil", "Muito útil"),
            ("Utilidade de guardar os comprovantes no celular (foto/PDF)", "Nada útil", "Muito útil"),
            ("Utilidade de receber avisos de eventos que valem horas", "Nada útil", "Muito útil"),
            ("Confiança em enviar comprovantes por app para a coordenação validar", "Nenhuma", "Total"),
            ("Interesse em usar um app único para as horas complementares", "Nenhum", "Muito"),
        ]),
    ],
    tema=dict(accent="#4338ca", dark="#3730a3", soft="#eef2ff", rgb="67,56,202", accent2="#f59e0b",
              tinta="#1e1b4b", tinta2="#3730a3", fundo="#f5f6ff",
              fonte='"Poppins", "Segoe UI", system-ui, Arial, sans-serif',
              fonte_titulo='"Poppins", "Segoe UI", system-ui, Arial, sans-serif',
              gfont="Poppins:wght@400;600;700", tom="Acadêmico e motivador (progresso, metas)"),
),
# ------------------------------------------------------------------ G2
2: dict(
    nome="GuiaMobi",
    pasta="Grupo2-GuiaMobi",
    slug="guiamobi",
    tagline="Seu guia turístico de bolso, guiado pela sua localização",
    foco="turismo guiado por localização (latitude/longitude), rotas e conhecimento sobre o lugar",
    ideia_expandida=(
        "O **GuiaMobi** é um guia turístico de bolso: a partir da **latitude e longitude** do celular, mostra os "
        "atrativos próximos, conta a **história e a cultura** de cada ponto (texto e áudio) e **monta rotas** de "
        "acordo com o tempo disponível (manhã, tarde, dia inteiro) e o perfil do visitante (natureza, história, "
        "gastronomia). O foco inicial é a região de Cuiabá e Várzea Grande, porta de entrada da Chapada dos "
        "Guimarães e do Pantanal."
    ),
    publico="turistas de outras cidades/estados/países e moradores que querem conhecer melhor a própria região",
    hipotese=(
        "As pessoas deixam de conhecer atrativos que estão perto porque **não sabem que eles existem** e "
        "**não têm tempo de montar um roteiro** — a informação existe, mas está espalhada e não é contextualizada "
        "pela localização."
    ),
    objetivo=(
        "Entender como moradores e visitantes planejam passeios e validar se a **falta de informação contextual "
        "(perto de mim, agora)** e a **dificuldade de montar rotas** são dores reais."
    ),
    onde="Praça de alimentação, entrada principal e quiosques de turismo/lojas regionais",
    quem="Adultos em geral; priorizar quem aparenta ser visitante (malas, grupos, sotaque) sem excluir moradores",
    como="\"Você gosta de passear e viajar? 2 minutinhos de pesquisa sobre turismo.\"",
    pitch15="Você costuma passear ou viajar? Podemos fazer umas perguntas rápidas sobre como você escolhe o que visitar?",
    triagem=("relacao", "Relação com a região (triagem)", ["Morador(a) de VG/Cuiabá", "Visitante de outra cidade de MT", "Visitante de outro estado/país", "Não sei informar"]),
    nota_campo="Serve para **moradores e visitantes** — a triagem permite comparar os dois públicos na análise.",
    blocos=[
        ("Hábitos de passeio e viagem", "Ribeiro et al. (2022); Silva et al. (2022)", [
            ("Com que frequência você faz passeios ou viagens de lazer", "Nunca", "Sempre"),
            ("O quanto você conhece os atrativos turísticos da região (Chapada, Pantanal, centro histórico)", "Nada", "Muito"),
            ("Como você costuma montar o roteiro de um passeio", "Improvisa na hora", "Planeja tudo antes"),
            ("Com que frequência já descobriu depois que havia um lugar interessante perto e não visitou", "Nunca", "Sempre"),
            ("Quanto tempo você perde procurando o que fazer quando chega a um lugar", "Pouco", "Muito"),
        ]),
        ("Informação e orientação no destino", "Cilkin & Toksöz (2024); Afolabi et al. (2021)", [
            ("Facilidade de encontrar informação confiável sobre atrativos (horário, preço, acesso)", "Muito difícil", "Muito fácil"),
            ("Com que frequência usa o celular (mapas, redes sociais) para se orientar num passeio", "Nunca", "Sempre"),
            ("Com que frequência contrata guia ou agência de turismo", "Nunca", "Sempre"),
            ("Interesse em conhecer a história e a cultura do lugar visitado", "Nenhum", "Muito"),
            ("Sensação de segurança ao explorar sozinho(a) um lugar desconhecido", "Muito inseguro(a)", "Muito seguro(a)"),
        ]),
        ("Rotas e experiência", "Mou et al. (2022); Zhang et al. (2022); Torabi et al. (2022)", [
            ("Importância de uma rota montada de acordo com o tempo que você tem", "Nada importante", "Muito importante"),
            ("Preferência entre lugares famosos e lugares pouco conhecidos", "Só famosos", "Só pouco conhecidos"),
            ("Importância de apoiar o comércio local (restaurantes, artesanato, guias locais)", "Nada importante", "Muito importante"),
            ("O quanto a falta de sinal de internet atrapalha seus passeios", "Nada", "Muito"),
            ("Com que frequência você compartilha passeios nas redes sociais", "Nunca", "Sempre"),
        ]),
        ("O guia de bolso (app)", "Xiong & Zhang (2024); Evagelou et al. (2024); Gao et al. (2023)", [
            ("Utilidade de um app que mostra atrativos próximos pela sua localização", "Nada útil", "Muito útil"),
            ("Utilidade de um áudio/narração contando a história do lugar", "Nada útil", "Muito útil"),
            ("Utilidade de uma rota automática (manhã, tarde ou dia inteiro)", "Nada útil", "Muito útil"),
            ("Conforto em compartilhar sua localização com um app de turismo", "Nenhum", "Total"),
            ("Interesse em usar um guia turístico de bolso no celular", "Nenhum", "Muito"),
        ]),
    ],
    tema=dict(accent="#0f766e", dark="#115e59", soft="#f0fdfa", rgb="15,118,110", accent2="#f97316",
              tinta="#042f2e", tinta2="#115e59", fundo="#f3fbf9",
              fonte='"Nunito", "Segoe UI", system-ui, Arial, sans-serif',
              fonte_titulo='"Nunito", "Segoe UI", system-ui, Arial, sans-serif',
              gfont="Nunito:wght@400;700;800", tom="Aventura e descoberta (natureza, pôr do sol)"),
),
# ------------------------------------------------------------------ G3
3: dict(
    nome="VozGuia",
    pasta="Grupo3-VozGuia",
    slug="vozguia",
    tagline="O celular vira um assistente sonoro — e a cidade fica sabendo onde está o obstáculo",
    foco="autonomia de pessoas cegas e com baixa visão (assistente sonoro) e alertas de acessibilidade ao poder público",
    ideia_expandida=(
        "O **VozGuia** transforma o celular da pessoa cega ou com baixa visão em um **assistente sonoro**: "
        "anuncia por voz e vibração o que está por perto (pontos de ônibus, faixas, obstáculos já mapeados), "
        "guia rotas conhecidas e lê informações em voz alta. Ao mesmo tempo, funciona como **canal de alertas ao "
        "poder público**: o usuário (ou um acompanhante) registra com um toque o obstáculo encontrado — buraco, "
        "calçada quebrada, piso tátil interrompido — e o alerta vai para o órgão responsável com local, foto e "
        "protocolo, formando um **mapa colaborativo de acessibilidade**."
    ),
    publico="pessoas cegas e com baixa visão, seus familiares e acompanhantes, e órgãos públicos (prefeitura, secretarias de mobilidade e de pessoa com deficiência)",
    hipotese=(
        "A falta de autonomia da pessoa cega na rua vem mais da **falta de informação sobre o caminho** (onde estão "
        "os obstáculos e os pontos de referência) do que da falta de tecnologia — e os problemas de acessibilidade "
        "persistem porque **não chegam ao poder público de forma organizada**."
    ),
    objetivo=(
        "Medir como a população percebe a acessibilidade urbana para pessoas cegas e validar se um **assistente "
        "sonoro** somado a um **canal de alertas ao poder público** é visto como útil e confiável."
    ),
    onde="Entrada principal, corredores de acesso e ponto de ônibus/estacionamento do shopping",
    quem="Adultos em geral; com atenção e respeito, incluir pessoas com deficiência visual e seus acompanhantes",
    como="\"Podemos te fazer umas perguntas rápidas sobre acessibilidade na cidade?\"",
    pitch15="Estamos pesquisando acessibilidade para pessoas cegas em Várzea Grande. São 2 minutinhos e é anônimo.",
    triagem=("relacao_dv", "Relação com deficiência visual (triagem)", ["Tem deficiência visual", "Convive com alguém com DV", "Não convive", "Prefere não informar"]),
    nota_campo=(
        "**Tema sensível e de acessibilidade.** Se o(a) entrevistado(a) tiver deficiência visual: apresente-se pelo "
        "nome, **leia as opções em voz alta** e confirme a marcação com a pessoa. Nunca toque ou conduza a pessoa sem "
        "perguntar antes. Pergunte a triagem com delicadeza (\"você convive com alguém que tem deficiência visual?\")."
    ),
    blocos=[
        ("Percepção da acessibilidade na cidade", "Cohen et al. (2024); Caetano et al. (2021); Nuzzi et al. (2024)", [
            ("Como você avalia as calçadas da cidade para quem não enxerga", "Muito ruins", "Muito boas"),
            ("Com que frequência você vê obstáculos nas calçadas (buracos, postes, carros, entulho)", "Nunca", "Sempre"),
            ("Presença de piso tátil e semáforo sonoro nos lugares que você frequenta", "Nenhuma", "Em todo lugar"),
            ("O quanto você acha que uma pessoa cega consegue andar sozinha com segurança no centro da cidade", "Nada", "Totalmente"),
            ("Acessibilidade do transporte público para cegos (achar o ponto, identificar o ônibus)", "Muito ruim", "Muito boa"),
        ]),
        ("Autonomia e tecnologia", "Abidi et al. (2024); Kuriakose et al. (2022); Theodorou et al. (2022)", [
            ("O quanto a pessoa com deficiência visual depende de outra pessoa para se deslocar (sua percepção)", "Nada", "Totalmente"),
            ("Conhecimento dos recursos de acessibilidade do celular (leitor de tela, TalkBack, VoiceOver)", "Nenhum", "Muito"),
            ("Confiança em um app que orienta o deslocamento por voz", "Nenhuma", "Total"),
            ("Importância de o app funcionar mesmo sem internet", "Nada importante", "Muito importante"),
            ("Preferência de aviso no celular", "Só vibração", "Só voz"),
        ]),
        ("Alertas ao poder público", "Labbé et al. (2023); Morra et al. (2024)", [
            ("Com que frequência você já reclamou de um problema urbano na prefeitura", "Nunca", "Sempre"),
            ("Facilidade de registrar uma reclamação na prefeitura hoje", "Muito difícil", "Muito fácil"),
            ("Confiança de que a prefeitura resolve os problemas relatados", "Nenhuma", "Total"),
            ("Importância de acompanhar o andamento do alerta (protocolo, prazo, resposta)", "Nada importante", "Muito importante"),
            ("Disposição para registrar um alerta de obstáculo quando encontrar um", "Nenhuma", "Total"),
        ]),
        ("O assistente sonoro (app)", "See et al. (2022); Martínez-Cruz et al. (2021); Cunha & Santos (2022)", [
            ("Utilidade de um app que avisa por voz o que está à frente (obstáculo, faixa, ponto de ônibus)", "Nada útil", "Muito útil"),
            ("Utilidade de um mapa colaborativo de pontos perigosos para pedestres", "Nada útil", "Muito útil"),
            ("Utilidade de um botão que envia alerta com foto e local ao órgão público", "Nada útil", "Muito útil"),
            ("Importância de o app ser gratuito e apoiado pelo poder público", "Nada importante", "Muito importante"),
            ("Interesse em usar ou indicar o app (para você ou alguém que conhece)", "Nenhum", "Muito"),
        ]),
    ],
    tema=dict(accent="#1e3a8a", dark="#172554", soft="#eff6ff", rgb="30,58,138", accent2="#facc15",
              tinta="#0b1020", tinta2="#1e3a8a", fundo="#f7f8fb",
              fonte='"Atkinson Hyperlegible", "Segoe UI", system-ui, Arial, sans-serif',
              fonte_titulo='"Atkinson Hyperlegible", "Segoe UI", system-ui, Arial, sans-serif',
              gfont="Atkinson+Hyperlegible:wght@400;700", tom="Alto contraste e clareza (azul-marinho + amarelo)"),
),
# ------------------------------------------------------------------ G4
4: dict(
    nome="CasaPiloto",
    pasta="Grupo4-CasaPiloto",
    slug="casapiloto",
    tagline="Escolha a casa e veja o caminho: guardar, investir ou financiar",
    foco="simulação de compra do imóvel para construtoras: quanto guardar, investir ou financiar por tipo de casa",
    ideia_expandida=(
        "O **CasaPiloto** é um simulador oferecido por **construtoras** a quem quer comprar a casa: a pessoa escolhe "
        "o **tipo de casa** desejado (a \"casa piloto\" — modelo, tamanho, padrão de acabamento) e o app mostra, lado a "
        "lado, **três caminhos**: quanto **guardar** por mês para comprar à vista ou dar a entrada, quanto render "
        "**investindo** esse valor e quanto custa **financiar** (parcela, prazo, juros, uso do FGTS). A construtora "
        "ganha um cliente preparado; o cliente ganha um plano realista antes de sentar com o corretor."
    ),
    publico="famílias que pagam aluguel ou moram com parentes e querem comprar a casa; construtoras e incorporadoras de médio porte",
    hipotese=(
        "As pessoas não compram (ou compram mal) porque **não conseguem traduzir o sonho da casa em números mensais** — "
        "não sabem quanto guardar, onde investir nem se a parcela cabe — e desconfiam da simulação feita só pelo "
        "corretor no plantão de vendas."
    ),
    objetivo=(
        "Descobrir como as pessoas se preparam financeiramente para comprar o imóvel e validar se um **simulador por "
        "tipo de casa** (guardar × investir × financiar) oferecido pela construtora gera confiança e interesse."
    ),
    onde="Praça de alimentação, entrada principal e perto de estandes de imobiliárias/construtoras",
    quem="Adultos que aparentam formar família ou morar de aluguel (25–59 anos)",
    como="\"Você pensa em comprar sua casa? 2 minutinhos de pesquisa, é anônima.\"",
    pitch15="Você pensa em comprar casa ou apartamento? Podemos fazer umas perguntas rápidas sobre como se planejar pra isso?",
    triagem=("moradia", "Moradia atual (triagem)", ["Aluguel", "Própria financiada", "Própria quitada", "Cedida / com família"]),
    nota_campo="**Nunca pergunte renda, salário ou valor de patrimônio.** Meça só percepções (\"a parcela te dá medo?\").",
    blocos=[
        ("Desejo e momento da compra", "Hassan et al. (2021); Kaynak et al. (2022)", [
            ("Força do desejo de comprar casa ou apartamento nos próximos anos", "Nenhum", "Muito forte"),
            ("Clareza sobre o tipo de casa que você quer (tamanho, quartos, padrão)", "Nenhuma", "Total"),
            ("Com que frequência você visita decorados, casas modelo ou plantões de venda", "Nunca", "Sempre"),
            ("Confiança no que as construtoras mostram no plantão e no decorado", "Nenhuma", "Total"),
            ("O quanto você já pesquisou preços de imóveis na planta ou prontos", "Nada", "Muito"),
        ]),
        ("Guardar, investir e financiar", "Thorp et al. (2023); Ilan & Mugerman (2025); Schlafmann (2021)", [
            ("Clareza sobre quanto precisa guardar para a entrada", "Nenhuma", "Total"),
            ("Com que frequência você consegue guardar dinheiro todo mês", "Nunca", "Sempre"),
            ("Conhecimento sobre onde investir o dinheiro da entrada (poupança, CDB, Tesouro)", "Nenhum", "Muito"),
            ("Entendimento de financiamento (juros, prazo, SAC/Price, uso do FGTS)", "Nenhum", "Muito"),
            ("Medo de a parcela não caber no orçamento", "Nenhum", "Muito"),
        ]),
        ("Relação com a construtora", "Lee & Liu (2025); Hu et al. (2024)", [
            ("Importância de simular valores sozinho(a) antes de falar com o corretor", "Nada importante", "Muito importante"),
            ("O quanto você se sente pressionado(a) a fechar negócio no plantão de vendas", "Nada", "Muito"),
            ("Facilidade de comparar o valor final de casas de tipos e padrões diferentes", "Muito difícil", "Muito fácil"),
            ("Importância de a construtora acompanhar seu plano de poupança até a compra", "Nada importante", "Muito importante"),
            ("Confiança em informar sua faixa de renda à construtora para simular", "Nenhuma", "Total"),
        ]),
        ("O simulador CasaPiloto", "Azmi et al. (2021); Yan et al. (2024); Miljković et al. (2023)", [
            ("Utilidade de escolher o tipo de casa e ver quanto guardar por mês", "Nada útil", "Muito útil"),
            ("Utilidade de comparar lado a lado guardar × investir × financiar", "Nada útil", "Muito útil"),
            ("Utilidade de conhecer a casa piloto virtualmente (fotos 360°, planta)", "Nada útil", "Muito útil"),
            ("Utilidade de metas de poupança com lembretes no celular", "Nada útil", "Muito útil"),
            ("Interesse em usar um simulador da construtora antes de comprar", "Nenhum", "Muito"),
        ]),
    ],
    tema=dict(accent="#b45309", dark="#92400e", soft="#fffbeb", rgb="180,83,9", accent2="#0d9488",
              tinta="#1c1917", tinta2="#44403c", fundo="#fbf8f4",
              fonte='"Inter", "Segoe UI", system-ui, Arial, sans-serif',
              fonte_titulo='"Space Grotesk", "Segoe UI", system-ui, Arial, sans-serif',
              gfont="Space+Grotesk:wght@500;700&family=Inter:wght@400;600", tom="Construção e planejamento (planta, régua, concreto)"),
),
# ------------------------------------------------------------------ G5
5: dict(
    nome="CasaHumanizada",
    pasta="Grupo5-CasaHumanizada",
    slug="casahumanizada",
    tagline="Todos os programas de moradia num lugar só — com atendimento humano",
    foco="acesso a programas habitacionais: informação, cadastro e acompanhamento dos processos de moradia",
    ideia_expandida=(
        "O **CasaHumanizada** é uma plataforma digital que **centraliza as informações sobre programas e oportunidades "
        "habitacionais** (municipais, como o Casa Cuiabana; estaduais; e federais, como o Minha Casa, Minha Vida), explica os "
        "**requisitos sem jargões**, faz um **teste rápido de elegibilidade** (\"tenho direito?\"), guia o **checklist de "
        "documentos**, mostra o **status do cadastro em tempo real**, com **etapas e prazos**, e envia **notificações** de "
        "atualização — tudo em linguagem simples e com opção de **atendimento humano** para quem tem dificuldade com o digital. "
        "O grupo trata o projeto como **gestão da mudança** na inovação pública: preparar cidadãos e servidores para trocar "
        "uma jornada fragmentada por uma experiência acessível."
    ),
    publico="famílias de baixa e média renda que pagam aluguel, moram de favor ou em condição precária; órgãos de habitação e assistência social",
    hipotese=(
        "Muitas famílias que teriam direito a um programa habitacional **não chegam a se inscrever, perdem prazos ou desistem no meio** "
        "— não por falta de programas, mas por **falta de informação clara, excesso de burocracia e atendimento pouco "
        "humanizado** (o chamado ônus administrativo)."
    ),
    objetivo=(
        "Medir o quanto as pessoas conhecem os programas habitacionais e validar se **informação centralizada**, "
        "**cadastro simplificado** e **acompanhamento humanizado** resolvem a dor de acesso."
    ),
    onde="Entrada principal, praça de alimentação e corredores de serviços (lotéricas, bancos)",
    quem="Adultos que aparentam pagar aluguel ou chefiar família (25–59 anos)",
    como="\"2 minutinhos de pesquisa sobre moradia e programas habitacionais? É anônima.\"",
    pitch15="Estamos pesquisando como as pessoas procuram programas de moradia. Podemos fazer umas perguntas rápidas?",
    triagem=("moradia", "Situação de moradia (triagem)", ["Aluguel", "Própria", "Cedida / com família", "Não sei informar"]),
    nota_campo=(
        "Tema **sensível** (renda e moradia): **nunca pergunte renda nem se a pessoa recebe benefício**. Se a pessoa "
        "se emocionar ou contar uma situação difícil, acolha e não insista."
    ),
    blocos=[
        ("Moradia e necessidade", "Forcel et al. (2026); Villa et al. (2022)", [
            ("O quanto o aluguel ou o custo de moradia pesa no orçamento da família", "Pesa pouco", "Pesa muito"),
            ("Como você avalia a condição da sua moradia atual (espaço, estrutura)", "Muito ruim", "Muito boa"),
            ("Força da necessidade de conseguir a moradia própria", "Nenhuma", "Muito forte"),
            ("Com que frequência já pensou em se inscrever em um programa habitacional", "Nunca", "Sempre"),
            ("Há quanto tempo procura uma solução de moradia", "Não procura", "Há muitos anos"),
        ]),
        ("Informação sobre os programas", "Euclydes et al. (2022); Vieira et al. (2021)", [
            ("Conhecimento dos programas habitacionais existentes (Minha Casa, Minha Vida e outros)", "Nenhum", "Muito"),
            ("Clareza sobre se a sua família tem direito (faixa de renda, requisitos)", "Nenhuma", "Total"),
            ("Facilidade de encontrar informação oficial e confiável sobre moradia", "Muito difícil", "Muito fácil"),
            ("Com que frequência recebeu informação errada ou soube de golpe envolvendo programa habitacional", "Nunca", "Sempre"),
            ("Conhecimento sobre o CadÚnico e a importância de mantê-lo atualizado", "Nenhum", "Muito"),
        ]),
        ("Cadastro, atendimento e acompanhamento", "Bækgaard & Tankink (2021); Madsen et al. (2021); Peeters (2022)", [
            ("Facilidade do processo de cadastro ou inscrição (se já tentou ou imagina)", "Muito difícil", "Muito fácil"),
            ("Clareza sobre quais documentos são exigidos", "Nenhuma", "Total"),
            ("Com que frequência precisou voltar várias vezes a um órgão público para resolver algo", "Nunca", "Sempre"),
            ("Como você se sentiu tratado(a) no atendimento público de moradia/assistência", "Muito mal", "Muito bem"),
            ("Clareza sobre o andamento de um processo depois de se inscrever", "Nenhuma", "Total"),
        ]),
        ("O app CasaHumanizada", "Djatmika et al. (2025); Choi & Cucciniello (2026); Aiken et al. (2023)", [
            ("Utilidade de um app que reúne todos os programas de moradia num lugar só", "Nada útil", "Muito útil"),
            ("Utilidade de um teste rápido \"tenho direito?\"", "Nada útil", "Muito útil"),
            ("Utilidade de acompanhar o processo pelo celular, com avisos", "Nada útil", "Muito útil"),
            ("Confiança em enviar documentos por um app", "Nenhuma", "Total"),
            ("Interesse em usar o CasaHumanizada (ou indicar a alguém)", "Nenhum", "Muito"),
        ]),
    ],
    tema=dict(accent="#15803d", dark="#166534", soft="#f0fdf4", rgb="21,128,61", accent2="#e11d48",
              tinta="#14301f", tinta2="#166534", fundo="#f6fbf7",
              fonte='"Nunito Sans", "Segoe UI", system-ui, Arial, sans-serif',
              fonte_titulo='"Lora", Georgia, serif',
              gfont="Nunito+Sans:wght@400;700&family=Lora:wght@600;700", tom="Acolhedor e humano (casa, cuidado, confiança)"),
),
}

FUNCOES = ["Formulário + controle de tempo", "Abordagem", "Áudio (WhatsApp) + código", "Tabulação", "Abordagem + apoio"]
