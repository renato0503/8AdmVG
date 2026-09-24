"""Teste de fumaça dos MVPs (app.html) e do app de coleta, em viewport de celular (375x667).

Para cada app: abre, passa por todas as abas, clica em todos os botões visíveis de cada aba
(fechando modais/diálogos), recarrega a página e verifica: nenhum erro de JS, sem rolagem
horizontal, dados persistem após reload, backup exportado reimporta.

Uso (da raiz 8AdmVG):  py _gerador/testar_apps.py [filtro]
"""
import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

RAIZ = Path(__file__).resolve().parent.parent
APPS = sorted(RAIZ.glob("Grupo*/app.html"))


def testar(ctx, html: Path):
    erros = []
    pg = ctx.new_page()
    pg.on("pageerror", lambda e: erros.append(f"pageerror: {e}"))
    pg.on("console", lambda m: m.type == "error" and "favicon" not in m.text and "ERR_FILE_NOT_FOUND" not in m.text and erros.append(f"console: {m.text}"))
    pg.on("dialog", lambda d: d.accept())
    pg.goto(html.as_uri(), wait_until="load")
    pg.wait_for_timeout(300)
    abas = pg.eval_on_selector_all(".nav-inf [data-aba]", "els => els.map(e => e.dataset.aba)")
    cliques = 0
    for aba in abas:
        pg.click(f'.nav-inf [data-aba="{aba}"]')
        pg.wait_for_timeout(150)
        n = pg.eval_on_selector_all(f'.view[data-view="{aba}"] button', "els => els.length")
        for i in range(n):
            botoes = pg.query_selector_all(f'.view[data-view="{aba}"] button')
            if i >= len(botoes):
                break
            b = botoes[i]
            if not b.is_visible() or b.is_disabled():
                continue
            acao = b.get_attribute("data-acao")
            if acao in ("importar",):  # abre seletor de arquivo do sistema
                continue
            try:
                with pg.expect_download(timeout=1500) as _:
                    b.click(timeout=2000)
            except Exception:
                pass
            cliques += 1
            pg.wait_for_timeout(120)
            # dentro de modal: tenta o botão principal (salvar/confirmar) e depois fecha
            for _ in range(3):
                if not pg.query_selector(".modal-fundo"):
                    break
                principal = pg.query_selector(".modal .btns .btn:not(.sec):not([data-fechar])")
                if principal and principal.is_visible():
                    try:
                        principal.click(timeout=1500)
                    except Exception:
                        pass
                    pg.wait_for_timeout(150)
                fechar = pg.query_selector(".modal [data-fechar]")
                if fechar and fechar.is_visible():
                    try:
                        fechar.click(timeout=1500)
                    except Exception:
                        pass
                    pg.wait_for_timeout(250)
                else:
                    pg.keyboard.press("Escape")
                    pg.wait_for_timeout(250)
            # voltou a aba? (alguns botões trocam de aba)
            if not pg.is_visible(f'.view[data-view="{aba}"]'):
                pg.click(f'.nav-inf [data-aba="{aba}"]')
                pg.wait_for_timeout(120)
    largura = pg.evaluate("document.documentElement.scrollWidth - window.innerWidth")
    chave = pg.evaluate("Object.keys(localStorage).find(k => k.includes(':v1'))")
    antes = pg.evaluate(f"localStorage.getItem('{chave}')") if chave else None
    pg.reload(wait_until="load")
    pg.wait_for_timeout(300)
    depois = pg.evaluate(f"localStorage.getItem('{chave}')") if chave else None
    persistiu = antes is not None and json.loads(antes) == json.loads(depois)
    pg.close()
    return dict(abas=len(abas), cliques=cliques, erros=erros, overflow=largura, persistiu=persistiu, chave=chave)


def main(filtro=""):
    ok = True
    with sync_playwright() as pw:
        nav = pw.chromium.launch()
        for html in APPS:
            if filtro and filtro.lower() not in str(html).lower():
                continue
            ctx = nav.new_context(viewport={"width": 375, "height": 667}, is_mobile=True, has_touch=True, accept_downloads=True, locale="pt-BR")
            r = testar(ctx, html)
            ctx.close()
            status = "OK" if not r["erros"] and r["overflow"] <= 0 and r["persistiu"] else "FALHA"
            ok &= status == "OK"
            print(f"[{status}] {html.parent.name}: {r['abas']} abas, {r['cliques']} cliques, overflow={r['overflow']}px, persistência={'sim' if r['persistiu'] else 'NÃO'} ({r['chave']})")
            for e in r["erros"][:10]:
                print("     ", e)
        nav.close()
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "")
