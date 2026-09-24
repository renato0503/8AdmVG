"""Hub raiz do 8AdmVG (index.html + manifest.json + sw.js), gerado a partir de dados.py e grupos.md.
Chamado por gen.py (main)."""
import json

from dados import GRUPOS, CURSO, TURMA
from extra import EXTRA

ESTRELA = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><rect width='24' height='24' rx='6' fill='%230b1220'/><path d='M12 3l2.2 6.8L21 12l-6.8 2.2L12 21l-2.2-6.8L3 12l6.8-2.2z' fill='%2338bdf8'/></svg>"

ICONES = {
    "coleta": '<rect x="6" y="2" width="12" height="20" rx="2"/><path d="M11 18h2"/>',
    "slides": '<rect x="2" y="4" width="20" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>',
    "livro": '<path d="M4 19.5A2.5 2.5 0 016.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15A2.5 2.5 0 016.5 2z"/>',
    "lupa": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>',
}


def e(s):
    import html
    return html.escape(s, quote=True)


def card_util(href, ic, tit, sub):
    return (f'        <a href="{href}" class="doc-card"><div class="doc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{ICONES[ic]}</svg></div>'
            f'<b>{tit}</b><small>{sub}</small></a>')


def gen_hub(infos, total_papers):
    mvps = []
    for n, g in GRUPOS.items():
        t, info = g["tema"], infos[n]
        mvps.append(f"""        <a href="{g['pasta']}/" class="mvp" style="--c:{t['accent']};--c2:{t['accent2']};--t:{t['tinta']}">
          <div class="mvp-top"><img src="assets/logos/g{n}.svg" alt="" width="52" height="52"><div><span class="mvp-g">Grupo {n} · {e(info['prof'])}</span><h3>{e(g['nome'])}</h3></div></div>
          <p>{e(g['tagline'])}.</p>
          <div class="mvp-feats">{''.join(f'<span>{e(a)}</span>' for a, _ in EXTRA[n]['cards'])}</div>
          <div class="mvp-team">{e(' · '.join(info['integrantes']))}</div>
          <span class="mvp-cta">Ver projeto →</span>
        </a>""")
    defesa = "\n".join(f'        <a href="{g["pasta"]}/Slides-{g["nome"]}.html" class="doc-card"><div class="doc-icon" style="color:{g["tema"]["accent"]}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{ICONES["slides"]}</svg></div><b>{e(g["nome"])}</b><small>Grupo {n} · 12 slides · <span>PDF</span></small></a>'
                       for n, g in GRUPOS.items())
    logos = "".join(f'<img src="assets/logos/g{n}.svg" alt="{e(g["nome"])}" width="44" height="44">' for n, g in GRUPOS.items())
    materiais = "\n".join([
        card_util("coleta/", "coleta", "App de coleta (campo)", "Formulário offline · perfil + 20 perguntas · código G&lt;n&gt;-&lt;nnn&gt;"),
        card_util("Parte%201/Slides-Shopping.html", "slides", "Parte 1 · Preparação", "Slides da visita técnica e roteiros por grupo"),
        card_util("Parte%202/Slides-Shopping-Parte2.html", "slides", "Parte 2 · Formulários", "Validação das perguntas e construção no app"),
        card_util("Parte%203/Slides-Shopping-Parte3.html", "slides", "Parte 3 · Campo + sprints", "Ida ao shopping e log de sprints"),
    ])
    cadernos = "\n".join([
        card_util("Parte%201/caderno-shopping.html", "livro", "Caderno · Parte 1", "Guia completo da preparação (PDF disponível)"),
        card_util("Parte%202/caderno-shopping-parte2.html", "livro", "Caderno · Parte 2", "Validação, app de formulário e áudio"),
        card_util("Parte%203/caderno-shopping-parte3.html", "livro", "Caderno · Parte 3", "Protocolo de campo e sprints"),
        card_util("assets/md-viewer.html?src=../_pesquisa/INDICE-PESQUISA.md&voltar=../index.html", "lupa", "Índice de pesquisa", f"{total_papers} artigos reais (OpenAlex) com DOI"),
    ])
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Customer Discovery · {TURMA}</title>
<meta name="description" content="Materiais, pesquisa e MVPs dos 5 grupos de Customer Discovery da turma {TURMA} (Unifacc).">
<meta name="theme-color" content="#0b1220">
<link rel="manifest" href="manifest.json">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,{ESTRELA}">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/landing.css">
<style>
:root{{--acc:#38bdf8;--acc2:#f59e0b;--tinta:#0b1220}}
.nav .links{{margin-left:auto;display:flex;gap:16px;font-size:13px;font-weight:600}}
.nav .links a{{color:#c7cee8;text-decoration:none}}
.nav .links a:hover{{color:#fff}}
.nav .marca{{display:flex;align-items:center;gap:8px;font-family:'Space Grotesk',sans-serif;font-weight:700}}
.hero h1 span{{color:var(--acc)}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:12px;margin-top:28px;max-width:640px}}
.stats div{{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);border-radius:14px;padding:12px 14px}}
.stats b{{display:block;font-family:'Space Grotesk',sans-serif;font-size:26px;color:#fff}}
.stats span{{font-size:12px;color:#9aa5c3}}
.faixa{{display:flex;gap:10px;margin-top:26px;flex-wrap:wrap}}
.faixa img{{border-radius:12px;box-shadow:0 6px 16px rgba(0,0,0,.35)}}
.mvps{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}}
.mvp{{background:#fff;border:1px solid var(--line);border-top:5px solid var(--c);border-radius:18px;padding:18px;text-decoration:none;color:inherit;display:flex;flex-direction:column;gap:10px;transition:transform .15s,box-shadow .15s}}
.mvp:hover{{transform:translateY(-3px);box-shadow:var(--shadow-card)}}
.mvp-top{{display:flex;gap:12px;align-items:center}}
.mvp-top img{{border-radius:14px}}
.mvp-g{{font-size:11.5px;font-weight:700;color:var(--c);text-transform:uppercase;letter-spacing:.04em}}
.mvp h3{{font-family:'Space Grotesk',sans-serif;font-size:20px;color:var(--t)}}
.mvp p{{font-size:13.5px;color:var(--ink-soft);line-height:1.5}}
.mvp-feats{{display:flex;flex-wrap:wrap;gap:6px}}
.mvp-feats span{{font-size:11.5px;font-weight:700;background:color-mix(in srgb,var(--c) 12%,white);color:var(--t);padding:4px 9px;border-radius:999px}}
.mvp-team{{font-size:12px;color:var(--ink-soft)}}
.mvp-cta{{margin-top:auto;font-weight:700;font-size:13.5px;color:var(--c)}}
@media (max-width:560px){{.nav .links{{display:none}}}}
</style>
</head>
<body>

<nav class="nav"><div class="wrap">
  <span class="marca"><img src="data:image/svg+xml,{ESTRELA}" alt="" width="22" height="22"> Customer Discovery · {TURMA}</span>
  <div class="links"><a href="#mvps">MVPs</a><a href="#materiais">Materiais</a><a href="#cadernos">Cadernos</a><a href="#defesa">Defesa</a></div>
</div></nav>

<header class="hero">
  <div class="wrap">
    <div class="hero-group">{e(CURSO)} · FACC/Unifacc · Cerrado Tech</div>
    <h1>5 ideias, <span>5 MVPs funcionais</span><br>prontos para o campo</h1>
    <p class="pitch">Horas complementares, turismo por localização, acessibilidade para pessoas cegas, simulador de compra da casa e acesso humanizado a programas de moradia. Cada grupo tem defesa com dados reais, pesquisa científica verificada, formulário de campo e um app que funciona no celular.</p>
    <div class="stats">
      <div><b>5</b><span>MVPs publicados</span></div>
      <div><b>100</b><span>perguntas de campo</span></div>
      <div><b>{total_papers}</b><span>artigos com DOI</span></div>
      <div><b>PWA</b><span>funciona offline</span></div>
    </div>
    <div class="faixa">{logos}</div>
  </div>
</header>

<main>
  <section class="block" id="mvps"><div class="wrap">
    <div class="block-head"><h2>Os projetos</h2><p>Toque num projeto para ver a landing do grupo, os documentos e abrir o app.</p></div>
    <div class="mvps">
{chr(10).join(mvps)}
    </div>
  </div></section>

  <section class="block" id="materiais"><div class="wrap">
    <div class="block-head"><h2>Materiais da atividade</h2><p>App de coleta do shopping e os slides das três partes.</p></div>
    <div class="doc-grid">
{materiais}
    </div>
  </div></section>

  <section class="block" id="cadernos"><div class="wrap">
    <div class="block-head"><h2>Cadernos e pesquisa</h2><p>Guias completos para estudar (com versão PDF) e o índice dos artigos científicos.</p></div>
    <div class="doc-grid">
{cadernos}
    </div>
  </div></section>

  <section class="block" id="defesa"><div class="wrap">
    <div class="block-head"><h2>Slides de defesa</h2><p>Dor com dados reais, ideia, hipótese, referencial científico e pitch de 30 segundos.</p></div>
    <div class="doc-grid">
{defesa}
    </div>
  </div></section>
</main>

<footer><div class="wrap">
  <p>Customer Discovery · {TURMA} · Prof. Renato Rosa · Cerrado Tech · Unifacc · 2026</p>
  <p><a href="https://github.com/renato0503/8AdmVG" target="_blank" rel="noopener">Repositório</a> · <a href="coleta/">App de coleta</a> · <a href="#mvps">Voltar ao topo</a></p>
</div></footer>

</body>
</html>
"""
    manifest = json.dumps({
        "name": f"Customer Discovery {TURMA}", "short_name": f"CD {TURMA}",
        "description": "Materiais e MVPs da pesquisa de campo Customer Discovery", "start_url": "./",
        "display": "standalone", "background_color": "#f4f6fb", "theme_color": "#0b1220", "orientation": "portrait-primary",
        "icons": [{"src": "data:image/svg+xml," + ESTRELA.replace("'", "'"), "sizes": "any", "type": "image/svg+xml"}],
    }, ensure_ascii=False, indent=2) + "\n"
    sw = """const CACHE = '8admvg-hub-v1';
const PRE = ['./', './index.html', './assets/landing.css'];
self.addEventListener('install', e => e.waitUntil(caches.open(CACHE).then(c => c.addAll(PRE)).then(() => self.skipWaiting())));
self.addEventListener('activate', e => e.waitUntil(caches.keys().then(k => Promise.all(k.filter(v => v !== CACHE).map(v => caches.delete(v)))).then(() => self.clients.claim())));
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(fetch(e.request).then(res => {
    if (res && res.ok && new URL(e.request.url).origin === location.origin) { const c = res.clone(); caches.open(CACHE).then(x => x.put(e.request, c)); }
    return res;
  }).catch(() => caches.match(e.request).then(r => r || caches.match('./index.html'))));
});
"""
    return html, manifest, sw
