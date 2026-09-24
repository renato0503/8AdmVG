"""Gera Parte 1, 2 e 3 (slides + cadernos) do 8AdmVG a partir dos modelos do 3SemVG.

Os modelos ficam em ../../3SemVG/Parte N/. Este script troca o cabeçalho da turma e todos os
trechos específicos dos 6 grupos do 3SemVG pelos 5 grupos do 8AdmVG (dados.py + grupos.md).
Uso (da raiz 8AdmVG):  py _gerador/gen_partes.py
"""
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
MODELO = RAIZ.parent / "3SemVG"
sys.path.insert(0, str(AQUI))
from dados import GRUPOS  # noqa: E402
from gen import ler_grupos_md, md_inline_to_html, e, FUNCOES  # noqa: E402

INFO = ler_grupos_md()
TEMA = "Inovação em Serviços — Educação, Turismo, Acessibilidade e Moradia"
TURMA_TXT = "Turma de Administração · 8º Semestre (VG)"
DATA = "Setembro de 2026"


def ler(rel):
    return (MODELO / rel).read_text(encoding="utf-8")


def gravar(rel, s):
    (RAIZ / rel).parent.mkdir(parents=True, exist_ok=True)
    (RAIZ / rel).write_text(s, encoding="utf-8")


def troca(s, velho, novo, obrig=True):
    if velho not in s:
        if obrig:
            raise ValueError(f"não achei: {velho[:80]}")
        return s
    return s.replace(velho, novo)


def entre(s, ini, fim, novo):
    i = s.index(ini)
    j = s.index(fim, i)
    return s[:i] + novo + s[j:]


def comuns(s):
    s = s.replace("3SemVG", "8AdmVG")
    s = s.replace("Saúde Financeira, Dívidas e Orçamento Familiar", TEMA)
    s = s.replace("Turma de Tecnologia e Inovação · 3º Semestre (VG)", TURMA_TXT)
    s = s.replace("3º Semestre (VG)", "8º Semestre (VG) · Administração")
    s = s.replace("21 de Setembro de 2026", DATA)
    s = s.replace("de Tecnologia e Inovação.", "de Administração.")
    s = s.replace("Tema: Saúde Financeira", "5 ideias de inovação")
    s = s.replace("<b>Grupos</b> 6 ·", "<b>Grupos</b> 5 ·")
    s = s.replace("<strong>+100 respostas somadas</strong> entre os 6 grupos", "<strong>+75 respostas somadas</strong> entre os 5 grupos")
    s = s.replace("para os 6 grupos", "para os 5 grupos")
    return s


def funcoes(n):
    return [(m, FUNCOES[i % len(FUNCOES)]) for i, m in enumerate(INFO[n]["integrantes"])]


def essenciais(g):
    return ", ".join((t[0][0].lower() + t[0][1:]) if i else t[0] for i, t in enumerate(g["blocos"])) + "."


SENSIVEL = {
    3: "<strong>Acessibilidade:</strong> se o(a) entrevistado(a) tiver deficiência visual, apresente-se, <strong>leia as opções em voz alta</strong> e nunca conduza a pessoa sem perguntar.",
    5: "<strong>Tema sensível:</strong> renda e moradia. Nunca pergunte renda nem se a pessoa recebe benefício; se ela contar uma situação difícil, acolha e não insista.",
}


