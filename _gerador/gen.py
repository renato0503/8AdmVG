"""Gera os arquivos por grupo do 8AdmVG a partir de dados.py / pesquisa.py / extra.py e ../grupos.md.

Uso (da raiz 8AdmVG):  py _gerador/gen.py
Gera/atualiza, para cada grupo: README.md, formulario-app.md, Pesquisa-Dados.md, Slides-<Nome>.html,
index.html (landing), manifest.json, sw.js; e também assets/identidade/temas.css, assets/logos/gN.svg
e as perguntas do app de coleta (App/index.html, copiado para coleta/).
NÃO toca em ContextoApp.md nem app.html (escritos à mão).
"""
import html, json, re, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
sys.path.insert(0, str(AQUI))
from dados import GRUPOS, PERFIL, CURSO, INSTITUICAO, FUNCOES, TURMA  # noqa: E402
from pesquisa import P  # noqa: E402
from extra import EXTRA, KPIS  # noqa: E402

PROF_TITULO = {"Renato": "Prof. Renato", "Sandra": "Profa. Sandra", "Polyana": "Profa. Polyana", "Heitor": "Prof. Heitor"}


def ler_grupos_md():
    txt = (RAIZ / "grupos.md").read_text(encoding="utf-8")
    out = {}
    for linha in txt.splitlines():
        m = re.match(r"\|\s*\*\*Grupo (\d)\*\*\s*\|(.*)", linha)
        if not m:
            continue
        cols = [c.strip() for c in m.group(2).split("|")]
        n = int(m.group(1))
        resp, integrantes, ideia = cols[0], [c for c in cols[1:6] if c], cols[6]
        out[n] = dict(prof=PROF_TITULO.get(resp, resp), resp=resp, integrantes=integrantes, ideia_original=ideia)
    return out


def e(s):
    return html.escape(s, quote=True)


