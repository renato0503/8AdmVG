"""Textos curtos usados nos slides, landing pages e hub: problema, 3 cartões da ideia e pitch de 30s."""

EXTRA = {
1: dict(
    problema=[
        "Todo aluno de graduação precisa cumprir <strong>horas complementares</strong> e, desde 2018, <strong>horas de extensão</strong> (mínimo de 10% da carga horária) para se formar.",
        "O controle ainda é <strong>manual</strong>: certificado em papel, e-mail, planilha e fila na secretaria.",
        "O aluno <strong>não sabe o saldo</strong> que já tem validado, <strong>perde comprovantes</strong> e só descobre o que falta no fim do curso.",
        "Quem trabalha e estuda tem <strong>pouco tempo</strong> e perde eventos que valeriam horas por não ficar sabendo.",
        "Resultado: correria no último semestre e risco de <strong>atrasar a colação de grau</strong>.",
    ],
    destaque=("<strong>9,9 milhões</strong> de matrículas na graduação (INEP, 2023) — e uma universidade brasileira descreve o processo de atividades complementares como \"manual, descentralizado e altamente burocrático\", com extravio de comprovantes (Camargo et al., 2026).",
              "INEP, Censo da Educação Superior 2023 · Camargo et al. (2026), DOI 10.66104/zh5a8c55"),
    cards=[
        ("Saldo em tempo real", "Painel com horas exigidas, validadas, em análise e faltantes — por categoria (ensino, pesquisa, extensão, cultura)."),
        ("Comprovantes no bolso", "Foto ou PDF do certificado vira comprovante na hora, enviado para a coordenação validar sem papel."),
        ("Oportunidades próximas", "Agenda de eventos e cursos que valem horas, com aviso — para o aluno que tem pouco tempo."),
    ],
    diferencial="Um app <strong>único</strong> do aluno para todas as horas — e, para a faculdade, validação organizada e sem papel.",
    pitch30=("Você está no fim do curso e não sabe quantas horas complementares ainda faltam? Perdeu aquele certificado? "
             "O HoraCerta mostra em tempo real quantas horas você já tem validadas, quantas faltam em cada categoria e "
             "quais eventos perto de você valem horas. Tirou foto do certificado, está enviado para a coordenação. "
             "Sem papel, sem fila, sem susto na formatura. Suas horas, certas, na palma da mão."),
),
2: dict(
    problema=[
        "O turismo bate recordes, e <strong>Várzea Grande é a porta de entrada</strong> de Mato Grosso (aeroporto internacional).",
        "Visitantes e até moradores <strong>não sabem o que existe perto</strong>: história, cultura, natureza e comércio local ficam invisíveis.",
        "A informação está <strong>espalhada</strong> (redes sociais, sites, boca a boca) e não é contextualizada pela localização.",
        "Montar um roteiro que caiba no <strong>tempo disponível</strong> dá trabalho — e guia contratado nem sempre cabe no bolso.",
        "Em áreas naturais, <strong>o sinal de internet falha</strong> justamente quando o turista mais precisa de orientação.",
    ],
    destaque=("<strong>9,3 milhões</strong> de turistas internacionais no Brasil em 2025, recorde (Embratur) · <strong>1,2 milhão</strong> de turistas em MT (+18%) e a Chapada dos Guimarães passou de 92 mil para <strong>183 mil</strong> visitas (Sedec-MT).",
              "Embratur (2026) · Sedec-MT / DataHub MT (2025)"),
    cards=[
        ("Perto de mim, agora", "Pela latitude e longitude do celular, mostra os atrativos próximos com distância, horário e acesso."),
        ("Guia que conta a história", "Cada ponto tem texto e narração em áudio sobre história, cultura e curiosidades — um guia de bolso."),
        ("Rota do seu jeito", "Monta roteiros por tempo (manhã, tarde, dia) e interesse (natureza, história, gastronomia), com modo offline."),
    ],
    diferencial="Conteúdo <strong>local</strong> e contextualizado pela localização, valorizando guias e comércio da região.",
    pitch30=("Chegou em Várzea Grande ou Cuiabá e não sabe o que fazer com a tarde livre? O RotaViva usa a sua localização "
             "para mostrar o que tem de interessante perto de você, conta a história de cada lugar em áudio, como um guia de "
             "bolso, e monta uma rota que cabe no seu tempo — da Chapada ao centro histórico, passando pelo comércio local. "
             "Menos tempo procurando, mais tempo vivendo o lugar."),
),
3: dict(
    problema=[
        "<strong>7,9 milhões</strong> de brasileiros têm dificuldade de enxergar mesmo com óculos (IBGE, Censo 2022).",
        "Calçadas com buracos, postes, carros e piso tátil interrompido tornam o deslocamento <strong>perigoso e dependente</strong> de outra pessoa.",
        "Tecnologias assistivas dedicadas são <strong>caras</strong> e exigem treino; o celular, que já está no bolso, é pouco aproveitado.",
        "Os obstáculos <strong>não chegam ao poder público</strong> de forma organizada: falta dado para priorizar obras de acessibilidade.",
        "A Lei Brasileira de Inclusão garante acessibilidade, mas a execução nas cidades ainda é <strong>lenta e fragmentada</strong>.",
    ],
    destaque=("<strong>14,4 milhões</strong> de pessoas com deficiência no Brasil (7,3%) e <strong>enxergar</strong> é a dificuldade funcional mais comum: <strong>7,9 milhões</strong> (IBGE, Censo 2022).",
              "IBGE, Censo Demográfico 2022 — pessoas com deficiência"),
    cards=[
        ("Assistente sonoro", "O celular anuncia por voz e vibração pontos de ônibus, faixas e obstáculos mapeados no caminho."),
        ("Mapa colaborativo", "Usuários, familiares e voluntários registram obstáculos — o mapa de acessibilidade melhora com o uso."),
        ("Alerta ao poder público", "Um toque envia local, foto e categoria do problema ao órgão responsável, com protocolo e acompanhamento."),
    ],
    diferencial="Une <strong>autonomia</strong> de quem não enxerga e <strong>dados</strong> para o poder público agir — no celular que a pessoa já tem.",
    pitch30=("Imagine atravessar a cidade sem enxergar a calçada. O VozGuia transforma o celular em um assistente sonoro: "
             "avisa por voz onde está o ponto de ônibus, a faixa e o buraco que alguém já registrou. E, quando encontra um "
             "obstáculo novo, com um toque o alerta vai para a prefeitura com local, foto e protocolo. Mais autonomia para "
             "quem não enxerga, mais informação para quem precisa consertar a cidade."),
),
4: dict(
    problema=[
        "Quem quer comprar a casa visita o decorado, se encanta — mas <strong>não sabe traduzir o sonho em números</strong> mensais.",
        "Não sabe <strong>quanto guardar</strong> para a entrada, <strong>onde investir</strong> enquanto junta nem se a <strong>parcela cabe</strong>.",
        "A simulação feita só no plantão gera <strong>desconfiança</strong> e sensação de pressão para fechar negócio.",
        "Mais da metade do déficit habitacional é <strong>aluguel pesado demais</strong>: sobra pouco para juntar a entrada.",
        "Para a construtora: visitas que não viram venda e clientes que <strong>desistem na análise de crédito</strong>.",
    ],
    destaque=("Financiamento habitacional de <strong>R$ 134,6 bilhões</strong> só no 1º semestre de 2025 (Abecip) e nova <strong>Faixa 4</strong> do MCMV para renda até R$ 12 mil — mercado aquecido, comprador despreparado.",
              "Abecip (2025) · Agência Brasil / Ministério das Cidades (2025)"),
    cards=[
        ("Escolha a casa piloto", "Tipos de casa da construtora (tamanho, quartos, acabamento) com planta e preço de referência."),
        ("Três caminhos lado a lado", "Guardar × investir × financiar: quanto por mês, em quanto tempo e quanto custa no total."),
        ("Plano até a chave", "Metas de poupança com lembretes, uso do FGTS e checklist de documentos até a compra."),
    ],
    diferencial="O cliente chega ao corretor <strong>preparado</strong>; a construtora ganha lead qualificado e venda mais rápida.",
    pitch30=("Você visitou o decorado, se apaixonou pela casa, mas saiu sem saber se consegue comprar. No CasaPiloto você "
             "escolhe o tipo de casa e vê, lado a lado, quanto precisa guardar por mês, quanto renderia investindo e quanto "
             "custa financiar. Tudo no seu celular, no seu tempo, antes de falar com o corretor. A casa dos sonhos vira um "
             "plano com data para acontecer."),
),
5: dict(
    problema=[
        "Só o programa <strong>Casa Cuiabana</strong> recebeu <strong>83.991 inscrições</strong> em 2025 — a demanda por moradia é imensa aqui do lado.",
        "Existem programas federais, estaduais e municipais, mas a informação está <strong>espalhada</strong> e muda com frequência.",
        "A jornada é fragmentada: <strong>cadastro e triagem → documentos físicos → análise e seleção → acompanhamento de prazos</strong>.",
        "A família não sabe se <strong>tem direito</strong>, quais documentos levar nem em que etapa está — e corre o risco de <strong>perder prazos</strong>.",
                "Informação confusa abre espaço para <strong>golpes</strong> envolvendo \"inscrição\" em programas habitacionais.",
    ],
    destaque=("<strong>83.991</strong> cadastros no Casa Cuiabana em 2025 (Prefeitura de Cuiabá) · <strong>6,2 milhões</strong> de domicílios em déficit habitacional no Brasil, <strong>52,2%</strong> por aluguel pesado demais (FJP, 2022).",
              "Prefeitura de Cuiabá (2025) · Fundação João Pinheiro (2024)"),
    cards=[
        ("Tudo num lugar só", "Programas habitacionais reunidos, com requisitos em linguagem simples e fonte oficial de cada informação."),
        ("\"Tenho direito?\"", "Teste rápido de elegibilidade, que roda no celular sem enviar dados, e checklist de documentos."),
        ("Status, prazos e avisos", "Linha do tempo do cadastro com etapas, prazos e notificações — e opção de falar com uma pessoa."),
    ],
    ideia_slide="O <strong>CasaHumanizada</strong> é uma plataforma digital que centraliza os programas de moradia e torna a jornada do cidadão <strong>simples, clara e humanizada</strong> — do cadastro à entrega das chaves.",
    diferencial="Digital <strong>e</strong> humano: reduz o ônus administrativo sem transferir o trabalho para quem tem menos recursos.",
    pitch30=("Você paga um aluguel que pesa no bolso e já ouviu falar de programa de moradia, mas não sabe se tem direito, "
             "que documentos levar nem onde se inscrever? O CasaHumanizada reúne todos os programas num lugar só, faz um "
             "teste rápido pra você saber se se encaixa, organiza os documentos e mostra em que etapa está o seu processo — "
             "com gente de verdade pra ajudar quando precisar. Moradia é direito; o caminho até ela tem que ser simples."),
),
}