# ------------------------------------------------------------------ Parte 1 · slides
def slide_grupo(n, g):
    info = INFO[n]
    badges = "\n".join(f'        <span class="badge">{e(m)}</span>' for m in info["integrantes"])
    linhas = "\n".join(f"        <tr><td>{e(m)}</td><td>{e(f)}</td></tr>" for m, f in funcoes(n))
    sens = f'\n    <div class="warning-box" style="font-size: 15px; margin-top: 8px;">\n        {SENSIVEL[n]}\n    </div>' if n in SENSIVEL else ""
    return f"""<!-- SLIDE {n + 2}: GRUPO {n} -->
<section>
    <span class="group-chip">GRUPO {n}</span>
    <h1>{e(g['nome'])} <span style="font-size: 18px; color: #666; font-weight: 400;">· {e(info['prof'])}</span></h1>
    <div>
{badges}
    </div>
    <div class="highlight-box" style="font-size: 16px;">
        <strong>Objetivo:</strong> {md_inline_to_html(g['objetivo'])}
    </div>{sens}
    <div class="two-col" style="margin-top: 10px;">
        <div class="card">
            <h3>Roteiro no Shopping</h3>
            <p><strong>Onde:</strong> {e(g['onde'])}.<br>
            <strong>Abordagem:</strong> {e(g['como'])}<br>
            <strong>Meta:</strong> <span class="badge green">15–20 respostas</span></p>
        </div>
        <div class="card">
            <h3>Perguntas Essenciais</h3>
            <p>{e(essenciais(g))}</p>
        </div>
    </div>
    <table style="margin-top: 12px;">
        <tr><th>Integrante</th><th>Função no campo</th></tr>
{linhas}
    </table>
    <div class="subtitle">Customer Discovery na Prática · Visita Técnica ao Shopping · Prof. Renato Rosa</div>
</section>

"""


def parte1_slides():
    s = comuns(ler("Parte 1/Slides-Shopping.html"))
    s = entre(s, "<!-- SLIDE 3: GRUPO 1 -->", "<!-- SLIDE 9: CHECKLIST FINAL -->", "".join(slide_grupo(n, g) for n, g in GRUPOS.items()))
    s = s.replace("<!-- SLIDE 9: CHECKLIST FINAL -->", "<!-- SLIDE 8: CHECKLIST FINAL -->").replace("<!-- SLIDE 10: DICA DE OURO -->", "<!-- SLIDE 9: DICA DE OURO -->")
    gravar("Parte 1/Slides-Shopping.html", s)


# ------------------------------------------------------------------ Parte 1 · caderno
def secao_grupo(n, g):
    info = INFO[n]
    linhas = "\n".join(f"      <tr><td>{e(m)}</td><td>{e(f)}</td></tr>" for m, f in funcoes(n))
    sens = f'\n    <div class="callout err"><span class="lbl">Atenção</span>\n      {SENSIVEL[n]}</div>' if n in SENSIVEL else ""
    return f"""  <!-- G{n} -->
  <section id="g{n}">
    <div class="secnum">00</div>
    <h2>Grupo {n} — {e(g['nome'])} <span class="pill">{e(info['prof'])}</span></h2>
    <div class="ficha">
      <h4>Integrantes</h4>
      <p class="who">{' · '.join(e(m) for m in info['integrantes'])}</p>
    </div>
    <div class="ficha g">
      <h4>Objetivo</h4>
      <p>{md_inline_to_html(g['objetivo'])}</p>
    </div>{sens}
    <h3>Roteiro de campo</h3>
    <div class="tbl"><table>
      <tr><th>Item</th><th>Definição do grupo</th></tr>
      <tr><td>Onde</td><td>{e(g['onde'])}</td></tr>
      <tr><td>Quem abordar</td><td>{e(g['quem'])}</td></tr>
      <tr><td>Pitch de abordagem</td><td>{e(g['como'])}</td></tr>
      <tr><td>Meta</td><td><strong>15–20 respostas</strong></td></tr>
    </table></div>
    <h3>Perguntas essenciais</h3>
    <p>{e(essenciais(g))}</p>
    <h3>Hipótese</h3>
    <p>{md_inline_to_html(g['hipotese'])}</p>
    <h3>Divisão de tarefas</h3>
    <div class="tbl"><table>
      <tr><th>Integrante</th><th>Função</th></tr>
{linhas}
    </table></div>
  </section>

"""


def modelo_form(n, g):
    qs = [g["blocos"][0][2][0], g["blocos"][1][2][0], g["blocos"][2][2][0], g["blocos"][3][2][0], g["blocos"][3][2][4]]
    corpo = "\n\n".join(f'<span class="c">{i}. Escala 1–5</span>\n{e(q)}\n1 = {e(a)} · 5 = {e(b)}' for i, (q, a, b) in enumerate(qs, 1))
    return f"""    <div class="ex">
      <span class="tag">Modelo · Grupo {n} — {e(g['nome'])}</span>
      <h4>{e(g['foco'][0].upper() + g['foco'][1:])}</h4>
      <div class="f">
{corpo}
      </div>
    </div>

"""