def md_inline_to_html(s):
    s = e(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s


def perguntas(g):
    return [q for _, _, qs in g["blocos"] for q in qs]


def papers(n):
    return {p["doi"].lower(): p for p in json.loads((RAIZ / "_pesquisa/selecionados" / f"G{n}.json").read_text(encoding="utf-8"))}


def cit_curta(p):
    nomes = [a.strip() for a in p["autores"].replace(" et al.", "").split(";") if a.strip()]
    sob = lambda nm: nm.split()[-1]
    if len(nomes) == 1:
        a = sob(nomes[0])
    elif len(nomes) == 2:
        a = f"{sob(nomes[0])} & {sob(nomes[1])}"
    else:
        a = f"{sob(nomes[0])} et al."
    return f"{a} ({p['ano']})"


# ------------------------------------------------------------------ formulario-app.md
def gen_formulario(n, g, info):
    L = [f"# Formulário do App — Grupo {n} · {g['nome']}", "",
         f"**Professor(a):** {info['prof']} · **Meta:** 15–20 respostas · **Código:** `G{n}-<nnn>` · **Total:** 20 perguntas", "",
         "> **Lógica de marcação (vale para todos os grupos)**",
         "> 1. **Bloco 0 — Perfil:** é a **exceção** — o entrevistador **marca por observação** (categórico, não é escala).",
         "> 2. **Todas as demais 20 perguntas são marcadas de 1 a 5**, sendo **1 uma dimensão e 5 a dimensão oposta**. O entrevistador pergunta **aberto** e marca onde a fala da pessoa cai.",
         "> 3. O formulário **não tem respostas abertas**. Falas, justificativas e reações são **anotadas no áudio** pelo aluno que grava (o formulário é o quanti; o áudio é o quali).",
         f"> 4. Cada resposta salva gera um **CÓDIGO** (`G{n}-<nnn>`), lido no começo do **áudio do WhatsApp**. **São 20 perguntas em todos os formulários.**",
         "", "---", "", "## Bloco 0 — Perfil (exceção: marcado por observação)", "", "| Campo | Opções |", "|---|---|"]
    for _, lab, ops in PERFIL:
        L.append(f"| {lab} | {' · '.join(ops)} |")
    tid, tlab, tops = g["triagem"]
    L += [f"| {tlab} | {' · '.join(tops)} |", "",
          "> A **triagem** é a única pergunta de perfil feita em voz alta (não é escala e não conta nas 20).", "",
          f"> **Nota de campo:** {g['nota_campo']}", "", "---", ""]
    q = 1
    for bi, (tit, base, qs) in enumerate(g["blocos"], 1):
        L += [f"## Bloco {bi} — {tit} (Q{q}–Q{q + len(qs) - 1})", "", f"*Base na pesquisa: {base}*", "",
              "| # | Perguntar (aberto) | 1 = | 5 = |", "|---|---|---|---|"]
        for pq, a, b in qs:
            L.append(f"| Q{q} | {pq} | {a} | {b} |")
            q += 1
        L += ["", "---", ""]
    L += ["## Regras de campo", "",
          "- **Não pergunte o perfil** — observe e marque; na dúvida, \"Não sei estimar\".",
          "- **Nunca pergunte renda, salário, raça ou dados que identifiquem a pessoa.**",
          "- Pergunte **aberto**; só depois marque a nota **1–5** (1 = dimensão A, 5 = dimensão B).",
          "- **Sem campo de texto no app.** As falas vão no **áudio** com o código.",
          "- O celular fica com o **entrevistador**.", "",
          "## Áudio do WhatsApp (modelo)", "",
          f"\"Código **G{n}-___**. Principais pontos: [2–3 ideias]. Frase marcante: '[...]'.\" — 20 a 40 segundos.", "",
          "## Checklist rápido", "", "- [ ] Bloco 0 (perfil) por observação + triagem",
          "- [ ] **20 perguntas** em escala 1–5 com polos rotulados", f"- [ ] código `G{n}-<nnn>` na tela",
          "- [ ] teste no celular", "- [ ] ensaio do áudio com código", ""]
    return "\n".join(L)


# ------------------------------------------------------------------ README.md
def gen_readme(n, g, info):
    L = [f"# Grupo {n} — {g['nome']}", "", f"**Professor(a) responsável:** {info['prof']}",
         "**Atividade:** Customer Discovery na prática — defesa da ideia + pesquisa de campo no shopping",
         f"**Turma:** {CURSO} · {INSTITUICAO}", "", "---", "", "## Integrantes", "", "| Integrante | Função no campo |", "|---|---|"]
    for i, nome in enumerate(info["integrantes"]):
        L.append(f"| {nome} | {FUNCOES[i % len(FUNCOES)]} |")
    L += ["", "> Funções sugeridas — o grupo pode trocar. Em campo, trabalhem em **duplas** (formulário + áudio).", "", "---", "",
          "## Ideia (como enviada pelo grupo)", "", f"> {info['ideia_original']}", "",
          "## Ideia proposta (organizada)", "", g["ideia_expandida"], "",
          f"**Foco temático:** {g['foco']}.", "", f"**Público:** {g['publico']}.", "", "---", "",
          "## Objetivo da pesquisa", "", g["objetivo"], "", "## Hipótese", "", g["hipotese"], "",
          "> A hipótese existe para ser testada — se os dados mostrarem o contrário, isso é um resultado, não um erro.", "", "---", "",
          "## Roteiro de campo", "", "| Item | Definição |", "|---|---|",
          f"| **Onde** | {g['onde']} |", f"| **Quem abordar** | {g['quem']} |", f"| **Como abordar** | {g['como']} |",
          "| **Meta de respostas** | **15–20** |", "", "### Pitch de 15 segundos", "",
          "1. \"Oi! Somos alunos de Administração da Unifacc.\"", "2. \"Estamos fazendo uma pesquisa rápida de 2 minutos. É anônima.\"",
          f"3. \"{g['pitch15']}\"", "4. \"Respondo no meu celular — não precisa instalar nada.\"", "",
          f"> {g['nota_campo']}", "", "---", "",
          "## Protocolo de coleta (todos os grupos)", "", "| Camada | Quem faz | O que registra |", "|---|---|---|",
          "| 1 · Perfil | Entrevistador (observação, **não pergunta**) | Faixa etária, sexo, classe social, raça + triagem |",
          "| 2 · Respostas | Entrevistador (marca no app) | Opção mais próxima, em escala 1–5 |",
          "| 3 · Áudio | Outro aluno | WhatsApp: **código** + ideias principais (20–40s) |", "",
          f"**Código:** `G{n}-<nº da resposta>` — ex.: `G{n}-014`. Igual na tela do formulário e no início do áudio.", "", "---", "",
          "## Checklist antes de sair", "", "- [ ] App de coleta aberto e **testado no celular** (`../coleta/`)",
          "- [ ] **20 perguntas** revisadas com o(a) professor(a)", "- [ ] Modelo de **áudio com código** combinado",
          "- [ ] Pitch ensaiado em voz alta (3x)", "- [ ] Tarefas divididas", "- [ ] Plano B impresso (formulário em papel)",
          "- [ ] Dois celulares carregados", "- [ ] Ponto de encontro combinado", "", "---", "", "## Materiais do grupo", "",
          "- `formulario-app.md` — as 20 perguntas (escala 1–5) + perfil + regras",
          "- `ContextoApp.md` — documento de produto (personas, jornada, MVP/v1/v2, KPIs, riscos, LGPD)",
          "- `Pesquisa-Dados.md` — dados oficiais + 14 artigos científicos reais (OpenAlex) com DOI",
          f"- `Slides-{g['nome']}.html` / `.pdf` — apresentação de defesa (12 slides)",
          "- `app.html` — MVP funcional (PWA, dados no próprio celular)", "", "## Materiais da turma", "",
          "- Parte 1 — preparação: `../Parte 1/Slides-Shopping.html` · `../Parte 1/caderno-shopping.html`",
          "- Parte 2 — formulários: `../Parte 2/Slides-Shopping-Parte2.html` · `../Parte 2/caderno-shopping-parte2.html`",
          "- Parte 3 — campo e sprints: `../Parte 3/Slides-Shopping-Parte3.html` · `../Parte 3/caderno-shopping-parte3.html`",
          "- App de coleta: `../coleta/index.html`", ""]
    return "\n".join(L)


# ------------------------------------------------------------------ Pesquisa-Dados.md
def gen_pesquisa(n, g, info):
    d, pp = P[n], papers(n)
    total = sum(len(ds) for _, ds in d["blocos"])
    L = [f"# Pesquisa e Dados — Grupo {n} · {g['nome']}", "",
         f"> Apoio à defesa da ideia: dados reais (Brasil/MT) + {total} artigos peer-reviewed (2021–2026). "
         "Os metadados dos artigos (autores, título, periódico, DOI, citações) foram copiados **automaticamente** dos resultados da API "
         "OpenAlex salvos em `_pesquisa/saidas/` — o script `_pesquisa/selecao.py` falha se algum DOI não existir nesses brutos. "
         "Números brasileiros têm fonte com link (conferidos em 23/09/2026). O que não foi confirmado está marcado `[verificar]`.", "",
         f"**Grupo:** {n} · {g['nome']} · **Professor(a):** {info['prof']} · **Integrantes:** {', '.join(info['integrantes'])} · "
         f"**Código:** G{n}-<nnn> · **Meta:** 15–20", "", f"**Hipótese de campo:** {g['hipotese']}", "", "---", "",
         "## 1. Resumo executivo", "", d["resumo"], "", "---", "", "## 2. Dados e notícias reais", "", "### 2.1 Tabela de dados", "",
         "| Dado | Número | Ano | Fonte |", "|---|---|---|---|"]
    for dado, num, ano, fonte, url in d["dados"]:
        dom = re.sub(r"^https?://(www\.)?", "", url).split("/")[0]
        L.append(f"| {dado} | {num} | {ano} | {fonte} ([{dom}]({url})) |")
    L += ["", "### 2.2 Leitura dos dados", ""] + [f"{i}. {t}" for i, t in enumerate(d["leitura"], 1)]
    L += ["", "---", "", f"## 3. Referencial científico ({total} artigos, 2021–2026)", ""]
    k = 1
    quadro = []
    for tb, dois in d["blocos"]:
        L += [f"### {tb}", ""]
        for doi in dois:
            p = pp[doi.lower()]
            sus, usar = d["notas"][doi]
            acesso = "aberto" if p["acesso_aberto"] else "fechado"
            L += [f"**{k}. {p['autores']} ({p['ano']}).** {p['titulo']}. *{p['periodico'] or 'n/d'}*. "
                  f"DOI: [{p['doi']}](https://doi.org/{p['doi']}). Citações (OpenAlex): {p['citacoes']}. Acesso: {acesso}.",
                  f"- **O que sustenta:** {sus}", f"- **Como usar na defesa:** {usar}", ""]
            quadro.append((k, cit_curta(p), tb.split(".")[0], p["doi"]))
            k += 1
    L += ["### Quadro-resumo", "", "| # | Referência | Bloco | DOI |", "|---|---|---|---|"]
    L += [f"| {a} | {b} | {c} | {dd} |" for a, b, c, dd in quadro]
    L += ["", "---", "", "## 4. Argumentos prontos para a defesa", ""] + [f"{i}. {t}" for i, t in enumerate(d["argumentos"], 1)]
    L += ["", "---", "", "## 5. Lacunas, limites e cuidados", ""] + [f"- {t}" for t in d["lacunas"]]
    L += ["", "---", "", "## 6. Fontes e proveniência", "",
          "- **Artigos:** OpenAlex (api.openalex.org), buscas registradas em `_pesquisa/saidas/G" + str(n) + "_*.json|.md` "
          "(script `_pesquisa/openalex_busca.py`, rodado em 23/09/2026). Seleção final em `_pesquisa/selecionados/G" + str(n) + ".json`.",
          "- **Contagem de citações:** valor do OpenAlex no dia da busca (muda com o tempo).",
          "- **Dados brasileiros:** links na tabela 2.1; notícias oficiais (gov.br, Embratur, IBGE, INEP, FJP) têm prioridade sobre imprensa.",
          "- **Regra do projeto:** nenhuma referência pode ser inventada. Se precisar de outro artigo, rode uma nova busca e acrescente o DOI em `_pesquisa/selecao.py`.", ""]
    return "\n".join(L)


# ------------------------------------------------------------------ Slides
def paper_card(k, p, sus):
    frase = sus.split(". ")[0].rstrip(".") + "."
    if len(frase) > 230:
        frase = frase[:227].rsplit(" ", 1)[0] + "…"
    cit = f"{p['citacoes']} citaç{'ão' if p['citacoes'] == 1 else 'ões'}"
    return (f'    <div class="paper-card">\n        <b>{k}. {e(cit_curta(p).replace(" (", " ("))}.</b> {e(p["titulo"])}. <i>{e(p["periodico"])}</i>.\n'
            f'        <span class="doi">DOI: {e(p["doi"])}</span> · <span class="cite">{cit}</span>\n'
            f'        <div class="abs">{e(frase)}</div>\n    </div>')


def gen_slides(n, g, info):
    x, d, pp = EXTRA[n], P[n], papers(n)
    dois = [doi for _, ds in d["blocos"] for doi in ds]
    sel = dois[:12]
    badges = "\n".join(f'        <span class="badge">{e(m)}</span>' for m in info["integrantes"])
    kpis = "\n".join(
        f'        <div class="kpi"><b>{e(big)}</b><span>{e(lab)}</span>\n'
        f'            <div class="source">{e(fonte)}</div></div>' for big, lab, fonte in KPIS[n])
    ref_slides = []
    for i in range(3):
        grupo = sel[i * 4:(i + 1) * 4]
        cards = "\n".join(paper_card(i * 4 + j + 1, pp[doi.lower()], d["notas"][doi][0]) for j, doi in enumerate(grupo))
        ref_slides.append(f"""<!-- {7 + i} · REFERENCIAL {'I' * (i + 1)} -->
<section>
    <h1>Referencial científico {['I', 'II', 'III'][i]}</h1>
    <p style="font-size: 14px; color: #718096; margin-bottom: 6px;">Artigos peer-reviewed (2021–2026) · metadados OpenAlex · {len(dois)} no total em Pesquisa-Dados.md</p>
{cards}
</section>""")
    leit = "\n".join(f"            <li>{md_inline_to_html(t)}</li>" for t in d["leitura"][:6])
    args = "\n".join(f"            <li>{md_inline_to_html(t.strip(chr(34)))}</li>" for t in d["argumentos"][:7])
    lac = "\n".join(f"                    <li>{md_inline_to_html(t)}</li>" for t in d["lacunas"][:4])
    probl = "\n".join(f"            <li>{t}</li>" for t in x["problema"])
    cards = "\n".join(f'        <div class="card">\n            <h3>{e(a)}</h3>\n            <p>{e(b)}</p>\n        </div>' for a, b in x["cards"])
    blocos_li = "\n".join(f"            <li><strong>Bloco {i}:</strong> {e(t)}.</li>" for i, (t, _, _) in enumerate(g["blocos"], 1))
    nome = g["nome"]
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Defesa da Ideia — {e(nome)} | Customer Discovery · {TURMA}</title>
<link rel="stylesheet" href="../assets/identidade/temas.css">
<link rel="stylesheet" href="../assets/reveal/reset.css">
<link rel="stylesheet" href="../assets/reveal/reveal.css">
<link rel="stylesheet" href="../assets/reveal/grupo-slides.css">
</head>
<body class="tema-g{n}">
<div class="reveal">
<div class="slides">

<!-- 1 · CAPA -->
<section class="cover">
    <img src="../assets/logos/g{n}.svg" alt="" style="width: 76px; height: 76px; margin: 0 auto 10px;">
    <span class="group-chip">GRUPO {n}</span>
    <h1 style="font-size: 42px;">{e(nome)}</h1>
    <h2 style="font-size: 22px; margin-bottom: 18px;">{e(g['tagline'])}</h2>
    <div>
{badges}
    </div>
    <div style="font-size: 15px; color: #666; margin-top: 12px;">
        {e(info['prof'])} · Customer Discovery — Defesa de Projetos Inovadores<br>
        Setembro de 2026 · {e(CURSO)}
    </div>
    <div style="display: flex; align-items: center; justify-content: center; gap: 18px; margin-top: 22px;">
        <img src="../Parte 1/Renato.jpg" alt="Prof. Renato Rosa" style="width: 64px; height: 64px; border-radius: 50%; object-fit: cover; border: 3px solid var(--accent);">
        <div style="text-align: left;">
            <div style="font-size: 17px; color: #2D3748;">Prof. Renato Rosa</div>
            <div style="font-size: 14px; color: #666;">Cerrado Tech · Unifacc</div>
        </div>
    </div>
</section>

<!-- 2 · O PROBLEMA -->
<section>
    <h1>O problema (a dor)</h1>
    <div class="content">
        <ul style="font-size: 19px;">
{probl}
        </ul>
    </div>
    <div class="highlight-box" style="font-size: 16px;">
        {x['destaque'][0]}
        <div class="source">Fonte: {e(x['destaque'][1])}</div>
    </div>
</section>

<!-- 3 · A IDEIA -->
<section>
    <h1>A ideia</h1>
    <p style="font-size: 17px; color: #4A5568; margin-bottom: 10px;">{x.get('ideia_slide') or md_inline_to_html(g['ideia_expandida'].split('. ')[0] + '.')}</p>
    <div class="three-col">
{cards}
    </div>
    <div class="success-box" style="font-size: 16px;">
        <strong>Diferencial:</strong> {x['diferencial']}
    </div>
</section>

<!-- 4 · HIPÓTESE -->
<section>
    <h1>Hipótese</h1>
    <div class="quote" style="font-size: 19px;">
        {md_inline_to_html(g['hipotese'])}
    </div>
    <h3 style="margin-top: 12px;">O formulário de campo (20 perguntas, escala 1–5)</h3>
    <div class="content">
        <ul style="font-size: 18px;">
{blocos_li}
        </ul>
    </div>
    <div class="highlight-box" style="font-size: 15px;">
        A hipótese existe para ser testada: se os dados mostrarem o contrário, <strong>isso é um resultado, não um erro</strong>.
    </div>
</section>

<!-- 5 · DADOS -->
<section>
    <h1>Dados reais</h1>
    <div class="kpi-grid">
{kpis}
    </div>
</section>

<!-- 6 · LEITURA DOS DADOS -->
<section>
    <h1>Leitura dos dados</h1>
    <div class="content">
        <ul style="font-size: 17.5px;">
{leit}
        </ul>
    </div>
</section>

{chr(10).join(ref_slides)}

<!-- 10 · COMO A PESQUISA EMBASA A IDEIA -->
<section>
    <h1>Como a pesquisa embasa a ideia</h1>
    <div class="content">
        <ul style="font-size: 17px;">
{args}
        </ul>
    </div>
</section>

<!-- 11 · LACUNAS E CUIDADOS -->
<section>
    <h1>Lacunas e cuidados</h1>
    <div class="two-col">
        <div>
            <div class="warning-box" style="font-size: 15px;">
                <strong>Lacunas da pesquisa</strong>
                <ul style="font-size: 14px; margin-top: 6px; padding-left: 16px;">
{lac}
                </ul>
            </div>
        </div>
        <div>
            <div class="highlight-box" style="font-size: 15px;">
                <strong>Cuidados de campo e LGPD</strong>
                <ul style="font-size: 14px; margin-top: 6px; padding-left: 16px;">
                    <li>Amostra de <strong>15–20 respostas</strong>: exploratória, não representativa.</li>
                    <li>Perfil marcado por <strong>observação</strong>; na dúvida, "Não sei estimar".</li>
                    <li><strong>Nunca</strong> perguntar renda, raça ou dados que identifiquem a pessoa.</li>
                    <li>Falas vão para o <strong>áudio com o código G{n}-&lt;nnn&gt;</strong>, não para o formulário.</li>
                    <li>No MVP, os dados ficam <strong>só no celular</strong> do usuário (localStorage).</li>
                </ul>
            </div>
        </div>
    </div>
</section>

<!-- 12 · PITCH -->
<section class="cover">
    <h1 style="font-size: 32px;">Pitch de 30 segundos</h1>
    <div class="quote" style="font-size: 19px; max-width: 900px; text-align: left; font-style: normal;">
        "{e(x['pitch30'])}"
    </div>
    <div style="margin-top: 22px;">
        <span class="badge green">Grupo {n}</span>
{badges}
    </div>
    <h2 style="font-size: 22px; margin-top: 22px;">Obrigado!</h2>
    <div class="subtitle" style="border-top: none;">Customer Discovery na Prática · {e(nome)} · {e(info['prof'])} · Cerrado Tech · Unifacc · 2026</div>
</section>

</div>
</div>
<script src="../assets/reveal/reveal.js"></script>
<script>
Reveal.initialize({{ width:1280, height:720, margin:0.03, controls:true, progress:true, history:true, slideNumber:'c/t', hash:true, center:true, transition:'slide' }});
</script>
</body>
</html>
"""


# ------------------------------------------------------------------ Landing
ICON = {
    "readme": '<path d="M4 19.5A2.5 2.5 0 016.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15A2.5 2.5 0 016.5 2z"/>',
    "form": '<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/>',
    "ctx": '<path d="M12 2l2.4 6.6L21 11l-6.6 2.4L12 20l-2.4-6.6L3 11l6.6-2.4z"/>',
    "pesq": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>',
    "slides": '<rect x="2" y="4" width="20" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>',
    "coleta": '<rect x="6" y="2" width="12" height="20" rx="2"/><path d="M11 18h2"/>',
}


def gen_landing(n, g, info):
    t, x, nome, pasta = g["tema"], EXTRA[n], g["nome"], g["pasta"]
    total = sum(len(ds) for _, ds in P[n]["blocos"])
    cards = [
        ("readme", f"../assets/md-viewer.html?src=../{pasta}/README.md&voltar=../{pasta}/", "README do grupo", "Integrantes, hipótese, roteiro de campo e pitch"),
        ("form", f"../assets/md-viewer.html?src=../{pasta}/formulario-app.md&voltar=../{pasta}/", "Formulário de campo", f"20 perguntas em escala 1–5, código G{n}-&lt;nnn&gt;"),
        ("ctx", f"../assets/md-viewer.html?src=../{pasta}/ContextoApp.md&voltar=../{pasta}/", "Contexto do produto", "Personas, jornada, MVP/v1/v2, KPIs, riscos e LGPD"),
        ("pesq", f"../assets/md-viewer.html?src=../{pasta}/Pesquisa-Dados.md&voltar=../{pasta}/", "Pesquisa e dados", f"Dados oficiais + {total} artigos científicos com DOI"),
        ("slides", f"Slides-{nome}.pdf", "Slides de defesa (PDF)", "Versão para download e impressão"),
        ("coleta", "../coleta/", "App de coleta (campo)", "Formulário offline usado no shopping"),
    ]
    cards_html = "\n".join(
        f'        <a href="{h}" class="doc-card">\n          <div class="doc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{ICON[i]}</svg></div>\n'
        f'          <b>{tit}</b>\n          <small>{sub}</small>\n        </a>' for i, h, tit, sub in cards)
    team = "\n".join(f"        <span>{e(m)}</span>" for m in info["integrantes"])
    feats = "\n".join(f'        <div class="feat"><b>{e(a)}</b><p>{e(b)}</p></div>' for a, b in x["cards"])
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(nome)} — Grupo {n} · Customer Discovery {TURMA}</title>
<meta name="description" content="{e(g['tagline'])}">
<meta name="theme-color" content="{t['tinta']}">
<link rel="icon" type="image/svg+xml" href="../assets/logos/g{n}.svg">
<link rel="apple-touch-icon" href="../assets/logos/g{n}-192.png">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/landing.css">
<style>:root{{--acc:{t['accent']};--acc2:{t['accent2']};--tinta:{t['tinta']}}}</style>
</head>
<body>

<nav class="nav">
  <div class="wrap">
    <a href="../index.html" class="nav-back">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M19 12H5M11 18l-6-6 6-6"/></svg>
      Todos os projetos
    </a>
    <span class="nav-title">Grupo {n} · {e(nome)}</span>
  </div>
</nav>

<header class="hero">
  <div class="wrap">
    <div class="hero-top">
      <img class="hero-logo" src="../assets/logos/g{n}.svg" alt="Logo {e(nome)}">
      <div>
        <div class="hero-group">Grupo {n} · Customer Discovery</div>
        <h1>{e(nome)}</h1>
      </div>
    </div>
    <p class="pitch">{e(g['tagline'])}. {md_inline_to_html(g['ideia_expandida'].split('. ')[0].replace('**' + nome + '**', nome) + '.')}</p>
    <div class="hero-meta">
      <div><b>Professor(a)</b>{e(info['prof'])}</div>
      <div><b>Integrantes</b>{e(', '.join(info['integrantes']))}</div>
      <div><b>Código de campo</b>G{n}-&lt;nnn&gt;</div>
    </div>
    <div class="cta-row">
      <a href="app.html" class="btn-cta">
        Abrir o app
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </a>
      <a href="Slides-{nome}.html" class="btn-secondary">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{ICON['slides']}</svg>
        Ver slides de defesa
      </a>
    </div>
  </div>
</header>

<main>
  <section class="block">
    <div class="wrap">
      <div class="block-head">
        <h2>O que o app faz</h2>
        <p>{e(x['diferencial'].replace('<strong>', '').replace('</strong>', ''))}</p>
      </div>
      <div class="feat-grid">
{feats}
      </div>
    </div>
  </section>
  <section class="block">
    <div class="wrap">
      <div class="block-head">
        <h2>Materiais do grupo</h2>
        <p>Toda a documentação produzida para a defesa e para a pesquisa de campo.</p>
      </div>
      <div class="doc-grid">
{cards_html}
      </div>
      <div class="team">
{team}
      </div>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">
    <a href="../index.html">← Voltar ao hub Customer Discovery</a>
    <p>Grupo {n} · {e(nome)} · Cerrado Tech · Unifacc · {e(CURSO)}, 2026</p>
  </div>
</footer>

</body>
</html>
"""


LANDING_CSS = """:root{
  --acc:#4338ca; --acc2:#f59e0b; --tinta:#1e1b4b;
  --surface:#fff; --surface-2:#f4f6fb; --ink:#0f172a; --ink-soft:#5b6478; --line:#e7e9f2;
  --radius-md:16px; --shadow-card:0 10px 30px -12px rgba(15,23,42,.18);
}
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
body{font-family:'Inter',system-ui,-apple-system,sans-serif;background:var(--surface-2);color:var(--ink);min-height:100dvh}
h1,h2{font-family:'Space Grotesk',system-ui,sans-serif}
a{color:inherit}
img{display:block;max-width:100%}
.wrap{max-width:920px;margin:0 auto;padding:0 16px}
.nav{position:sticky;top:0;z-index:50;background:rgba(11,18,32,.92);backdrop-filter:blur(10px)}
.nav .wrap{display:flex;align-items:center;gap:12px;padding:12px 16px;color:#fff}
.nav-back{display:flex;align-items:center;gap:6px;font-size:13px;font-weight:600;color:#c7cee8;text-decoration:none;flex-shrink:0}
.nav-back svg{width:16px;height:16px}
.nav-back:hover{color:#fff}
.nav-title{margin-left:auto;font-size:13px;font-weight:700;opacity:.85;text-align:right}
.hero{position:relative;color:#fff;padding:48px 0 64px;overflow:hidden;background:linear-gradient(160deg,var(--tinta) 0%,#0b1220 100%)}
.hero::before{content:"";position:absolute;inset:0;background:radial-gradient(600px 320px at 85% 0%, color-mix(in srgb, var(--acc) 40%, transparent), transparent 60%)}
.hero .wrap{position:relative;z-index:2}
.hero-top{display:flex;align-items:center;gap:16px;margin-bottom:22px}
.hero-logo{width:64px;height:64px;border-radius:16px;box-shadow:0 8px 22px rgba(0,0,0,.35);flex-shrink:0}
.hero-group{font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--acc2)}
.hero h1{font-size:clamp(26px,4.2vw,36px);font-weight:700;letter-spacing:-.01em;margin-top:2px}
.hero p.pitch{margin-top:14px;font-size:15px;line-height:1.6;color:#c7cee8;max-width:640px}
.hero p.pitch strong{color:#fff}
.hero-meta{display:flex;gap:22px;margin-top:26px;flex-wrap:wrap;font-size:12.5px;color:#9aa5c3}
.hero-meta b{color:#fff;display:block;font-size:13px;margin-bottom:2px}
.cta-row{display:flex;gap:12px;margin-top:28px;flex-wrap:wrap}
.btn-cta{display:inline-flex;align-items:center;gap:8px;background:var(--acc2);color:#0b1220;font-weight:700;font-size:14.5px;padding:13px 22px;border-radius:100px;text-decoration:none;box-shadow:0 10px 24px -8px rgba(0,0,0,.4);transition:transform .15s}
.btn-cta:hover{transform:translateY(-2px)}
.btn-cta svg{width:16px;height:16px}
.btn-secondary{display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.2);color:#fff;font-weight:600;font-size:13.5px;padding:12px 18px;border-radius:100px;text-decoration:none}
.btn-secondary:hover{background:rgba(255,255,255,.14)}
.btn-secondary svg{width:14px;height:14px}
section.block{padding:40px 0 8px}
.block-head{margin-bottom:20px}
.block-head h2{font-size:19px;font-weight:700;color:var(--ink)}
.block-head p{font-size:13.5px;color:var(--ink-soft);margin-top:4px}
.feat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}
.feat{background:var(--surface);border:1px solid var(--line);border-top:4px solid var(--acc);border-radius:var(--radius-md);padding:18px}
.feat b{font-size:15px}
.feat p{font-size:13px;color:var(--ink-soft);margin-top:6px;line-height:1.5}
.doc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px}
.doc-card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-md);padding:18px;text-decoration:none;color:inherit;display:flex;flex-direction:column;gap:10px;box-shadow:0 1px 3px rgba(15,23,42,.05);transition:transform .15s,box-shadow .15s,border-color .15s}
.doc-card:hover{transform:translateY(-3px);box-shadow:var(--shadow-card);border-color:var(--acc)}
.doc-icon{width:38px;height:38px;border-radius:10px;display:flex;align-items:center;justify-content:center;background:color-mix(in srgb, var(--acc) 14%, white);color:var(--acc)}
.doc-icon svg{width:19px;height:19px}
.doc-card b{font-size:14px;font-weight:700}
.doc-card small{font-size:12px;color:var(--ink-soft);line-height:1.4}
.team{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0 36px}
.team span{background:var(--surface);border:1px solid var(--line);padding:6px 12px;border-radius:100px;font-size:12.5px;font-weight:600}
footer{background:var(--tinta);color:#cbd5f5;padding:32px 0;margin-top:20px}
footer .wrap{display:flex;flex-direction:column;gap:6px;align-items:center;text-align:center}
footer a{color:#fff;text-decoration:none;font-weight:600}
footer p{font-size:12px;opacity:.85}
"""


# ------------------------------------------------------------------ logos, temas, manifest, sw, coleta
GLIFO = {
    1: '<circle cx="256" cy="268" r="118" fill="none" stroke="#fff" stroke-width="30"/><path d="M256 190v82l52 34" fill="none" stroke="#fff" stroke-width="30" stroke-linecap="round"/><circle cx="366" cy="158" r="56" fill="ACC2"/><path d="M340 158l18 18 34-36" fill="none" stroke="TINTA" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>',
    2: '<path d="M256 392s-104-104-104-180a104 104 0 01208 0c0 76-104 180-104 180z" fill="#fff"/><circle cx="256" cy="212" r="40" fill="ACC2"/><path d="M112 420c60-36 110 10 160-20s96-30 128-6" fill="none" stroke="ACC2" stroke-width="20" stroke-linecap="round" stroke-dasharray="4 30"/>',
    3: '<path d="M150 214h54l70-58v200l-70-58h-54z" fill="#fff"/><path d="M318 200a80 80 0 010 112M350 164a130 130 0 010 184" fill="none" stroke="ACC2" stroke-width="26" stroke-linecap="round"/><rect x="124" y="398" width="264" height="18" rx="9" fill="ACC2"/>',
    4: '<path d="M128 262L256 150l128 112" fill="none" stroke="#fff" stroke-width="30" stroke-linejoin="round" stroke-linecap="round"/><path d="M160 244v142h192V244" fill="none" stroke="#fff" stroke-width="30" stroke-linejoin="round"/><path d="M160 410h192" stroke="ACC2" stroke-width="16" stroke-linecap="round" stroke-dasharray="2 22"/><rect x="226" y="306" width="60" height="80" rx="6" fill="ACC2"/>',
    5: '<path d="M128 256L256 146l128 110" fill="none" stroke="#fff" stroke-width="30" stroke-linejoin="round" stroke-linecap="round"/><path d="M160 238v150h192V238" fill="none" stroke="#fff" stroke-width="30" stroke-linejoin="round"/><path d="M256 360s-58-36-58-74a30 30 0 0158-12 30 30 0 0158 12c0 38-58 74-58 74z" fill="ACC2"/>',
}


def gen_logo(n, t):
    gl = GLIFO[n].replace("ACC2", t["accent2"]).replace("TINTA", t["tinta"])
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="{t["accent"]}"/><stop offset="1" stop-color="{t["tinta"]}"/></linearGradient></defs>'
            f'<rect width="512" height="512" rx="112" fill="url(#g)"/>{gl}</svg>\n')