# KPIs do slide 5 (número grande, rótulo, fonte) — só números com fonte na tabela do Pesquisa-Dados.md
KPIS = {
1: [("9,9 mi", "matrículas na graduação (2023)", "INEP, Censo da Educação Superior"),
    ("79,3%", "das matrículas em IES privadas (2023)", "INEP, Censo da Educação Superior"),
    ("10%", "da carga horária mínima em extensão", "Resolução CNE/CES nº 7/2018"),
    ("≤ 20%", "da carga horária: estágio + atividades complementares", "Resolução CNE/CES nº 2/2007"),
    ("17,5%", "evasão anual 2023–2024 [verificar]", "INEP, Censo 2024 (via imprensa)"),
    ("65%", "dos internautas acessam só pelo celular (2025)", "TIC Domicílios 2025")],
2: [("9,3 mi", "turistas internacionais no Brasil (2025, recorde)", "Embratur"),
    ("US$ 7,9 bi", "gastos por estrangeiros no Brasil (2025)", "Embratur"),
    ("1,2 mi", "turistas em Mato Grosso (2025, +18%)", "Sedec-MT / DataHub MT"),
    ("183 mil", "visitas ao PN Chapada dos Guimarães (2025)", "Sedec-MT"),
    ("22,6 mil", "estrangeiros no aeroporto de VG (jan–out 2025)", "Sedec-MT / DataHub MT"),
    ("65%", "dos internautas acessam só pelo celular (2025)", "TIC Domicílios 2025")],
3: [("14,4 mi", "pessoas com deficiência no Brasil (2022)", "IBGE, Censo 2022"),
    ("7,9 mi", "com dificuldade de enxergar mesmo com óculos", "IBGE, Censo 2022"),
    ("7,3%", "da população com 2 anos ou mais tem deficiência", "IBGE, Censo 2022"),
    ("2015", "Lei Brasileira de Inclusão garante acessibilidade", "Lei nº 13.146/2015"),
    ("2013", "desde quando prefeituras recebem demandas por app (Colab)", "Comunitas"),
    ("88%", "da população usou internet (2025)", "TIC Domicílios 2025")],
4: [("R$ 134,6 bi", "financiamento habitacional no 1º sem. 2025 (+25%)", "Abecip"),
    ("R$ 78,7 bi", "via poupança/SBPE no 1º sem. 2025 (+22%)", "Abecip"),
    ("R$ 12 mil", "teto de renda da nova Faixa 4 do MCMV (2025)", "Agência Brasil / MCid"),
    ("10,5% a.a.", "juros da Faixa 4, até 420 parcelas", "Agência Brasil / MCid"),
    ("6,2 mi", "domicílios em déficit habitacional (2022)", "Fundação João Pinheiro"),
    ("52,2%", "do déficit é aluguel pesado demais", "Fundação João Pinheiro")],
5: [("83.991", "inscrições no Casa Cuiabana (jul–set/2025)", "Prefeitura de Cuiabá"),
    ("6,2 mi", "domicílios em déficit habitacional (2022)", "Fundação João Pinheiro"),
    ("52,2%", "do déficit é ônus excessivo com aluguel", "Fundação João Pinheiro"),
    ("5,9 mi", "nova estimativa do déficit (divulgada em 2025)", "FJP / Câmara dos Deputados"),
    ("1,9 mi+", "unidades do MCMV contratadas desde 2023", "Ministério das Cidades"),
    ("65%", "dos internautas acessam só pelo celular (2025)", "TIC Domicílios 2025")],
}