def renumerar(s):
    k = iter(range(100))
    s = re.sub(r'<div class="secnum">\d+</div>', lambda m: f'<div class="secnum">{next(k):02d}</div>', s)
    k2 = iter(range(100))
    s = re.sub(r'(<li><a href="#[^"]+">)\d+( · )', lambda m: f"{m.group(1)}{next(k2):02d}{m.group(2)}", s)
    return s


def parte1_caderno():
    s = comuns(ler("Parte 1/caderno-shopping.html"))
    toc = "\n".join(f'      <li><a href="#g{n}">00 · Grupo {n} — {e(g["nome"])}</a></li>' for n, g in GRUPOS.items())
    s = entre(s, '      <li><a href="#g1">', '      <li class="grp">Mãos à obra</li>', toc + "\n")
    s = entre(s, "  <!-- 03 G1 -->", "  <!-- 09 PITCH -->", "".join(secao_grupo(n, g) for n, g in GRUPOS.items()))
    i = s.index('<span class="tag">Modelo · Grupo 1')
    i = s.rindex('    <div class="ex">', 0, i)
    j = s.index("  </section>", i)
    s = s[:i] + "".join(modelo_form(n, GRUPOS[n]) for n in (1, 3, 5)) + s[j:]
    resumo = "\n".join(f"      <tr><td>{n}</td><td>{e(g['nome'])}</td><td>{e(g['onde'].split(',')[0])}</td><td>15–20</td></tr>" for n, g in GRUPOS.items())
    s = entre(s, "      <tr><td>1</td><td>Dinheiro na Mão</td>", "    </table></div>\n\n    <h3>Nunca esqueça</h3>", resumo + "\n")
    s = troca(s, '"Você não acha que as dívidas são um absurdo?"', '"Você não acha que a burocracia é um absurdo?"', False)
    s = troca(s, '"Você concorda que a família precisa de ajuda financeira?"', '"Você concorda que a cidade precisa de mais acessibilidade?"', False)
    s = troca(s, '"Você não acha as dívidas um absurdo?"', '"Você não acha a burocracia um absurdo?"', False)
    s = troca(s, "(saúde, dívidas, moradia)", "(saúde, deficiência, renda, moradia)", False)
    s = s.replace("<code>Pesquisa — Dinheiro na Mão</code>", "<code>Pesquisa — HoraCerta</code>")
    s = renumerar(s)
    gravar("Parte 1/caderno-shopping.html", s)


# ------------------------------------------------------------------ Parte 2
IDEIA_CURTA = {1: "App único de horas complementares", 2: "Guia turístico de bolso por localização", 3: "Assistente sonoro + alertas ao poder público",
               4: "Simulador da construtora por tipo de casa", 5: "Programas de moradia num lugar só"}
CORES = {1: "blue", 2: "green", 3: "purple", 4: "orange", 5: "green"}
AUDIO_SLIDE = """Código na tela:  G3-014

Áudio (20–40s):
"Código G3-014. Principais pontos: convive com um tio cego; acha as calçadas do
centro muito ruins; já reclamou na prefeitura e nunca teve resposta. Frase marcante:
'ele só sai de casa se alguém for junto'."
"""
AUDIO_CAD = """Código na tela:  G3-014

Áudio (20 a 40 segundos):
"Código G3-014. Principais pontos: convive com um tio cego; calçadas do centro
muito ruins; já reclamou na prefeitura e não teve resposta.
Frase marcante: 'ele só sai de casa se alguém for junto'."
"""