def gen_temas():
    fontes = "&family=".join(g["tema"]["gfont"] for g in GRUPOS.values())
    L = ["/* ==========================================================================",
         f"   temas.css — Identidade visual por grupo (Customer Discovery · {TURMA})",
         "   GERADO por _gerador/gen.py a partir de _gerador/dados.py — edite lá.",
         "   Uso: <link .../temas.css> + <body class=\"tema-gN\">", "   ========================================================================== */", "",
         f"@import url('https://fonts.googleapis.com/css2?family={fontes}&display=swap');", "",
         ":root{", "  --accent:#0f766e; --accent-dark:#115e59; --accent-soft:#f0fdfa; --accent-rgb:15,118,110;",
         "  --accent2:#f59e0b; --tinta:#0b1220; --tinta2:#1e293b;",
         "  --texto:#2d3748; --texto-suave:#4a5568; --linha:#e2e8f0; --fundo:#f7fafc;",
         '  --fonte:"Segoe UI", system-ui, -apple-system, Roboto, Arial, sans-serif;',
         '  --fonte-titulo:"Segoe UI", system-ui, -apple-system, Roboto, Arial, sans-serif;', "  --raio:14px;", "}", ""]
    for n, g in GRUPOS.items():
        t = g["tema"]
        L += [f"/* ---------------------------------------------------------------- G{n} · {g['nome']}",
              f"   Tom: {t['tom']}. */",
              f"body.tema-g{n}, .tema-g{n}{{",
              f"  --accent:{t['accent']}; --accent-dark:{t['dark']}; --accent-soft:{t['soft']}; --accent-rgb:{t['rgb']};",
              f"  --accent2:{t['accent2']}; --tinta:{t['tinta']}; --tinta2:{t['tinta2']}; --fundo:{t['fundo']};",
              f"  --fonte:{t['fonte']};", f"  --fonte-titulo:{t['fonte_titulo']};", "}", ""]
    L += ["/* Faixa de identidade no topo de cada slide dos decks de grupo */",
          '.reveal .slides section::before{content:"";position:absolute;top:0;left:0;right:0;height:6px;',
          "  background:linear-gradient(90deg,var(--accent) 0%,var(--accent2) 100%);}", ""]
    return "\n".join(L)