def parte2_slides():
    s = comuns(ler("Parte 2/Slides-Shopping-Parte2.html"))
    linhas = "\n".join(f'        <tr><td>{n}</td><td>{e(g["nome"])}</td><td>{e(INFO[n]["resp"])}</td><td><span class="badge {CORES[n]}">{e(IDEIA_CURTA[n])}</span></td></tr>' for n, g in GRUPOS.items())
    s = entre(s, "        <tr><td>1</td><td>Dinheiro na Mão</td>", "    </table>\n    <div class=\"warning-box\" style=\"margin-top: 12px; font-size: 15px;\">\n        <strong>Grupo 2:</strong>", linhas + "\n")
    i = s.index('    <div class="warning-box" style="margin-top: 12px; font-size: 15px;">\n        <strong>Grupo 2:</strong>')
    j = s.index("    </div>\n", i) + len("    </div>\n")
    s = s[:i] + '    <div class="success-box" style="margin-top: 12px; font-size: 15px;">\n        <strong>Ponto de partida pronto:</strong> cada grupo já tem uma proposta de 20 perguntas em <code>GrupoN/formulario-app.md</code> — a aula serve para <strong>validar, cortar e reescrever</strong>, não para começar do zero.\n    </div>\n' + s[j:]
    s = entre(s, "Código na tela:  G5-014", "    </div>\n    <div class=\"success-box\">", AUDIO_SLIDE)
    novo11 = """<!-- SLIDE 11: GRUPOS COM TEMA SENSÍVEL -->
<section>
    <h1>Atenção especial: Grupos 3 e 5</h1>
    <div class="warning-box" style="font-size: 16px;">
        <strong>G3 VozGuia</strong> pode entrevistar pessoas com deficiência visual. <strong>G5 CasaHumanizada</strong> toca em renda e moradia. Os dois exigem respeito, anonimato e acolhimento.
    </div>
    <div class="three-col" style="margin-top: 12px;">
        <div class="card"><h3 style="color:#e94560;">Nunca pergunte</h3><p>Renda, se recebe benefício, diagnóstico, nome de familiares ou dados pessoais.</p></div>
        <div class="card"><h3 style="color:#e94560;">Sempre faça</h3><p>Leia as opções em voz alta para quem não enxerga; confirme a marcação; lembre que pode parar a qualquer momento.</p></div>
        <div class="card"><h3 style="color:#e94560;">Se surgir uma história difícil</h3><p>Acolha, agradeça e não insista. Oriente a procurar o CRAS ou a ouvidoria da prefeitura quando fizer sentido.</p></div>
    </div>
    <div class="success-box" style="margin-top: 12px;">
        <strong>Nunca conduza</strong> uma pessoa cega pelo braço sem perguntar antes — ofereça o seu braço e deixe que ela segure.
    </div>
    <div class="subtitle">Parte 2 · Validação e construção do app · Prof. Renato Rosa</div>
</section>

"""
    s = entre(s, "<!-- SLIDE 11: GRUPOS COM TEMA SENSÍVEL -->", "<!-- SLIDE 12: FECHAMENTO -->", novo11)
    gravar("Parte 2/Slides-Shopping-Parte2.html", s)


CASOS = """    <div class="ex">
      <span class="tag">Caso — Grupo 1 HoraCerta</span>
      <h4>Validação das perguntas propostas (20 perguntas)</h4>
      <p>Aplicar os 6 critérios à lista de perguntas de cada bloco:</p>
      <div class="tbl"><table>
        <tr><th>Problema</th><th>Exemplo</th><th>Ação</th></tr>
        <tr><td>Pergunta de futuro</td><td>"Você usaria um app de horas complementares?"</td><td>Reescrever para comportamento: "Com que frequência você já perdeu um certificado?"</td></tr>
        <tr><td>Duas ideias</td><td>"O processo é demorado e burocrático?"</td><td>Dividir: tempo de espera (Q8) e dependência de papel (Q10)</td></tr>
        <tr><td>Público errado</td><td>Aplicar as 20 perguntas a quem nunca fez faculdade</td><td>Usar a <strong>triagem</strong> e encerrar com agradecimento</td></tr>
      </table></div>
    </div>

    <div class="ex">
      <span class="tag">Caso — Grupo 3 VozGuia</span>
      <h4>Validação das perguntas — acessibilidade</h4>
      <div class="tbl"><table>
        <tr><th>Problema</th><th>Exemplo</th><th>Ação</th></tr>
        <tr><td>Pergunta sobre a condição da pessoa</td><td>"Você é cego?"</td><td>Remover — usar a triagem com delicadeza: "Você convive com alguém com deficiência visual?"</td></tr>
        <tr><td>Pergunta de hipótese</td><td>"Você usaria um app para cegos?"</td><td>Reescrever: "Com que frequência você vê obstáculos nas calçadas?"</td></tr>
        <tr><td>Escala visual</td><td>Mostrar a tela para quem não enxerga</td><td>Ler as opções em voz alta e confirmar a marcação</td></tr>
      </table></div>
    </div>

    <div class="ex">
      <span class="tag">Caso — Grupo 5 CasaHumanizada</span>
      <h4>Validação das perguntas — tema sensível</h4>
      <p>O risco clássico aqui é a <strong>"pergunta educada"</strong> e a pergunta que expõe a pessoa (renda, benefício).</p>
      <div class="tbl"><table>
        <tr><th>Problema</th><th>Exemplo</th><th>Ação</th></tr>
        <tr><td>Pergunta pessoal sensível</td><td>"Quanto a família ganha?" / "Recebe Bolsa Família?"</td><td>Remover — medir só percepção: "O quanto o aluguel pesa no orçamento?"</td></tr>
        <tr><td>Pergunta de futuro</td><td>"Você se inscreveria num programa?"</td><td>Reescrever para passado: "Com que frequência já pensou em se inscrever?"</td></tr>
        <tr><td>Duas ideias</td><td>"O cadastro é difícil e demorado?"</td><td>Dividir: facilidade do cadastro (Q11) e idas repetidas ao órgão (Q13)</td></tr>
      </table></div>
      <div class="callout err"><span class="lbl">Reprovado no critério</span>
        Pergunta de futuro gera resposta educada. <strong>"Você usaria um app do governo?"</strong> quase sempre recebe "sim" — e isso não é dado, é gentileza.</div>
    </div>
  </section>
"""


def parte2_caderno():
    s = comuns(ler("Parte 2/caderno-shopping-parte2.html"))
    i = s.index('    <div class="ex">\n      <span class="tag">Caso — Grupo 1')
    j = s.index("  <!-- 04 -->")
    s = s[:i] + CASOS + "\n" + s[j:]
    s = entre(s, "Código na tela:  G5-014", "    </div>\n    <div class=\"semaforo\">", AUDIO_CAD)
    g = GRUPOS[1]
    linhas = "\n".join(f"        <tr><td>{k}</td><td>{e(q)}</td><td>Escala 1–5 ({e(a.lower())} → {e(b.lower())})</td></tr>"
                       for k, (q, a, b) in enumerate(g["blocos"][0][2], 1))
    s = s.replace("Exemplo — bloco de perguntas do Grupo 1 (Dinheiro na Mão)", "Exemplo — bloco 1 do Grupo 1 (HoraCerta)")
    s = entre(s, "        <tr><td>1</td><td>Como está a situação financeira", "      </table></div>\n    </div>\n    </details>", linhas + "\n")
    s = s.replace("ex.: <code>G5-014</code>", "ex.: <code>G3-014</code>")
    s = s.replace('"Com que frequência você perde uma data de vencimento?"', '"Com que frequência você perdeu um certificado?"')
    gravar("Parte 2/caderno-shopping-parte2.html", s)


def parte3():
    for rel in ("Parte 3/Slides-Shopping-Parte3.html", "Parte 3/caderno-shopping-parte3.html"):
        gravar(rel, comuns(ler(rel)))


def checar():
    ruins = re.compile(r"Dinheiro na Mão|Quita\.AI|SuaCasaSuaVida|Endividados|\bEDA\b|Vida no Controle|LifePath|Olivia|Péricles|Pantale|Giselle|Cássia|Hitalo|3SemVG|Saúde Financeira|3º Semestre")
    ok = True
    for f in sorted((RAIZ).glob("Parte */*.html")):
        achados = sorted(set(ruins.findall(f.read_text(encoding="utf-8"))))
        if achados:
            ok = False
            print(f"  resto do 3SemVG em {f.relative_to(RAIZ)}: {achados}")
    return ok


if __name__ == "__main__":
    parte1_slides(); parte1_caderno(); parte2_slides(); parte2_caderno(); parte3()
    print("Partes 1–3 geradas." if checar() else "ATENÇÃO: sobrou conteúdo do 3SemVG (veja acima).")