def gen_manifest(n, g):
    t = g["tema"]
    return json.dumps({
        "name": g["nome"], "short_name": g["nome"], "description": g["tagline"], "start_url": "app.html",
        "display": "standalone", "background_color": t["fundo"], "theme_color": t["accent"], "orientation": "portrait",
        "icons": [{"src": f"../assets/logos/g{n}-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": f"../assets/logos/g{n}-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}],
    }, ensure_ascii=False, indent=2) + "\n"


def gen_sw(n, g):
    return f"""const CACHE = '{g['slug']}-v1';
const PRE = ['./', './index.html', './app.html', '../assets/mvp/mvp.css', '../assets/mvp/mvp.js', '../assets/logos/g{n}.svg'];

self.addEventListener('install', e => {{
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(PRE)).then(() => self.skipWaiting()));
}});

self.addEventListener('activate', e => {{
  e.waitUntil(caches.keys().then(k => Promise.all(k.filter(v => v !== CACHE).map(v => caches.delete(v)))).then(() => self.clients.claim()));
}});

self.addEventListener('fetch', e => {{
  if (e.request.method !== 'GET') return;
  // rede primeiro (conteúdo sempre atualizado); sem internet, usa o cache
  e.respondWith(fetch(e.request).then(res => {{
    if (res && res.ok && new URL(e.request.url).origin === location.origin) {{
      const copia = res.clone();
      caches.open(CACHE).then(c => c.put(e.request, copia));
    }}
    return res;
  }}).catch(() => caches.match(e.request).then(r => r || caches.match('./app.html'))));
}});
"""


def injetar_coleta(infos):
    """Insere o objeto GRUPOS no app de coleta (arquivo único, offline) e copia App/ -> coleta/."""
    grupos = {}
    for n, g in GRUPOS.items():
        tid, tlab, tops = g["triagem"]
        grupos[n] = {
            "nome": g["nome"], "prof": infos[n]["prof"],
            "nota": md_inline_to_html(g["nota_campo"]),
            "triagem": {"id": tid, "label": tlab.replace(" (triagem)", ""), "opcoes": tops},
            "blocos": [{"titulo": t, "perguntas": [{"q": q, "a": a, "b": b} for q, a, b in qs]} for t, _, qs in g["blocos"]],
        }
    app = RAIZ / "App/index.html"
    s = app.read_text(encoding="utf-8")
    ini, fim = "/* GRUPOS:INICIO", "/* GRUPOS:FIM */"
    i, j = s.index(ini), s.index(fim) + len(fim)
    bloco = ("/* GRUPOS:INICIO — gerado por _gerador/gen.py (não edite à mão) */\n"
             "const GRUPOS = " + json.dumps(grupos, ensure_ascii=False, indent=1) + ";\n" + fim)
    s = s[:i] + bloco + s[j:]
    app.write_text(s, encoding="utf-8")
    (RAIZ / "coleta").mkdir(exist_ok=True)
    (RAIZ / "coleta/index.html").write_text(s, encoding="utf-8")
    (RAIZ / "coleta/README.md").write_text((RAIZ / "App/README.md").read_text(encoding="utf-8"), encoding="utf-8")


def main():
    infos = ler_grupos_md()
    (RAIZ / "assets/identidade").mkdir(parents=True, exist_ok=True)
    (RAIZ / "assets/logos").mkdir(parents=True, exist_ok=True)
    (RAIZ / "assets/identidade/temas.css").write_text(gen_temas(), encoding="utf-8")
    (RAIZ / "assets/landing.css").write_text(LANDING_CSS, encoding="utf-8")
    injetar_coleta(infos)
    for n, g in GRUPOS.items():
        info = infos[n]
        assert len(perguntas(g)) == 20, f"G{n} não tem 20 perguntas"
        pasta = RAIZ / g["pasta"]
        pasta.mkdir(exist_ok=True)
        (RAIZ / f"assets/logos/g{n}.svg").write_text(gen_logo(n, g["tema"]), encoding="utf-8")
        arquivos = {
            "formulario-app.md": gen_formulario(n, g, info),
            "README.md": gen_readme(n, g, info),
            "Pesquisa-Dados.md": gen_pesquisa(n, g, info),
            f"Slides-{g['nome']}.html": gen_slides(n, g, info),
            "index.html": gen_landing(n, g, info),
            "manifest.json": gen_manifest(n, g),
            "sw.js": gen_sw(n, g),
        }
        for nome, conteudo in arquivos.items():
            (pasta / nome).write_text(conteudo, encoding="utf-8")
        print(f"G{n} {g['nome']}: {len(info['integrantes'])} integrantes, {len(arquivos)} arquivos")
    from hub import gen_hub
    total = sum(len(ds) for n in GRUPOS for _, ds in P[n]["blocos"])
    html_, manifest, sw = gen_hub(infos, total)
    (RAIZ / "index.html").write_text(html_, encoding="utf-8")
    (RAIZ / "manifest.json").write_text(manifest, encoding="utf-8")
    (RAIZ / "sw.js").write_text(sw, encoding="utf-8")
    print(f"Hub: {total} artigos")
    (RAIZ / "_pesquisa/INDICE-PESQUISA.md").write_text(gen_indice(infos), encoding="utf-8")


def gen_indice(infos):
    L = ["# Índice de Pesquisa — Customer Discovery · 8AdmVG", "",
         "> Gerado por `_gerador/gen.py`. Todos os artigos abaixo existem nos resultados brutos da API OpenAlex salvos em "
         "`_pesquisa/saidas/` e foram selecionados por `_pesquisa/selecao.py`, que **falha** se algum DOI não estiver nos brutos. "
         "Nenhuma referência foi digitada à mão.", "",
         "## Visão geral", "", "| Grupo | Projeto | Professor(a) | Artigos | Buscas brutas |", "|---|---|---|---|---|"]
    for n, g in GRUPOS.items():
        buscas = sorted(f.stem for f in (RAIZ / "_pesquisa/saidas").glob(f"G{n}_*.json"))
        total = sum(len(ds) for _, ds in P[n]["blocos"])
        L.append(f"| G{n} | {g['nome']} | {infos[n]['prof']} | {total} | {', '.join('`' + b + '`' for b in buscas)} |")
    for n, g in GRUPOS.items():
        pp = papers(n)
        L += ["", f"## G{n} · {g['nome']}", "", "| # | Referência | Título | Periódico | DOI | Citações |", "|---|---|---|---|---|---|"]
        k = 1
        for _, dois in P[n]["blocos"]:
            for doi in dois:
                p = pp[doi.lower()]
                L.append(f"| {k} | {cit_curta(p)} | {p['titulo'].replace('|', '/')} | {p['periodico'] or 'n/d'} | [{p['doi']}](https://doi.org/{p['doi']}) | {p['citacoes']} |")
                k += 1
    L += ["", "## Como acrescentar um artigo", "",
          "1. Rode uma busca: `py _pesquisa/openalex_busca.py --tema \"termo em inglês\" --limit 25 --json _pesquisa/saidas/G<n>_<tema>.json --md _pesquisa/saidas/G<n>_<tema>.md`",
          "2. Copie o DOI escolhido para a lista do grupo em `_pesquisa/selecao.py` e rode `py _pesquisa/selecao.py`.",
          "3. Escreva a leitura do artigo em `_gerador/pesquisa.py` (notas e bloco) e rode `py _gerador/gen.py`.", ""]
    return "\n".join(L)


if __name__ == "__main__":
    main()
